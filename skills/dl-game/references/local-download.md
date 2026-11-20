# Local Download & Verification

Use this mode when saving files directly to a local directory.

## Prerequisites

- `aria2c` (recommended for multi-connection resume and built-in SHA-1 verification) or `curl` / `ia` CLI.
- Optional: `<IA_COOKIES_FILE>` (`ia.ini`) containing `logged-in-user` and `logged-in-sig` if downloading `private=True` items.

## 1. Download with `aria2c` + SHA-1 verification

Generate URLs and checksums from `https://archive.org/metadata/<item>`, then run `aria2c`:

```bash
# Example single-file download with resume and SHA-1 verification
aria2c -c -x8 -s8 \
  --checksum=sha-1=<EXPECTED_SHA1> \
  --dir="<LOCAL_DEST>/<item>" \
  --out="<FILENAME>" \
  "https://archive.org/download/<item>/<URL_ENCODED_FILENAME>"
```

For `private=True` items, add:

```bash
--header="Cookie: logged-in-user=<USER_COOKIE>; logged-in-sig=<SIG_COOKIE>"
```

## 2. Verify local directory

After downloads finish, verify exact byte sizes and SHA-1 hashes against Archive.org metadata:

```bash
python3 scripts/ia_verify.py --dir "<LOCAL_DEST>/<item>" --item "<item>" --ext nsp,xci --sha1
```
