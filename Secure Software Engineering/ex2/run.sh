#!/bin/sh
set -eu

cd "$(dirname "$0")"
BITS_ID="${1:-2025MT12100}"
python3 users_original.py "$BITS_ID"
python3 users.py "$BITS_ID"
python3 --version
