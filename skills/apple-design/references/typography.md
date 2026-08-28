# Typography — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/typography  
Updated: 2025

---

## Fonts

| Platform | System font | Display font |
|---|---|---|
| iOS / iPadOS / watchOS | SF Pro | SF Pro Display (≥ 20 pt) |
| macOS | SF Pro | SF Pro Display (≥ 20 pt) |
| tvOS | SF Pro | SF Pro Display |
| visionOS | SF Pro | SF Pro Display |

Rounded variant: SF Pro Rounded — use for numerals, friendly UI, buttons.  
Monospace: SF Mono — code, terminal, data.  
Serif: New York — reading experiences, editorial.

Never ship SF fonts as embedded assets — they are system fonts, accessed via API only.  
Custom fonts: always scale with `UIFontMetrics`.

---

## Text styles (Dynamic Type)

Use semantic styles, not raw point sizes.

| Style | Default pt | Weight | Use |
|---|---|---|---|
| Large Title | 34 | Regular | Page titles (iOS nav) |
| Title 1 | 28 | Regular | Section headers |
| Title 2 | 22 | Regular | Sub-section headers |
| Title 3 | 20 | Regular | Tertiary headers |
| Headline | 17 | Semibold | List headers, emphasis |
| Subheadline | 15 | Regular | Supporting labels |
| Body | 17 | Regular | Primary reading text |
| Callout | 16 | Regular | Captions, secondary body |
| Footnote | 13 | Regular | Metadata, timestamps |
| Caption 1 | 12 | Regular | Image captions |
| Caption 2 | 11 | Regular | Fine print |

All sizes scale with Dynamic Type. See `references/accessibility.md` for size range.

---

## 2025 type direction

- **Bold, left-aligned** headings. Center-aligned headlines deprecated for navigation.
- Typography anchors the left edge — creates rhythm with the new concentricity system.
- Avoid italic for UI text; use weight changes for emphasis.
- Tight tracking for display sizes (≥ 20 pt): system handles automatically with SF Pro Display.

---

## Line length

Optimal: 45–75 characters per line (reading text).  
On iPad / Mac: use multi-column or constrained width — do not stretch body text full-width.

---

## Alignment

| Context | Alignment |
|---|---|
| Body / reading text | Leading (left in LTR) |
| Navigation titles (2025) | Leading |
| Tab labels | Center |
| Buttons | Center |
| Numeric data | Trailing |

---

## SF Symbols

Use SF Symbols for icons alongside text — they scale with Dynamic Type automatically.

- Use `.symbolRenderingMode()` to pick monochrome / hierarchical / palette / multicolor.
- Match symbol weight to adjacent text weight.
- Minimum symbol size: same as minimum touch target text size in context.
- Prefer SF Symbols over custom icons where a symbol exists.

Symbol catalog: https://developer.apple.com/sf-symbols/

---

## Localization considerations

- Allow 30–40% text expansion for translated strings — do not hardcode widths.
- Right-to-left (RTL): use leading/trailing, not left/right anchors.
- Arabic / Hebrew: system switches automatically when `semanticContentAttribute` is correct.
- CJK: system font falls back to Hiragino / PingFang — test with long strings.

---

## watchOS-specific

Body text minimum: 16 pt (system enforces via watch face).  
Ultra Small text (watch complications): use system-provided complication templates — do not go below 12 pt.

---

## tvOS-specific

Viewing distance ≈ 3 m. Minimum legible: 24 pt.  
Title: 76 pt. Headline: 38 pt. Body: 29 pt. Caption: 25 pt.  
High contrast required — light text on dark background preferred for living room.
