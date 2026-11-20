#!/usr/bin/env python3
"""Verify downloaded files in a local or mounted Drive directory against Archive.org metadata."""

import argparse
import hashlib
import json
import os
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
                raise RuntimeError(f"Failed to fetch {item}: {exc}") from exc
            time.sleep(1.5 * (attempt + 1))
    return {}


def sha1_file(path: str) -> str:
    """Compute SHA-1 hex digest of a file in 8 MiB chunks."""
    digest = hashlib.sha1()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(8 * 1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest().lower()


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify downloaded Archive.org files.")
    parser.add_argument("--dir", required=True, help="Directory containing downloaded files")
    parser.add_argument("--item", required=True, help="Archive.org item identifier")
    parser.add_argument("--ext", help="Comma-separated extensions to verify (e.g. nsp,xci)")
    parser.add_argument("--sha1", action="store_true", help="Read back files and verify SHA-1")
    args = parser.parse_args()

    if not os.path.isdir(args.dir):
        print(f"ERROR: Directory not found: {args.dir}", file=sys.stderr)
        return 2

    exts = None
    if args.ext:
        exts = tuple("." + e.strip().lstrip(".").lower() for e in args.ext.split(",") if e.strip())

    meta = fetch_metadata(args.item)
    expected = []
    for f in meta.get("files", []):
        name = f.get("name", "")
        low = name.lower()
        if low.endswith(SYSTEM_SUFFIXES):
            continue
        if exts and not low.endswith(exts):
            continue
        expected.append((os.path.basename(name), int(f.get("size") or 0), f.get("sha1", "").lower()))

    ok = 0
    errors = []
    total = len(expected)
    for idx, (fn, exp_sz, exp_sha1) in enumerate(expected, 1):
        path = os.path.join(args.dir, fn)
        if not os.path.exists(path):
            errors.append((fn, "MISSING"))
            print(f"[{idx}/{total}] MISSING: {fn}", flush=True)
            continue
        act_sz = os.path.getsize(path)
        if act_sz != exp_sz:
            errors.append((fn, f"SIZE {act_sz} != {exp_sz}"))
            print(f"[{idx}/{total}] SIZE_MISMATCH: {fn} ({act_sz} != {exp_sz})", flush=True)
            continue
        if args.sha1 and exp_sha1:
            act_sha1 = sha1_file(path)
            if act_sha1 != exp_sha1:
                errors.append((fn, f"SHA1 {act_sha1} != {exp_sha1}"))
                print(f"[{idx}/{total}] SHA1_MISMATCH: {fn}", flush=True)
                continue
        ok += 1
        print(f"[{idx}/{total}] OK: {fn} ({act_sz / 1024**3:.2f} GiB)", flush=True)

    print(f"SUMMARY: OK={ok}/{total} ERRORS={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
