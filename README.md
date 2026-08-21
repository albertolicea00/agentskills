<!-- # >> agentskills -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="ascii-art-text-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="ascii-art-text-light.png">
  <img alt="clawflows" src="ascii-art-text-light.png">
</picture>

My personal set of skills for AI coding agents — the ones I actually use.  
Made for the ✨ vive‑coding workflow.

![Claude Code](https://img.shields.io/badge/Claude-Code-8A2BE2)
![Antigravity](https://img.shields.io/badge/Antigravity-Supported-purple)
![OpenCode](https://img.shields.io/badge/OpenCode-Supported-darkgreen)
![Codex](https://img.shields.io/badge/Codex-OpenAI-black)


## What is this?

A curated collection of reusable **skills** that teach AI coding agents how to perform specific tasks — from commit conventions to project scaffolding. Each skill is a self‑contained package with instructions the agent reads at runtime.

## Installation

Install all skills from this repository:
```bash
npx skills add albertolicea00/agentskills
```

Or cherry‑pick a single skill:

```bash
npx skills add albertolicea00/agentskills --skill <skill-name>

# Add `-g` (`--global`) to install at the user level instead of the current project:
npx skills add albertolicea00/agentskills --skill <skill-name> -g
```


List what's available without installing anything:
```bash
npx skills add albertolicea00/agentskills -l
```

## Skills

| Skill | What it does | Install |
| --- | --- | --- |
| 🌍 [`CommitAll`](skills/commit-all/) | Groups the working tree into semantic commits. Never pushes unless you ask. | `npx skills add albertolicea00/agentskills --skill commit-all -g` |
| 🌍 [`Timesheet Description Generator`](skills/timesheet-description-generator/) | Turns git commits into tab‑delimited timesheet entries, ready to paste. | `npx skills add albertolicea00/agentskills --skill timesheet-description-generator -g` |

<sub>🌍 global — install once at user level, available in every project · 📁 project — install into the repo that needs it (drop the `-g`)</sub>

## Related repos


- [**albertolicea00/clawflows**](https://github.com/albertolicea00/clawflows) — the workflow half of this setup: ready-to-use OpenClaw workflows for multi-step tasks you can fire from a chat app. *code, vibe, repeat...*
- [**vercel-labs/skills**](https://github.com/vercel-labs/skills) — the open agent skills ecosystem, and the `npx skills` CLI every install command on this page runs on.
- [**midudev/autoskills**](https://github.com/midudev/autoskills) — auto-detects your project and installs the best AI agent skills for it. ([autoskills.sh](https://autoskills.sh))

## License

[MIT](LICENSE) — Powered by @albertolicea00 and his unstoppable AI‑agents

> 🤖 Many of these skills are **AI‑generated** and then reviewed & refined by me. The AI proposes, I approve — every skill passes through manual review before being merged.

<!-- <a href="https://github.com/albertolicea00/agentskills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=albertolicea00/agentskills" />
</a>

Made with [contrib.rocks](https://contrib.rocks). -->