#!/usr/bin/env bash
# Multilogin Local API — curl helpers
# Usage: export MULTILOGIN_TOKEN=... && ./profiles.sh list

set -euo pipefail

BASE="${MULTILOGIN_BASE_URL:-http://127.0.0.1:35000}"
TOKEN="${MULTILOGIN_TOKEN:?Set MULTILOGIN_TOKEN}"
AUTH=(-H "Authorization: Bearer ${TOKEN}")

cmd="${1:-}"

case "$cmd" in
  list)
    curl -s "${AUTH[@]}" "${BASE}/api/v2/profile" | jq .
    ;;
  start)
    PID="${2:?Usage: ./profiles.sh start PROFILE_UUID}"
    curl -s "${AUTH[@]}" "${BASE}/api/v2/profile/start?profileId=${PID}"
    ;;
  stop)
    PID="${2:?Usage: ./profiles.sh stop PROFILE_UUID}"
    curl -s "${AUTH[@]}" "${BASE}/api/v2/profile/stop?profileId=${PID}"
    ;;
  *)
    echo "Usage: $0 list|start|stop [profileId]"
    exit 1
    ;;
esac
