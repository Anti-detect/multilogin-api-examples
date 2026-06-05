# Multilogin API Examples — Antidetect Browser Automation

[![CI](https://github.com/Anti-detect/multilogin-api-examples/actions/workflows/ci.yml/badge.svg)](https://github.com/Anti-detect/multilogin-api-examples/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-3776ab.svg)](examples/python/)
[![Node 18+](https://img.shields.io/badge/node-18+-339933.svg)](examples/nodejs/)
[![Maintainer](https://img.shields.io/badge/maintainer-Anti--detect-24292f.svg)](https://github.com/Anti-detect)

> **Disclaimer:** Independent open-source examples by [@Anti-detect](https://github.com/Anti-detect) — not affiliated with Multilogin Ltd. Some pricing links are partner referrals (no extra cost to you).

**Open-source SDK-style examples** for [Multilogin X](https://multilogin.com/) **Local REST API** — antidetect browser profiles, fingerprint isolation, multi-account management, Playwright/Selenium/Puppeteer automation, batch workflows, and CI-ready unit tests.

| | |
|---|---|
| **Repository** | [github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples) |
| **Pricing** | [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) |
| **`SAAS50`** | 50% off new browser subscriptions |
| **`MIN50`** | 50% off Cloud Phone |
| **Official API** | [Postman collection](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) |
| **Documentation** | [docs/index.md](docs/index.md) |

### Languages / 语言 / Языки

| Language | Guide |
|----------|-------|
| English | [docs/index.md](docs/index.md) |
| Tiếng Việt | [docs/vi/README.md](docs/vi/README.md) |
| 中文 | [docs/zh/README.md](docs/zh/README.md) |
| Русский | [docs/ru/README.md](docs/ru/README.md) |
| Português (BR) | [docs/pt/README.md](docs/pt/README.md) |

---

## Table of contents

- [Features](#features)
- [Quick start](#quick-start)
- [Project structure](#project-structure)
- [Examples catalog](#examples-catalog)
- [Python client](#python-client)
- [Documentation](#documentation)
- [Development](#development)
- [Promo codes](#promo-codes)

---

## Features

- **Reusable clients** — Python (`MultiloginClient`) + Node (`client.js`)
- **Context manager** — auto `stop` on exit (`with client.profile(id)`)
- **Batch workflows** — start/stop multiple antidetect profiles safely
- **Browser automation** — Playwright CDP, Selenium debugger attach, Puppeteer
- **Health check** — verify agent + token before production runs
- **Unit tests** — mocked HTTP, runs in CI without Multilogin installed
- **curl + Node + Python** — pick your stack
- **Multilingual docs** — EN, VI, ZH, RU, PT

---

## Quick start

### 1. Prerequisites

- [Multilogin X](https://multilogin.com/) installed, logged in, agent running
- Automation token: **Settings → Automation → Generate**
- Profile UUID from the app

### 2. Python (recommended)

```bash
git clone https://github.com/Anti-detect/multilogin-api-examples.git
cd multilogin-api-examples/examples/python
pip install -r requirements.txt
cp .env.example .env   # edit token + profile id
```

**Windows PowerShell:**

```powershell
$env:MULTILOGIN_TOKEN="your-token"
$env:MULTILOGIN_PROFILE_ID="profile-uuid"
python health_check.py
python list_profiles.py
python start_profile.py
```

**Linux / macOS:**

```bash
export MULTILOGIN_TOKEN="your-token"
export MULTILOGIN_PROFILE_ID="profile-uuid"
make -C ../.. health
```

### 3. Node.js

```bash
cd examples/nodejs
$env:MULTILOGIN_TOKEN="your-token"
npm run health
npm run list
```

---

## Project structure

```
multilogin-api-examples/
├── .github/workflows/ci.yml
├── config/links.json             ← affiliate & repo URLs (single source)
├── docs/
│   ├── index.md                  ← documentation hub
│   ├── comparison.md
│   ├── vi/  zh/  ru/  pt/        ← multilingual guides
├── examples/
│   ├── python/                   # SDK-style client + 8 scripts
│   ├── nodejs/
│   └── curl/
├── scripts/
├── Makefile
```

---

## Examples catalog

### Python

| Script | Description |
|--------|-------------|
| [`multilogin_client.py`](examples/python/multilogin_client.py) | Core library — import into your projects |
| [`health_check.py`](examples/python/health_check.py) | Agent + token + profile count |
| [`list_profiles.py`](examples/python/list_profiles.py) | List profiles (JSON) |
| [`start_profile.py`](examples/python/start_profile.py) | Start → wait → stop |
| [`session_context_demo.py`](examples/python/session_context_demo.py) | `with client.profile()` auto cleanup |
| [`batch_workflow.py`](examples/python/batch_workflow.py) | Start/stop N profiles |
| [`playwright_connect.py`](examples/python/playwright_connect.py) | Playwright over CDP |
| [`selenium_connect.py`](examples/python/selenium_connect.py) | Selenium debugger attach |

### Node.js · curl

| Path | Description |
|------|-------------|
| [`examples/nodejs/`](examples/nodejs/) | `client.js`, health, list, start, puppeteer |
| [`examples/curl/profiles.sh`](examples/curl/profiles.sh) | Shell helper |

---

## Python client

```python
from multilogin_client import MultiloginClient, MultiloginError

with MultiloginClient() as client:
    assert client.ping()
    for p in client.list_profiles_normalized():
        print(p.id, p.name)
    with client.profile("your-profile-uuid") as session:
        print("CDP:", session.cdp_url)
        print("Selenium:", session.selenium_address)
```

| Env variable | Required | Default |
|--------------|----------|---------|
| `MULTILOGIN_TOKEN` | Yes | — |
| `MULTILOGIN_PROFILE_ID` | For start scripts | — |
| `MULTILOGIN_BASE_URL` | No | `http://127.0.0.1:35000` |
| `MULTILOGIN_BATCH_LIMIT` | No | `1` |
| `MULTILOGIN_CDP_URL` | Playwright | — |

---

## Documentation

| Guide | Description |
|-------|-------------|
| [docs/index.md](docs/index.md) | Full documentation index |
| [docs/getting-started.md](docs/getting-started.md) | Install → first API call |
| [docs/api-quickstart.md](docs/api-quickstart.md) | Auth, endpoints, patterns |
| [docs/api-reference.md](docs/api-reference.md) | Endpoint reference table |
| [docs/architecture.md](docs/architecture.md) | System design & scaling |
| [docs/browser-automation.md](docs/browser-automation.md) | Playwright, Selenium, Puppeteer |
| [docs/comparison.md](docs/comparison.md) | Antidetect browser API comparison |
| [docs/security.md](docs/security.md) | Tokens, network, compliance |
| [docs/troubleshooting.md](docs/troubleshooting.md) | Error fixes |
| [docs/faq.md](docs/faq.md) | Common questions |

---

## Development

```bash
make install && make test
```

See [CONTRIBUTING.md](CONTRIBUTING.md) · [SECURITY.md](SECURITY.md)

**Report issues:** [github.com/Anti-detect/multilogin-api-examples/issues](https://github.com/Anti-detect/multilogin-api-examples/issues)

---

## Promo codes

| Code | Product |
|------|---------|
| `SAAS50` | New browser subscriptions |
| `MIN50` | Cloud Phone |

[View pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## GitHub Topics

`multilogin` `multilogin-api` `antidetect-browser` `anti-detect` `browser-fingerprint` `browser-automation` `multi-account` `fingerprint-browser` `playwright` `selenium` `puppeteer` `python` `nodejs` `rest-api` `cloud-phone` `web-scraping` `e-commerce-automation`

---

## License

[MIT](LICENSE) — examples and docs only. Multilogin® is a trademark of Multilogin Ltd.
