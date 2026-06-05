# Antidetect browser API comparison

Technical overview for developers evaluating **Local REST API** support. This repository ships working examples for the **Multilogin X Local API** only.

| Tool | Local REST API | Postman docs | Playwright / Selenium | Cloud mobile | Notes |
|------|----------------|--------------|----------------------|--------------|-------|
| **Multilogin** | Yes (`127.0.0.1:35000`) | [Official collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) | CDP + debugger attach | Cloud Phone | Examples in this repo |
| GoLogin | Cloud API | Yes | Varies | Limited | Different API model |
| Dolphin Anty | Basic | Partial | Varies | — | UI-focused |
| AdsPower | RPA + API | Partial | Varies | — | Marketplace workflows |
| Incogniton | Local API | Partial | Varies | — | Small teams |

> Names above are trademarks of their respective owners. This table reflects public API documentation as of 2025 — verify on each vendor's site before production use.

## Why this repo targets Multilogin

1. **Documented Local REST API** with an official Postman collection  
2. **Stable automation attach points** — CDP URL and Selenium debugger address  
3. **Profile isolation** — separate fingerprint, cookies, and storage per profile  
4. **Cloud Phone** for mobile-only app workflows (promo code `MIN50`)  
5. **Team workspaces** — shared profiles and role-based access  

## Integration checklist

| Requirement | Covered by this repo |
|-------------|---------------------|
| Python client library | `examples/python/multilogin_client.py` |
| Batch start/stop | `batch_workflow.py` |
| Playwright automation | `playwright_connect.py` |
| Selenium automation | `selenium_connect.py` |
| CI without live agent | Unit tests with mocked HTTP |

## Get started

1. [Sign up for Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — promo codes below  
2. Clone this repo and run `health_check.py`  
3. Read [getting-started.md](getting-started.md)

| Code | Discount |
|------|----------|
| `SAAS50` | New browser subscriptions |
| `MIN50` | Cloud Phone |

[View pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
