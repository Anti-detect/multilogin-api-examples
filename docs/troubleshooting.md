# Troubleshooting — Multilogin Local API

Solutions for common issues when running [examples/python](../examples/python/).

---

## Connection refused / Cannot reach agent

**Cause:** Multilogin X desktop app is not running, or wrong port.

**Fix:**

1. Open Multilogin X and wait until fully logged in
2. Check agent port in settings (default `35000`)
3. Set `MULTILOGIN_BASE_URL=http://127.0.0.1:YOUR_PORT`
4. Test: `curl http://127.0.0.1:35000` (any response means port is open)

---

## 401 Unauthorized / 403 Forbidden

**Cause:** Missing, wrong, or revoked automation token.

**Fix:**

1. App → **Settings → Automation** → generate new token
2. Update `MULTILOGIN_TOKEN` (no quotes/spaces in shell)
3. Ensure your plan includes API access

---

## Start times out

**Cause:** Heavy proxy, first launch, or antivirus slowing browser.

**Fix:**

- Increase timeout in `MultiloginClient(timeout=180)`
- Test profile manually in UI first
- Try without custom proxy to isolate issue

---

## Profile already running

**Cause:** Previous script exited without `stop_profile()`.

**Fix:**

1. Stop profile in Multilogin UI, or
2. Run `python start_profile.py` after fixing — it calls stop at the end, or
3. `curl` the stop endpoint with same `profileId`

---

## list_profiles returns empty or unexpected JSON

**Cause:** API response shape changed between Multilogin versions.

**Fix:**

1. Run `python list_profiles.py` and read raw JSON
2. Compare with [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
3. Open an issue on this repo with redacted JSON sample

`MultiloginClient.list_profiles()` checks keys: `profiles`, `data`, `value`, `items`.

---

## Playwright cannot connect to CDP

**Cause:** Wrong URL or profile not fully started.

**Fix:**

1. Print full `start_profile()` response
2. Set `MULTILOGIN_CDP_URL` explicitly
3. Wait 2–5s after start before connecting
4. Install browsers: `playwright install chromium`

---

## Works on Windows but not Linux

**Cause:** Agent path, firewall, or headless server without display.

**Fix:**

- Multilogin desktop agent is required — typical install is workstation with GUI
- Allow localhost firewall rule for port 35000
- For servers, check Multilogin docs for supported environments

---

## Still stuck?

- [Multilogin Help Center](https://multilogin.com/help/)
- [API beginners guide](https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide)
- Open a [GitHub issue](https://github.com/Anti-detect/multilogin-api-examples/issues) (no tokens in screenshots)

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
