#!/bin/sh
set -eu

cd "$(dirname "$0")/lab"
python3 reader_original.py
python3 reader.py
python3 --version
