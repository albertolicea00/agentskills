# Inputs & Controls — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/  
Updated: 2025

---

## Gestures (iOS / iPadOS)

### Standard system gestures — never override

| Gesture | System action |
|---|---|
| Swipe from left edge | Back navigation |
| Swipe from right edge | Forward (some apps) |
| Swipe from top edge | Notification Center / Control Center |
| Swipe from bottom edge | Home / app switcher |
| Long press on app icon | Edit mode / context menu |

### App gestures

| Gesture | Use |
|---|---|
| Tap | Primary action |
| Double tap | Zoom / secondary action |
| Long press | Context menu / edit mode |
| Swipe (in-content) | Delete row, reveal actions |
| Pinch | Zoom in/out |
| Rotate | Rotate object (maps, images) |
| Drag | Reorder, move, pan |
| Two-finger drag | Scroll (when single-finger is captured) |

Rules:
- Do not redefine standard gestures.
- Provide visual affordance for non-obvious gestures.
- Gestures must have keyboard / button equivalents for accessibility.

### Multitasking gestures (iPad)
Four/five-finger pinch → Home. Do not intercept.

---

## Text input

### Keyboard types

| Type | `UIKeyboardType` | Use |
|---|---|---|
| Default | `.default` | General text |
| Email | `.emailAddress` | Email fields |
| URL | `.URL` | URL/web fields |
| Number pad | `.numberPad` | PIN, code |
| Phone | `.phonePad` | Phone number |
| Decimal | `.decimalPad` | Price, measurement |
| Twitter | `.twitter` | @handles, #tags |
| Web search | `.webSearch` | Search bars |

Always set `keyboardType`, `textContentType`, and `autocorrectionType` correctly.

### Text content types (autofill)

| Field | `UITextContentType` |
|---|---|
| Username | `.username` |
| Password | `.password` |
| New password | `.newPassword` |
| Email | `.emailAddress` |
| Phone | `.telephoneNumber` |
| Address | `.fullStreetAddress` |
| One-time code | `.oneTimeCode` |
| Name | `.name` |

Missing `textContentType` breaks autofill and Password Manager integration.

### Return key labels

Match label to action: `.go`, `.search`, `.send`, `.done`, `.next`, `.continue`.  
Never use "Return" when a specific action applies.

---

## Buttons

### Styles (2025 — match Liquid Glass context)

| Style | When |
|---|---|
| Filled | Primary action on screen — one max |
| Tinted | Secondary action |
| Gray | Tertiary / neutral action |
| Plain | Least emphasis, inline actions |
| Bordered | macOS standard |

Button role:
- `.destructive` → system renders red
- `.cancel` → system positions correctly in sheets/alerts

Size: minimum 44×44 pt touch target.  
Filled + Tinted buttons: use capsule shape (concentric with container).

### Do not
- Multiple filled buttons on one screen.
- Filled button for destructive action (use `.tinted` + `.destructive` role).
- Disable buttons without explanation — show why via inline error instead.

---

## Pickers

| Picker | Use |
|---|---|
| Wheel picker | Date/time, short lists (< 20 items) |
| Inline picker | Date embedded in form |
| Compact picker | Date in tight spaces — taps to expand |
| Menu picker | List of options in a menu |
| Segmented control | 2–5 mutually exclusive options, always visible |

Segmented control: labels short (1–2 words). Max 5 segments. Equal widths.

---

## Sliders

Continuous value in a range.  
Always show current value label (above or beside thumb).  
Provide step increments for discrete values (use Stepper instead if steps are few).  
Minimum track: left = minimum color. Maximum track: right = gray.

---

## Steppers

Integer or stepped values with +/– buttons.  
Always display current value — stepper alone does not show it.  
Use when the range is small and the exact value matters.

---

## Toggles (Switches)

Binary on/off only.  
Label describes what is enabled, not the action.  
"Enable notifications" ✓ / "Notifications" ✓  
"Turn on notifications" ✗ (label, not action)

---

## Search

Use `UISearchController` / SwiftUI `.searchable()`.  
Position: in nav bar (standard), below nav bar (prominent).  
Scope bar: show when results can be filtered by category.  
Do not build custom search UI — standard search integrates with Spotlight.

---

## Forms & settings

Group related fields with `Form` / `List` grouped style.  
Labels: left-aligned, brief, sentence case (not Title Case).  
Validation: inline, below the field, on submit — never disruptive modal.  
Required fields: mark optional, not required (default assumption is required).

---

## Focus (iPadOS / macOS / tvOS)

iPad hardware keyboard: Tab moves focus. All interactive elements must be reachable.  
macOS: full keyboard access — Tab, Space to activate, arrow keys for groups.  
tvOS: D-pad navigates focus. Focus halo: system-rendered, do not customize.

---

## Pointer (iPadOS / macOS)

iPadOS pointer adapts shape on hover:
- Over text → I-beam
- Over button → snap to button with halo
- Over scroll area → default arrow

Use `UIPointerInteraction` / `.pointerStyle()` to set custom pointer styles.  
Do not use hover state as sole indicator — touch users have no hover.

---

## Drag and drop

Provide drag from any content that can be moved or copied.  
Show visual lift (system-provided scale + shadow) on drag start.  
Drop targets: highlight on hover.  
Support both in-app and cross-app drop where the data type allows.  
Use `UTType` for data type declaration.
