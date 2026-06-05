"""Demonstrate context-manager profile lifecycle (auto stop)."""

import os
import sys

from load_env import bootstrap_env
from multilogin_client import MultiloginClient, MultiloginError

bootstrap_env()


def main() -> None:
    profile_id = os.environ.get("MULTILOGIN_PROFILE_ID", "")
    if not profile_id:
        print("Set MULTILOGIN_PROFILE_ID", file=sys.stderr)
        sys.exit(1)

    try:
        with MultiloginClient() as client:
            with client.profile(profile_id) as session:
                print("Profile running.")
                print("  CDP URL :", session.cdp_url)
                print("  Port    :", session.debug_port)
                print("  Raw keys:", list(session.response.keys()))
                print("\nDo your automation here, then exit block to auto-stop.")
    except MultiloginError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Profile stopped cleanly.")


if __name__ == "__main__":
    main()
