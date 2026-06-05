# Getting Started with Multilogin

From zero to your first automated profile start — then use [api-quickstart.md](api-quickstart.md) and [examples/python](../examples/python/).

> Examples repo: [github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

---

## 1. Account & install

| Step | Action |
|------|--------|
| Sign up | [Pricing page](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — code **`SAAS50`** for new plans |
| Download | [multilogin.com](https://multilogin.com/) → Multilogin X for your OS |
| Login | Use your workspace email |

---

## 2. Create a browser profile

1. Workspace → **Create profile**
2. Browser: **Mimic** (Chromium) or **Stealthfox** (Firefox)
3. Fingerprint: random or manual (OS, screen, timezone, language)
4. Proxy: built-in residential (paid plans) or custom SOCKS5/HTTP

Copy the **profile UUID** from profile settings — needed for `MULTILOGIN_PROFILE_ID`.

---

## 3. Enable API access

1. **Settings → Automation**
2. Click **Generate automation token**
3. Save token as `MULTILOGIN_TOKEN` (never share publicly)

The agent listens at `http://127.0.0.1:35000` while the app runs.

---

## 4. Verify fingerprint (recommended)

1. Start profile in UI
2. Open [pixelscan.net](https://pixelscan.net/)
3. Green consistency, no WebRTC leak

---

## 5. Run your first API script

```bash
cd examples/python
pip install -r requirements.txt
```

```powershell
# Windows
$env:MULTILOGIN_TOKEN="your-token"
$env:MULTILOGIN_PROFILE_ID="profile-uuid"
python list_profiles.py
python start_profile.py
```

Success = profile opens, waits, closes. Next: [browser-automation.md](browser-automation.md).

---

## Best practices

| Rule | Reason |
|------|--------|
| One profile per account | Prevents platform linking |
| One proxy per profile | IP isolation |
| Match timezone to proxy country | Fingerprint consistency |
| Stop profiles in scripts | Frees resources, avoids lock |

---

## Next steps

| Doc | Topic |
|-----|-------|
| [api-quickstart.md](api-quickstart.md) | All endpoints & Python client |
| [browser-automation.md](browser-automation.md) | Playwright, Selenium |
| [cloud-phone.md](cloud-phone.md) | Mobile + `MIN50` |
| [use-cases.md](use-cases.md) | E-commerce, ads, affiliate |

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
