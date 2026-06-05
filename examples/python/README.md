# Python examples — Multilogin X Local API

Production-oriented client and scripts for the Local API.

## Install

```bash
pip install -r requirements.txt
# optional dev tools
pip install -r requirements-dev.txt
# optional playwright
pip install playwright && playwright install chromium
# optional selenium
pip install selenium
```

## Configure

Copy `.env.example` → `.env` — scripts auto-load via `load_env.py` (uses `python-dotenv` if installed).

Or export manually:

| Variable | Required |
|----------|----------|
| `MULTILOGIN_TOKEN` | Yes |
| `MULTILOGIN_PROFILE_ID` | start / selenium / playwright / session demo |
| `MULTILOGIN_BASE_URL` | No (default `http://127.0.0.1:35000`) |
| `MULTILOGIN_BATCH_LIMIT` | batch_workflow (default `1`) |
| `MULTILOGIN_CDP_URL` | playwright_connect |
| `MULTILOGIN_DEMO_WAIT` | seconds (default `10`) |

## Scripts

| File | Command | Purpose |
|------|---------|---------|
| `health_check.py` | `python health_check.py` | Verify agent + list profiles |
| `list_profiles.py` | `python list_profiles.py` | JSON dump |
| `start_profile.py` | `python start_profile.py` | Start → wait → stop |
| `session_context_demo.py` | `python session_context_demo.py` | Context manager demo |
| `batch_workflow.py` | `python batch_workflow.py` | Multi-profile batch |
| `playwright_connect.py` | `python playwright_connect.py` | Playwright CDP |
| `selenium_connect.py` | `python selenium_connect.py` | Selenium attach |

## Library usage

```python
from multilogin_client import MultiloginClient, ProfileInfo, MultiloginError

with MultiloginClient(timeout=180) as client:
    pid = client.get_profile_id_by_name("Amazon US", exact=False)
    with client.profile(pid) as session:
        ...
```

## Tests

```bash
python -m unittest discover -s tests -v
```

No running Multilogin agent required.

## Repo

[github.com/Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

## Promo

[Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — `SAAS50`, `MIN50`
