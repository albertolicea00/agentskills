# Metadata Reference

## What metadata is needed

| File | Purpose | Consumers |
|------|---------|-----------|
| `poster.jpg` | Show/season poster | Jellyfin, Kodi, Plex |
| `{show}-thumb.jpg` / `{ep}-thumb.jpg` | Episode thumbnail | Kodi |
| `tvshow.nfo` | Show metadata (XML) | Kodi |
| `{episode}.nfo` | Episode metadata (XML) | Kodi |
| `season.nfo` | Season metadata | Kodi |

**Plex and Jellyfin** scrape metadata automatically from TVDB/TMDB if filenames follow `Show SxxExx.ext` — no manual NFO needed in most cases.

**Kodi** requires NFO files or a scraper plugin.

---

## Method 1 — Let the media server scrape (recommended for Plex/Jellyfin)

Just ensure filenames are correct (`Show SxxExx.ext`) — see [`references/rename.md`](rename.md).
Plex/Jellyfin match against TVDB/TMDB automatically on library scan.

Nothing else needed.

---

## Method 2 — Download poster manually (TMDB)

```bash
# 1. Find show on TMDB (free API key at https://themoviedb.org)
curl -s "https://api.themoviedb.org/3/search/tv?api_key=YOUR_KEY&query=The+Mentalist" \
  | python3 -m json.tool | grep -E '"id"|"name"|"poster_path"'

# 2. Download poster (use the poster_path from above)
curl -L -o poster.jpg "https://image.tmdb.org/t/p/original/POSTER_PATH.jpg"
```

---

## Method 3 — NFO from visuales.uclv.cu (bundled)

Some shows on visuales include `.nfo` and `-thumb.jpg` alongside the video files.
Download them with the episode:

```bash
# List what's available (nfo, thumbs, poster)
curl -s "https://visuales.uclv.cu/Series/Ingles/Show/Season/" \
  -H "User-Agent: Mozilla/5.0" \
  | grep -oP 'href="\K[^"]+' | grep -vE '^[?.]' \
  | python3 -c "import sys,urllib.parse; [print(urllib.parse.unquote(l.strip())) for l in sys.stdin]" \
  | grep -E "\.(nfo|jpg|png)$"

# Download a specific nfo
curl -o "S01E03.nfo" "https://visuales.uclv.cu/Series/Ingles/Show/Season/S01E03.nfo"
```

---

## Method 4 — Generate NFO manually (Kodi format)

Minimal `tvshow.nfo` for Kodi:
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<tvshow>
  <title>The Mentalist</title>
  <year>2008</year>
  <plot>A former fake psychic uses his keen observer skills to help the CBI solve murders.</plot>
  <genre>Crime</genre>
  <genre>Drama</genre>
</tvshow>
```

Minimal episode NFO (`The Mentalist S01E03.nfo`):
```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<episodedetails>
  <title>Red Tide</title>
  <season>1</season>
  <episode>3</episode>
  <plot>The team investigates the death of a surfer.</plot>
</episodedetails>
```

---

## Method 5 — Bulk metadata with tmdbsimple (Python)

```bash
pip3 install tmdbsimple requests
```

```python
import tmdbsimple as tmdb
tmdb.API_KEY = 'YOUR_KEY'

search = tmdb.Search()
search.tv(query='The Mentalist')
show_id = search.results[0]['id']

tv = tmdb.TV(show_id)
info = tv.info()
season = tmdb.TV_Seasons(show_id, 1).info()

for ep in season['episodes']:
    print(ep['episode_number'], ep['name'], ep['overview'])
```

---

## Poster naming for Kodi/Jellyfin

```
/Series/Show Name/
  poster.jpg          ← show poster
  fanart.jpg          ← background art
  Season 01/
    season01-poster.jpg
    Show S01E01-thumb.jpg
    Show S01E01.avi
    Show S01E01.nfo
```

---

## Known metadata on visuales.uclv.cu

The remote includes per-episode files alongside videos:
- `{ep}-thumb.jpg` — episode thumbnail
- `{ep}.nfo` — minimal Kodi NFO
- `sinopsis.txt` — plain-text show description (root of show folder)
- `poster.jpg` / show image at root

These are already downloaded if you used `download_season.py` with image extensions, or download manually via curl.
