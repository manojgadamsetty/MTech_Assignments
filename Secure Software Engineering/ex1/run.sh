#!/bin/sh
set -eu

cd "$(dirname "$0")"
python3 checkout_original.py
python3 checkout.py
python3 --version
