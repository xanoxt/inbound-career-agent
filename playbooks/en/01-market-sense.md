# Playbook 01 — Market Sense

> **When to run:** once a week before the digest, or on request.
> **Language:** active locale (this file: English). **Mode:** API-only, no scraping; human-in-the-loop.
> **Inputs:** `profile/positioning.md` (esp. axis, mission, geography, archetypes), `market-config.md`.

---

## Goal

Understand **where** the demand aligned with the user's positioning is, and what it pays at the user's level. Output: a ranked watchlist + a comp anchor. This is the "sense" loop (see `BOOTSTRAP.md`).

## Tool

Search via the provider in `AgentContract.xml` (Tavily default; `deepseek-websearch-mcp` as an option). Sources from `market-config.md`. **No scraping.**

## Output

`output/watchlist-YYYY-MM-DD.md`:

```md
# Watchlist — YYYY-MM-DD

## Top companies/roles this week (ranked by alignment)
1. [Company] — [role] — why aligned (mission/product/level) — source — alignment ✅/⚠️
2. ...

## Comp anchor (user's level)
- Method: aggregate of configured sources (NOT a single source)
- Range for your level and geography: ...
- Comment vs last week

## Signals
- New players/products in the target segment
- Where design-lead hiring is active
```

## Rules

1. **Level honesty.** Don't pass off profession-wide averages as figures for a lead — the user's level sits higher. See methodology in `market-config.md`.
2. **Alignment filter.** Only aligned items (mission/archetype/geography) make the top. Misaligned → "filtered out" with a reason.
3. **Date and source** on every entry (verifiability).
4. **No applying.** The watchlist is observation, not applications. Applications are only via playbook 06 (fallback) and only on the user's decision.
5. If data is thin — say so honestly; propose broadening sources in `market-config.md`.
