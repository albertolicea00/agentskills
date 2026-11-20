---
name: dl-game
description: Search Archive.org game collections and download/verify via Colab or local.
---

# Game & ROM Downloader (`dl-game`)

## Objective

Given an Archive.org item URL/identifier, an uploader/series pattern, or a list of game titles, inspect Archive.org metadata (file counts, sizes, extensions, `private` lock flags), search for matching titles, and download + SHA-1 verify the selected files either **to Google Drive via Colab** or **directly to a local directory**.

---

## Output format

### 1. Catalog search / size estimate

```text
Item: retro-console-set | Matching files: 12 | Total: 48.20 GiB | Private: 0
Estimated time: ~10–15 min at 50–80 MiB/s (Colab) / ~20–40 min (typical home fiber)

Matches:
- Game Title A [US].iso (4.12 GiB, public)
- Game Title B [EU].nsp (6.85 GiB, public)
```

### 2. Active download / verification progress (every 5 minutes)

```text
Progress (<item>): 18 / 23 files (68.97 / 100.54 GiB — 68.6%)
Current: [19/23] Example Game.nsp — 4.2 / 6.3 GiB (66%) @ 8.5 MiB/s | File ETA: 4m12s
Errors: 0
```

### 3. Final integrity summary

```text
Verified on <target>: 23 / 23 files | Exact size: 23 / 23 | SHA-1 OK: 23 / 23 | Errors: 0
```

---

## Rules

1. **Inspect metadata before downloading.** Always query `https://archive.org/metadata/<item>` first to report exact file count, total size (`GiB`/`TiB`), extensions, and whether any files have `private: true`.
2. **Exclude Archive.org system artifacts.** Ignore `_files.xml`, `_meta.xml`, `_meta.sqlite`, `_reviews.xml`, and `.torrent` files unless the user explicitly asks for them.
3. **Detect auth requirements upfront.** If any target file has `"private": true`, check for an Archive.org cookie/config file (`ia.ini` or `<IA_COOKIES_FILE>`) before starting downloads. Do not silently fail on HTTP 401/403.
4. **Never fill Colab ephemeral disk.** In Colab-to-Drive mode, copy each verified file to Google Drive and immediately delete the temporary local copy before starting the next file.
5. **Verify integrity after transfer.** Verify SHA-1 during download (`aria2c --checksum=sha-1=...`), then verify exact byte sizes (and optional full SHA-1 readback) directly on the destination (`Drive` or local) against Archive.org metadata.
6. **Monitor long-running jobs.** Check progress every 5 minutes and report file count, percentage, transfer speed, and ETA. Wrap remote Colab SSH runs in an auto-retry loop for `exit 255` disconnects.
7. **Ask before large downloads.** Present size estimates and let the user confirm or filter by extension/title before downloading collections larger than ~10 GiB.

---

## Examples

### Example 1 — Search a multi-part Archive.org collection for a wishlist

**Input:**
> Check if `Example Quest 3` and `Pixel Racer` are in `console-collection-a` through `console-collection-z`.

**Output:**
```text
Found (1 / 2):
- Example Quest 3 -> [console-collection-e] Example Quest 3 [US] [v1.02].pkg (18.40 GiB, private=True)

Not found (1 / 2):
- Pixel Racer
```
*Why:* The agent queried `advancedsearch.php` for `console-collection-*`, fetched metadata sequentially for the relevant letter shards (`e`, `p`), excluded `.xml`/`.torrent` metadata files, and reported exact filenames, sizes, and `private` status.

### Example 2 — Download filtered Switch titles to Google Drive via Colab

**Input:**
> Download only `.nsp` and `.xci` files from `https://archive.org/details/sample-switch-set` to Drive.

**Output:**
Runs `scripts/ia_inspect.py` first (`14 files, 42.10 GiB`), executes the Colab-to-Drive `aria2c` + SHA-1 pipeline with `-e nsp,xci`, reports 5-minute progress check-ins, and finishes with a post-copy byte-size + SHA-1 verification summary (`14 / 14 OK, 0 mismatches`).
*Why:* Filtering avoids downloading covers/metadata, Colab-to-Drive preserves local disk space, and post-copy verification catches silent Drive FUSE truncation.

---

## Procedure

### Step 1: Search and inspect Archive.org

1. Use `scripts/ia_inspect.py` (or the API queries in [`references/archive-search.md`](references/archive-search.md)) to:
   - Discover multi-part collections (`advancedsearch.php?q=identifier:<prefix>*`).
   - Fetch `/metadata/<identifier>` for each item.
   - Filter by requested extensions (`.nsp`, `.xci`, `.pkg`, `.iso`, `.chd`, `.zip`, `.7z`, `.rar`) or title keywords.
   - Report file count, total `GiB`/`TiB`, `private=True` status, and estimated duration.

### Step 2: Choose execution mode

- **Colab-to-Drive mode** (best for large sets > 20 GiB or saving directly to Google Drive): follow [`references/colab-download.md`](references/colab-download.md). If the current workspace already provides a project downloader script (such as `colab-archive-dl.sh`), prefer invoking it; otherwise use the self-contained Colab SSH pipeline in the reference.
- **Local mode** (best for saving directly to the local machine): follow [`references/local-download.md`](references/local-download.md).

### Step 3: Download with resume and checksums

1. Download using `aria2c` (`-c` resume, `-x8 -s8` connections, `--checksum=sha-1=<expected>` when SHA-1 is present in Archive.org metadata).
2. Pass `logged-in-user` and `logged-in-sig` cookies from `ia.ini` whenever `private=True` files exist.
3. For Colab-to-Drive, verify disk space on Drive first, copy each verified file to `<DRIVE_DEST>/<item>/`, and remove the temporary copy from `/content/` immediately.

### Step 4: Post-download verification

Run `scripts/ia_verify.py` against the destination folder (locally or over `ssh <COLAB_HOST>`) to confirm:
1. All expected files exist (`0` missing, `0` leftover `.aria2`/partial files).
2. Every file matches Archive.org's exact byte `size`.
3. When full bit-for-bit confirmation is requested (recommended after large Drive FUSE copies), run `scripts/ia_verify.py --sha1` to read back and verify every file's SHA-1.

---

## Edge cases

- **Archive.org TLS resets / rate limits:** Fetching many `/metadata/<item>` endpoints concurrently can trigger `ConnectionResetError`. Fetch sequentially or with low concurrency (`<= 2` workers) and exponential backoff.
- **Locked items (`private: true`):** Public `aria2c` requests return HTTP 401/403. Extract `logged-in-user` and `logged-in-sig` from the user's `ia.ini` / cookies file and pass them as `Cookie:` headers.
- **Taken-down / dark items:** `/metadata/<item>` returns `{}` or `is_dark: true`. Report that the item is no longer publicly hosted on Archive.org instead of retrying indefinitely.
- **Colab SSH drops (`exit 255`) or HTTP 429 (`Already-active SSH session`):** Wrap remote commands in a retry loop with a `20–30s` sleep so the stale proxy session clears before reconnecting.
- **Silent Drive FUSE truncation:** A file can pass `aria2c` SHA-1 locally on Colab and still end up truncated on Google Drive if FUSE stalls during copy. Always run `scripts/ia_verify.py` on Drive afterwards; delete any mismatched file and re-run to replace only that file.
- **Colab OAuth prompt (`colab drivemount`):** Never attempt to bypass OAuth; pause and ask the user to approve the browser OAuth prompt.
