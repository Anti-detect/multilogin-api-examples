# API Reference — Multilogin X Local API

> **Source of truth:** [Official Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9).  
> This table reflects common Local API usage; paths may change after app updates.

## Base configuration

| Setting | Value |
|---------|--------|
| Host | `127.0.0.1` (localhost only) |
| Default port | `35000` |
| Protocol | HTTP REST |
| Auth | `Authorization: Bearer <automation_token>` |

## Profile lifecycle

| Method | Path | Params | Description |
|--------|------|--------|-------------|
| `GET` | `/api/v2/profile` | — | List workspace profiles |
| `GET` | `/api/v2/profile/start` | `profileId` | Launch isolated browser |
| `GET` | `/api/v2/profile/stop` | `profileId` | Close browser and free resources |

Additional endpoints (create profile, update proxy, cookies, extensions) are documented in Postman — import the collection into your API client.

## Response fields (start profile)

Field names **vary by Multilogin version**. Client code in this repo checks:

| Field | Used for |
|-------|----------|
| `port`, `debugPort` | Selenium `debuggerAddress` |
| `cdpUrl`, `debuggerUrl` | Playwright / Puppeteer CDP |
| `wsEndpoint` | WebSocket debugger |

Use `MultiloginClient.extract_cdp_url()` or inspect raw JSON.

## HTTP status handling

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Parse JSON body |
| 401 | Unauthorized | Regenerate automation token |
| 403 | Forbidden | Check plan / permissions |
| 404 | Not found | Verify path in Postman |
| 5xx | Server error | Retry; check agent logs |

## Timeouts (recommended)

| Operation | Timeout |
|-----------|---------|
| List profiles | 30s |
| Start profile | 120–180s |
| Stop profile | 30s |
| Playwright connect | After start completes |

## Code mapping

| Operation | Python | Node.js | curl |
|-----------|--------|---------|------|
| List | `list_profiles()` | `listProfiles()` | [curl/README](../examples/curl/README.md) |
| Start | `start_profile()` | `startProfile()` | curl start |
| Stop | `stop_profile()` | `stopProfile()` | curl stop |
| Auto-stop | `with client.profile(id):` | manual | — |

## Official help articles

- [API beginners guide](https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide)
- [Efficient task automation with API](https://multilogin.com/help/en_US/api)
- [Create profile with Postman](https://multilogin.com/help/en_US/how-to-create-a-profile-with-postman)

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
