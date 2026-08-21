# AI Knowledge Base

> If you're an AI, read this first before starting any task.

## What this repo is

A collection of reusable **skills** for AI coding agents. Each skill is a self-contained directory under [skills/](skills/) holding instructions an agent reads at runtime. Skills are published for public installation via `npx skills add albertolicea00/agentskills --skill <skill-name>`, so treat everything here as public.

Supported agents: Claude Code, Antigravity, OpenCode, Codex. Skills must not depend on any single agent's proprietary features.

## Rule zero: nothing private ships

Skills are public. Before writing or editing any file here, strip:

- Employer, client, and product names
- Internal module, service, repo, table, and endpoint names
- Real commit hashes, ticket IDs, order IDs, customer IDs, account numbers
- Real URLs to internal tooling, dashboards, or staging environments
- Credentials, tokens, API keys, absolute paths containing a username

Examples and few-shot demos need a **fictional** project with invented names, invented hashes, and invented dates. If a skill genuinely needs domain vocabulary, do not bake it in — have the skill read a per-project context file from the consuming repo and ship only a template. See [skills/timesheet-description-generator/](skills/timesheet-description-generator/) for the pattern.

When a real-world detail is the only way to make an instruction clear, say so and ask before writing it.

## Repository layout

```text
skills/<skill-name>/
├── SKILL.md          # required — frontmatter + instructions
├── scripts/          # optional — helper scripts & utilities
├── examples/         # optional — reference implementations
├── resources/        # optional — templates, configs, assets
└── references/       # optional — extra docs the agent loads on demand
docs/                 # repo-level documentation
tests/                # skill test fixtures & expected outputs
```

## Creating a skill

1. **Create the directory** — `skills/<skill-name>/`, `kebab-case`.

2. **Write `SKILL.md`** with YAML frontmatter:

   ```yaml
   ---
   name: skill-name
   description: One-line summary of what the skill does
   ---
   ```

   `name` must match the directory name exactly. `description` under 80 characters — it is the only text an agent sees when deciding whether to load the skill, so it must state the trigger, not just the topic.

3. **Structure the body** in this order. Skip a section only when it genuinely does not apply:

   - **Objective** — one paragraph: what goes in, what comes out.
   - **Output format** — the exact shape of the result, with a literal example. If whitespace matters (tabs, indentation), say so and use real characters in the code block.
   - **Rules** — numbered, imperative, testable. "Group related commits into 1–4 entries per day" beats "be concise".
   - **Examples** — few-shot input/output pairs on a fictional project. Add one line per example explaining *why* the output came out that way.
   - **Procedure** — the ordered steps the agent executes.
   - **Edge cases** — what to do with missing input, ambiguity, conflicting instructions. Every skill needs this; it is where most skills fail in practice.

4. **Push variable content out of `SKILL.md`.** Anything project-, user-, or environment-specific belongs in `references/` as a template the consumer fills in, or in a file the skill discovers at runtime. `SKILL.md` stays generic.

5. **Never block on missing context.** A skill that cannot find its optional context file must degrade to a generic result and say so once — not stop and interrogate the user.

6. **Test it** — run it in at least one supported agent, with a real prompt, and verify the output matches the spec. Record the prompt and result in the PR's Testing section.

7. **Add a row to the `## Skills` table in [README.md](README.md)** — the skill name linked to its directory, its scope (`🌍 global` if it is useful in any repo, `📁 project` if it only makes sense inside one project), one short line on what it does, and the install command. Global rows carry `-g` in the install command; project rows omit it. Keep rows alphabetical.

8. **Update the changelog** (see below).

9. **Ship it through the issue and PR flow** — never straight to `main`. See below.

## Changelog upkeep

[CHANGELOG.md](CHANGELOG.md) tracks the essence of this project — the skills. It is **not** a commit log. Most commits get no entry.

**The test:** would someone who installed a skill from this repo care? If no, it does not belong in the changelog.

Add an entry when:

- A skill is added, removed, renamed, or deprecated
- A skill's instructions, output format, or behavior change in a way an installer would notice
- A skill's supporting files change what it actually does — a new `references/` template, a new script, a new discovery mechanism
- Repo structure changes in a way that affects how skills are installed or discovered
- Private data leaked and was scrubbed (`### Security`)

Do **not** add an entry for:

- README, docs, badges, images, branding, wording, typo fixes
- Meta files — `AGENTS.md`, `CONTRIBUTING.md`, `credits`, issue and PR templates
- Formatting, link fixes, reflowed prose that changes no instruction
- CI, `.gitignore`, chores, tooling with no user-visible effect

When a change does qualify, the entry goes in the **same commit**, under `## [Unreleased]`, in one of the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) categories: `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`.

One bullet per user-visible change, naming the skill, written for someone installing it — not a restatement of the diff:

```text
- Added `timesheet-description-generator` — turns git commits into tab-delimited timesheet entries.
```

Versioning follows [SemVer](https://semver.org/spec/v2.0.0.html): a breaking change to a skill's output format or frontmatter `name` is major, a new skill is minor, an instruction fix is patch. Do not invent a release version or move entries out of `[Unreleased]` unless explicitly asked to cut a release.

## Conventions

- **Directories and skill names** — `kebab-case`.
- **Commits** — Conventional Commits. Subject in imperative mood, ≤72 chars, no trailing period. See the commit shape below.
- **Co-authorship** — allowed, and **mandatory for any commit an AI wrote or substantially edited**. See below.
- **Prose in skills** — plain English, no hedging, no filler. The reader is a model following instructions, not a human being persuaded.
- **File references in docs** — relative Markdown links, not bare backticks.
- **No absolute paths**, no `~/`, no machine-specific assumptions anywhere in a skill.

## New skill intake

A new skill is not a drive-by commit. It goes through both templates, in order:

1. **Open an issue** with [`.github/ISSUE_TEMPLATE/new-skill.md`](.github/ISSUE_TEMPLATE/new-skill.md) *before* writing the skill. Fill in every field: the `kebab-case` name, what it does and why it is worth having, which supported agents it targets, the frontmatter block, and a preview of the core instructions. The issue is where the shape gets argued, so a rejected idea costs an issue instead of a branch.
2. **Branch** — `skill/<skill-name>` off `main`. Never commit a new skill directly to `main`.
3. **Build it** following the steps above.
4. **Open a PR** with [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md). Tick the 🆕 New skill type, name the skill under Skill(s) Affected, link the issue (`Closes #<n>`), and clear every checklist box. The Testing section needs the actual agent, the actual prompt, and the actual output — not "works".
5. **Merge only with the checklist green.** An unchecked box is a blocker, not a note.

The same flow applies to removing or renaming a skill — both are user-visible breaks. Fixes to an existing skill's instructions may go straight to a PR without an issue.

## Commit shape

Every commit that touches a skill uses the skill's directory name as the scope, so `git log` reads as a per-skill history:

```text
<type>(<skill-name>): <imperative summary of the behavior>
```

The scope must match the skill directory and its frontmatter `name` exactly. Types are the standard Conventional Commits set — `feat`, `fix`, `docs`, `refactor`, `chore`, `test`, `build`, `ci`, `revert`. There is no `skill:` type; a new skill is a `feat`.

The subject says what the skill now does. It never lists the files that changed — the diff already does that.

```text
feat(commit-all): add semantic commit grouping with opt-in push
fix(commit-all): stop pushing without an explicit flag
docs(commit-all): clarify the --amend safety conditions
refactor(timesheet-description-generator): move project vocabulary to a template
chore(timesheet-description-generator): rename from timesheet-generator
```

Not this:

```text
skill(timesheet-description-generator): add SKILL.md and project context template
```

Wrong type, and the subject describes the file tree instead of the capability.

Repo-level changes that belong to no skill take a conventional area scope, or none at all: `docs(readme):`, `ci:`, `chore(deps):`.

A skill's `CHANGELOG.md` entry ships in the same commit as the change it describes — never as a follow-up `docs:` commit.

## AI co-authorship

Co-author trailers are welcome here, and required whenever a model authored or substantially edited the change. This repo is openly AI-assisted — the attribution is the point, not an embarrassment to hide.

Append the trailer as the last line of the commit message, after a blank line:

```text
feat(timesheet): add per-project context discovery

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
```

Rules:

- One trailer per model that did substantive work. Multiple models on one commit get multiple trailers.
- Use the model's own published trailer identity — do not invent an email or a version string. If you do not know your exact trailer, use your model family name and the vendor's `noreply` address.
- "Substantially edited" means the model wrote the prose, the instructions, or the logic. A model that only ran `git mv` or fixed a typo the human dictated does not need a trailer.
- The human remains the commit `Author`. Co-authorship never replaces authorship.
- Add the model to [credits](credits) the first time it contributes.

## Before you report done

- `SKILL.md` frontmatter parses, `name` matches the directory
- No private data anywhere in the diff (grep for employer and product names)
- Instructions are deterministic — two agents reading them produce the same shape of output
- Edge cases section exists and covers missing/ambiguous input
- Opened via the new-skill issue template, built on a `skill/<name>` branch
- PR uses the PR template, links the issue, and has every box ticked
- Listed in `README.md` under `## Skills`
- `CHANGELOG.md` updated under `[Unreleased]`
- Tested on at least one agent, with the prompt and output recorded
