"""Verify Multilogin agent connectivity and token validity."""

import sys

from load_env import bootstrap_env
from multilogin_client import MultiloginClient, MultiloginError

bootstrap_env()


def main() -> int:
    import os

    print("Multilogin X — health check\n")
    base = os.environ.get("MULTILOGIN_BASE_URL", "http://127.0.0.1:35000")
    print(f"  Base URL : {base}")

    try:
        with MultiloginClient() as client:
            if not client.ping():
                print("  Agent    : UNREACHABLE")
                return 1
            print("  Agent    : OK")

            profiles = client.list_profiles_normalized()
            print(f"  Profiles : {len(profiles)} found")
            for p in profiles[:5]:
                print(f"    - {p.name or '(unnamed)'}  [{p.id}]")
            if len(profiles) > 5:
                print(f"    ... and {len(profiles) - 5} more")

    except MultiloginError as exc:
        print(f"  Error    : {exc}", file=sys.stderr)
        return 1

    print("\nAll checks passed. Ready for automation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
