import { MultiloginClient } from "./client.js";

const base = process.env.MULTILOGIN_BASE_URL || "http://127.0.0.1:35000";
console.log("Multilogin health check");
console.log("  Base:", base);

try {
  const client = new MultiloginClient();
  const ok = await client.ping();
  if (!ok) {
    console.error("  Agent: UNREACHABLE");
    process.exit(1);
  }
  const profiles = await client.listProfiles();
  console.log("  Agent: OK");
  console.log(`  Profiles: ${profiles.length}`);
  profiles.slice(0, 5).forEach((p, i) => {
    const id = p.id || p.profileId || "?";
    const name = p.name || p.profileName || "";
    console.log(`    ${i + 1}. ${name} [${id}]`);
  });
  console.log("\nReady.");
} catch (e) {
  console.error("  Error:", e.message);
  process.exit(1);
}
