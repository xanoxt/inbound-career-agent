# CLAUDE.md — project memory for Claude Code

> You are running the **Inbound Career Agent** pack. This file is the Claude Code entry point.
> Authority chain: this file → `AGENTS.md` → `BOOTSTRAP.md`.

## What to do (on launch)

1. Read `AGENTS.md` and `BOOTSTRAP.md` now.
2. Execute `SETUP.md` (scaffold workspace; choose locale → write `profile/.locale`, default `ru`).
3. Run **Ritual A** → **Ritual B** (in `playbooks/<locale>/`).
4. Only after the user explicitly confirms positioning, run capability playbooks `01`–`07`.

## Hard rules (from AGENTS.md)

- **Human-in-the-loop** — never auto-apply / post / email / connect / publish.
- **API-only** — no scraping. Search via MCP (see `TOOLING.md` + `.mcp.json`).
- **Language** — all user-facing output in the active locale (`profile/.locale`).
- **No invention** — never infer positioning; always ask (Ritual A).

## Tooling

Configure a search provider in `.mcp.json` (Tavily default; DeepSeek websearch MCP optional). See `TOOLING.md`.

## Notes

- Single orchestrator — no subagents required. (Optional: wrap each playbook in `.claude/agents/*.md` if you prefer per-capability subagents.)
- Playbooks live in `playbooks/<locale>/` (RU default, EN available).
- Tool switch later (open-weights): the workspace is plain MD/XML; only this adapter dir + `.mcp.json` are Claude-Code-specific.
