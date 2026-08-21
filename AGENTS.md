# AI Knowledge Base

> If you're an AI, read this first before starting any task.

## What this repo is

A collection of reusable **skills** for AI coding agents. Each skill is a self-contained directory under [skills/](skills/) holding instructions an agent reads at runtime. Skills are published for public installation via `npx skills add albertolicea00/agentskills/<skill-name>`, so treat everything here as public.

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

7. **Update the changelog** (see below), then open a PR with [the template](.github/PULL_REQUEST_TEMPLATE.md) and clear its checklist.

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
- **Commits** — Conventional Commits, matching existing history: `docs:`, `feat:`, `fix:`, `chore:`, `refactor:`. Subject in imperative mood, no trailing period.
- **Co-authorship** — allowed, and **mandatory for any commit an AI wrote or substantially edited**. See below.
- **Prose in skills** — plain English, no hedging, no filler. The reader is a model following instructions, not a human being persuaded.
- **File references in docs** — relative Markdown links, not bare backticks.
- **No absolute paths**, no `~/`, no machine-specific assumptions anywhere in a skill.

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
- `CHANGELOG.md` updated under `[Unreleased]`
- Tested on at least one agent, with the prompt and output recorded
