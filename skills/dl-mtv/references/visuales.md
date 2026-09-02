# visuales.uclv.cu Download Reference

> **⚠️ Cuba intranet only.**
> `visuales.uclv.cu` is hosted on Cuba's national intranet (RedCuba/UCLV network).
> Only accessible from within Cuba — VPN from outside Cuba will NOT work because the server is not on the public internet.
> If outside Cuba: no workaround, the host simply does not route.

## Base URL pattern

```
https://visuales.uclv.cu/Series/Ingles/{Show Name encoded}/
```

Examples:
```
https://visuales.uclv.cu/Series/Ingles/CSI%20Las%20Vegas/S12/
https://visuales.uclv.cu/Series/Ingles/The%20Mentalist/The%20Mentalist%20x%201/
```

> Season folder naming is inconsistent. CSI uses `S11/`, `S12/`. The Mentalist uses `The Mentalist x 1/`. Always fetch the show root first to discover season folder names.

---

## Step 0 — Discover season folders

```bash
curl -s --max-time 20 "https://visuales.uclv.cu/Series/Ingles/Show%20Name/" \
  -H "User-Agent: Mozilla/5.0" \
  | grep -oP 'href="\K[^"]+' | grep -v '^[?.]' \
  | python3 -c "import sys,urllib.parse; [print(urllib.parse.unquote(l.strip())) for l in sys.stdin]"
```

## Step 1 — Fetch remote file listing

```bash
curl -s --max-time 20 "https://visuales.uclv.cu/Series/Ingles/Show%20Name/Season%20Folder/" \
  -H "User-Agent: Mozilla/5.0" \
  | grep -oP 'href="\K[^"]+' | grep -v '^[?.]' \
  | python3 -c "import sys,urllib.parse; [print(urllib.parse.unquote(l.strip())) for l in sys.stdin]"
```

---

## Remote filename patterns (vary per show)

| Show | Pattern | Example |
|------|---------|---------|
| CSI Las Vegas S11 | `CSI {season}x{ep}.avi` | `CSI 11x12.avi` |
| CSI Las Vegas S12 | `CSI_S12_{ep}.avi` | `CSI_S12_07.avi` |
| The Mentalist S1 | `S01E{ep}.{title}.HDTV.XviD-{tag}.avi` | `S01E03.Red.Tide.PROPER.HDTV.XviD-FQM.avi` |

**Always fetch the remote listing to get exact filenames — never assume.**

---

## Step 2 — Check remote file size before downloading

```bash
curl -sI --max-time 10 "https://visuales.uclv.cu/.../filename.avi" \
  | grep -i content-length
```

Use to: know expected size, detect server-down (0 or no header), verify completeness after download.

---

## Step 3 — Download with resume support

```bash
curl \
  --retry 15 \
  --retry-delay 5 \
  --retry-max-time 600 \
  --connect-timeout 30 \
  --speed-limit 1024 \
  --speed-time 60 \
  -C - \
  -L \
  -# \
  -o "/local/path/Show S01E03.avi" \
  "https://visuales.uclv.cu/.../S01E03.Title.avi"
```

Key flags:
- `-C -` — resume partial download
- `--speed-limit 1024 --speed-time 60` — abort if < 1KB/s for 60s
- `--retry 15 --retry-delay 5` — retry on transient failures

---

## Step 4 — Verify completeness

**Compare sizes:**
```bash
local_sz=$(stat -f%z "/local/path/file.avi")
remote_sz=$(curl -sI --max-time 10 "https://..." | grep -i content-length | awk '{print $2}' | tr -d '\r')
# complete if local_sz >= remote_sz - 1024
```

**Detect HTML error pages saved as .avi:**
```bash
xxd "/local/path/file.avi" | head -1
# Good:  RIFF....AVI LIST
# Bad:   3c68 746d  (<htm — HTML error page)
```

---

## Server quirks

### Intermittent availability
- Server returns HTTP 200 with HTML body: `"Upps ... Esta página no está disponible ahora."`
- Produces a ~220B `.avi` file that is actually HTML — not a video
- 0B file = curl failed before receiving anything
- Both cases: delete and re-download

**Detection:**
```bash
file_sz=$(stat -f%z "file.avi")
if (( file_sz < 1024 )); then
  head -c 10 "file.avi" | grep -q "<html" && echo "ERROR PAGE — delete and retry"
fi
```

### urllib vs curl
- Python `urllib` times out more aggressively than `curl` on this server
- Prefer `curl` for actual downloads
- Use `urllib` only for listing fetches (short timeout ok)
- SSL errors (`SSL_ERROR_SYSCALL`) are transient — retry works

### Speed / parallelism
- Server is slow and throttled
- Parallel downloads from same season trigger SSL failures
- Download sequentially, one file at a time

---

## Local directory structure

```
/Volumes/HDDTRANSINT/visuales.uclv.cu/Series/Ingles/
  CSI Las Vegas/
    S11/                    ← 22/22 complete
    S12/                    ← E01-E19 complete, E20-E22 server pending
  The Mentalist/
    The Mentalist x 1/      ← E01-E18 complete, E19-E23 server pending
```

---

## Scripts (in `./scripts/`)

| Script | Purpose | Usage |
|--------|---------|-------|
| `check_processes.sh` | Check active wget/curl/aria2c | `bash scripts/check_processes.sh` |
| `audit_season.py` | Flag 0B and <120MB files | `python3 scripts/audit_season.py "/path/season"` |
| `check_missing.py` | Local vs remote diff | `python3 scripts/check_missing.py "/local" "https://url/"` |
| `download_season.py` | Download missing + auto-rename | `python3 scripts/download_season.py "/local" "Show" 1 "https://url/" srt,avi` |
| `normalize_names.py` | Rename to `Show SxxExx.ext` | `python3 scripts/normalize_names.py "/path" "Show Name" 1` |
| `clean_duplicates.py` | Remove originals when normalized copy exists | `python3 scripts/clean_duplicates.py "/path"` |
| `download_s12_missing.sh` | Targeted retry for CSI S12 bad files | `bash scripts/download_s12_missing.sh` |

---

## Full workflow for a new season

1. `bash scripts/check_processes.sh` — verify no active downloads
2. Fetch remote listing to discover folder name and filenames
3. `curl -sI` each remote file to get sizes
4. `python3 scripts/check_missing.py` — diff local vs remote
5. Download with `curl --retry 15 -C - ...`
6. Verify: `stat -f%z` local == remote content-length (allow -1024 tolerance)
7. Verify file header: `xxd file.avi | head -1` must show `RIFF...AVI`
8. `python3 scripts/normalize_names.py` — standardize names
9. `python3 scripts/clean_duplicates.py` — remove originals
