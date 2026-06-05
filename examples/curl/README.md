# curl examples

Multilogin X must be running. Requires `curl` and `jq` (optional).

## Shell script

```bash
export MULTILOGIN_TOKEN="your-token"
chmod +x profiles.sh
./profiles.sh list
./profiles.sh start PROFILE_UUID
./profiles.sh stop PROFILE_UUID
```

## Manual

```bash
export MULTILOGIN_TOKEN="your-token"
BASE="${MULTILOGIN_BASE_URL:-http://127.0.0.1:35000}"

curl -s -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  "$BASE/api/v2/profile" | jq .

curl -s -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  "$BASE/api/v2/profile/start?profileId=PROFILE_UUID"

curl -s -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  "$BASE/api/v2/profile/stop?profileId=PROFILE_UUID"
```

Python · Node: [../python/](../python/) · [../nodejs/](../nodejs/)
