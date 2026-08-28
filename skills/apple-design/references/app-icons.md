# App Icons — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/app-icons  
Updated: 2025 (Icon Composer / Liquid Glass era)

---

## Workflow (2025+)

Design with **Icon Composer** (Apple tool). Exports `.icon` → drag into Xcode.  
Xcode generates all platform sizes automatically.

### Canvas sizes
| Platform | Canvas |
|---|---|
| iOS / iPadOS / macOS | 1024 px |
| watchOS | 1088 px (overshoots mask; system clips) |

### Layer structure
- 1–4 groups (Z-order: bottom = background, top = foreground)
- Formats per layer: **SVG** (preferred, text → outlines first) or **PNG** (for gradients/rasters)
- Do NOT include: rounded masks, background fills, baked shadows/bevels
- Masks and material effects applied automatically by Icon Composer / system

### Appearance modes (all: iOS, iPadOS, macOS; watchOS: light only)
| Mode | Description |
|---|---|
| Light | Default; new glass material |
| Dark | Dark glass; background shifts |
| Tinted light | Color infused into light glass |
| Tinted dark | Color added to dark foreground |
| Clear light / dark | Fully transparent glass |
| Mono | Monochrome glass |

---

## iOS / iPadOS Icon Sizes

| Context | Device | Points | Scale | Pixels |
|---|---|---|---|---|
| App Store | — | 1024×1024 | 1× | 1024×1024 |
| Home screen | iPhone | 60×60 | 2× | 120×120 |
| Home screen | iPhone | 60×60 | 3× | 180×180 |
| Home screen | iPad | 76×76 | 2× | 152×152 |
| Home screen | iPad Pro | 83.5×83.5 | 2× | 167×167 |
| Spotlight | iPhone | 40×40 | 2× | 80×80 |
| Spotlight | iPhone | 40×40 | 3× | 120×120 |
| Spotlight | iPad | 40×40 | 1× | 40×40 |
| Spotlight | iPad | 40×40 | 2× | 80×80 |
| Settings | iPhone | 29×29 | 2× | 58×58 |
| Settings | iPhone | 29×29 | 3× | 87×87 |
| Settings | iPad | 29×29 | 1× | 29×29 |
| Settings | iPad | 29×29 | 2× | 58×58 |
| Notification | iPhone | 20×20 | 2× | 40×40 |
| Notification | iPhone | 20×20 | 3× | 60×60 |
| Notification | iPad | 20×20 | 1× | 20×20 |
| Notification | iPad | 20×20 | 2× | 40×40 |

Corner radius: system-applied rounded rect mask. Do not pre-round.

---

## macOS Icon Sizes

Supply all sizes — system does NOT auto-generate from 1024.

| Size @1× | Size @2× |
|---|---|
| 16×16 | 32×32 |
| 32×32 | 64×64 |
| 128×128 | 256×256 |
| 256×256 | 512×512 |
| 512×512 | 1024×1024 |

Format: PNG (each size) or single PDF (vector).  
Corner radius: system applies squircle mask.  
Note: icons with secondary elements outside the shape get auto-masked; redraw recommended for 2025 material.

---

## watchOS Icon Sizes

| Context | Watch size | Pixels |
|---|---|---|
| App Store | — | 1024×1024 |
| Home screen | 38mm | 80×80 |
| Home screen | 40mm | 88×88 |
| Home screen | 41mm | 92×92 |
| Home screen | 44mm | 100×100 |
| Home screen | 45mm | 102×102 |
| Home screen | 49mm (Ultra) | 108×108 |
| Notification | 38mm | 48×48 |
| Notification | 40mm | 55×55 |
| Notification | 41mm | 58×58 |
| Notification | 44mm | 66×66 |
| Notification | 45mm | 66×66 |
| Notification | 49mm (Ultra) | 75×75 |

Canvas: 1088 px (circular mask; breathing room built into grid).  
From Icon Composer: light mode only on Watch.

---

## tvOS Icon Sizes

tvOS uses a **layered** format (2–5 layers; system applies parallax).

| Context | Size (px) |
|---|---|
| Home screen (small) | 400×240 |
| Home screen (large) | 800×480 |
| App Store | 1280×768 |
| Top Shelf (wide) | 2320×720 |
| Top Shelf (inset) | 1920×720 |

No automatic mask — provide pre-composited art per layer as PNG.  
Each layer: same pixel dimensions, transparent background.

---

## visionOS Icon Sizes

3-layer system (distinct from iOS layered icons):

| Layer | Role |
|---|---|
| Front | Foreground subject |
| Middle | Mid-depth element |
| Back | Background |

Canvas: 1024×1024 px per layer, PNG.  
System applies specular highlights and depth rendering. Do not bake in lighting.

---

## Design principles (2025)

- Flat / frontal view. No perspective, no isometric 3D.
- Remove baked effects: drop shadows, bevels, inner glows — material adds these.
- Bold, simple shapes. Material adds richness; complexity competes with it.
- Soft gradients OK (light-to-dark); avoid harsh contrast within icon.
- Colored backgrounds encouraged (light mode especially).
- Line weights: bolder than pre-2025. Thin lines disappear against glass.
- On iOS: gyro input creates dynamic specular on icon edge — leave edge clear.

## Legacy (pre-2025 / no Icon Composer)

Provide single 1024×1024 PNG.  
No dark/tinted/clear modes. System applies corner radius mask.  
Still required for: watchOS Complications, some Settings contexts.
