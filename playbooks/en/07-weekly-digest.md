# Playbook 07 — Weekly Digest

> **When to run:** once a week (or on request). The main glue of the system — ties the other playbooks into one rhythm.
> **Language:** active locale (this file: English). **Mode:** human-in-the-loop (drafts only).
> **Inputs:** `profile/positioning.md`, `market-config.md`, fresh artifacts in `output/` (watchlist, inbound opportunities, content drafts).

---

## Goal

Roll the week into one short document: what appeared on the market, what came inbound, what content is ready, and **at most 3 actions** for the week. The user decides what to do — the agent sends nothing itself.

## Output

`output/YYYY-MM-DD-digest.md`. Structure:

```md
# Weekly digest — YYYY-MM-DD

## ⭐ Action this week (max 3, by priority)
1. [specific action] — why it matters
2. ...
3. ...

## 📡 Market (delta vs last week)
- New companies/roles aligned with positioning (from watchlist)
- Movement in comp anchors for your level

## 📥 Inbound (needs qualifying)
- Requests/messages needing a reply → playbook 02

## ✍️ Content ready to publish
- Draft(s) from playbook 03 — for your approval

## 🎯 Conversations in flight
- Interviews/calls needing prep → playbook 05

## ❓ Open questions for you
- What needs your decision
```

## Rules

1. **Actions at the top.** The user must see them without scrolling. Max 3, each with a reason.
2. **No invention.** Every line rests on an artifact in `output/` or `profile/`. No data → that section is empty with a "no change this week" note.
3. **Alignment filter.** Only items passing the alignment check (section 12 of `positioning.md`) go into "Market" and "Inbound". The rest → a single "filtered out: N" line.
4. **Never apply, publish, or write on the user's behalf.** Only propose.
5. Close by asking: "Which action do we take this week?"
