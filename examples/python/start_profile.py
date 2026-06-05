"""
Start a Multilogin profile, wait briefly, then stop it.

Usage (Windows PowerShell):
  $env:MULTILOGIN_TOKEN="your-token"
  $env:MULTILOGIN_PROFILE_ID="profile-uuid"
  python start_profile.py
"""

import os
import sys
import time

from load_env import bootstrap_env
from multilogin_client import MultiloginClient, MultiloginError

bootstrap_env()


def main() -> None:
    profile_id = os.environ.get("MULTILOGIN_PROFILE_ID", "")
    if not profile_id:
        print("Set MULTILOGIN_PROFILE_ID to a profile UUID.", file=sys.stderr)
        sys.exit(1)

    try:
        client = MultiloginClient()
    except MultiloginError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Starting profile {profile_id}...")
    try:
        session = client.start_profile(profile_id)
    except MultiloginError as exc:
        print(f"Start failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Session:", session)
    cdp = client.extract_cdp_url(session)
    if cdp:
        print(f"CDP hint: {cdp}")
        print("For Playwright: set MULTILOGIN_CDP_URL and run playwright_connect.py")

    wait = int(os.environ.get("MULTILOGIN_DEMO_WAIT", "10"))
    print(f"Running {wait}s (override with MULTILOGIN_DEMO_WAIT)...")
    time.sleep(wait)

    print(f"Stopping profile {profile_id}...")
    try:
        client.stop_profile(profile_id)
    except MultiloginError as exc:
        print(f"Stop failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Done.")


if __name__ == "__main__":
    main()
