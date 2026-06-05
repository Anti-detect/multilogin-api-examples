"""
Selenium attach example (requires selenium + chromedriver compatible with Mimic).

  pip install selenium
  set MULTILOGIN_PROFILE_ID=...
  python selenium_connect.py
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
        print("Set MULTILOGIN_PROFILE_ID", file=sys.stderr)
        sys.exit(1)

    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
    except ImportError:
        print("pip install selenium", file=sys.stderr)
        sys.exit(1)

    with MultiloginClient() as client:
        try:
            with client.profile(profile_id) as session:
                addr = session.selenium_address
                if not addr:
                    print("No debug port in start response. Set options manually.")
                    print("Response:", session.response)
                    sys.exit(1)

                options = Options()
                options.add_experimental_option("debuggerAddress", addr)
                print(f"Connecting Selenium to {addr}...")
                driver = webdriver.Chrome(options=options)
                driver.get("https://browserleaks.com/javascript")
                print("Title:", driver.title)
                time.sleep(3)
                driver.quit()
        except MultiloginError as exc:
            print(f"Error: {exc}", file=sys.stderr)
            sys.exit(1)

    print("Done.")


if __name__ == "__main__":
    main()
