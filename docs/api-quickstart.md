# Multilogin X API Quickstart

Complete reference for automating Multilogin from this repo's Python examples.

| Resource | Link |
|----------|------|
| Postman (official) | [Multilogin X API](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) |
| Help: beginners | [API automation guide](https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide) |
| Python client | [multilogin_client.py](../examples/python/multilogin_client.py) |

---

## Architecture

```
┌─────────────────┐     HTTP (localhost)      ┌──────────────────────┐
│  Your script    │ ────────────────────────► │  Multilogin X Agent  │
│  Python / curl  │   Bearer token            │  port 35000 (default)│
└─────────────────┘                           └──────────┬───────────┘
                                                         │
                                                         ▼
                                              ┌──────────────────────┐
                                              │  Isolated profiles   │
                                              │  Mimic / Stealthfox  │
                                              └──────────────────────┘
```

The API runs **only on your machine** — not in the cloud. The desktop app must be open.

---

## Setup checklist

1. Install [Multilogin X](https://multilogin.com/) and log in
2. Create at least one browser profile in the UI
3. **Settings → Automation →** create token → copy to `MULTILOGIN_TOKEN`
4. Copy profile UUID → `MULTILOGIN_PROFILE_ID`
5. Confirm agent port (default `35000`) → `MULTILOGIN_BASE_URL` if different

Account: [pricing & promo codes](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — `SAAS50`, `MIN50`

---

## Authentication

```http
GET /api/v2/profile HTTP/1.1
Host: 127.0.0.1:35000
Authorization: Bearer YOUR_AUTOMATION_TOKEN
```

Tokens are workspace-scoped. Rotate if leaked; never commit to git.

---

## Core endpoints

> Paths match common Multilogin X Local API usage. If a call fails after an app update, check the [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) for the latest path.

### List profiles

```bash
curl -s -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  "http://127.0.0.1:35000/api/v2/profile"
```

```bash
python list_profiles.py
```

### Start profile

```bash
curl -s -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  "http://127.0.0.1:35000/api/v2/profile/start?profileId=PROFILE_UUID"
```

Typical response includes debugging port or CDP URL (field names vary):

```json
{
  "status": "OK",
  "port": 12345
}
```

Use a **120s+ timeout** — cold starts are slow.

### Stop profile

```bash
curl -s -H "Authorization: Bearer $MULTILOGIN_TOKEN" \
  "http://127.0.0.1:35000/api/v2/profile/stop?profileId=PROFILE_UUID"
```

Always stop profiles in scripts to free RAM and avoid "already running" errors.

---

## Python (recommended)

Install and run from `examples/python/`:

```bash
pip install -r requirements.txt
export MULTILOGIN_TOKEN="..."
export MULTILOGIN_PROFILE_ID="..."
python start_profile.py
```

Import the shared client:

```python
from multilogin_client import MultiloginClient, MultiloginError

client = MultiloginClient()
profiles = client.list_profiles()
session = client.start_profile("uuid")
cdp = client.extract_cdp_url(session)
client.stop_profile("uuid")
```

---

## Automation flow

1. `list_profiles()` — pick UUID  
2. `start_profile(uuid)` — get port / CDP  
3. Connect [Playwright / Selenium / Puppeteer](browser-automation.md)  
4. Run your logic  
5. `stop_profile(uuid)`  

See [browser-automation.md](browser-automation.md) for framework snippets.

---

## Error handling

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Connection refused | Agent not running | Open Multilogin X |
| 401 / 403 | Bad or expired token | Regenerate automation token |
| Timeout on start | Profile or proxy slow | Increase timeout to 180s |
| Profile already running | Previous crash | Stop in UI or call stop endpoint |
| Empty profile list | Wrong workspace / token | Re-login, regenerate token |

More: [troubleshooting.md](troubleshooting.md)

---

## Rate & safety tips

- Serialize starts if you have 50+ profiles — don't spawn 50 parallel starts
- One proxy per profile for production workloads
- Log `profileId` not passwords
- Pin Multilogin app version in team docs when API shape changes

---

## Related

- [Getting started](getting-started.md)
- [Browser automation](browser-automation.md)
- [Troubleshooting](troubleshooting.md)
- [Examples README](../examples/python/README.md)

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
