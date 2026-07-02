# Inbound Career Agent

A self-bootstrapping, **tool-agnostic skill pack** that turns your coding agent (Claude Code, open-weights, etc.) into an **inbound career-positioning assistant** — helping senior specialists get the *right* people to come to them, aligned on goals, instead of spraying job applications.

> **Status:** v1 build in progress (P0). First worked example: a Senior UX/UI Product Design Lead (St Petersburg). The pack itself is **generic** — your positioning comes from your own onboarding, never baked in.

## What it does
- **Signal** — make you findable and compelling to the right audience.
- **Sense** — market sensing: where aligned demand is, with comp anchors for your level.
- **Screen** — qualify inbound for alignment before you spend your time.
- Active job-search is a **secondary fallback**, not the main loop.

## How it works
A single orchestrator (the agent you launch) + 7 playbooks (read on demand). **API-only** (no scraping). **Human-in-the-loop** (drafts only; you approve everything). Output in your language (Russian shipped by default).

## Three on-ramps
| Path | For | How |
|---|---|---|
| **Green** | Not agent-ready | Paste `LAUNCHER.md` to your agent and give it the repo link. It sets up and onboards you. |
| **Usual** | Savvy | `git clone`, then point your agent at the repo and run `SETUP.md`. |
| **Agent-driven** | You hand agents repo URLs | Give your agent the repo URL + `AGENTS.md`; it figures it out. |

No git yet? See `git-helper/`.

## Repo layout
- `BOOTSTRAP.md` — start here (what / why / rules).
- `AGENTS.md` — agent operating manual.
- `SETUP.md` — workspace scaffolding flow.
- `LAUNCHER.md` — green-path launcher.
- `AgentContract.xml` — role + tool definitions.
- `playbooks/` — capability runbooks (RU).
- `templates/` — blank templates copied into your workspace.
- `market-config.md` — market source map (RU default, swappable).
- `claude-code-adapter/`, `git-helper/` — optional helpers.

## Roadmap
- **P0** repo + on-ramp docs + contract stub ← current
- **P1** Ritual A (intake) + Ritual B (explication) playbooks
- **P2** the 7 capability playbooks
- **P3** tooling wiring (Tavily, DeepSeek MCP) in `AgentContract.xml`
- **P4** market-data layer
- **P5** Claude-Code adapter + polish + end-to-end smoke test

## License
MIT — see `LICENSE`.
