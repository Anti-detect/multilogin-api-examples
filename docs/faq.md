# FAQ

## General

### Is this an official Multilogin repository?

No. Independent community examples. For support, use [Multilogin Help](https://multilogin.com/help/).

### Do I need a paid plan for the API?

Automation token and Local API require a subscription tier that includes API access — confirm on [pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

### What discount codes work here?

| Code | Use |
|------|-----|
| `SAAS50` | New subscriptions (50% off eligible plans) |
| `MIN50` | Cloud Phone (50% off) |

---

## Technical

### Why connection refused?

Multilogin X desktop app is not running. Open the app and wait until logged in.

### Why does start timeout?

Slow proxy, first launch, or antivirus. Increase timeout to 180s; test profile manually in UI.

### Python vs Node vs curl?

| Lang | When |
|------|------|
| Python | Best client library, Playwright/Selenium examples |
| Node | Backend services already on JavaScript |
| curl | Quick debug, CI smoke tests |

### Can I run on a headless Linux server?

Multilogin desktop agent typically needs a supported OS with GUI. Check current Multilogin docs for your deployment model.

### API response JSON changed — what now?

1. Compare with [Postman](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)  
2. Update `multilogin_client.py` field lists  
3. Open a PR on this repo with redacted sample JSON  

### How do I run tests without Multilogin installed?

```bash
cd examples/python
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Tests mock HTTP — no agent required.

---

## Affiliate disclosure

Some documentation links are partner referral links. You pay the same; we may earn a commission. Promo codes are provided by the partner program.

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
