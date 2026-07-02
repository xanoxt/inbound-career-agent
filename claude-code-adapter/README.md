# Claude Code adapter

Thin shim to run the **Inbound Career Agent** pack in Claude Code. The pack itself is tool-agnostic MD/XML; this adapter just makes Claude Code discover it natively.

## Install (in your workspace)

1. Get the pack into your workspace (webfetch per `SETUP.md` green path, or `git clone`).
2. Copy `claude-code-adapter/CLAUDE.md` to the workspace **root** as `CLAUDE.md`. Claude Code auto-reads a root `CLAUDE.md` as project memory.
3. Add `.mcp.json` at the root per `TOOLING.md` (Tavily and/or DeepSeek websearch MCP).
4. Launch Claude Code in that dir. It reads `CLAUDE.md` → `AGENTS.md` → `BOOTSTRAP.md`, then runs `SETUP.md` → Rituals.

## What the adapter does (and doesn't)

- **Does:** point Claude Code at the pack's authority docs and the search providers.
- **Doesn't:** lock you in. Everything else is plain MD/XML. Subagents are optional (single orchestrator by design).

## Switching tools later

To move to an open-weights setup: keep the workspace (`profile/`, `output/`, `playbooks/<locale>/`); drop this adapter dir and `.mcp.json`; add your new tool's equivalent memory file (e.g., an `AGENTS.md`-style pointer) and search wiring.
