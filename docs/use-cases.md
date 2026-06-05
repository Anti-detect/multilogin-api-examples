# Multilogin Use Cases

Practical scenarios where antidetect browser isolation helps — and how to set up safely.

## E-commerce & Marketplace

**Amazon / eBay / Etsy sellers** running multiple stores or buyer accounts.

- One profile per seller account
- Residential proxy matching store region
- Separate payment and email per profile
- Never log into two seller accounts from the same profile

## Digital Marketing & Ads

**Facebook Ads, Google Ads, TikTok Ads** agencies managing client accounts.

- Client-isolated profiles prevent accidental cross-contamination
- Team members access shared workspace with role permissions
- API automation for bulk profile provisioning

## Affiliate Marketing

**Multiple affiliate accounts** across networks (CJ, Impact, native platforms).

- Geographic profiles for geo-targeted offers
- Cookie isolation prevents commission attribution conflicts
- Fingerprint consistency reduces manual review triggers

## Social Media Management

**Managing brand accounts** across regions or niches.

- Separate profiles per account cluster
- Cloud Phone for mobile-first platforms — see [cloud-phone.md](cloud-phone.md)
- Consistent posting timezone aligned with proxy location

## Web Scraping & QA (Legitimate)

**Testing geo-specific UX** or running authenticated scrapers with consent.

- Profile per test environment
- API-driven start/stop for CI pipelines
- See [api-quickstart.md](api-quickstart.md)

## Data Collection & Research

Researchers studying platform behavior across regions.

- Document ethical boundaries and ToS compliance
- Use profiles only for permitted research scope

---

## Setup Checklist (Any Use Case)

1. [ ] Create dedicated profile per account
2. [ ] Assign unique proxy per profile
3. [ ] Align timezone, language, and geo
4. [ ] Verify fingerprint on Pixelscan before go-live
5. [ ] Store credentials securely (password manager, not plain text in repo)
6. [ ] Enable workspace 2FA

## Automate with API

Most use cases above scale with scripts:

1. [Getting started](getting-started.md) — token + profile UUID  
2. [API quickstart](api-quickstart.md) — start/stop/list  
3. [examples/python](../examples/python/) — copy `multilogin_client.py` into your project  

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
