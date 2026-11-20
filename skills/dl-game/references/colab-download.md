# Colab-to-Drive Download & Verification

Use this mode when downloading large collections (> 20 GiB) or saving directly to Google Drive via a configured Colab SSH host (`<COLAB_HOST>`).

## Prerequisites

- Working SSH alias to a Colab runtime (`ssh <COLAB_HOST>`).
- Google Drive mounted at `/content/drive/MyDrive` on the Colab VM.
- Optional: Archive.org `ia.ini` with `logged-in-user` and `logged-in-sig` cookies if any file has `private=True`.
- If the active workspace already includes a dedicated script (e.g., `colab-archive-dl.sh`), prefer running that script.

## Pipeline Pattern

1. **Check Drive mount & free space** before starting:
   ```bash
   ssh <COLAB_HOST> 'df -h /content/drive/MyDrive /content'
   ```
2. **Download per-file with `aria2c` + SHA-1 checksum**:
   - Download into `/content/downloads/<item>/verified/<filename>`.
   - Pass `--checksum=sha-1=<expected_sha1>` when available in Archive.org metadata.
   - Pass `--header="Cookie: logged-in-user=...; logged-in-sig=..."` for `private=True` items.
   - Use `-c -x8 -s8 --summary-interval=15` for fast, resumable multi-connection downloads.
3. **Copy to Drive and clean `/content/` immediately**:
   - Skip files that already exist on `<DRIVE_DEST>/<item>/<filename>` with matching byte size.
   - Copy each verified file to `<DRIVE_DEST>/<item>/<filename>` and delete `/content/downloads/<item>/verified/<filename>` immediately so Colab's ~108 GiB disk never fills up.
4. **Wrap in an SSH retry loop**:
   Colab SSH sessions drop periodically (`exit 255`) or briefly reject reconnects with HTTP 429 (`Already-active SSH session`). Retry with a 25-second delay:
   ```bash
   for attempt in $(seq 1 10); do
     echo "=== [<item>] Attempt $attempt ==="
     <download_command> && break
     rc=$?
     echo "=== exited with $rc; waiting 25s before retry ==="
     sleep 25
   done
   ```
5. **Post-copy verification on Drive**:
   Drive FUSE copies can occasionally truncate a file without raising an error. Run `scripts/ia_verify.py` remotely via SSH after completion:
   ```bash
   ssh <COLAB_HOST> 'python3 -u -' < scripts/ia_verify.py --dir /content/drive/MyDrive/<dest>/<item> --item <item>
   # Add --sha1 for full bit-for-bit readback verification from Google Drive
   ```
   If any file reports `SIZE_MISMATCH` or `SHA1_MISMATCH`, delete only that file from Drive and re-run the download command.
