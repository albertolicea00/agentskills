# Archive.org Search & Metadata Inspection

## 1. Discover multi-part collections or uploader items

Query Archive.org `advancedsearch.php`:

```bash
# Search by identifier prefix (e.g., A-Z shards)
curl -s "https://archive.org/advancedsearch.php?q=identifier:ps4-fpkg-collection-english*&fl[]=identifier,title&rows=100&output=json"

# Search by uploader
curl -s "https://archive.org/advancedsearch.php?q=uploader:<USER>&fl[]=identifier,title&rows=100&output=json"

# Search software items by title keywords
python3 -c '
import json, urllib.parse, urllib.request
q = urllib.parse.quote("(\"Title One\" OR \"Title Two\") AND mediatype:software")
url = f"https://archive.org/advancedsearch.php?q={q}&fl[]=identifier,title,addeddate&sort[]=addeddate+desc&rows=20&output=json"
res = json.loads(urllib.request.urlopen(url, timeout=20).read())
for d in res.get("response", {}).get("docs", []):
    print(d.get("addeddate"), d["identifier"], "-", d.get("title"))
'
```

## 2. Inspect item metadata (`/metadata/<identifier>`)

Archive.org returns all files, byte sizes, `sha1` hashes, and `private` flags in a single JSON endpoint:

```text
https://archive.org/metadata/<identifier>
```

### Filtering rules

- Ignore Archive.org-generated metadata files:
  - `*.xml` (`_files.xml`, `_meta.xml`, `_reviews.xml`)
  - `*_meta.sqlite`
  - `*.torrent`
- Check `bool(f.get("private", False))`: if `True`, an authenticated Archive.org session cookie (`ia.ini`) is required.
- Always fetch sequentially or with `<= 2` concurrent connections and `0.3–0.5s` delay + retries; higher concurrency triggers TLS resets (`Errno 54`).

## 3. Using the bundled inspector script

```bash
# Inspect one or more items and estimate sizes
python3 scripts/ia_inspect.py <item1> <item2> --ext nsp,xci

# Search across A-Z letter shards for specific game titles
python3 scripts/ia_inspect.py --prefix <collection-prefix-> --az --match "elden ring" --match "bloodborne"
```
