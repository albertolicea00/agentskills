---
name: timesheet-description-generator
description: Turn git commits or task notes into tab-delimited timesheet log entries
---

# Timesheet Description Generator

## Objective

Convert raw git commits, pull requests, issue notes, or informal task descriptions into concise, informative, professionally formatted timesheet log entries — ready to paste into a spreadsheet.

## Output Format

Tab-delimited, one line per entry, no leading column:

```text
M/D/YYYY<TAB>H:MM<TAB>Description text here.
```

- **Date** — `M/D/YYYY` (e.g. `8/18/2026`). No zero padding.
- **Hours** — `H:MM` (e.g. `1:00`, `2:30`, `8:00`). Daily blocks sum to a full shift (4h + 4h, or 8h).
- **Language** — descriptions always in English, regardless of input language.
- **Separator** — a single literal tab. No Markdown tables unless the user explicitly asks.
- **No preamble** — emit the lines only. No intro sentence, no trailing commentary unless asked.

## Writing Rules

### 1. Business and technical impact over jargon

State *what* changed, *where* (which component/layer), and *why/how* it affects the flow. Open with a past-tense action verb: Implemented, Refactored, Resolved, Migrated, Built, Enhanced, Extracted, Vendored, Investigated.

Ban empty buzzwords ("streamlined workflows", "optimized processes", "leveraged synergies") whenever a concrete specific exists.

### 2. Consolidate by default — never a 1-to-1 commit dump

Unless the user explicitly asks for a per-commit breakdown, group related commits into **1–4 coherent entries per day**, each a 2–4h block.

Group by domain/layer:

- Backend / APIs
- Database / queries
- Worker / Celery tasks
- Frontend / UI
- Bugfixes / investigative support

### 3. Project vocabulary comes from the project, not from this skill

Before writing entries, look for a per-project context file, checking in order:

1. `.timesheet-context.md` at the repo root of the project being logged
2. `.timesheet/context.md`
3. A `## Timesheet` section in that project's `CLAUDE.md` / `AGENTS.md`

If one exists, follow it: use its domain groupings, its shift length, its vocabulary, and its avoid-list. A project's own terms always beat a generic phrasing.

If none exists, work generically from the commit text alone — do not invent domain jargon. Mention once that `references/project-context-template.md` can be copied into the project to sharpen future entries, then produce the output anyway. Never block on a missing context file.

## Examples

All examples use a fictional project (**ShipCrate**, a subscription-box shop) so the style is visible without borrowing any real repository's names. Substitute your own project's vocabulary via its context file.

**Input** — database and tooling commits, same day

```text
2026-03-04 | aaa1111 | feat(debug): add local job runner (no broker, no Docker)
2026-03-04 | bbb2222 | refactor(contacts): extract contact-tag queries into .sql files
2026-03-04 | ccc3333 | refactor(orders): consolidate pre/post-processing into one module
```

**Output**

```text
3/4/2026	4:00	Built a local job runner to debug background tasks directly without Docker or broker setup, and reorganized the developer tooling scripts around it.
3/4/2026	4:00	Extracted inline contact-tag queries into dedicated .sql files and consolidated order pre/post-processing into a single module.
```

Two entries, not three: the tooling commit is its own concern, the two refactors share a layer.

---

**Input** — feature plus the cleanup it enables

```text
feat(batch): resolve monthly items per order's own billing cycle (cutoff 25th / 5th)
feat(ui): drop the month picker and its /monthly-items endpoint
```

**Output**

```text
3/5/2026	5:00	Reworked batch processing to resolve each order's monthly items from its own billing cycle and cutoff dates, and removed the now-obsolete month picker along with its backend endpoint.
```

One entry: the deletion only makes sense as part of the feature.

---

**Input** — dependency replacement, described informally

```text
swapped the third-party billing client for our own requests-based one, moved the modules in-tree, ran the tests, merged and deployed
```

**Output**

```text
3/6/2026	3:30	Replaced the third-party billing client with an in-tree requests-based implementation, ran end-to-end tests, and merged and deployed the change.
```

Informal prose in, same structure out. The trailing verbs (tested, merged, deployed) belong in the entry — they are the hours.

---

**Input** — platform workaround

```text
feat(signup): show the confirmation as a modal on the shop page, using client-side state to bypass the platform's hardcoded redirect
```

**Output**

```text
3/9/2026	2:00	Replaced the hosted platform's default post-signup landing page with an in-shop confirmation modal, passing state client-side to work around its hardcoded redirect.
```

Names the limitation worked around, not just the modal.

---

**Input** — investigation with no commit

```text
looked into an order where one item shipped the same day but the promo items stayed hidden and never got batched
```

**Output**

```text
3/9/2026	2:00	Investigated partially shipped orders dropping out of the batch queue, traced the filter logic that caused split promo items to miss later runs, and identified the tracking fix.
```

Investigation is billable work. Describe what was traced and concluded — never cite a real order or customer identifier in a timesheet line.

## Procedure

1. Look for a project context file (see rule 3). If found, its shift length, domains, and vocabulary override the defaults below.
2. Parse the input into `(date, scope, change)` tuples. Infer the date from commit metadata; if absent, ask once or use the date the user states.
3. Cluster changes by day, then by domain/layer.
4. Assign hours per block. Default to a standard 8h day split across 2–4 blocks; weight blocks by apparent scope.
5. Emit the tab-delimited lines, nothing else.

## Edge cases

- **No dates in input** — ask for the date range once rather than guessing; a wrong date is worse than a round-trip.
- **Input spans more than one day** — emit one group per day, days in ascending order.
- **User gives a total hour count** — respect it exactly; distribute across blocks so the sum matches.
- **One trivial commit for a whole day** — still describe the day's real work; do not pad the description with invented detail. Say what the commit shows and let the user correct the hours.
- **Merge commits, version bumps, lint-only commits** — fold into a neighboring entry; never make them their own line.
