# Layout — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/layout  
Updated: 2025

---

## Safe areas

Content must not be obscured by system chrome (notch, Dynamic Island, home indicator, status bar, tab bar).

### iOS safe area insets (approximate — use API, not hardcoded values)

| Area | Approx. inset |
|---|---|
| Status bar top | 44–59 pt (varies by device) |
| Dynamic Island top | 59 pt (iPhone 14 Pro+) |
| Home indicator bottom | 34 pt (Face ID devices) |
| Side bezels | 0 pt (extend to edge) |

Always use `safeAreaLayoutGuide` / SwiftUI `safeAreaInset` — never hardcode.

### Key rules
- Backgrounds and media: extend edge-to-edge (behind safe areas) for immersive look.
- Interactive controls: stay within safe area.
- Text: stay within safe area + standard margin.

---

## Standard margins

| Context | Margin |
|---|---|
| iOS content margin | 16 pt (compact) / 20 pt (regular) |
| iPad content margin | 20–40 pt (scales with display size) |
| macOS window content | 20 pt |
| List row horizontal padding | 16 pt |

Use `layoutMarginsGuide` / `.padding()` — not fixed values where possible.

---

## Adaptive layout (size classes)

| Size class | Context |
|---|---|
| Compact width + Compact height | iPhone landscape (small phones) |
| Compact width + Regular height | iPhone portrait |
| Regular width + Compact height | iPad landscape (slide over) |
| Regular width + Regular height | iPad full screen, Mac |

Design for compact first, then progressively enhance for regular.

---

## Concentricity (2025)

Apple's 2025 design language uses three shape families with matched corner radii.

### Shape families
| Name | Behavior | Examples |
|---|---|---|
| Fixed | Absolute corner radius (does not scale) | App icon, avatar |
| Capsule | Corner radius = half the height | Buttons, pills, tags |
| Concentric | Radius scales with padding from an outer shape | Modal on rounded screen, card in rounded bar |

### Concentric radius formula
```
innerRadius = outerRadius - padding
```
Example: screen corner radius ≈ 44 pt. A card inset 8 pt has radius ≈ 36 pt.

Apply concentricity whenever an element nests inside a rounded container:
- Buttons inside a modal sheet
- Cards inside a sidebar
- Controls inside a Liquid Glass bar

---

## Grid & columns

### iOS
| Width | Columns |
|---|---|
| Compact (< 480 pt) | 4 |
| Regular (≥ 480 pt) | 8 or 12 |

### iPad / Mac
Use 12-column grid. Sidebar typically 3–4 columns, content area 8–9.

Gutters: 16–20 pt.

---

## Scroll behavior (2025)

Soft edge effects replace hard dividers at scroll boundaries.  
- Top of scroll: content fades into the navigation bar (glass blur).
- Bottom of scroll: content fades into the tab bar / toolbar.
- Do not use `hairline` borders at top/bottom of scroll views — the system handles this.

---

## Spacing scale

Use multiples of 4 pt for all spacing values.

| Token | Value |
|---|---|
| xs | 4 pt |
| sm | 8 pt |
| md | 12 pt |
| base | 16 pt |
| lg | 20 pt |
| xl | 24 pt |
| 2xl | 32 pt |
| 3xl | 48 pt |

---

## watchOS layout

Screen sizes (pts):
| Watch | Width × Height |
|---|---|
| 38mm | 136×170 |
| 40mm | 162×197 |
| 41mm | 176×215 |
| 44mm | 184×224 |
| 45mm | 198×242 |
| 49mm (Ultra) | 205×251 |

Use `WKInterfaceGroup` / SwiftUI stacks — do not pin absolute coordinates.  
Minimum padding from edge: 2 pt.

---

## tvOS layout

Safe zone: inset all content 60 pt from all edges (accounts for TV overscan + focus halo).  
Focus halo: system adds ~15 pt visual expansion on focus — do not cut off at edges.  
Standard card size: 250×375 pt (portrait), 548×308 pt (landscape 16:9).

---

## visionOS layout

No screen boundary — app windows float in space.  
Standard window minimum: 400×400 pt.  
Ornaments (toolbar / sidebar extensions): appear 16 pt below the window.  
Do not use absolute screen coordinates — use scene-relative layout.
