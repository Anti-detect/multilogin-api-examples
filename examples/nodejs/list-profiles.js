import { MultiloginClient } from "./client.js";

try {
  const client = new MultiloginClient();
  const profiles = await client.listProfiles();
  console.log(JSON.stringify(profiles, null, 2));
} catch (e) {
  console.error(e.message);
  process.exit(1);
}
