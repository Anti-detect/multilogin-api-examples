"""List browser profiles via Multilogin X Local API."""

import json
import sys

from load_env import bootstrap_env
from multilogin_client import MultiloginClient, MultiloginError

bootstrap_env()


def main() -> None:
    try:
        client = MultiloginClient()
        profiles = client.list_profiles()
    except MultiloginError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    if not profiles:
        print("No profiles returned. Check token and that the agent is running.")
        return

    print(f"Profiles ({len(profiles)}):\n")
    for i, profile in enumerate(profiles, 1):
        if isinstance(profile, dict):
            pid = profile.get("id") or profile.get("profileId") or profile.get("uuid") or "?"
            name = profile.get("name") or profile.get("profileName") or ""
            print(f"  {i}. {name}  id={pid}")
        else:
            print(f"  {i}. {profile}")

    print("\nFull JSON:")
    print(json.dumps(profiles, indent=2, default=str))


if __name__ == "__main__":
    main()
