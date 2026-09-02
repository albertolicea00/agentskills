# Filename Normalization Reference

## Standard format

```
{Show Name} S{season:02d}E{episode:02d}.{ext}
```

Examples:
```
CSI Las Vegas S11E01.avi
CSI Las Vegas S11E01.srt
The Mentalist S01E03.avi
Suits S09E01.srt
```

---

## Why normalize

- Raw downloads have scene tags: `S01E03.Red.Tide.PROPER.HDTV.XviD-FQM.avi`
- Remote naming is inconsistent per show: `CSI 11x12.avi`, `CSI_S12_07.avi`
- Plex/Jellyfin/Kodi require `Show SxxExx.ext` for auto-matching

---

## Script: `normalize_names.py`

```bash
python3 scripts/normalize_names.py "/path/to/season" "Show Name" SeasonNumber
```

Examples:
```bash
python3 scripts/normalize_names.py \
  "/Volumes/HDDTRANSINT/visuales.uclv.cu/Series/Ingles/CSI Las Vegas/S11" \
  "CSI Las Vegas" 11

python3 scripts/normalize_names.py \
  "/Volumes/HDDTRANSINT/visuales.uclv.cu/Series/Ingles/The Mentalist/The Mentalist x 1" \
  "The Mentalist" 1
```

---

## Episode number extraction patterns

The script uses these regex patterns to extract episode numbers from messy filenames:

```python
# Pattern 1: S12E07, S01E03, S12_07
r'(?:S\d{2}[E_]|11x|S12_|x)(\d{2})'

# Pattern 2: 11x12, 1x03
r'(\d{1,2})[x_](\d{2})'

# Pattern 3: E07 anywhere
r'E(\d{2})'
```

---

## Duplicate cleanup after renaming

After normalizing, originals remain alongside renamed copies:

```
CSI 11x12.avi          ← original (to delete)
CSI Las Vegas S11E12.avi  ← normalized (keep)
```

Run:
```bash
python3 scripts/clean_duplicates.py "/path/to/season"
```

Safe: only deletes originals when the normalized `SxxExx` copy exists and is non-empty.

---

## Manual rename (single file)

```bash
mv "/path/CSI 11x12.avi" "/path/CSI Las Vegas S11E12.avi"
```

---

## Known naming irregularities by show

| Show | Remote pattern | Local target |
|------|---------------|-------------|
| CSI Las Vegas S11 | `CSI 11x{ep}.avi` | `CSI Las Vegas S11E{ep}.avi` |
| CSI Las Vegas S12 | `CSI_S12_{ep}.avi` | `CSI Las Vegas S12E{ep}.avi` |
| The Mentalist S1 | `S01E{ep}.Title.HDTV.XviD-tag.avi` | `The Mentalist S01E{ep}.avi` |

---

## Subtitle pairing

Subtitle must share exact basename with video:
```
The Mentalist S01E03.avi
The Mentalist S01E03.srt   ← same name, different ext
```

Plex/Jellyfin auto-detect when names match.
