# Platform-Specific Design Guidelines — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/  
Updated: 2025

---

## Designing for iOS

### Context
Held in hand. Portrait primary. Thumb reach critical. Interactions: touch, gestures, voice.

### Key constraints
- One app, full screen at a time (except Slide Over).
- Thumb reach: content requiring frequent interaction → bottom half of screen.
- Top-of-screen actions: difficult to reach on large iPhones (avoid primary actions there).
- Battery / performance sensitive: minimize background work.

### iOS-specific patterns
- Swipe-from-left edge: always navigates back (do not intercept).
- Pull-to-refresh: standard pattern for feed/list updates.
- Tap + hold: reveals context menu.
- Bottom sheet: preferred over centered modal for most non-destructive overlays.
- Dynamic Island: Live Activities and real-time status only.

### Navigation
`NavigationStack` (hierarchical) or `TabView` (flat). Never both at top level simultaneously.  
Tab bar: bottom. Max 5 tabs.  
Large title: top-level screens only.

---

## Designing for iPadOS

### Context
Held in hand or on desk. Both orientations common. Hardware keyboard frequent. Pointer (Apple Pencil, mouse) possible.

### Key differences from iOS
- Regular width in landscape → sidebar layout preferred over tab bar.
- Multitasking: Slide Over, Split View, Stage Manager — design for all widths.
- Pointer: provide hover states for interactive elements.
- Drag and drop: critical on iPad — users expect it.
- Keyboard shortcuts: provide for all primary actions.
- Larger tap targets not needed — pointer users are precise.

### Navigation
`NavigationSplitView` preferred: sidebar (primary) + detail.  
Falls back to `NavigationStack` in compact width automatically.  
Tab bar: appears in compact only (sidebar otherwise).

### Multitasking widths
| Scenario | Width class |
|---|---|
| Full screen landscape | Regular |
| Split 50/50 | Both regular (13"), one compact (11") |
| Slide Over | Compact |
| Stage Manager window | Varies |

---

## Designing for macOS

### Context
Desk-based. Mouse / trackpad + keyboard. Precise pointer. Multiple windows. Larger screen.

### Key differences
- Menu bar: primary action surface (not nav bar).
- Multiple windows: support it — do not block or prevent.
- Keyboard shortcuts: required for all frequently used actions.
- Right-click: context menus expected everywhere.
- Toolbar: top of window. Contains primary actions.
- Sidebar: left, collapsible.
- Inspector: right, for properties/details.
- No touch — no swipe gestures, no tap-and-hold.

### Window anatomy
```
[title bar / toolbar]
[sidebar] | [content] | [inspector (optional)]
[status bar (optional)]
```

### macOS-specific
- Preferences (Settings): `Cmd+,` — always available.
- Services menu: support for selected content.
- Drag and drop: expected everywhere.
- Full screen mode: `Cmd+Ctrl+F` — support it.
- Dark mode: must support (macOS users toggle frequently).
- Scroll bars: overlay or always-visible depending on user preference.

### Typography on macOS
Nav bar title: not present (use window title bar).  
Main content: regular weight, higher density than iOS acceptable.

---

## Designing for watchOS

### Context
Glanceable. Worn on wrist. 1–3 second interactions. Small screen. Crown + side button. Haptics primary feedback.

### Key constraints
- Interactions must complete in < 30 s — long tasks → phone.
- One active session at a time (watch app suspends in background).
- No persistent keyboard — use dictation, scribble, or pre-defined responses.
- Battery critical — minimize polling, use background refresh API.

### Interaction model
- Crown: scroll, zoom, select.
- Side button: app switcher / action button (Series 9+).
- Tap: primary action.
- Long press: context menu (limited).
- No swipe-from-edge for back — use back button or `.navigationBarBackButtonHidden(false)`.

### Layout
Full-bleed backgrounds (extend to screen edges).  
System-provided margins: 2 pt from edge for content.  
Single column. No tabs (use page-style navigation or list).  
Complications: use `WidgetKit` complication families.

### watchOS-specific patterns
- Digital Crown integration: `focusable()` + `.digitalCrownRotation()`.
- Workout sessions: keep active in foreground via `WKExtendedRuntimeSession`.
- Notifications: short look (2 s) → long look (scroll for actions).
- Complications: always-on display aware — use `isLuminanceReduced`.

---

## Designing for tvOS

### Context
Living room. 3 m viewing distance. D-pad remote. No touch. Focus-based UI.

### Key constraints
- No touch, no mouse — D-pad only (Up/Down/Left/Right/Select/Menu/Play).
- Focus: always one focused element. System renders focus halo.
- Viewing distance: everything must be readable at 3 m.
- Safe zone: 60 pt inset from all edges.
- No text input without remote or game controller (use search suggestions).

### Focus engine
System manages focus automatically.  
`UIFocusEnvironment`: customize focus behavior.  
Never build custom focus — use system `focusable()`.  
Tab bar: top (not bottom — users sit far away, bottom is harder).  
Cards: primary navigation element. 16:9 or 2:3 aspect ratio.

### tvOS-specific
- Parallax effect: system-applied on focused elements.
- Top Shelf extension: featured content when app is in top row of Home Screen.
- Layered images: 2–5 layers for parallax. System animates on focus.
- Screensaver-safe: app must handle `UIApplicationDelegate.applicationWillResignActive` (TV turns off screensaver mode).

### Typography for TV
Headline: 76 pt. Title: 57 pt. Body: 29 pt. Caption: 25 pt.  
High contrast: light text on dark.  
No thin font weights — disappear at distance.

---

## Designing for visionOS

### Context
Spatial. User sees real world + digital content. Eye tracking + pinch gestures. Variable proximity to virtual objects. No fixed screen.

### Key concepts
- Windows float in space (no fixed position).
- Ornaments: toolbars/sidebars that attach to window edges, floating 16 pt outside.
- Spaces: Shared (see other apps + real world), Full Space (only your app).
- Immersive: 360° environment override.

### Interaction model
- Look + pinch: equivalent to tap.
- Look + pinch-and-hold: equivalent to long press.
- Look + two-finger pinch: zoom / scale.
- No physical keyboard by default — use virtual keyboard or voice.
- Pointer: eye tracking is the pointer (no mouse).

### Window sizing
Default window size: 1280×720 pt.  
Minimum: 400×400 pt.  
User can resize freely — design for all sizes.  
Content should not rely on window position in space.

### Depth & materials
Three material depths: `.regularMaterial`, `.thickMaterial`, `.chrome`.  
Content behind windows: blurred (same as Liquid Glass).  
3D content: `RealityKit` / `Model3D`.  
Depth sorting: system-managed — do not override Z-order for standard UI.

### visionOS-specific
- Eye tracking privacy: system only tells you what was selected, not where eyes are looking continuously.
- Spatial audio: position audio in 3D space with `RealityKit`.
- Hands: available via hand tracking API (Full Space only, requires entitlement).
- App icon: 3-layer (front/middle/back) 1024×1024 per layer.
- Hover effect: automatic on focusable elements — do not disable.
