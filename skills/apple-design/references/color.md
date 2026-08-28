# Color — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/color  
Updated: 2025

---

## Color space

| Platform | Color space |
|---|---|
| iOS / iPadOS / macOS | Display P3 (preferred), sRGB fallback |
| watchOS | sRGB |
| tvOS | sRGB |
| visionOS | Display P3 |

Always use wide-color assets (Display P3) where the hardware supports it.  
Provide sRGB fallback in asset catalogs.

---

## System colors (iOS / iPadOS / macOS)

Adaptive — automatically adjust for light mode, dark mode, and Increase Contrast.

### Semantic colors (use these, not hex values)

| Token | Purpose |
|---|---|
| `label` | Primary text |
| `secondaryLabel` | Secondary text |
| `tertiaryLabel` | Tertiary text |
| `quaternaryLabel` | Disabled / placeholder |
| `systemBackground` | Primary background |
| `secondarySystemBackground` | Grouped background |
| `tertiarySystemBackground` | Inset grouped |
| `systemGroupedBackground` | Form / settings background |
| `separator` | Dividers |
| `opaqueSeparator` | Non-transparent dividers |
| `link` | Tappable links |
| `placeholderText` | Input placeholder |

### System accent colors

| Color | SwiftUI / UIKit token |
|---|---|
| Blue (default) | `.accentColor` / `tintColor` |
| Red | `.red` |
| Orange | `.orange` |
| Yellow | `.yellow` |
| Green | `.green` |
| Mint | `.mint` |
| Teal | `.teal` |
| Cyan | `.cyan` |
| Blue | `.blue` |
| Indigo | `.indigo` |
| Purple | `.purple` |
| Pink | `.pink` |
| Brown | `.brown` |

Never hardcode hex values for system colors — use semantic tokens so dark mode and contrast modes work automatically.

---

## Dark mode

Every UI must support light and dark.  
Rules:
- Use adaptive semantic colors (above) — they switch automatically.
- Custom colors: provide both light and dark variants in the asset catalog.
- Never use pure black (#000000) for background — use `systemBackground`.
- Dark mode backgrounds are dark gray, not pure black (depth layers differentiate surfaces).
- Elevation in dark mode: lighter surfaces appear higher.

---

## Increase Contrast mode

System automatically increases contrast between foreground/background when the user enables this.  
Use `accessibilityContrast` environment to provide alternate assets if needed.  
Test all color combinations in this mode.

---

## 2025 Liquid Glass color

### Glass tints
Applied per-app via the app's tint color (`.accentColor`).  
In tinted glass mode: the app's tint color infuses into the glass material.  
Do not apply tint in your artwork — the system does it.

### Backgrounds under glass
- Avoid pure white / pure black backgrounds behind glass surfaces — gradients and rich colors work better.
- Light mode: colored backgrounds encouraged; they show through the glass and add personality.
- Dark mode: deep, saturated backgrounds complement glass specular.

### System Light / System Dark gradients
For icon backgrounds, use System Light Gradient or System Dark Gradient (available in Apple design templates) rather than pure white/black.

---

## Color usage rules

1. Use color to communicate, not decorate. Every color choice should have a purpose.
2. Never rely on color alone to convey state — pair with shape, label, or icon.
3. Test with Color Blind simulator (Xcode Accessibility Inspector) — at minimum Protanopia and Deuteranopia.
4. App tint color: one per app. Applied system-wide to interactive elements. Keep it recognizable.
5. Destructive actions: red only. Don't use red for non-destructive elements.
6. Disabled state: reduce opacity (typically 30–50%) rather than changing color.

---

## watchOS colors

Limited palette — watch faces use system colors.  
Complications: white / light gray text on dark background.  
Avoid color that looks similar to the watch face status indicators (red crown notification dot).

---

## tvOS colors

Default: light text on dark background for living room environment.  
Focused element: system applies a white-bordered highlight automatically.  
Do not override focus appearance color with custom code.
