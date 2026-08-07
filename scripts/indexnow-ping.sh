#!/usr/bin/env bash
# IndexNow ping — auto-pulls URLs from sitemap.xml and submits to Bing/Yandex/IndexNow.
# Run after each Vercel deploy: bash scripts/indexnow-ping.sh
set -euo pipefail

HOST="opauto-clicker.com"
KEY="60970e5e83ece9727d8acbbff9150316"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
SITEMAP="$(dirname "$0")/../sitemap.xml"

# Pull all <loc> URLs from sitemap and build the JSON payload with Python.
PAYLOAD=$(python3 - <<PY
import json, re, sys
with open("${SITEMAP}") as f:
    urls = re.findall(r"<loc>([^<]+)</loc>", f.read())
print(json.dumps({
    "host": "${HOST}",
    "key": "${KEY}",
    "keyLocation": "${KEY_LOCATION}",
    "urlList": urls,
}))
PY
)

echo "Submitting $(python3 -c "import json;print(len(json.loads('''${PAYLOAD}''')['urlList']))") URLs from sitemap.xml"

for endpoint in \
  "https://api.indexnow.org/indexnow" \
  "https://www.bing.com/indexnow"
do
  echo "== ${endpoint} =="
  curl -sS -X POST "${endpoint}" \
    -H "Content-Type: application/json; charset=utf-8" \
    -d "${PAYLOAD}" \
    -w "HTTP %{http_code}\n" || true
done

# Yandex is intentionally omitted — it rejects www.opauto-clicker.com bulk submissions.
# If you want Yandex coverage, submit individual URLs via yandex.com/indexnow?url=<u>&key=<k>
