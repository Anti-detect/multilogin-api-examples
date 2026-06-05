# Architecture — Local API automation

How Multilogin X fits into a multi-account automation stack.

## System diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Your infrastructure                       │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────────────┐ │
│  │  Scheduler   │   │  Your API    │   │  Python / Node jobs  │ │
│  │  (cron/K8s)  │──►│  (optional)  │──►│  this repo's client  │ │
│  └──────────────┘   └──────────────┘   └──────────┬───────────┘ │
└────────────────────────────────────────────────────┼─────────────┘
                                                     │ HTTP localhost
                                                     ▼
┌─────────────────────────────────────────────────────────────────┐
│              Workstation / VPS with GUI (Multilogin X)             │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │ Multilogin Agent  :35000  — Local REST API                  │  │
│  └───────────────────────────────┬─────────────────────────────┘  │
│                                  │                                 │
│     ┌────────────┬───────────────┼───────────────┬────────────┐   │
│     ▼            ▼               ▼               ▼            ▼   │
│  Profile A   Profile B      Profile C       Cloud Phone    ...   │
│  (Mimic)     (Stealthfox)   (Mimic+proxy)   (mobile)             │
└─────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
                          Target platforms (web/apps)
```

## Components

| Layer | Responsibility |
|-------|----------------|
| **Automation scripts** | Orchestrate start → work → stop |
| **Local API** | Profile lifecycle on one machine |
| **Browser cores** | Mimic (Chromium), Stealthfox (Firefox) |
| **Fingerprint engine** | Per-profile isolation |
| **Proxy layer** | Residential / custom per profile |
| **Cloud Phone** | Separate product for native mobile apps |

## Design patterns

### 1. One-shot script

```
start → selenium/playwright → stop
```

Good for: cron jobs, single account checks.

### 2. Context manager (Python)

```python
with client.profile(profile_id) as session:
    # automation
# auto stop
```

Good for: exception-safe cleanup.

### 3. Worker pool

Multiple machines, each running Multilogin agent + worker process.  
**Do not** share one agent across unrelated tenants without isolation.

### 4. Queue-based

Redis/RabbitMQ job → worker picks `profileId` → API start → process task → stop.

## Security boundaries

- API binds to **localhost** — not exposed to internet by default
- Tokens grant full workspace control — rotate regularly
- See [security.md](security.md)

## Scaling limits

| Factor | Limit |
|--------|-------|
| Profiles per machine | RAM/CPU (each browser ~300MB–1GB+) |
| Parallel starts | Serialize or small batches |
| API | Single agent per Multilogin install |

## Related

- [api-reference.md](api-reference.md)
- [security.md](security.md)
- [browser-automation.md](browser-automation.md)

---

**Get Multilogin:** [Pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) · `SAAS50` · `MIN50`
