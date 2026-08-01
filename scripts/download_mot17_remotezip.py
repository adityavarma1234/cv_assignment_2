#!/usr/bin/env python3
"""Fetches only the MOT17-04-FRCNN sequence out of the remote MOT17.zip via HTTP
range requests, instead of downloading the full ~5.5GB archive.

Requires: pip3 install remotezip
"""
import sys
from pathlib import Path

try:
    from remotezip import RemoteZip
except ImportError:
    sys.exit("Missing dependency: run `pip3 install remotezip` first.")

URL = "https://motchallenge.net/data/MOT17.zip"
SEQUENCE = "MOT17-04-FRCNN"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "data" / "MOT17"


def main():
    with RemoteZip(URL) as zf:
        matches = [i for i in zf.infolist() if SEQUENCE in i.filename]
        if not matches:
            sys.exit(f"No files matching '{SEQUENCE}' found in the archive.")

        total_mb = sum(i.file_size for i in matches) / 1e6
        print(f"{len(matches)} files, {total_mb:.1f} MB total")
        for i in matches[:5]:
            print(" ", i.filename)
        if len(matches) > 5:
            print(f"  ... and {len(matches) - 5} more")

        answer = input(f"\nExtract all {len(matches)} files to {OUTPUT_DIR}? [y/N] ").strip().lower()
        if answer != "y":
            print("Aborted, nothing extracted.")
            return

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        for i in matches:
            zf.extract(i.filename, OUTPUT_DIR)
        print(f"Done. Extracted to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
