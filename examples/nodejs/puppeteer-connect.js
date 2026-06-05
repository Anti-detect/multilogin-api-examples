/**
 * Puppeteer attach to Multilogin profile (puppeteer-core).
 * npm install puppeteer-core
 * MULTILOGIN_PROFILE_ID=... MULTILOGIN_TOKEN=... node puppeteer-connect.js
 */

import { MultiloginClient } from "./client.js";

const profileId = process.env.MULTILOGIN_PROFILE_ID;
const wait = Number(process.env.MULTILOGIN_DEMO_WAIT || 5);

if (!profileId) {
  console.error("Set MULTILOGIN_PROFILE_ID");
  process.exit(1);
}

let puppeteer;
try {
  puppeteer = await import("puppeteer-core");
} catch {
  console.error("npm install puppeteer-core");
  process.exit(1);
}

const client = new MultiloginClient();
let started = false;

try {
  console.log("Starting profile...");
  const session = await client.startProfile(profileId);
  started = true;
  const port = session.port || session.debugPort;
  const browserURL = process.env.MULTILOGIN_BROWSER_URL || (port ? `http://127.0.0.1:${port}` : null);
  if (!browserURL) {
    console.error("No port in response. Set MULTILOGIN_BROWSER_URL manually.", session);
    process.exit(1);
  }
  console.log("Connecting Puppeteer to", browserURL);
  const browser = await puppeteer.default.connect({ browserURL });
  const pages = await browser.pages();
  const page = pages[0] || (await browser.newPage());
  await page.goto("https://example.com");
  console.log("Title:", await page.title());
  await browser.disconnect();
  console.log(`Waiting ${wait}s...`);
  await new Promise((r) => setTimeout(r, wait * 1000));
} finally {
  if (started) {
    console.log("Stopping profile...");
    await client.stopProfile(profileId);
  }
}
console.log("Done.");
