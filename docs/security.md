# Security best practices

Guidelines when automating Multilogin via the Local API.

## Token hygiene

| Do | Don't |
|----|-------|
| Store tokens in env vars / secret manager | Commit tokens to git |
| Rotate after team member leaves | Share one token in Slack |
| Use separate tokens per environment | Log full Bearer header |

```bash
# .gitignore already excludes .env
MULTILOGIN_TOKEN=...
```

## Network exposure

- Local API is **127.0.0.1** — do not port-forward to the public internet
- If using remote desktop to a VPS, tunnel via VPN/SSH instead of exposing :35000

## Profile & account data

- Each profile holds cookies and session data — treat disks as sensitive
- Encrypt workstation drives where Multilogin stores profiles
- Backup profiles through official Multilogin mechanisms, not random folder copies

## Automation code

- Validate `profileId` before start — avoid injection in custom wrappers
- Rate-limit starts to prevent agent crashes (DoS yourself)
- Log profile IDs, not passwords or 2FA seeds

## Compliance

- Respect platform Terms of Service for target sites
- This repo is educational — you are responsible for lawful use
- Not affiliated with Multilogin Ltd.

## Incident response

1. Revoke automation token in app settings  
2. Change workspace password + enable 2FA  
3. Audit git history for accidental token commits (`git log -S TOKEN_PREFIX`)

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
