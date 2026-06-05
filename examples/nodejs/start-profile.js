import { MultiloginClient } from "./client.js";

const profileId = process.env.MULTILOGIN_PROFILE_ID;
const wait = Number(process.env.MULTILOGIN_DEMO_WAIT || 10);

if (!profileId) {
  console.error("Set MULTILOGIN_PROFILE_ID");
  process.exit(1);
}

const client = new MultiloginClient();
console.log("Starting", profileId);
const session = await client.startProfile(profileId);
console.log("Session:", session);
console.log(`Waiting ${wait}s...`);
await new Promise((r) => setTimeout(r, wait * 1000));
console.log("Stopping...");
await client.stopProfile(profileId);
console.log("Done.");
