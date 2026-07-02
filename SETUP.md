# SETUP — Workspace scaffolding flow

> Executed by the agent on first launch (all on-ramps). Creates a per-user workspace **outside** the repo, copies templates + playbooks, then hands off to Ritual A.

---

## Inputs

- **Repo location:** a URL (for green/agent-driven paths) or a local clone path (usual path).
- **Workspace target dir:** confirm with the user; suggest `~/career-agent/` or let them choose.

## Steps

1. **Confirm the workspace dir** with the user. Create it if it does not exist. **Never write user data inside the repo itself.**
2. **Scaffold the workspace:**
   - `profile/` — empty (user data lands here during Ritual A).
   - `output/` — empty (dated RU dossiers).
   - `playbooks/` — copy from the repo.
   - `templates/` — copy from the repo.
   - `market-config.md` — copy from the repo.
   - `AgentContract.xml` — copy from the repo.
   - `profile/README.md` — write a short RU note explaining what this workspace is and that nothing leaves the machine without the user's approval.
3. **Record origin:** write `profile/.origin` with the repo URL/version and the setup date (for traceability and updates).
4. **Check state:**
   - If `profile/materials-present.md` exists → enter **ready state**.
   - Otherwise → proceed to **Ritual A**.
5. **Hand off:** tell the user (in Russian) that setup is complete and that you will now ask a short set of onboarding questions.

## Rules

- All user-facing text is in **Russian**.
- Do not create materials yourself; the user supplies them.
- Keep the workspace **portable**: plain Markdown + XML only, so it survives a tool switch (e.g., Claude Code → an open-weights setup). No tool-specific lock-in.
- If fetching the repo over HTTP, use `webfetch` against the published **raw** file URLs (the green-path user has no git).

## Green-path note (no git)

For users without git, fetch each needed file via its raw URL rather than cloning. The user's agent (you) performs the fetches; the user only pastes the launcher. If the user *wants* git later, point them to `git-helper/`.
