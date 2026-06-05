"""
Connect Playwright to a running Multilogin profile over CDP.

Steps:
  1. python start_profile.py   (in another terminal, or start profile in app)
  2. Copy CDP URL from output into MULTILOGIN_CDP_URL
  3. pip install playwright && playwright install chromium
  4. python playwright_connect.py
"""

import os
import sys

from load_env import bootstrap_env
from multilogin_client import MultiloginClient, MultiloginError

bootstrap_env()


def main() -> None:
    cdp_url = os.environ.get("MULTILOGIN_CDP_URL", "")
    profile_id = os.environ.get("MULTILOGIN_PROFILE_ID", "")

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Install: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    client = None
    started_here = False

    if not cdp_url and profile_id:
        try:
            client = MultiloginClient()
            print(f"Starting profile {profile_id} for Playwright...")
            session = client.start_profile(profile_id)
            cdp_url = client.extract_cdp_url(session) or ""
            started_here = True
            print("Start response:", session)
        except MultiloginError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

    if not cdp_url:
        print(
            "Set MULTILOGIN_CDP_URL (from start_profile output) or "
            "MULTILOGIN_PROFILE_ID to auto-start.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Connecting Playwright to {cdp_url}...")
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cdp_url)
        if browser.contexts:
            context = browser.contexts[0]
            page = context.pages[0] if context.pages else context.new_page()
        else:
            context = browser.new_context()
            page = context.new_page()

        page.goto("https://browserleaks.com/javascript")
        title = page.title()
        print(f"Page title: {title}")

        browser.close()

    if started_here and client and profile_id:
        print(f"Stopping profile {profile_id}...")
        client.stop_profile(profile_id)

    print("Done.")


if __name__ == "__main__":
    main()
