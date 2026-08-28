---
name: apple-design
description: Apple HIG reference for designing & reviewing iOS/iPadOS/macOS/watchOS/tvOS/visionOS UI — icons, accessibility, typography, color, layout, Liquid Glass
---

# Apple Design (HIG Reference)

## Objective

Provide authoritative Apple Human Interface Guidelines (HIG) specs to an agent designing, reviewing, or auditing UI for any Apple platform. Input: a design task or artifact (screen, component, icon). Output: spec-compliant guidance — sizes, constraints, tokens, and corrections — sourced from Apple HIG 2025.

## Procedure

1. Identify the platform(s) and task type from context:
   - **App icons** → load `references/app-icons.md`
   - **Accessibility audit** → load `references/accessibility.md`
   - **Typography / text / SF fonts** → load `references/typography.md`
   - **Colors / dark mode / tinted glass** → load `references/color.md`
   - **Layout / safe areas / spacing / concentricity** → load `references/layout.md`
   - **Liquid Glass / navigation bars / sheets / sidebars / tabs** → load `references/liquid-glass.md`
   - **Animation / haptics / loading / transitions** → load `references/motion.md`
   - **Buttons / pickers / gestures / text input / forms** → load `references/inputs.md`
   - **Lists / collections / alerts / menus / widgets / Live Activities** → load `references/components.md`
   - **Onboarding / permissions / notifications / navigation patterns** → load `references/patterns.md`
   - **SF Symbols / icons (non-app)** → load `references/sf-symbols.md`
   - **Platform-specific (iOS vs iPadOS vs macOS vs watchOS vs tvOS vs visionOS)** → load `references/platform-guidelines.md`
   - **Multiple concerns** → load all relevant refs
2. Apply the spec. State which guideline or value applies and why.
3. Flag violations with a correction. Format: `⚠ <violation> → <fix> (HIG: <section>)`.
4. When a value is not in the refs, say so and point to the canonical URL.

## Rules

1. Never invent measurements. Only output values from the loaded reference files or Apple's published docs.
2. Always specify platform and scale when giving sizes (e.g., "iOS home screen, 60 pt @ 3× = 180 px").
3. Prefer points (pt) for layout specs; use pixels (px) when specifying export assets.
4. Accessibility rules are non-negotiable — flag any violation even if the user did not ask for an a11y review.
5. Design system changed in 2025 (Liquid Glass). Flag if guidance applies to pre-2025 or post-2025 only.
6. If the user's design conflicts with HIG, say so before helping them implement it. Then implement whatever they decide.

## Output format

For design specs:
```
Platform: <iOS | iPadOS | macOS | watchOS | tvOS | visionOS>
Context: <home screen | notification | App Store | …>
Size: <N pt @ Nx = Npx>
Format: <PNG | SVG | .icon | …>
Notes: <any constraints, layer requirements, corner radius handling>
```

For violation reports:
```
⚠ <what violates HIG> → <correction> (HIG: <section name>)
```

## Edge cases

- **Unknown platform**: ask once, then default to iOS.
- **Pre-2025 icon format** (no Icon Composer): use legacy 1024×1024 single-layer PNG; note it won't support dark/tinted modes.
- **tvOS** has no standard icon mask — supply art already composited; layered format is separate.
- **visionOS** icons use a 3-layer system (front/middle/back) distinct from iOS layered icons.
- **Missing ref file**: degrade gracefully — state which file is missing and give best-effort guidance from training data, labeled as inference.
- **Conflicting HIG versions**: newer always wins; flag when a stale source contradicts current HIG.
