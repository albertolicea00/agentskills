# Motion & Haptics — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/motion  
Updated: 2025

---

## Principles

Motion communicates, orients, and delights — never decorates.  
Every animation must have a purpose: show relationship, confirm action, indicate state.  
Duration: short. Easing: natural. Never block interaction.

---

## Animation curves

| Curve | Use |
|---|---|
| Spring (default) | Most UI transitions — feels physical |
| Ease-in-out | Media scrubbing, progress bars |
| Ease-out | Elements entering the screen |
| Ease-in | Elements leaving the screen |
| Linear | Continuous motion (spinners, video) |

SwiftUI: `.spring()`, `.easeOut`, `.easeInOut`  
UIKit: `UISpringTimingParameters`, `UICubicTimingParameters`

---

## Duration guidelines

| Interaction | Duration |
|---|---|
| Micro (icon state change, badge) | 100–200 ms |
| Standard (push, modal, sheet) | 250–400 ms |
| Complex (page transition, onboarding) | 400–600 ms |
| Never exceed | 500 ms for standard UI |

Shorter feels snappy. Longer feels sluggish. When unsure, go shorter.

---

## Spring parameters (2025 defaults)

SwiftUI `.spring(response:dampingFraction:)`:

| Context | Response | Damping |
|---|---|---|
| Standard transition | 0.35 | 0.85 |
| Bouncy (app icon press) | 0.45 | 0.65 |
| Stiff (alert) | 0.25 | 1.0 |

UIKit: `UISpringTimingParameters(mass:stiffness:damping:initialVelocity:)`

---

## Liquid Glass motion

- Nav bar: content fades/blurs as it passes under glass on scroll. Do not replicate manually.
- Sheet presentation: springs from trigger point (spatial origin).
- Tab bar: floats; transitions are elastic, not linear.
- Icon press: spring bounce on tap. System handles for app icons.

---

## Parallax & gyroscope

iOS app icons respond to gyroscope with specular edge highlight.  
Do not build custom parallax layers on top of this — it competes.  
Wallpaper / visionOS environments: system-managed parallax.

---

## Reduce Motion

**Always check.** `UIAccessibility.isReduceMotionEnabled` / `.accessibilityReduceMotion`.

| Animation | Reduce Motion replacement |
|---|---|
| Zoom transitions | Cross-dissolve |
| Slide in/out | Cross-dissolve |
| Parallax | Static |
| Auto-play video / GIF | Paused (show first frame) |
| Spring bounce | Immediate / minimal |
| Spinning loaders | Allowed (purposeful motion) |

Do not remove all motion — dissolves are fine and help with orientation.

---

## Haptics

### iOS / iPadOS (Core Haptics / UIFeedbackGenerator)

| Pattern | Class | When |
|---|---|---|
| Impact light | `UIImpactFeedbackGenerator(.light)` | Snapping, small confirmation |
| Impact medium | `UIImpactFeedbackGenerator(.medium)` | Standard button confirm |
| Impact heavy | `UIImpactFeedbackGenerator(.heavy)` | Destructive action, strong confirm |
| Notification success | `UINotificationFeedbackGenerator(.success)` | Task completed |
| Notification warning | `UINotificationFeedbackGenerator(.warning)` | Non-critical issue |
| Notification error | `UINotificationFeedbackGenerator(.error)` | Failure |
| Selection | `UISelectionFeedbackGenerator` | Picker, slider tick |

Rules:
- Prepare generator before triggering: call `.prepare()` ~0.5 s before use.
- Never use haptics as decoration — only for meaningful state changes.
- Match haptic intensity to visual feedback intensity.
- Do not chain multiple haptics rapidly (< 100 ms apart).

### watchOS

Haptics are primary feedback channel (small screen, glanceable).  
Use `WKInterfaceDevice.current().play(.click)` for confirmation.  
Patterns: `.click`, `.success`, `.failure`, `.retry`, `.start`, `.stop`, `.notification`.

### macOS / tvOS

No haptics API on macOS (no Taptic Engine on Macs except Magic Trackpad — do not target).  
tvOS: no haptics.

---

## Loading states

| Duration | Pattern |
|---|---|
| < 1 s | No indicator (instant) |
| 1–3 s | Inline activity indicator (`ProgressView()`) |
| > 3 s | Progress bar with estimated time if known |
| Indeterminate | Spinner only — never fake progress |

Skeleton screens: acceptable for content-heavy views (feeds, cards).  
Do not use skeletons for actions (button taps, form submits).

---

## Page transitions

| Transition | When |
|---|---|
| Push (slide left) | Navigating deeper into hierarchy |
| Pop (slide right) | Back / up the hierarchy |
| Modal (slide up) | Context switch, sheet |
| Dissolve | Tab switch, unrelated destination |
| Cover (full screen) | Full-screen media, immersive views |

Never use custom transitions that contradict the navigation direction — users rely on direction to understand hierarchy.
