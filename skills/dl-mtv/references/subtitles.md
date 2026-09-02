# Subtitles Reference

How to get subtitles for any video — using subliminal (Python CLI) or VLC's built-in search.

---

## Method 1 — subliminal (recommended, CLI)

```bash
pip3 install subliminal
```

**Download best subtitle for one file:**
```bash
subliminal download -l es "Show S01E03.avi"   # Spanish
subliminal download -l en "Show S01E03.avi"   # English
```

**Batch — entire season directory:**
```bash
subliminal download -l es /path/to/season/*.avi
subliminal download -l es,en /path/to/season/*.avi   # try es, fallback en
```

subliminal searches: OpenSubtitles, Subscene, Addic7ed, TVsubtitles, Napiprojekt.

**With OpenSubtitles credentials (higher rate limit):**
```bash
subliminal download -l es \
  --opensubtitles username password \
  "Show S01E03.avi"
```

---

## Method 2 — VLC built-in subtitle search

1. Open video in VLC
2. Menu → **View → VLC media player** → **Subtitles** → **Download subtitles...**
3. Picks language from VLC preferences (Preferences → Subtitles & OSD)

VLC searches OpenSubtitles.org using video hash — very accurate, no filename dependency.

**Set preferred language once:**
- VLC → Preferences → Subtitles & OSD → Preferred subtitle language → `spa` / `eng`

---

## Method 3 — OpenSubtitles API (manual)

Free API key at https://www.opensubtitles.com/en/consumers

```bash
# Search by show + season + episode
curl -s "https://api.opensubtitles.com/api/v1/subtitles" \
  -G \
  --data-urlencode "query=The Mentalist" \
  --data-urlencode "season_number=1" \
  --data-urlencode "episode_number=3" \
  --data-urlencode "languages=es" \
  -H "Api-Key: YOUR_API_KEY" \
  -H "User-Agent: MyApp v1.0" \
  | python3 -m json.tool | grep -E '"url"|"language"|"file_name"'
```

---

## Pairing rule

Subtitle file must share **exact basename** with the video:

```
Show S01E03.avi
Show S01E03.srt   ← same name, .srt ext
```

Plex, Jellyfin, Kodi, VLC all auto-load when names match.

---

## Fix encoding (common with Spanish subs)

Subs often downloaded as `latin-1` — accented chars appear garbled (`?`, `Â`, etc.).

```bash
# Detect encoding
file -i "Show S01E03.srt"

# Convert latin-1 → utf-8 (in-place)
iconv -f latin-1 -t utf-8 "Show S01E03.srt" -o "Show S01E03.srt"

# Batch fix all srt in a directory
for f in /path/to/season/*.srt; do
  iconv -f latin-1 -t utf-8 "$f" -o "$f.tmp" 2>/dev/null && mv "$f.tmp" "$f"
done
```

---

## Integrity check

Valid `.srt` starts with a sequence number + timecode:
```
1
00:00:01,150 --> 00:00:03,520
```

Suspect if:
- 0B → missing, re-download
- `<html` as first bytes → error page saved as .srt, delete and retry
- < 5KB → probably wrong/empty (valid 40min ep srt: 40–90KB)

```bash
for f in /path/*.srt; do
  sz=$(stat -f%z "$f")
  (( sz < 5000 )) && echo "SUSPECT ($sz B): $f" && head -1 "$f"
done
```
