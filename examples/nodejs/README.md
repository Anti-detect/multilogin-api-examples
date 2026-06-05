# Node.js examples

Requires **Node.js 18+** (native `fetch`). Multilogin X agent must be running.

```bash
# Windows PowerShell
$env:MULTILOGIN_TOKEN="your-token"
$env:MULTILOGIN_PROFILE_ID="profile-uuid"

npm run health
npm run list
npm run start
npm run puppeteer   # requires: npm install puppeteer-core
```

Or directly:

```bash
node health-check.js
node list-profiles.js
node start-profile.js
```

Import `client.js` in your automation backend:

```javascript
import { MultiloginClient } from "./client.js";

const client = new MultiloginClient();
const profiles = await client.listProfiles();
const session = await client.startProfile(profiles[0].id);
await client.stopProfile(profiles[0].id);
```

Repo: [Anti-detect/multilogin-api-examples](https://github.com/Anti-detect/multilogin-api-examples)

Pricing & codes: [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — `SAAS50`, `MIN50`
