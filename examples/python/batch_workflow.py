"""
Batch workflow: list profiles → start first N → stop all.

Env:
  MULTILOGIN_BATCH_LIMIT=3   max profiles to start (default 1)
  MULTILOGIN_DEMO_WAIT=5    seconds per profile
"""

import os
import sys
import time

from load_env import bootstrap_env
from multilogin_client import MultiloginClient, MultiloginError

bootstrap_env()


def main() -> None:
    limit = int(os.environ.get("MULTILOGIN_BATCH_LIMIT", "1"))
    wait = int(os.environ.get("MULTILOGIN_DEMO_WAIT", "5"))

    try:
        client = MultiloginClient()
    except MultiloginError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    profiles = [p for p in client.list_profiles_normalized() if p.id]
    if not profiles:
        print("No profiles with IDs found.")
        sys.exit(1)

    batch = profiles[:limit]
    started: list[str] = []

    print(f"Batch start ({len(batch)} profiles)...")
    for p in batch:
        try:
            session = client.start_profile_session(p.id)
            started.append(p.id)
            print(f"  OK  {p.name}  cdp={session.cdp_url}  port={session.debug_port}")
        except MultiloginError as exc:
            print(f"  FAIL {p.name}: {exc}")

    if started:
        print(f"\nWaiting {wait}s...")
        time.sleep(wait)

    print("\nBatch stop...")
    results = client.batch_stop(started, delay_sec=0.3)
    for pid, status in results.items():
        print(f"  {pid}: {status}")

    client.close()
    print("Done.")


if __name__ == "__main__":
    main()
