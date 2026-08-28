# SF Symbols — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/sf-symbols  
Catalog: https://developer.apple.com/sf-symbols/  
Updated: 2025 (SF Symbols 6)

---

## What SF Symbols are

Vector symbols designed by Apple, integrated with SF Pro.  
Scale and weight automatically with Dynamic Type and font weight.  
6000+ symbols across categories.  
Available: iOS 13+, macOS 11+, watchOS 6+, tvOS 13+, visionOS 1+.

---

## Rendering modes

| Mode | Description | When |
|---|---|---|
| Monochrome | Single color (tint) | Default; simple icons |
| Hierarchical | Multi-layer, same hue, varying opacity | Icons with depth (folders, documents) |
| Palette | Multi-layer, different colors per layer | Custom color coding |
| Multicolor | Fixed Apple-defined colors | Weather, emoji-adjacent, Maps |
| Automatic | Apple picks best mode per symbol | Use when unsure |

SwiftUI: `.symbolRenderingMode(.hierarchical)`  
UIKit: `UIImage.SymbolConfiguration(paletteColors:)`

---

## Variable color (SF Symbols 4+)

Some symbols accept a 0.0–1.0 value to animate layers progressively.  
Examples: `wifi`, `speaker.wave.3`, `battery.100`.  
SwiftUI: `.symbolEffect(.variableColor.iterative)`  
Use for: signal strength, volume, fill level indicators.

---

## Symbol effects (SF Symbols 5+)

| Effect | Description |
|---|---|
| `.bounce` | Vertical bounce, confirms tap |
| `.pulse` | Opacity pulse, indicates activity |
| `.variableColor` | Animates color layers in sequence |
| `.scale` | Scale up/down |
| `.appear` / `.disappear` | Fade in/out |
| `.replace` | Morphs from one symbol to another |

SwiftUI: `.symbolEffect(.bounce, value: triggered)`  
UIKit: `imageView.addSymbolEffect(.bounce)`

Use `Reduce Motion` check — disable bounce/pulse effects when enabled.

---

## Weight matching

Symbol weight must match adjacent text weight.  
SwiftUI: `.fontWeight(.semibold)` on the symbol or its container.  
UIKit: `UIImage.SymbolConfiguration(weight: .semibold)`

| Context | Weight |
|---|---|
| Body text | Regular |
| Button label | Medium or Semibold |
| Tab bar | Regular |
| Navigation bar button | Regular |
| Toolbar | Regular |
| Headline | Semibold |

---

## Size scales

Three scales per point size:
| Scale | Use |
|---|---|
| Small | Tight spaces, inline with dense text |
| Medium (default) | Standard UI |
| Large | Hero icons, empty states, feature art |

SwiftUI: `.imageScale(.large)`  
UIKit: `UIImage.SymbolConfiguration(scale: .large)`

---

## Custom symbols

When no system symbol fits, create a custom symbol in SF Symbols app.  
Export as `.svg` with correct layer structure (Ultralight–Black weights × Small/Medium/Large scales).  
Import into Xcode asset catalog as symbol image.  
Custom symbols must follow the same weight/scale grid as system symbols.

Rules:
- Match stroke weight to SF Pro strokes at the target size.
- Single path preferred; compound paths for hollow elements.
- No fills except for "filled" variant.
- Name with reverse-DNS prefix: `com.myapp.symbol.name`.

---

## Naming conventions

Variants follow a consistent suffix pattern:
| Suffix | Meaning |
|---|---|
| `.fill` | Filled version |
| `.circle` / `.circle.fill` | Enclosed in circle |
| `.square` / `.square.fill` | Enclosed in square |
| `.slash` | Strikethrough / disabled state |
| `.badge.<symbol>` | With badge overlay |

---

## Localization

Some symbols have locale variants (e.g., RTL versions, regional iconography).  
SF Symbols app shows all variants — check "Localizations" tab.  
SwiftUI / UIKit automatically selects correct locale variant.  
Do not manually flip symbols for RTL — system handles `.environment(\.layoutDirection, .rightToLeft)`.

---

## Restricted symbols

Some symbols are restricted to specific use contexts (e.g., Apple Pay, SharePlay logos).  
Check the SF Symbols app "Restrictions" badge before using.  
Using restricted symbols in incorrect contexts violates App Store guidelines.

---

## Quick reference: common symbols

| Action | Symbol |
|---|---|
| Add | `plus`, `plus.circle.fill` |
| Delete / remove | `trash`, `minus.circle.fill` |
| Edit | `pencil`, `square.and.pencil` |
| Share | `square.and.arrow.up` |
| Search | `magnifyingglass` |
| Settings | `gearshape`, `gearshape.fill` |
| Close / dismiss | `xmark`, `xmark.circle.fill` |
| Back | `chevron.left` |
| Forward | `chevron.right` |
| Expand | `chevron.down` |
| Collapse | `chevron.up` |
| Favorite | `heart`, `heart.fill` |
| Bookmark | `bookmark`, `bookmark.fill` |
| Filter | `line.3.horizontal.decrease.circle` |
| Sort | `arrow.up.arrow.down` |
| Info | `info.circle` |
| Warning | `exclamationmark.triangle` |
| Success / check | `checkmark`, `checkmark.circle.fill` |
| Error | `xmark.circle.fill` |
| Notification | `bell`, `bell.fill`, `bell.badge` |
| Home | `house`, `house.fill` |
| Person / account | `person.circle`, `person.fill` |
| Camera | `camera`, `camera.fill` |
| Photo library | `photo.on.rectangle` |
| Location | `location`, `location.fill` |
| Lock | `lock`, `lock.fill` |
| Play / pause | `play.fill`, `pause.fill` |
