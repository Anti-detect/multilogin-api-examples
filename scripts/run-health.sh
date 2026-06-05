#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../examples/python"
if [[ -z "${MULTILOGIN_TOKEN:-}" ]]; then
  echo "Set MULTILOGIN_TOKEN first."
  exit 1
fi
python3 health_check.py
