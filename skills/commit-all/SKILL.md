---
name: commit-all
description: Group changes into semantic commits; never pushes unless explicitly asked
---

# Commit All

## Objective

Take the current working tree, split it into logically independent commits with Conventional Commits messages, and stop. Pushing is a separate, explicitly requested action that never happens by default.

## Rule zero: push is opt-in, always

Do not run `git push` unless the invocation contains the literal `--push` flag, or the user's message contains an explicit push instruction in their own words ("push it", "commit and push", "sube los cambios").

This rule outranks everything else in this skill:

- Absence of instruction is **not** permission. "Commit these changes" means commit, not push.
- `--no-push`, "don't push", "sin push", or any negation forbids pushing for the whole invocation. If `--push` also appears, stop and ask which one is meant — never guess.
- Finishing the commits is the end of the task. Do not offer to push by doing it; say the branch is unpushed and let the user decide.
- A remote already configured, a tracking branch already set, or a previous invocation having pushed are all irrelevant. Each invocation decides alone.
- Never `git push --force`, `--force-with-lease`, or push to the default branch without an explicit instruction naming that branch.

If push is authorized, push the current branch only, and only after every commit succeeds.

## Arguments

All arguments are optional. Anything not matching a flag is free-text context describing intent.

| Flag | Effect |
| --- | --- |
| `--push` | Push the current branch after all commits succeed. Off by default. |
| `--no-push` | Explicitly forbid pushing. Wins over `--push`, which becomes a conflict to resolve. |
| `--dry-run` | Print the commit plan and stop. Nothing is staged or committed. |
| `--single` | One commit for everything, instead of grouping. |
| `--staged` | Consider only already-staged changes; leave the rest of the tree alone. |
| `--paths <globs>` | Restrict to matching paths. Everything else is left uncommitted. |
| `--type <type>` | Force the Conventional Commits type on every commit. |
| `--scope <scope>` | Force the scope on every commit. |
| `--max <n>` | Cap the number of commits; merge the smallest groups to fit. |
| `--body` / `--no-body` | Always / never write a commit body. Default: only when the *why* is non-obvious. |
| `--attribution <auto\|on\|off>` | AI co-author trailer. Default `auto` — see below. |
| `--amend` | Amend `HEAD` instead of creating a commit. Requires the safety conditions below. |
| `--yes` | Skip the plan confirmation when the grouping is ambiguous. Never skips the push gate. |

Free text adjusts wording and grouping, but never overrides what the diff actually shows. If the text describes something the diff does not contain, say so rather than writing a message that lies.

## Commit format

```text
<type>(<scope>): <imperative subject>

<body>

<footer>
```

**Types** — `feat` new feature, `fix` bug fix, `docs` docs only, `style` formatting with no logic change, `refactor` neither feature nor fix, `perf` performance, `test` tests, `build` build system or dependencies, `ci` CI config, `chore` maintenance, `revert` reverting a prior commit.

**Subject** — imperative mood ("add", "fix", "remove", never "added" or "fixes"), ≤72 characters, no trailing period, scope optional.

**Body** — only when the subject cannot carry it: non-obvious rationale, breaking changes, migration notes. Wrap at 72. Skip it entirely for self-evident changes.

**Footer** — issue references (`Closes #123`, `Refs #456`), `BREAKING CHANGE:`, and the attribution trailer if enabled.

**Breaking change:**

```text
feat(api)!: remove deprecated search endpoint

BREAKING CHANGE: /v1/search is gone; callers must use /v2/query.
```

## AI attribution

`--attribution auto` (the default) resolves from the repository's own policy, in this order:

1. A rule in the repo's `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, or a `credits` file that requires or forbids co-author trailers — obey it, and use the exact trailer identity that file specifies.
2. Existing trailers in `git log` — match the repo's established habit.
3. Neither found → **no trailer.**

`--attribution on` forces the trailer, `off` forbids it. Never invent a co-author email or a version string; if the exact trailer identity is unknown, use the model family name with the vendor's `noreply` address, or omit it.

## Safety

Blocking — stop and ask, do not proceed:

- **Secrets.** Before staging, scan the diff for `.env` files, credentials, private keys, tokens, API keys, connection strings, and hardcoded values that look like secrets. On any hit: stage nothing, name the file and line, ask for manual review.
- **Sensitive-but-legitimate files** (`.env.example`, fixtures with fake keys) — call them out and let the user confirm.

Never, without an explicit instruction:

- `git push` in any form (see rule zero), `--force`, `--force-with-lease`
- `git reset --hard`, `git checkout --` over uncommitted work, `git clean`
- `git config` changes, `--no-verify`, rewriting published history
- Reverting or discarding changes the user made

`--amend` requires all three: the user asked, `HEAD` was created in this session, and it is not yet pushed. Otherwise refuse and make a new commit.

A failing pre-commit hook means fix the cause and make a new commit. Never amend around a hook, never bypass it.

## Procedure

1. **Read state** — `git status --short`, `git diff --stat`, `git diff`, `git diff --cached`, `git log --oneline -10`. The log establishes the repo's message style; match it.
2. **Resolve arguments**, including the push decision. Detect `--push`/`--no-push` conflicts now, before any work.
3. **Scan for secrets.** Any hit ends the run.
4. **Group by intent** — one logical change per commit. Never mix a feature with an unrelated fix. Tests and docs belong with the change they cover unless they stand alone.
5. **Present the plan** — every group, its files, its subject line. On `--dry-run`, stop here.
6. **Confirm only if ambiguous.** Unambiguous grouping proceeds. Genuine ambiguity (a file that could belong to two groups, an unclear type) asks first, unless `--yes`.
7. **Commit each group** — `git add` only that group's paths, then commit. Include new, modified, and deleted files. Never `git add -A` when grouping.
8. **Push only if authorized** in step 2, and only after every commit succeeded.
9. **Report** — the commits created, and explicitly whether the branch was pushed. When it was not, say so: `Not pushed — 3 commits on feature/x.`

## Examples

Fictional project **ShipCrate**, working tree containing an API fix, its regression test, and an unrelated README typo.

**Invocation** — `commit-all`

```text
Plan:
  1. fix(api): reject orders with an empty item list
     src/api/orders.py, tests/api/test_orders.py
  2. docs: correct install command in README
     README.md

Committed 2 commits on feature/order-validation.
Not pushed — no push was requested.
```

Two commits, not one: the typo has nothing to do with the fix. Push absent because no flag was given.

---

**Invocation** — `commit-all --dry-run --max 1`

```text
Plan (dry run, nothing staged):
  1. fix(api): reject empty orders and correct README install command
     src/api/orders.py, tests/api/test_orders.py, README.md

Merged 2 groups to satisfy --max 1. Nothing committed.
```

`--max 1` forces a mixed commit; the message names both changes rather than hiding one.

---

**Invocation** — `commit-all --push "part of the checkout rework"`

```text
Committed 2 commits on feature/order-validation.
Pushed feature/order-validation → origin.
```

Free text informs wording; `--push` is what authorizes the push.

---

**Invocation** — `commit-all --push --no-push`

```text
Conflicting flags: --push and --no-push. Which applies?
Nothing staged or committed.
```

Never resolved by guessing, even though `--no-push` is the safer default.

## Edge cases

- **Clean tree** — say so and stop. Do not create an empty commit.
- **Only staged changes exist** — commit those; do not stage the rest of the tree to "help".
- **Detached HEAD** — commit if asked, but refuse to push and say why.
- **Mid-rebase, mid-merge, or unresolved conflicts** — stop. Report the state; do not commit through it.
- **Everything is one inseparable change** — one commit is the correct answer. Do not split for appearance.
- **A single file spans two intents** — the honest options are one mixed commit or a staged hunk split. Present both, ask, and never silently pick.
- **Generated or vendored files** (lockfiles, build output, `dist/`) — group them with the change that produced them, or into their own `chore` commit. Never as a `feat`.
- **No remote configured** and push was requested — commit, then report that there is no remote. Do not add one.
- **Push rejected as non-fast-forward** — stop. Report it. Never force, never pull-rebase without being asked.
- **Repo requires signed commits** — respect existing config; do not add or remove `-S`.
