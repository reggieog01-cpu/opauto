# Rank Tracker

Free daily Bing-rank tracker for opauto-clicker.com.

## How it works

`check_rank.py` queries DuckDuckGo's HTML endpoint, which runs on Bing's
search index — so DuckDuckGo positions closely mirror Bing positions.
Bing itself blocks scrapers; DuckDuckGo does not (with polite delays).

It checks 8 keywords and appends the rank of `opauto-clicker.com` to
`rank-log.csv` with the date.

## Run it manually

```bash
python3 rank-tracker/check_rank.py
```

Takes ~3 minutes (18-second delay between queries — DuckDuckGo rate-limits
aggressively, so the delay is mandatory).

## rank-log.csv format

```
date,keyword,rank
2026-05-21,op auto clicker,0
```

Rank values:
- **positive number** = search position (1 = top, lower is better)
- **0** = not found in top 50
- **-1** = fetch error (network / rate-limit after retries)

## Automate it (daily, macOS)

Add a cron entry so it runs every morning at 9 AM:

```bash
crontab -e
```

Add this line (adjust the path if the repo moved):

```
0 9 * * * cd "/Applications/op auto/opauto" && /usr/bin/python3 rank-tracker/check_rank.py >> rank-tracker/cron.log 2>&1
```

Save and exit. macOS will prompt once for permission to run cron — allow it.

## View your trend

```bash
# Quick look at one keyword over time
grep "op auto clicker," rank-tracker/rank-log.csv

# Full log
column -t -s, rank-tracker/rank-log.csv
```

## The authoritative source is still Bing Webmaster Tools

This script is a convenient daily proxy. The *real* numbers are in
**Bing Webmaster Tools → Search Performance → Queries**, which gives the
true Bing average position (lagged 2-3 days). Use this script for daily
trend-watching; use BWT for the official record.

## Why DuckDuckGo as a proxy

| | Bing direct | DuckDuckGo HTML |
|---|---|---|
| Scrapeable | No (bot-blocked) | Yes (with delays) |
| Search index | Bing | Bing (licensed) |
| Position accuracy vs Bing | n/a | Very close, not identical |
| Personalization | Heavy | Minimal |

DuckDuckGo strips personalization, so it's actually a *cleaner* read of
"where do I rank for a neutral user" than searching Bing while logged in.
