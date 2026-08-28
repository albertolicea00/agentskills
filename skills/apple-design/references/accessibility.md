# Accessibility — Apple HIG Reference

Source: https://developer.apple.com/design/human-interface-guidelines/accessibility  
Platforms: iOS, iPadOS, macOS, watchOS, tvOS, visionOS

---

## Core principle

Design for everyone first. Accessibility features should not feel like workarounds — they improve the experience for all users.

---

## Touch & pointer targets

| Platform | Minimum target |
|---|---|
| iOS / iPadOS | 44×44 pt |
| watchOS | 44×44 pt |
| macOS | No enforced minimum; 20×20 pt recommended |
| tvOS | Focus-based; no tap target |

Add padding if the visual element is smaller — hit area can exceed the visible element.

---

## Color contrast (WCAG 2.1 / Apple extended)

| Text type | Minimum ratio |
|---|---|
| Normal text (< 18 pt regular / < 14 pt bold) | 4.5 : 1 |
| Large text (≥ 18 pt regular / ≥ 14 pt bold) | 3 : 1 |
| UI components & graphics | 3 : 1 |
| Decorative / inactive elements | No requirement |

Measure: foreground color vs. background color.  
Test both light and dark mode.  
Use "Increase Contrast" accessibility setting — design must remain usable.

Never use color as the **only** means to convey information.  
Pair color with shape, label, pattern, or icon.

---

## Dynamic Type

Support all 11 text sizes. Never truncate or clip text at any size.

| Size name | xSmall → AX5 range |
|---|---|
| xSmall | Smallest (≈11 pt body equiv.) |
| Small | — |
| Medium | — |
| Large | Default |
| xLarge | — |
| xxLarge | — |
| xxxLarge | — |
| AX1 | Accessibility sizes begin |
| AX2 | — |
| AX3 | — |
| AX4 | — |
| AX5 | Largest (≈50+ pt body equiv.) |

Rules:
- Use `UIFont.preferredFont(forTextStyle:)` / SwiftUI `.font(.body)` etc. — never hardcode pt sizes.
- Layouts must reflow, not truncate. Use `minimumScaleFactor` only as last resort, never below 0.8.
- Custom fonts must be scaled with `UIFontMetrics`.
- Icons next to text must scale proportionally.

---

## VoiceOver

Every interactive element needs an accessibility label.

| Element | Requirement |
|---|---|
| Image (informational) | `accessibilityLabel` describing content |
| Image (decorative) | Mark hidden: `accessibilityHidden = true` |
| Button | Label states purpose ("Submit form", not "Button") |
| Custom control | Must have `accessibilityTraits` set correctly |
| Groups | Use `accessibilityElements` to group logically |

Labels:
- Concise — one phrase, no punctuation at end.
- No type in label ("Submit button" → "Submit"; VoiceOver announces trait separately).
- Localized.

Hints (optional): describe result of action. "Double-tap to submit the form." Start with verb.

Avoid:
- Unlabeled images.
- Focus traps.
- Rapid auto-advancing content without pause control.

---

## Reduce Motion

When "Reduce Motion" is on, remove or replace:
- Parallax effects
- Zooming transitions (replace with fade/dissolve)
- Auto-playing video / GIF
- Springy physics animations

Check: `UIAccessibility.isReduceMotionEnabled` / `.accessibilityReduceMotion` env value.  
Don't remove all animation — dissolves and static transitions are fine.

---

## Reduce Transparency

When "Reduce Transparency" is on:
- Remove blur / vibrancy backgrounds.
- Provide a fully opaque fallback color.
- Liquid Glass surfaces: system handles automatically on UIKit; SwiftUI `.ultraThinMaterial` degrades automatically.

---

## Switch Control & Full Keyboard Access

All interactive elements must be reachable sequentially.  
Custom focus order: use `accessibilityViewIsModal` for modal overlays.  
Keyboard shortcuts (macOS/iPadOS): provide menu equivalents.

---

## Text alternatives for non-text content

| Content | Alternative |
|---|---|
| Charts / graphs | Summary label + data table |
| Maps | Text description of purpose |
| Video | Captions (CEA-608 / WebVTT) + audio description track |
| Audio | Transcript |
| CAPTCHA | Audio alternative |

---

## watchOS-specific

- Use Haptics to supplement visual feedback.
- Large text sizes more likely — watch faces are small.
- Do not rely on color alone on watch face complications.

---

## visionOS-specific

- Support eye tracking as primary interaction — ensure all targets are reachable by gaze.
- Spatial audio should be supplementary, not sole indicator.
- Avoid UI that requires precise pinch accuracy for critical actions.

---

## Testing checklist

- [ ] All sizes pass contrast ratio
- [ ] App fully navigable with VoiceOver, no unlabeled elements
- [ ] Dynamic Type AX5 does not clip or truncate content
- [ ] Reduce Motion mode tested
- [ ] Reduce Transparency mode tested
- [ ] Every interactive element ≥ 44×44 pt touch target
- [ ] Color not sole conveyor of meaning
- [ ] Captions / transcripts for all media
