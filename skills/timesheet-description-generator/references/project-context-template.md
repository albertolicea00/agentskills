# Project Context Template

Copy this into the project you log hours for, as `.timesheet-context.md` at its repo root. The skill reads it when generating entries for that project and ignores it everywhere else. Nothing project-specific belongs in the skill itself.

Keep only terms that change the wording of a log line. If a section would say "we use Postgres", drop it — that never changes a description.

---

```markdown
# Timesheet Context — <project name>

## Shift

Standard day: <8h | 6h | varies>
Default block split: <2-4 blocks | one block per day>

## Domains

Group commits by these layers. Rename or cut freely.

- <Backend / APIs>
- <Database / queries>
- <Workers / scheduled jobs>
- <Frontend / UI>
- <Bugfixes / investigation>

## Vocabulary

One line per platform or subsystem: the concrete nouns, then what an entry must name.

### <Platform or subsystem name>

<Concrete nouns: the objects, states, limits, and failure modes that show up in real work.>

Entries must name <the thing that makes the description specific — the limitation worked around, the object touched, the failure mode addressed>.

### <Second platform or subsystem>

<...>

## Avoid

<Words this project's timesheet reviewer rejects. Anything vague you keep catching yourself writing.>
```

---

## Worked example

A filled-in file for a fictional subscription-box shop, showing the intended density:

```markdown
# Timesheet Context — ShipCrate

## Shift

Standard day: 8h
Default block split: 2-4 blocks

## Domains

- Storefront (theme, checkout)
- Billing
- Fulfillment jobs
- Internal admin

## Vocabulary

### Hosted storefront platform

Theme template overrides, checkout field limits, hardcoded redirect targets, client-side state workarounds.

Entries must name the platform limitation worked around, not just the feature shipped.

### Billing

Gateway timeouts, invoice adjustments, billing-cycle-day limits, plan migrations.

Entries must name the billing object touched and the failure mode addressed.

### Fulfillment jobs

Idempotent reruns, execution traces, cycle cutoff dates, split shipments, unpicked items.

Entries must name which cutoff or item class was involved.

## Avoid

"streamlined", "optimized processes", "various improvements", "misc fixes"
```
