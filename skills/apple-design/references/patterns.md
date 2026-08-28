# Patterns — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/patterns  
Updated: 2025

---

## Launching

### Launch screen

Required: `LaunchScreen.storyboard` or `UILaunchScreen` info.plist key.  
Show immediately; load app state behind it.  
Match launch screen to first visible app screen — reduces perceived load time.  
Never use as a branding splash (Apple guideline).  
Duration: as short as possible, never artificial delay.

### First launch

Request permissions at point of use, not all at launch.  
Show value before asking for anything.  
Onboarding: 3 screens max, always skippable.

---

## Navigation patterns

### Hierarchical
One path per screen. Back = up hierarchy.  
Use: Settings, Mail, Files.  
Implementation: `NavigationStack`.

### Flat
Multiple sections at top level, no deep hierarchy.  
Switching between tabs does not push — it replaces context.  
Use: Music, App Store, Health.  
Implementation: `TabView`.

### Experience-driven
Non-standard, game/media-specific flows.  
Custom navigation — must still support back gesture and VoiceOver.

### Avoid
Mixing hierarchical and flat in the same level.  
Deep hierarchies (> 3 levels before content).  
Modal flows for multi-step forms that should be push navigation.

---

## Modality

Use modals for:
- Tasks that require completion or cancellation before returning (e.g., compose email).
- Confirming destructive actions.
- Getting required input before proceeding.

Do NOT use modals for:
- Navigation between main sections.
- Showing content the user could also see inline.
- Non-blocking information (use banners).

Always provide explicit dismiss (Done / Cancel / ✕).  
Nested modals: avoid. Max 1 level of modal depth.

---

## Permissions

Request at the moment the feature is needed, not before.  
Explain why before the system prompt appears (custom pre-prompt screen).  
Never request permissions on first launch with no context.

Common permissions:
| Permission | When to request |
|---|---|
| Camera | On first camera use |
| Microphone | On first audio recording |
| Location | On first map / location feature use |
| Notifications | After user has experienced value (not at launch) |
| Contacts | On first contact-related action |
| Photos | On first photo access |
| Health | On first health data use |

If denied: gracefully degrade. Offer Settings deep link.  
Do not repeatedly re-prompt for denied permissions.

---

## Notifications (push)

### Types
| Type | Interruption level |
|---|---|
| Passive | No sound, no banner — added to Notification Center |
| Active | Sound + banner (default) |
| Time sensitive | Breaks through Focus modes |
| Critical | Breaks through silent mode (requires entitlement) |

### Design
- Title: what happened (not app name — system shows that).
- Body: context / action needed, 1–2 lines.
- Category actions: max 4 (2 on lock screen without expanding).
- Rich notification: image, video, or custom UI via Notification Content Extension.

### Rules
- Do not send notifications users did not request.
- Batch non-urgent notifications — do not spam.
- Time Sensitive: use sparingly; Apple reviews apps that overuse it.
- Provide notification preferences in app settings.

---

## Settings

App settings in iOS Settings app (general preferences) vs. in-app settings (per-session, context-specific).  
In iOS Settings: use `Settings.bundle` for global app preferences.  
In-app settings: things users change frequently or contextually.

Settings screen structure:
1. Account / profile (if applicable) — top
2. Core preferences
3. Notifications
4. Privacy
5. About / Help / Feedback — bottom

---

## Searching

Use system `UISearchController` / `.searchable()`.  
Results update as user types (no "Submit" required).  
Recent searches: persist between sessions.  
No results: show empty state with suggestions.  
Scopes: show when results can be filtered categorically.  
Tokens: use for structured filters (e.g., `from: Alice`).

---

## Entering data

Reduce input burden:
- Default to the most common value.
- Pre-fill from existing data (autofill, Contacts, Health).
- Use pickers over free text where valid options are known.
- Progressive disclosure: show only required fields first.

Validation:
- Inline, below field, on change or on submit.
- Never block typing to validate.
- Never clear the field on error — keep user input.

---

## Undo & redo

Support shake-to-undo (iOS) — `UIApplication.shared.applicationSupportsShakeToEdit`.  
Provide Edit menu Undo / Redo on macOS and iPadOS.  
Never make destructive actions impossible to undo without warning.  
Confirmation dialog required for: delete, clear all, send (irreversible).

---

## Sharing

Use `UIActivityViewController` / SwiftUI `ShareLink` for all sharing.  
Never build a custom share sheet.  
Provide a default subject and body for email/message sharing.  
SharePlay (`GroupActivities`): use for real-time shared experiences in FaceTime.

---

## Ratings & reviews

Use `SKStoreReviewController.requestReview()` — never custom prompts.  
Prompt timing: after a meaningful positive interaction, not on launch.  
Max: system limits to 3 prompts per year regardless of how often you call the API.  
Never gate content behind a rating.

---

## Accounts & authentication

Sign in with Apple: required if app offers any third-party social login (App Store rule).  
PassKeys: preferred over passwords — use `ASAuthorizationController`.  
Biometrics: Face ID / Touch ID for re-authentication (not first sign-in).  
Never store plaintext passwords — use Keychain.

---

## Multitasking (iPad)

Support Slide Over, Split View, and Stage Manager.  
Layout must work at any width (compact through regular).  
Never disable multitasking via `UIRequiresFullScreen` without strong justification (games, AR).  
State must be preserved when app moves to background.

---

## Printing

Use `UIPrintInteractionController`.  
Provide print option in Share sheet / Edit menu.  
Print preview: system-provided, do not replicate.

---

## File management

Use `UIDocumentPickerViewController` for file selection.  
Save to Files app via `UIDocument`.  
iCloud Drive: opt in via `NSUbiquitousContainers` in Info.plist.  
Never access files outside your sandbox without document picker.
