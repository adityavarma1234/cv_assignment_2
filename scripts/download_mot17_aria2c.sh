#!/usr/bin/env bash
# Fallback for when remote range-requests aren't supported: downloads the full
# MOT17.zip with parallel connections (much faster than a single-stream
# curl/wget/browser download), then extracts just the one sequence needed.
#
# Requires: brew install aria2
set -euo pipefail

URL="https://motchallenge.net/data/MOT17.zip"
SEQUENCE="MOT17-04-FRCNN"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DEST_ZIP="$PROJECT_ROOT/data/MOT17.zip"
EXTRACT_DIR="$PROJECT_ROOT/data/MOT17"

if ! command -v aria2c >/dev/null 2>&1; then
    echo "aria2c not found. Install it with: brew install aria2" >&2
    exit 1
fi

mkdir -p "$(dirname "$DEST_ZIP")"
echo "Downloading MOT17.zip with 16 parallel connections..."
aria2c -x 16 -s 16 -o "$(basename "$DEST_ZIP")" -d "$(dirname "$DEST_ZIP")" "$URL"

echo "Listing entries matching $SEQUENCE ..."
unzip -l "$DEST_ZIP" | grep "$SEQUENCE" | head -20

echo "Extracting $SEQUENCE ..."
mkdir -p "$EXTRACT_DIR"
unzip "$DEST_ZIP" "*$SEQUENCE*" -d "$EXTRACT_DIR"

echo "Done. Extracted to $EXTRACT_DIR"
