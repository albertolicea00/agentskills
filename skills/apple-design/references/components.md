# Components — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/  
Updated: 2025

---

## Lists & tables

### List styles
| Style | Use |
|---|---|
| Plain | Continuous list, no grouping |
| Grouped | Settings-style, sectioned |
| Inset grouped | Rounded cards per section (iOS default settings) |
| Sidebar | Navigation list in split view |

### Row anatomy
- Leading: icon / avatar (optional)
- Content: primary label + secondary label (optional)
- Trailing: value / chevron / accessory (optional)

Chevron (`>`) only if tapping navigates deeper. Never as decoration.  
Disclosure indicator vs. detail disclosure: `>` = navigate, `ⓘ` = more info without navigating.

### Swipe actions
Leading swipe: positive actions (mark as read, favorite).  
Trailing swipe: destructive or secondary actions (delete, archive).  
Destructive: red background, confirm if irreversible.  
Limit to 3 actions per side.

---

## Collections & grids

Use `UICollectionView` / SwiftUI `LazyVGrid` / `LazyHGrid`.  
Min cell spacing: 8 pt.  
Cells must resize with Dynamic Type (especially if they contain text).  
Provide accessibility labels on cells — do not rely on image-only recognition.

---

## Navigation (components)

### Navigation bar
- Large title: entry-level screens, major sections.
- Inline title: pushed screens, detail views.
- Leading: back button (system) or custom left item.
- Trailing: primary action (Edit, Add, Done).
- Max 1 action per side unless using toolbar.

### Tab bar
- 2–5 tabs. Use "More" for extras (deprecated pattern — prefer fewer tabs).
- Icons: SF Symbols preferred. Filled = selected, outlined = unselected.
- Labels: 1–2 words max.
- Badges: numeric (count) or dot (unread indicator).

### Sidebar (iPad / Mac)
- Top level: app sections.
- Collapsible. Automatically collapses to tab bar on compact width.
- Source list style (macOS): shows hierarchy inline.

### Split view
- Primary: list / sidebar. Detail: content.
- Collapse to single column in compact width.
- Never put navigation in the detail column — it belongs in primary.

---

## Sheets & overlays

### Bottom sheet (iOS)
Detents: `.medium` (half screen), `.large` (near full).  
Drag indicator: always show for user-resizable sheets.  
Background: Liquid Glass (automatic).  
Dismiss: drag down or tap outside.

### Popover (iPad / Mac)
Anchors to a source element.  
Arrow points to source.  
Dismiss: tap outside or press Esc.  
Never on iPhone (use sheet instead — system adapts automatically).

### Alert
Disruptive — use sparingly.  
Title: brief statement of situation.  
Message: 1–2 sentences max. Omit if title is self-explanatory.  
Buttons: 1–3. Destructive = red. Cancel = always present for destructive actions.  
Never use alerts for passive information (use banners/toasts).

### Action sheet
List of choices related to current context.  
Always include Cancel.  
Destructive actions: red, at top of list.  
On iPad: appears as popover, not bottom sheet.

---

## Menus

Context menu (long press / right click): 5–10 items max.  
Pull-down menu (button): grouped with `Section`.  
Inline section headers: label the group, not each item.  
Icons: SF Symbols on leading side, 1 per item.  
Submenus: max 1 level deep. Indicate with trailing chevron.

---

## Toolbars

Bottom of screen (iOS), top or bottom (macOS).  
Principal item: center (most important action).  
Secondary: trailing. Navigation / cancel: leading.  
Use `.toolbar` + `ToolbarItem(placement:)`.  
Placements: `.principal`, `.primaryAction`, `.cancellationAction`, `.destructiveAction`, `.confirmationAction`.

---

## Indicators & feedback

### Progress
| Indicator | Use |
|---|---|
| Spinner (indeterminate) | Unknown duration, short wait |
| Progress bar (determinate) | Known progress, longer wait |
| Circular progress | Compact spaces (watch complications) |

Never fake progress. If duration unknown, use spinner.

### Badges
App icon badges: red circle + number. System-rendered — do not replicate.  
Tab bar badges: same.  
In-content badges: use semantic colors (`.badge` view modifier in SwiftUI).

### Banners / notifications (in-app)
Appear at top, auto-dismiss after 4 s.  
Include icon + title + optional subtitle.  
Tappable → deep link to relevant content.  
Do not interrupt critical user flows.

---

## Images & media

Aspect ratios: preserve original. Never stretch.  
Loading: `AsyncImage` / `URLSession` + placeholder.  
Placeholder: same aspect ratio as final image — prevents layout jump.  
Accessibility label required for all informational images.

Video:
- Provide captions track.
- Provide audio description for visual-only information.
- Play controls: system AVPlayerViewController preferred.
- Autoplay: muted only, with visible unmute control.

---

## Empty states

Every list / collection needs an empty state.  
Include: icon (SF Symbol) + title + optional description + primary action (if applicable).  
Tone: helpful, not apologetic.  
Example: "No messages" + "Send your first message" button.

---

## Onboarding screens

3 screens max for feature highlights.  
Skip button: always present.  
Permissions: request inline at point of use — not all upfront on launch.  
Do not use splash screens as branding moments beyond 1 second.

---

## Status bar

Never hide the status bar except in full-screen media / games.  
`preferredStatusBarStyle`: `.lightContent` on dark backgrounds, `.darkContent` on light.  
Status bar space: part of the safe area — do not place content under it.

---

## Home Screen widgets (WidgetKit)

Families: `.systemSmall` (2×2), `.systemMedium` (4×2), `.systemLarge` (4×4), `.systemExtraLarge` (iPad), `.accessoryCircular`, `.accessoryRectangular`, `.accessoryInline`.

Rules:
- No scrollable content inside widgets.
- No video, no animated GIFs (static snapshots only — timeline entries).
- Tap → deep link into app (no sub-actions inside widget except `.appIntent` interactive widgets).
- Content must be glanceable in < 2 s.
- Interactive widgets (iOS 17+): use `Button` and `Toggle` with `AppIntent`.

---

## Live Activities

Show real-time progress for short-duration tasks (delivery, sports, ride).  
Lock screen / Dynamic Island compact / expanded / minimal presentations.  
Update via `ActivityKit` push or local update.  
End when task completes — do not leave stale Live Activities.  
Compact leading: icon + key value. Compact trailing: status. Expanded: richer layout.
