# SETUP — Workspace scaffolding flow

> Executed by the agent on first launch (all on-ramps). Creates a per-user workspace **outside** the repo, copies templates + playbooks, then hands off to Ritual A.

---

## Inputs

- **Repo location:** a URL (for green/agent-driven paths) or a local clone path (usual path).
- **Workspace target dir:** confirm with the user; suggest `~/career-agent/` or let them choose.
- **Active locale:** the user's working language (what they read). Default `ru`. Available: `ru`, `en`. Selects which `playbooks/<locale>/` and `templates/<locale>/` are copied.

## Steps

1. **Confirm the workspace dir and the active locale** with the user (default locale `ru`). Create the dir if it does not exist. Write the chosen locale to `profile/.locale`. **Never write user data inside the repo itself.**
2. **Scaffold the workspace:**
   - `profile/` — empty (user data lands here during Ritual A).
   - `output/` — empty (dated dossiers in the active locale).
   - `playbooks/` — copy `playbooks/<locale>/` from the repo (only the active locale).
   - `templates/` — copy `templates/<locale>/` from the repo (only the active locale).
   - `market-config.md` — copy from the repo.
   - `AgentContract.xml` — copy from the repo.
   - `profile/README.md` — write a short note (in the active locale) explaining what this workspace is and that nothing leaves the machine without the user's approval.
3. **Record origin:** write `profile/.origin` with the repo URL/version and the setup date (for traceability and updates).
4. **Check state:**
   - If `profile/materials-present.md` exists → enter **ready state**.
   - Otherwise → proceed to **Ritual A**.
5. **Hand off:** tell the user (in the active locale) that setup is complete and that you will now ask a short set of onboarding questions.

## Rules

- All user-facing text is in the **active locale** (`ru` default; `en` available).
- Do not create materials yourself; the user supplies them.
- Keep the workspace **portable**: plain Markdown + XML only, so it survives a tool switch (e.g., Claude Code → an open-weights setup). No tool-specific lock-in.
- If fetching the repo over HTTP, use `webfetch` against the published **raw** file URLs (the green-path user has no git).

## Green-path note (no git)

For users without git, fetch each needed file via its raw URL rather than cloning. The user's agent (you) performs the fetches; the user only pastes the launcher. If the user *wants* git later, point them to `git-helper/`.
