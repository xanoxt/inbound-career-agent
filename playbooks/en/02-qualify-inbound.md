# Playbook 02 — Qualify Inbound

> **When to run:** on every inbound message/offer from a recruiter or company.
> **Language:** active locale. **This is the alignment gate** — before any reply.
> **Inputs:** `profile/positioning.md`, esp. section 12 (the alignment-screen checklist).

---

## Goal

Before the user spends time on a call — assess whether the offer aligns with their goals, surface mismatches, and prepare a **screening reply**: short, polite, with clarifying questions.

## Output

`output/inbound-<company>-YYYY-MM-DD.md`:

```md
# Inbound — [company / role] — YYYY-MM-DD
**Message source:** ...  **Date:** ...

## Checklist score (positioning.md §12)
| Criterion | ✅/⚠️/❌ | Comment |
|---|---|---|
| Mission/product helps people? |  |  |
| Company design maturity |  |  |
| Role autonomy |  |  |
| Comp ≥ floor (§7) |  |  |
| Geography (§8) |  |  |
| Level fit (craft↔strategy, §2–3) |  |  |

## Verdict: 🟢 Green / 🟡 Yellow / 🔴 Red
## What to surface to the user (mismatches)
## Screening reply draft
```

## Screening questions (starters)

- What does the product do, what impact on people is it aiming for?
- Is there a design function today, and who leads it?
- How is success measured for this role?
- What's the level of autonomy and who does the role report to?
- Compensation range and format (before a call, to not waste time).

## Red flags (🔴)

- Vague/absent mission; product doesn't help people.
- No design function, "need the first person" without authority.
- Pressure to decide fast; refusal to share a range.
- Role doesn't fit the user's craft↔strategy axis.

## Rules

1. **The gate is mandatory.** No score → no reply draft.
2. **Surface honestly.** If Red — say so and offer a polite decline.
3. **Don't write on the user's behalf.** The draft is sent by the user.
4. **Respect the user's time.** A polite "no thanks, with a clarifying question" beats an unwanted call.
5. Trust the user's gut — if they say "something's off," that outweighs any score.
