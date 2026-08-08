#!/usr/bin/env python3
"""
send_newsletter.py
CatnBloom Digital Art Studio — Шаг 5 плана "Рассылка своими руками"

Читает subscribers.csv и feed.xml в корне репозитория, отбирает пункты
за последние 7 дней, формирует HTML-письмо и рассылает через Gmail SMTP.

Переменные окружения (задаются в .github/workflows/newsletter.yml из GitHub Secrets):
  GMAIL_USER          — адрес отправителя (ccatnbloom@gmail.com)
  GMAIL_APP_PASSWORD  — App Password, сгенерированный в Google Account
  DRY_RUN             — "true"/"false"; при true письма не отправляются,
                         только печатается лог в консоль Actions

ДОПУЩЕНИЯ (не подтверждены в сессии создания файла — проверить после первого запуска):
  - subscribers.csv содержит колонку с заголовком "email" (регистр не важен,
    поиск идёт по названию столбца, а не по номеру позиции)
  - Окно отбора контента — 7 дней от текущего момента запуска
  - Тема письма — "CatnBloom Studio — Weekly Update"
  - Отписка НЕ реализована как рабочий механизм — это временная mailto-заглушка
"""

import csv
import os
import smtplib
import sys
from datetime import datetime, timedelta, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xml.etree import ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBSCRIBERS_PATH = os.path.join(REPO_ROOT, "subscribers.csv")
FEED_PATH = os.path.join(REPO_ROOT, "feed.xml")

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

WINDOW_DAYS = 7
EMAIL_SUBJECT = "CatnBloom Studio — Weekly Update"
SITE_URL = "https://www.catnbloom.com"

# Unsubscribe через mailto — согласовано как временное решение для старта
# (закрывает требования CAN-SPAM Act без разворачивания инфраструктуры удаления из CSV).
# Открытый долг: заменить на реальную ссылку/эндпоинт, когда появится unsubscribe-механизм.
# ВАЖНО: адрес ниже должен совпадать с GMAIL_USER — проверьте перед первой отправкой.
UNSUBSCRIBE_EMAIL = "ccatnbloom@gmail.com"
UNSUBSCRIBE_NOTE = (
    "You received this email because you subscribed to updates at CatnBloom. "
    "If you no longer wish to receive updates, reply to this email with "
    "\"UNSUBSCRIBE\" in the subject line or click "
    f'<a href="mailto:{UNSUBSCRIBE_EMAIL}?subject=Unsubscribe" style="color:#999;">Unsubscribe</a>.'
)


def log(message):
    print(f"[send_newsletter] {message}", flush=True)


def is_dry_run():
    return os.environ.get("DRY_RUN", "false").strip().lower() == "true"


def load_subscribers(path):
    """Читает CSV, ищет колонку email по заголовку. Возвращает список адресов."""
    if not os.path.exists(path):
        log(f"ОШИБКА: файл не найден: {path}")
        return []

    emails = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            log("ОШИБКА: subscribers.csv пуст или без заголовков")
            return []

        email_col = None
        for name in reader.fieldnames:
            if name and name.strip().lower() == "email":
                email_col = name
                break

        if email_col is None:
            log(
                "ОШИБКА: в subscribers.csv не найдена колонка 'email'. "
                f"Найденные заголовки: {reader.fieldnames}. "
                "Проверьте формат файла — скрипт не будет угадывать структуру."
            )
            return []

        for row in reader:
            addr = (row.get(email_col) or "").strip()
            if addr:
                emails.append(addr)

    # дедупликация с сохранением порядка
    seen = set()
    unique_emails = []
    for addr in emails:
        key = addr.lower()
        if key not in seen:
            seen.add(key)
            unique_emails.append(addr)

    return unique_emails


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


def load_recent_feed_items(path, window_days):
    """Читает feed.xml, возвращает список item'ов за последние window_days дней."""
    if not os.path.exists(path):
        log(f"ОШИБКА: файл не найден: {path}")
        return []

    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        log(f"ОШИБКА: не удалось распарсить feed.xml: {e}")
        return []

    root = tree.getroot()
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


def build_email_html(items):
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
    <p style="font-size:11px;color:#999;">{UNSUBSCRIBE_NOTE}</p>
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

    items = load_recent_feed_items(FEED_PATH, WINDOW_DAYS)
    log(f"Свежих пунктов в feed.xml (за {WINDOW_DAYS} дн.): {len(items)}")

    if not subscribers:
        log("Подписчиков нет — рассылка не выполняется.")
        return

    if not items:
        log("Новых пунктов нет — письмо не отправляется (нечего рассылать).")
        return

    html_body = build_email_html(items)

    if dry_run:
        log("DRY_RUN включён — письма НЕ отправляются. Ниже — кому бы ушло:")
        for addr in subscribers:
            log(f"  -> {addr}")
        log("Тема письма: " + EMAIL_SUBJECT)
        return

    sent_count = 0
    failed = []

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp_conn:
        smtp_conn.starttls()
        smtp_conn.login(gmail_user, gmail_password)

        for addr in subscribers:
            try:
                send_email(smtp_conn, gmail_user, addr, EMAIL_SUBJECT, html_body)
                sent_count += 1
            except Exception as e:
                log(f"ОШИБКА отправки на {addr}: {e}")
                failed.append(addr)

    log(f"Готово. Отправлено: {sent_count}/{len(subscribers)}")
    if failed:
        log(f"Не удалось отправить на: {failed}")


if __name__ == "__main__":
    main()
