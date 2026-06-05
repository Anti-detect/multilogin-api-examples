"""Load .env file into os.environ if python-dotenv is installed."""

from __future__ import annotations

import os
from pathlib import Path


def load_dotenv_if_available() -> bool:
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return False
    try:
        from dotenv import load_dotenv

        load_dotenv(env_path)
        return True
    except ImportError:
        return False


def bootstrap_env() -> None:
    """Call at top of CLI scripts — optional .env support."""
    if load_dotenv_if_available():
        return
    # Manual parse fallback (KEY=VALUE lines, no quotes required)
    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
