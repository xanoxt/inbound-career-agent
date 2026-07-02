# BOOTSTRAP — Inbound Career Agent

> Read this first. It orients any agent (or human) to what this project is, what it does, what it refuses to do, and how the pieces fit.
> **Zero-context survival:** everything needed to act is contained in this repo. No outside conversation required.

---

## 1. Identity

- **What:** A self-bootstrapping, **tool-agnostic skill pack** that turns a coding agent (Claude Code, open-weights setups, etc.) into an **inbound career-positioning assistant** for a senior professional.
- **For whom:** Senior specialists — design leads, staff engineers, product leads, and similar — who want the *right* people to come to them, aligned on goals, rather than spraying job applications.
- **First worked example:** a Senior UX/UI Product Design Lead (St Petersburg, Russia). The pack itself is **generic**; that person's specifics are produced by her own onboarding and never baked into the repo.

## 2. What this is NOT

- Not a job-application bot. Not a resume blaster. Not a LinkedIn auto-connector.
- Mass outbound applications are explicitly **out of scope** and counterproductive to the inbound goal. Active job-search exists only as a secondary fallback capability (`06-active-search-fallback`).

## 3. The problem frame — three loops, in priority order

1. **Signal** — make the user findable and compelling to the right audience.
2. **Sense** — know where aligned demand is (market sensing, watchlists, comp anchors).
3. **Screen** — qualify inbound for alignment before the user spends time.

Loop 0 (active applications) is a **fallback**, not the main loop.

## 4. Architecture (v1)

- **Single orchestrator** (the agent the user launches) + **7 playbooks** (Markdown files read on demand). No multi-agent crew — simpler, debuggable, portable.
- **API-only.** Never scrape. Search via configured provider (Tavily default; DeepSeek websearch MCP optional).
- **Alignment-screen-before-reply gate** on every outbound suggestion.
- **Human-in-the-loop:** the agent drafts; the user decides. Never auto-apply, auto-post, auto-email, or auto-connect.
- **Tool-agnostic:** playbooks are plain Markdown; a thin optional `claude-code-adapter/` wires them for Claude Code. The workspace survives a tool switch (Claude Code → open-weights).

## 5. The rituals (initialization)

- **Ritual A — Intake:** the agent asks the adapted career-intake questionnaire (RU), ingests the user's materials (CV, portfolio, cases), stores results to `profile/`.
- **Ritual B — Explication:** the agent synthesizes `profile/positioning.md` from intake + materials and reflects it back to the user for **explicit confirmation BEFORE any work**.

No capability playbook runs before Ritual B is confirmed.

## 6. File map

| File / Dir | Purpose | Lang |
|---|---|---|
| `README.md` / `README.ru.md` | Public face, three on-ramps, roadmap | EN / RU |
| `AGENTS.md` | Agent operating manual (path-3 entry) | EN |
| `SETUP.md` | Workspace scaffolding flow | EN |
| `LAUNCHER.md` | Green-path self-applying launcher (sent to not-agent-ready users) | RU + EN |
| `AgentContract.xml` | Role + tool definitions (XML-DOM, tool-agnostic) | EN |
| `TOOLING.md` | Search-provider setup (Tavily, DeepSeek MCP) | EN |
| `playbooks/ru/`, `playbooks/en/` | Capability runbooks per locale | per locale |
| `templates/ru/`, `templates/en/` | Blank templates per locale, copied into the workspace | per locale |
| `market-config.md` | Market source map (RU default, swappable) | RU |
| `claude-code-adapter/` | Optional Claude Code wiring | EN |
| `git-helper/` | Step-by-step git setup for path-2 stragglers | RU + EN |

## 7. Workspace (generated on the user's machine, NOT in the repo)

`profile/` (user data), `output/` (dated dossiers in the active locale), a copy of `playbooks/<locale>/`. The repo contains only generic material.

## 8. Language rule

- **Human-facing output:** the active locale — **RU** (default) or **EN**. Chosen in `SETUP.md`, stored in `profile/.locale`.
- **Machine-readable internals** (this file, `AGENTS.md`, `AgentContract.xml`, `SETUP.md`): English (EN).
- Playbooks/templates ship per locale under `playbooks/<lang>/`, `templates/<lang>/`. RU is the shipped default market; swappable via `market-config.md`.

## 9. Constraints (hard)

- No personal data in the repo.
- No secrets in the repo.
- API-only; no scraping.
- Never infer the user's positioning — always ask (Ritual A).
- Every artifact must orient a cold reader/agent on its own.

## 10. Status

v1 build in progress. **P0** = repo skeleton + on-ramp docs + contract stub. See `README.md` for the phase roadmap.
