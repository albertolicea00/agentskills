#!/usr/bin/env python3
"""Inspect Archive.org item metadata, filter files, and search titles."""

import argparse
import json
import string
import sys
import time
import urllib.request

SYSTEM_SUFFIXES = (".xml", ".sqlite", ".torrent")


def fetch_metadata(item: str, retries: int = 4) -> dict:
    """Fetch JSON metadata for an Archive.org item with backoff retries."""
    url = f"https://archive.org/metadata/{item}"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            if attempt == retries - 1:
                print(f"ERROR fetching {item}: {exc}", file=sys.stderr)
                return {}
            time.sleep(1.5 * (attempt + 1))
    return {}


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect Archive.org game collections.")
    parser.add_argument("items", nargs="*", help="Archive.org item identifiers")
    parser.add_argument("--prefix", help="Identifier prefix for A-Z shard expansion")
    parser.add_argument("--az", action="store_true", help="Expand --prefix with a..z")
    parser.add_argument("--ext", help="Comma-separated extensions (e.g. nsp,xci,pkg)")
    parser.add_argument("--match", action="append", default=[], help="Case-insensitive substring filter (repeatable)")
    args = parser.parse_args()

    items = list(args.items)
    if args.prefix and args.az:
        items.extend(f"{args.prefix}{ch}" for ch in string.ascii_lowercase)
    if not items:
        parser.error("Provide at least one item or --prefix --az")

    exts = None
    if args.ext:
        exts = tuple("." + e.strip().lstrip(".").lower() for e in args.ext.split(",") if e.strip())
    keywords = [m.lower() for m in args.match]

    total_files = 0
    total_bytes = 0
    private_count = 0

    for idx, item in enumerate(items):
        if idx > 0:
            time.sleep(0.3)
        meta = fetch_metadata(item)
        files = meta.get("files", [])
        if not files:
            print(f"{item}: 0 files (missing or private/dark item)")
            continue

        matched = []
        for f in files:
            name = f.get("name", "")
            low = name.lower()
            if low.endswith(SYSTEM_SUFFIXES):
                continue
            if exts and not low.endswith(exts):
                continue
            if keywords and not any(k in low for k in keywords):
                continue
            size = int(f.get("size") or 0)
            priv = bool(f.get("private", False))
            matched.append((name, size, priv))

        item_bytes = sum(x[1] for x in matched)
        item_priv = sum(1 for x in matched if x[2])
        total_files += len(matched)
        total_bytes += item_bytes
        private_count += item_priv
        print(f"{item}: {len(matched)} matching files | {item_bytes / 1024**3:.2f} GiB | private={item_priv}")
        for name, size, priv in matched:
            print(f"  - {name} ({size / 1024**3:.2f} GiB, private={priv})")

    print(f"TOTAL: {total_files} files | {total_bytes / 1024**3:.2f} GiB | private={private_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
