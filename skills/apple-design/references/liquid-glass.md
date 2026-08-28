# Liquid Glass & Navigation — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/  
WWDC25: "Say hello to the new look of app icons" (220), "Get to know the new design system" (356)  
Updated: 2025

---

## What is Liquid Glass

Liquid Glass is a material system introduced in 2025 across iOS, iPadOS, macOS, and watchOS.  
It replaces opaque UI surfaces (nav bars, tab bars, toolbars, sheets) with translucent glass panels that:
- Blur and refract content behind them
- Reflect ambient light with specular highlights
- Respond to gyroscope / device tilt with light animation
- Adapt automatically to light, dark, tinted, and clear modes

Do NOT bake glass effects into designs — use system-provided materials.

---

## Glass materials (SwiftUI / UIKit)

| SwiftUI | UIKit | Opacity |
|---|---|---|
| `.ultraThinMaterial` | `UIBlurEffect(.systemUltraThinMaterial)` | Most transparent |
| `.thinMaterial` | `UIBlurEffect(.systemThinMaterial)` | — |
| `.regularMaterial` | `UIBlurEffect(.systemMaterial)` | Default |
| `.thickMaterial` | `UIBlurEffect(.systemThickMaterial)` | — |
| `.ultraThickMaterial` | `UIBlurEffect(.systemThickMaterialDark)` | Most opaque |

Reduce Transparency: all materials automatically fall back to opaque adaptive colors.

---

## Navigation bars (2025)

- Glass material — content scrolls behind and blurs through.
- No hairline separator at bottom — scroll edge effect handles transition.
- Title: **leading-aligned**, not centered (replaces prior default).
- Large title collapses to inline title on scroll (unchanged behavior, new visual treatment).
- Back button: system-provided chevron + previous screen title — do not customize label to "Back".

---

## Tab bars (2025)

- Float above content as a glass pill/bar.
- Position: bottom of screen for iOS/iPadOS; sidebar on iPad in regular width; top for macOS.
- Max tabs visible: 5 (iOS). Use "More" disclosure for additional tabs.
- Badges: system-rendered. Do not recreate custom badge overlays.
- Tab bar shrinks / adapts when keyboard appears.

### Sidebar (iPad / Mac)
- Inset from window edge; content flows behind it.
- Use `.navigationSplitViewStyle(.balanced)` / `NavigationSplitView`.
- Collapsible in compact width — degrades to tab bar on iPhone.

---

## Sheets & modals

### Action sheets (2025)
- Spring from the element that triggered them (spatial origin matters).
- Position the trigger near the bottom of the screen when possible.
- Do not use action sheets for navigation — use menus or push views.

### Bottom sheets
- Detents: `.medium`, `.large`, and custom fractions.
- Glass background automatically.
- Drag indicator: always show for user-resizable sheets.

### Alerts
- Centered modal. Two buttons max in one row; stacks vertically beyond two.
- Destructive action: red. Cancel: default style, always present if action is destructive.

---

## Toolbars

- Attach to bottom of screen (iOS) or top/bottom of window (macOS).
- Glass material same as nav bar.
- Semantic placement: organize by function and frequency of use.
- Principal item (most important action): center. Secondary: trailing. Back/cancel: leading.

---

## Menus (context menus, pull-down menus)

- Use `.menu` button style for pull-down menus.
- Context menus on long press (iOS) / right click (Mac).
- Destructive items: `.destructive` role — system renders red.
- Max items before submenu: ~10. Group with `Section` for clarity.

---

## Scroll edge effects

Replace hard separator lines at top/bottom of scroll containers.

| Scroll position | Effect |
|---|---|
| At top | Soft fade; nav bar glass shows through |
| Scrolled | Nav bar becomes more opaque |
| At bottom | Soft fade into tab bar / toolbar |

Do not add custom shadows or borders at scroll edges — the system handles this.

---

## Structure summary

Three principles govern 2025 layout structure:

1. **Design language**: refined color + bold left-aligned type + concentricity
2. **Structure**: Liquid Glass floats above content; bars organize by function; scroll edge replaces dividers
3. **Continuity**: single anatomy, scaled per platform (iPhone compact → iPad middle → Mac wide)

---

## What to remove from pre-2025 designs

| Pre-2025 pattern | 2025 replacement |
|---|---|
| Opaque white/gray nav bar | Liquid Glass nav bar |
| Centered nav title | Leading-aligned title |
| Hairline separator under nav bar | Scroll edge effect |
| Opaque tab bar | Floating glass tab bar |
| Custom blur backgrounds | System material tokens |
| Baked drop shadows on bars | Removed — material provides elevation |
| Inline centered buttons in nav bar | Principal item toolbar pattern |

---

## Platform differences

| Platform | Liquid Glass |
|---|---|
| iOS / iPadOS | Full — nav bar, tab bar, sheets, toolbars |
| macOS | Full — title bar, toolbar, sidebar, inspector |
| watchOS | Light mode only — nav bar glass |
| tvOS | Not applicable — focus-based UI |
| visionOS | Spatial glass — windows float; ornaments use glass |
