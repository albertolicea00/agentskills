---
name: dl-mtv
description: Download, organize, and manage video — HLS/M3U8, direct MP4/AVI, full seasons from directory-style servers. Covers download, subtitle retrieval (subliminal/VLC), filename normalization, metadata, and integrity verification.
---

# Video Downloader

## When to trigger

Activate this skill when the user:

1. Pastes a `curl` command or URL pointing to a video stream (`.m3u8`, `.txt`, `.mp4`, `.mkv`, `.webm`, or any stream URL).
2. Pastes an HLS playlist body starting with `#EXTM3U`.
3. Says "download this video", "descargar este video", "bajame esto", "bájame la serie" + a URL.
4. Pastes a direct video file URL that needs to be downloaded with specific headers (Referer, cookies).

---

## Download methods

Pick the method that matches what the user has:

| Trigger | Method | Reference |
|---------|--------|-----------|
| `.m3u8` / `.txt` URL or `#EXTM3U` body | HLS segment pipeline | [`references/m3u8.md`](references/m3u8.md) |
| Season/series page URL | Batch episode download | [`references/m3u8.md`](references/m3u8.md) — "Full-season batch" section |
| Direct `.mp4`/`.mkv`/`.webm` URL | Single `curl -L -o output.mp4 URL` | — |
| `visuales.uclv.cu` URL | Cuba-intranet directory download | [`references/visuales.md`](references/visuales.md) |

More methods will be documented in `references/` as they are encountered.

---

## Filename normalization

After downloading, rename files to `Show SxxExx.ext` for Plex/Jellyfin/Kodi compatibility.

→ [`references/rename.md`](references/rename.md)

---

## Subtitles

Download, fix encoding (latin-1 → utf-8), pair with video, fallback to subliminal/OpenSubtitles.

→ [`references/subtitles.md`](references/subtitles.md)

---

## Metadata

Posters, NFO files, TMDB/TVDB scraping for Plex, Jellyfin, Kodi.

→ [`references/metadata.md`](references/metadata.md)

---

## Prerequisites

```bash
brew install ffmpeg yt-dlp curl
pip3 install subliminal tmdbsimple requests chardet
```
