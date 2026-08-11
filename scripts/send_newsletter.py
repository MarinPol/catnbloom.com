#!/usr/bin/env python3
"""
send_newsletter.py
CatnBloom Digital Art Studio — Шаг 5 плана "Рассылка своими руками"

Читает subscribers.csv из репозитория и скачивает живой feed.xml с сайта,
отбирает пункты за последние 7 дней, формирует HTML-письмо и рассылает
через Gmail SMTP.

Переменные окружения (задаются в .github/workflows/newsletter.yml из GitHub Secrets):
  GMAIL_USER          — адрес отправителя (ccatnbloom@gmail.com)
  GMAIL_APP_PASSWORD  — App Password, сгенерированный в Google Account
  DRY_RUN             — "true"/"false"; при true письма не отправляются,
                         только печатается лог в консоль Actions

ВАЖНО: feed.xml в самом репозитории — это НЕрендеренный Jekyll-шаблон,
а не готовый XML. Скрипт скачивает реальный, собранный файл с сайта
(https://www.catnbloom.com/feed.xml), а не читает его из репозитория.

ОТПИСКА (обновлено 2026-08-11): subscribers.csv теперь содержит 3-ю колонку
unsub_token — постоянный персональный токен, выданный воркером newsletter
(worker.js) в момент подтверждения подписки. Каждое письмо теперь содержит
СВОЮ уникальную ссылку https://newsletter.catnbloom.com/unsubscribe?token=...,
а не общую mailto-заглушку. Поэтому HTML письма собирается ОТДЕЛЬНО для
каждого подписчика (build_email_html теперь принимает unsub_token),
в отличие от прежней версии, где один и тот же HTML рассылался всем.

ДОПУЩЕНИЯ:
  - subscribers.csv содержит колонки "email" и "unsub_token" (регистр не
    важен, поиск идёт по названию столбца, а не по номеру позиции)
  - Строки, записанные ДО введения токена (без unsub_token), получат письмо
    с fallback-заглушкой mailto — см. UNSUBSCRIBE_FALLBACK_NOTE ниже. Эти
    строки нужно будет закрыть отдельно (переподписка или бэкфилл).
  - Окно отбора контента — 7 дней от текущего момента запуска
  - Тема письма — "CatnBloom Studio — Weekly Update"
"""

import csv
import os
import smtplib
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xml.etree import ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBSCRIBERS_PATH = os.path.join(REPO_ROOT, "subscribers.csv")

# ВАЖНО: feed.xml в самом репозитории — это НЕрендеренный Jekyll-шаблон
# (содержит {% for %}, {% if %} и т.д.), а не готовый XML. Реальный,
# собранный Jekyll'ом файл существует только на опубликованном сайте.
# Поэтому скрипт скачивает живой feed.xml с сайта, а не читает файл из репо.
FEED_URL = "https://www.catnbloom.com/feed.xml"

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

WINDOW_DAYS = 7
EMAIL_SUBJECT = "CatnBloom Studio — Weekly Update"
SITE_URL = "https://www.catnbloom.com"

# Базовый адрес воркера рассылки — используется для построения персональной
# ссылки отписки. Должен совпадать с доменом, подключённым в Cloudflare
# Workers Routes (см. MASTER LOG 2026-08-11).
NEWSLETTER_WORKER_URL = "https://newsletter.catnbloom.com"

# Fallback-заглушка — используется ТОЛЬКО для строк CSV без unsub_token
# (старые записи, сделанные до внедрения токена). Как только эти строки
# получат токен (переподписка или бэкфилл), эта ветка перестанет
# использоваться сама собой.
UNSUBSCRIBE_FALLBACK_EMAIL = "ccatnbloom@gmail.com"


def log(message):
    print(f"[send_newsletter] {message}", flush=True)


def is_dry_run():
    return os.environ.get("DRY_RUN", "false").strip().lower() == "true"


def load_subscribers(path):
    """Читает CSV, ищет колонки email и unsub_token по заголовку (регистронезависимо).
    Возвращает список словарей {"email": ..., "unsub_token": ... или None}.
    """
    if not os.path.exists(path):
        log(f"ОШИБКА: файл не найден: {path}")
        return []

    subscribers = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            log("ОШИБКА: subscribers.csv пуст или без заголовков")
            return []

        email_col = None
        token_col = None
        for name in reader.fieldnames:
            if not name:
                continue
            key = name.strip().lower()
            if key == "email":
                email_col = name
            elif key == "unsub_token":
                token_col = name

        if email_col is None:
            log(
                "ОШИБКА: в subscribers.csv не найдена колонка 'email'. "
                f"Найденные заголовки: {reader.fieldnames}. "
                "Проверьте формат файла — скрипт не будет угадывать структуру."
            )
            return []

        if token_col is None:
            log(
                "ПРЕДУПРЕЖДЕНИЕ: в subscribers.csv не найдена колонка 'unsub_token'. "
                "Все письма уйдут с fallback-заглушкой отписки (mailto). "
                f"Найденные заголовки: {reader.fieldnames}."
            )

        for row in reader:
            addr = (row.get(email_col) or "").strip()
            if not addr:
                continue
            token = (row.get(token_col) or "").strip() if token_col else ""
            subscribers.append({"email": addr, "unsub_token": token or None})

    # дедупликация по email с сохранением порядка
    seen = set()
    unique_subscribers = []
    for sub in subscribers:
        key = sub["email"].lower()
        if key not in seen:
            seen.add(key)
            unique_subscribers.append(sub)

    return unique_subscribers


def parse_feed_datetime(raw):
    """Пытается распарсить pubDate в формате RFC 822 (стандарт RSS)."""
    if not raw:
        return None
    raw = raw.strip()
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(raw, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


def fetch_feed_xml(url):
    """Скачивает живой feed.xml с опубликованного сайта. Возвращает текст или None."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CatnBloom-Newsletter-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=20) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        log(f"ОШИБКА: не удалось скачать {url}: {e}")
        return None
    except Exception as e:
        log(f"ОШИБКА при скачивании feed.xml: {e}")
        return None


def load_recent_feed_items(feed_url, window_days):
    """Скачивает feed.xml с сайта, возвращает список item'ов за последние window_days дней."""
    xml_text = fetch_feed_xml(feed_url)
    if xml_text is None:
        return []

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        log(f"ОШИБКА: не удалось распарсить feed.xml, скачанный с {feed_url}: {e}")
        return []
    channel = root.find("channel")
    if channel is None:
        log("ОШИБКА: в feed.xml не найден тег <channel>")
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(days=window_days)
    items = []

    for item in channel.findall("item"):
        title_el = item.find("title")
        link_el = item.find("link")
        pubdate_el = item.find("pubDate")
        desc_el = item.find("description")

        title = title_el.text.strip() if title_el is not None and title_el.text else ""
        link = link_el.text.strip() if link_el is not None and link_el.text else ""
        pub_raw = pubdate_el.text if pubdate_el is not None else None
        description = desc_el.text.strip() if desc_el is not None and desc_el.text else ""

        pub_dt = parse_feed_datetime(pub_raw)
        if pub_dt is None:
            log(f"ПРЕДУПРЕЖДЕНИЕ: не удалось распознать дату у item '{title}', пропущен")
            continue

        if pub_dt >= cutoff:
            items.append({
                "title": title,
                "link": link,
                "pub_date": pub_dt,
                "description": description,
            })

    items.sort(key=lambda x: x["pub_date"], reverse=True)
    return items


def build_unsubscribe_note(unsub_token):
    """Строит блок отписки для письма. Персональная ссылка через токен,
    если он есть; иначе — временная mailto-заглушка (старые записи без токена).
    """
    if unsub_token:
        unsub_url = f"{NEWSLETTER_WORKER_URL}/unsubscribe?token={unsub_token}"
        return (
            "You received this email because you subscribed to updates at CatnBloom. "
            f'If you no longer wish to receive updates, <a href="{unsub_url}" '
            'style="color:#999;">unsubscribe here</a>.'
        )
    return (
        "You received this email because you subscribed to updates at CatnBloom. "
        "If you no longer wish to receive updates, reply to this email with "
        "\"UNSUBSCRIBE\" in the subject line or click "
        f'<a href="mailto:{UNSUBSCRIBE_FALLBACK_EMAIL}?subject=Unsubscribe" '
        'style="color:#999;">Unsubscribe</a>.'
    )


def build_email_html(items, unsub_token):
    if not items:
        body_rows = "<p>No new updates this week.</p>"
    else:
        rows = []
        for it in items:
            rows.append(
                f'<tr><td style="padding:12px 0;border-bottom:1px solid #e5e5e5;">'
                f'<a href="{it["link"]}" style="font-size:16px;font-weight:600;'
                f'color:#1D4D54;text-decoration:none;">{it["title"]}</a><br>'
                f'<span style="font-size:13px;color:#666;">'
                f'{it["pub_date"].strftime("%B %d, %Y")}</span>'
                f'</td></tr>'
            )
        body_rows = f'<table role="presentation" width="100%">{"".join(rows)}</table>'

    unsubscribe_note = build_unsubscribe_note(unsub_token)

    html = f"""\
<!DOCTYPE html>
<html>
<body style="font-family:Georgia,serif;background:#fff;color:#2b2b2b;margin:0;padding:24px;">
  <div style="max-width:600px;margin:0 auto;">
    <h1 style="font-size:22px;color:#1D4D54;">CatnBloom Studio</h1>
    <p style="font-size:15px;line-height:1.6;">Here's what's new this week:</p>
    {body_rows}
    <p style="margin-top:24px;">
      <a href="{SITE_URL}" style="color:#1D4D54;">Visit the studio</a>
    </p>
    <hr style="border:none;border-top:1px solid #e5e5e5;margin:32px 0 16px;">
    <p style="font-size:11px;color:#999;">{unsubscribe_note}</p>
  </div>
</body>
</html>
"""
    return html


def send_email(smtp_conn, from_addr, to_addr, subject, html_body):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg.attach(MIMEText(html_body, "html"))
    smtp_conn.sendmail(from_addr, [to_addr], msg.as_string())


def main():
    dry_run = is_dry_run()
    log(f"Запуск. DRY_RUN={dry_run}")

    gmail_user = os.environ.get("GMAIL_USER")
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD")

    if not gmail_user or not gmail_password:
        log("ОШИБКА: не заданы GMAIL_USER / GMAIL_APP_PASSWORD в окружении. Прерываю.")
        sys.exit(1)

    subscribers = load_subscribers(SUBSCRIBERS_PATH)
    log(f"Подписчиков найдено: {len(subscribers)}")
    no_token_count = sum(1 for s in subscribers if not s["unsub_token"])
    if no_token_count:
        log(
            f"ПРЕДУПРЕЖДЕНИЕ: {no_token_count} из {len(subscribers)} подписчиков "
            "без unsub_token — им уйдёт письмо с fallback mailto-заглушкой отписки."
        )

    items = load_recent_feed_items(FEED_URL, WINDOW_DAYS)
    log(f"Свежих пунктов в feed.xml (за {WINDOW_DAYS} дн.): {len(items)}")

    if not subscribers:
        log("Подписчиков нет — рассылка не выполняется.")
        return

    if not items:
        log("Новых пунктов нет — письмо не отправляется (нечего рассылать).")
        return

    if dry_run:
        log("DRY_RUN включён — письма НЕ отправляются. Ниже — кому бы ушло:")
        for sub in subscribers:
            token_status = "с персональной ссылкой отписки" if sub["unsub_token"] else "с fallback mailto (нет токена)"
            log(f"  -> {sub['email']} ({token_status})")
        log("Тема письма: " + EMAIL_SUBJECT)
        return

    sent_count = 0
    failed = []

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp_conn:
        smtp_conn.starttls()
        smtp_conn.login(gmail_user, gmail_password)

        for sub in subscribers:
            try:
                html_body = build_email_html(items, sub["unsub_token"])
                send_email(smtp_conn, gmail_user, sub["email"], EMAIL_SUBJECT, html_body)
                sent_count += 1
            except Exception as e:
                log(f"ОШИБКА отправки на {sub['email']}: {e}")
                failed.append(sub["email"])

    log(f"Готово. Отправлено: {sent_count}/{len(subscribers)}")
    if failed:
        log(f"Не удалось отправить на: {failed}")


if __name__ == "__main__":
    main()
