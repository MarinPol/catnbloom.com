#!/usr/bin/env python3
"""
send_newsletter.py
CatnBloom Digital Art Studio -- Step 5 of the "DIY Newsletter" plan

Reads subscribers.csv from the repository and downloads the live feed.xml
from the site, selects items from the last 7 days, builds an HTML email,
and sends it via the Resend API.

Environment variables (set in .github/workflows/newsletter.yml from GitHub Secrets):
  RESEND_API_KEY  -- Resend API key (a SEPARATE secret in GitHub, not the same
                     store as the identically-named secret in Cloudflare --
                     the value can be the same key, but it must be added
                     separately in this repo's Settings -> Secrets and
                     variables -> Actions)
  DRY_RUN         -- "true"/"false"; when true, no emails are sent, only a
                     log is printed to the Actions console

IMPORTANT: feed.xml in the repository itself is an UNRENDERED Jekyll template,
not a ready XML file. The script downloads the real, built file from the live
site (https://www.catnbloom.com/feed.xml) instead of reading it from the repo.

SENDING (updated 2026-08-11): switched from Gmail SMTP to the Resend API.
Reason: the first real email sent via smtplib/Gmail landed in the recipient's
Spam folder -- Gmail SMTP sends have no sender reputation for automated mail
and lacked a List-Unsubscribe header, which Gmail/Yahoo use as one of the
signals of a legitimate mailing. Resend was already used and confirmed
working for subscription-confirmation emails (worker.js), and the sending
domain mail.catnbloom.com is already verified there -- reusing the same
channel for the newsletter itself made sense.

UNSUBSCRIBE: subscribers.csv has a 3rd column, unsub_token -- a permanent
personal token issued by the newsletter worker (worker.js) at the moment a
subscription is confirmed. Every email contains ITS OWN unique link
https://newsletter.catnbloom.com/unsubscribe?token=..., which is also passed
in the List-Unsubscribe header (RFC 8058, "one-click unsubscribe") -- a
deliverability signal independent of the text at the bottom of the email.

ASSUMPTIONS:
  - subscribers.csv contains "email" and "unsub_token" columns (case does not
    matter, lookup is by column name, not by position)
  - Rows written BEFORE the token was introduced (no unsub_token) will get an
    email with the mailto fallback -- see UNSUBSCRIBE_FALLBACK_EMAIL below.
    These rows need to be closed separately (re-subscription or backfill).
  - Content selection window -- 7 days from the current run time
  - Email subject -- "CatnBloom Studio -- Weekly Update"
  - Sender address -- newsletter@mail.catnbloom.com (the same verified
    subdomain that worker.js already uses for confirmation emails)
"""

import csv
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUBSCRIBERS_PATH = os.path.join(REPO_ROOT, "subscribers.csv")

# IMPORTANT: feed.xml in the repository itself is an UNRENDERED Jekyll
# template (contains {% for %}, {% if %}, etc.), not ready XML. The real,
# built file only exists on the published site. That's why the script
# downloads the live feed.xml instead of reading the file from the repo.
FEED_URL = "https://www.catnbloom.com/feed.xml"

RESEND_API_URL = "https://api.resend.com/emails"
SENDER_ADDRESS = "CatnBloom Studio <newsletter@mail.catnbloom.com>"

WINDOW_DAYS = 7
EMAIL_SUBJECT = "CatnBloom Studio — Weekly Update"
SITE_URL = "https://www.catnbloom.com"

# Base URL of the newsletter worker -- used to build the personal unsubscribe
# link. Must match the domain connected in Cloudflare Workers Routes.
NEWSLETTER_WORKER_URL = "https://newsletter.catnbloom.com"

# Fallback address -- used ONLY for CSV rows without an unsub_token (old
# records created before the token was introduced). Once those rows get a
# token (re-subscription or backfill), this branch stops being used on its own.
UNSUBSCRIBE_FALLBACK_EMAIL = "ccatnbloom@gmail.com"


def log(message):
    print(f"[send_newsletter] {message}", flush=True)


def is_dry_run():
    return os.environ.get("DRY_RUN", "false").strip().lower() == "true"


def load_subscribers(path):
    """Reads the CSV, looks up the email and unsub_token columns by header
    name (case-insensitive). Returns a list of dicts
    {"email": ..., "unsub_token": ... or None}.
    """
    if not os.path.exists(path):
        log(f"ERROR: file not found: {path}")
        return []

    subscribers = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            log("ERROR: subscribers.csv is empty or has no headers")
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
                "ERROR: no 'email' column found in subscribers.csv. "
                f"Headers found: {reader.fieldnames}. "
                "Check the file format -- the script will not guess the structure."
            )
            return []

        if token_col is None:
            log(
                "WARNING: no 'unsub_token' column found in subscribers.csv. "
                "All emails will use the mailto unsubscribe fallback. "
                f"Headers found: {reader.fieldnames}."
            )

        for row in reader:
            addr = (row.get(email_col) or "").strip()
            if not addr:
                continue
            token = (row.get(token_col) or "").strip() if token_col else ""
            subscribers.append({"email": addr, "unsub_token": token or None})

    # deduplicate by email, keeping order
    seen = set()
    unique_subscribers = []
    for sub in subscribers:
        key = sub["email"].lower()
        if key not in seen:
            seen.add(key)
            unique_subscribers.append(sub)

    return unique_subscribers


def parse_feed_datetime(raw):
    """Tries to parse pubDate in RFC 822 format (the RSS standard)."""
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
    """Downloads the live feed.xml from the published site. Returns text or None."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "CatnBloom-Newsletter-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=20) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        log(f"ERROR: failed to download {url}: {e}")
        return None
    except Exception as e:
        log(f"ERROR while downloading feed.xml: {e}")
        return None


def load_recent_feed_items(feed_url, window_days):
    """Downloads feed.xml from the site, returns items from the last window_days days."""
    xml_text = fetch_feed_xml(feed_url)
    if xml_text is None:
        return []

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as e:
        log(f"ERROR: failed to parse feed.xml downloaded from {feed_url}: {e}")
        return []
    channel = root.find("channel")
    if channel is None:
        log("ERROR: no <channel> tag found in feed.xml")
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
            log(f"WARNING: could not parse date for item '{title}', skipped")
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
    """Builds the unsubscribe block for the email. Personal link via token if
    available; otherwise a temporary mailto fallback (old records without a token).
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
                f'<tr><td style="padding:16px 0;border-bottom:1px solid #e5e5e5;">'
                f'<a href="{it["link"]}" style="font-size:16px;font-weight:600;'
                f'color:#1D4D54;text-decoration:none;">{it["title"]}</a><br>'
                f'<span style="font-size:13px;color:#666;">'
                f'{it["pub_date"].strftime("%B %d, %Y")}</span>'
                f'<div style="margin-top:10px;font-size:14px;line-height:1.5;color:#333;">'
                f'{it["description"]}</div>'
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


def send_email_via_resend(api_key, to_addr, subject, html_body, unsub_token):
    """Sends an email via the Resend API. Returns (True, None) on success or
    (False, error_text) on failure. Adds a List-Unsubscribe header (RFC 8058)
    for recipients with a token -- Gmail/Yahoo treat this as an independent
    deliverability signal, separate from the text in the email body.
    """
    payload = {
        "from": SENDER_ADDRESS,
        "to": [to_addr],
        "subject": subject,
        "html": html_body,
    }

    if unsub_token:
        unsub_url = f"{NEWSLETTER_WORKER_URL}/unsubscribe?token={unsub_token}"
        payload["headers"] = {
            "List-Unsubscribe": f"<{unsub_url}>",
            "List-Unsubscribe-Post": "List-Unsubscribe=One-Click",
        }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        RESEND_API_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            # REQUIRED by Resend: requests without a User-Agent header are
            # rejected with 403 "error code: 1010" before they are even
            # processed. See https://resend.com/docs/knowledge-base/403-error-1010
            "User-Agent": "CatnBloom-Newsletter-Script/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            response.read()
        return True, None
    except urllib.error.HTTPError as e:
        error_text = e.read().decode("utf-8", errors="replace")
        return False, f"HTTP {e.code}: {error_text}"
    except Exception as e:
        return False, str(e)


def main():
    dry_run = is_dry_run()
    log(f"Starting. DRY_RUN={dry_run}")

    resend_api_key = os.environ.get("RESEND_API_KEY")

    if not resend_api_key:
        log("ERROR: RESEND_API_KEY is not set in the environment. Aborting.")
        sys.exit(1)

    subscribers = load_subscribers(SUBSCRIBERS_PATH)
    log(f"Subscribers found: {len(subscribers)}")
    no_token_count = sum(1 for s in subscribers if not s["unsub_token"])
    if no_token_count:
        log(
            f"WARNING: {no_token_count} out of {len(subscribers)} subscribers "
            "have no unsub_token -- they will get the mailto unsubscribe fallback."
        )

    items = load_recent_feed_items(FEED_URL, WINDOW_DAYS)
    log(f"Fresh items in feed.xml (last {WINDOW_DAYS} days): {len(items)}")

    if not subscribers:
        log("No subscribers -- newsletter not sent.")
        return

    if not items:
        log("No new items -- email not sent (nothing to report).")
        return

    if dry_run:
        log("DRY_RUN is on -- emails will NOT be sent. Recipients below:")
        for sub in subscribers:
            token_status = "with personal unsubscribe link" if sub["unsub_token"] else "with mailto fallback (no token)"
            log(f"  -> {sub['email']} ({token_status})")
        log("Subject: " + EMAIL_SUBJECT)
        return

    sent_count = 0
    failed = []

    for sub in subscribers:
        html_body = build_email_html(items, sub["unsub_token"])
        ok, error_text = send_email_via_resend(
            resend_api_key, sub["email"], EMAIL_SUBJECT, html_body, sub["unsub_token"]
        )
        if ok:
            sent_count += 1
        else:
            log(f"ERROR sending to {sub['email']}: {error_text}")
            failed.append(sub["email"])

    log(f"Done. Sent: {sent_count}/{len(subscribers)}")
    if failed:
        log(f"Failed to send to: {failed}")


if __name__ == "__main__":
    main()
