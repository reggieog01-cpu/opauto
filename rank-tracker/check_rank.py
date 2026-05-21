#!/usr/bin/env python3
"""
Daily Bing-rank tracker for opauto-clicker.com.

Queries DuckDuckGo's HTML endpoint (which uses Bing's search index, so DDG
positions closely mirror Bing positions). Logs the rank of opauto-clicker.com
for each tracked keyword into rank-log.csv.

Run manually:   python3 rank-tracker/check_rank.py
Run via cron:   see rank-tracker/README.md
"""
import csv, os, re, time, json, datetime, urllib.parse, urllib.request

TARGET_DOMAIN = "opauto-clicker.com"
KEYWORDS = [
    "op auto clicker",
    "op auto clicker download",
    "auto clicker windows",
    "free auto clicker",
    "fastest auto clicker",
    "auto clicker for minecraft",
    "cookie clicker auto clicker",
    "how to use op auto clicker",
]
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "rank-log.csv")
WEBHOOK_FILE = os.path.join(SCRIPT_DIR, "webhook.txt")
MAX_RESULTS = 50  # how deep to look


def fetch_results(keyword):
    """POST to DuckDuckGo HTML endpoint, return ordered list of result domains."""
    data = urllib.parse.urlencode({"q": keyword}).encode()
    req = urllib.request.Request(
        "https://html.duckduckgo.com/html/",
        data=data,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17 Safari/605.1.15",
            "Accept": "text/html",
        },
    )
    html = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "ignore")
    # result__a anchors, in document order
    links = re.findall(r'<a[^>]*class="result__a"[^>]*href="([^"]+)"', html)
    domains = []
    for l in links:
        # DDG sometimes wraps in /l/?uddg=...
        m = re.search(r'uddg=([^&]+)', l)
        real = urllib.parse.unquote(m.group(1)) if m else l
        dom = re.sub(r'^https?://(www\.)?', '', real).split('/')[0].lower()
        domains.append(dom)
    return domains


def rank_for(keyword, retries=3):
    """Return 1-based rank of TARGET_DOMAIN, or 0 if not found in MAX_RESULTS."""
    for attempt in range(retries):
        try:
            domains = fetch_results(keyword)
            if not domains:           # rate-limited / empty -> retry
                raise ValueError("empty result set")
            for i, dom in enumerate(domains[:MAX_RESULTS], 1):
                if TARGET_DOMAIN in dom:
                    return i
            return 0  # genuinely not found
        except Exception:
            if attempt < retries - 1:
                time.sleep(25)        # back off before retry
            else:
                return -1             # error sentinel after all retries



def previous_ranks():
    """Read the most recent prior date's ranks from the log: {keyword: rank}."""
    if not os.path.exists(LOG_FILE):
        return {}
    rows = list(csv.DictReader(open(LOG_FILE)))
    if not rows:
        return {}
    dates = sorted({r["date"] for r in rows})
    if not dates:
        return {}
    last_date = dates[-1]
    return {r["keyword"]: int(r["rank"]) for r in rows if r["date"] == last_date}


def fmt_rank(r):
    return f"#{r}" if r > 0 else "not in top 50" if r == 0 else "fetch error"


def trend(old, new):
    """Return an arrow comparing old vs new rank (lower number = better)."""
    if old is None:
        return ""
    if old == new:
        return " (no change)"
    # Treat 0 (not found) as position 999 for comparison
    o = old if old > 0 else 999
    n = new if new > 0 else 999
    if n < o:
        return f" :arrow_up: improved from {fmt_rank(old)}"
    return f" :arrow_down: dropped from {fmt_rank(old)}"


def notify_discord(today, results, prev):
    """Post a summary to the Discord webhook, if configured."""
    if not os.path.exists(WEBHOOK_FILE):
        print("No webhook.txt — skipping Discord notification.")
        return
    url = open(WEBHOOK_FILE).read().strip()
    if not url.startswith("https://discord.com/api/webhooks/"):
        print("webhook.txt does not contain a valid Discord webhook URL.")
        return
    lines = [f"**Rank check — {today}**  ·  opauto-clicker.com"]
    for kw, r in results:
        icon = ":white_check_mark:" if r > 0 else ":small_red_triangle_down:"
        lines.append(f"{icon} {kw} — **{fmt_rank(r)}**{trend(prev.get(kw), r)}")
    payload = {"content": "\n".join(lines)}
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json",
                 "User-Agent": "opauto-rank-tracker/1.0 (+https://www.opauto-clicker.com)"})
    try:
        urllib.request.urlopen(req, timeout=15)
        print("Discord notification sent.")
    except Exception as e:
        print(f"Discord notification failed: {e}")


def main():
    today = datetime.date.today().isoformat()
    prev = previous_ranks()
    new_exists = os.path.exists(LOG_FILE)
    rows = []
    print(f"Rank check — {today}")
    print(f"{'keyword':<32} rank")
    print("-" * 42)
    for kw in KEYWORDS:
        r = rank_for(kw)
        label = (f"#{r}" if r > 0 else
                 "not in top 50" if r == 0 else
                 "FETCH ERROR")
        print(f"{kw:<32} {label}")
        rows.append({"date": today, "keyword": kw, "rank": r})
        time.sleep(18)  # DDG rate-limits aggressively; long delay required

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "keyword", "rank"])
        if not new_exists:
            writer.writeheader()
        writer.writerows(rows)
    print(f"\nLogged {len(rows)} rows to {LOG_FILE}")
    notify_discord(today, [(r["keyword"], r["rank"]) for r in rows], prev)
    print("rank meaning:  >0 = position  |  0 = not in top 50  |  -1 = fetch error")


if __name__ == "__main__":
    main()
