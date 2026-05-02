#!/usr/bin/env bash
# IndexNow ping — submits the sitemap-listed URLs to Bing/Yandex/Naver.
# Run after each Vercel deploy: bash scripts/indexnow-ping.sh
set -euo pipefail

HOST="opauto-clicker.com"
KEY="60970e5e83ece9727d8acbbff9150316"
KEY_LOCATION="https://${HOST}/${KEY}.txt"

URLS=(
  "https://${HOST}/"
  "https://${HOST}/download"
  "https://${HOST}/faq"
  "https://${HOST}/about"
  "https://${HOST}/cps-test"
  "https://${HOST}/how-to-use-auto-clicker"
  "https://${HOST}/minecraft-auto-clicker"
  "https://${HOST}/roblox-auto-clicker"
  "https://${HOST}/windows-11-auto-clicker"
  "https://${HOST}/fastest-auto-clicker"
  "https://${HOST}/safe-auto-clicker"
  "https://${HOST}/auto-clicker-for-games"
  "https://${HOST}/op-auto-clicker-vs-gs-auto-clicker"
  "https://${HOST}/op-auto-clicker-alternatives"
  "https://${HOST}/privacy"
  "https://${HOST}/terms"
)

JSON_URLS=$(printf '"%s",' "${URLS[@]}")
JSON_URLS="[${JSON_URLS%,}]"

PAYLOAD=$(cat <<EOF
{"host":"${HOST}","key":"${KEY}","keyLocation":"${KEY_LOCATION}","urlList":${JSON_URLS}}
EOF
)

for endpoint in \
  "https://api.indexnow.org/indexnow" \
  "https://www.bing.com/indexnow" \
  "https://yandex.com/indexnow"
do
  echo "Pinging ${endpoint}"
  curl -sS -X POST "${endpoint}" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "${PAYLOAD}" \
    -w "\n  HTTP %{http_code}\n" || true
done
