# Contributing

> **Note:** This is not an open‑contribution project. This guide exists as a personal reference so I (and my AI agents) know how to keep things organized.

## Adding a New Skill

1. **Create the directory**
   ```
   skills/<skill-name>/
   ```

2. **Write `SKILL.md`** with YAML frontmatter and markdown instructions:
   ```yaml
   ---
   name: skill-name
   description: One‑line summary of what the skill does
   ---
   ```
   The body contains step‑by‑step instructions the agent will follow at runtime.

3. **Add supporting files** (optional):
   ```
   <skill-name>/
   ├── SKILL.md
   ├── scripts/       # Helper scripts & utilities
   ├── examples/      # Reference implementations
   ├── resources/     # Templates, configs, assets
   └── references/    # Extra docs the agent can read
   ```

4. **Test the skill** — run it in at least one supported agent (Claude Code, Antigravity, OpenCode, or Codex) and verify the output matches expectations.

5. **Open a PR** using the PR template and let the review checklist pass.

## Naming Conventions

- Directories: `kebab-case`
- `SKILL.md` frontmatter `name` must match the directory name
- Keep descriptions under 80 characters

## Quality Checklist

- [ ] `SKILL.md` has valid YAML frontmatter (`name` + `description`)
- [ ] Instructions are clear and deterministic
- [ ] No hardcoded paths or user‑specific values
- [ ] Tested on at least one agent
