# Playbook 06 — Active Search Fallback

> **When to run:** ONLY as a fallback, when inbound is insufficient or on the user's explicit request.
> **Priority:** LOW. This is the **secondary** loop, not the main one. See `BOOTSTRAP.md` §2–3.
> **Language:** per role. **Mode:** human-in-the-loop, **quality over quantity**.

---

## Goal

Targeted, high-quality applications — not volume spraying (volume kills the inbound signal). Every application passes the alignment gate.

## Principles (strict)

1. **Quality > quantity.** Better 2 strong applications than 20 generic ones.
2. **Volume cap:** no more than **3 applications per week** (default; the user may change it).
3. **Alignment gate mandatory** — every role is scored by playbook 02. Not green/yellow → don't apply.
4. **Tailored, not generic.** Resume/cover letter adapted to the specific role (leaning on §11 cases).
5. **Never apply automatically.** Draft only — the user applies.

## Output

`output/active-search-YYYY-MM-DD.md`:
```md
# Active search (fallback) — week of YYYY-MM-DD
## Context
Why active search now (fallback)
## Target roles (from watchlist 01, passing alignment 02)
## Applications — drafts
### [Company] — [role] — alignment 🟢/🟡
- Why aligned
- Tailored CV excerpt (focus on relevant §11 cases)
- Cover note (per role)
## Cap: X/3 used
```

## Rules

1. Take roles **only** from the watchlist (playbook 01) that passed alignment (playbook 02).
2. Every application is individual. No template mass-apply.
3. If no aligned roles this week — honestly "none suitable," **do not lower the bar**.
4. Remind the user: active search is the fallback; the main focus stays inbound (playbooks 03–04).
5. Log the outcome (reply/rejection/silence) — it's feedback for positioning.
