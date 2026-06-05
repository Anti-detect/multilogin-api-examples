# Browser automation with Multilogin API

After `start_profile()` returns, attach your favorite automation framework to the running browser.

---

## Playwright (Python)

Included in this repo: [playwright_connect.py](../examples/python/playwright_connect.py)

```bash
pip install playwright
playwright install chromium
export MULTILOGIN_TOKEN="..."
export MULTILOGIN_PROFILE_ID="..."
python playwright_connect.py
```

Manual CDP URL:

```python
from playwright.sync_api import sync_playwright

cdp_url = "http://127.0.0.1:PORT"  # from start response

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(cdp_url)
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

`MultiloginClient.extract_cdp_url()` tries common response keys — if it returns `None`, inspect the JSON from `start_profile()` and set `MULTILOGIN_CDP_URL`.

---

## Selenium (Python)

When the start response includes a WebDriver port:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.debugger_address = "127.0.0.1:PORT"  # from Multilogin start response

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

You may need a ChromeDriver version compatible with the Mimic core version inside Multilogin — check Multilogin help for your release.

---

## Puppeteer (Node.js)

```javascript
const puppeteer = require("puppeteer-core");

const browser = await puppeteer.connect({
  browserURL: "http://127.0.0.1:PORT",
});
const pages = await browser.pages();
const page = pages[0] || (await browser.newPage());
await page.goto("https://example.com");
console.log(await page.title());
await browser.disconnect();
```

Start the profile via API first (curl or your own HTTP client).

---

## Recommended pattern

```
API start  →  attach automation  →  work  →  quit driver  →  API stop
```

Always call **stop** via API after `driver.quit()` / `browser.close()` so the profile does not stay locked.

---

## Official references

- [Multilogin X API (Postman)](https://documenter.getpostman.com/view/28533318/2s946h9Cv9)
- [API beginners guide](https://multilogin.com/help/en_US/multilogin-x-api-beginners-guide)

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
