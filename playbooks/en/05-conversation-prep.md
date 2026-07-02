# Playbook 05 — Conversation Prep

> **When to run:** when a call/interview is confirmed (after playbook 02).
> **Language:** active locale. **Mode:** API-only (search), human-in-the-loop.
> **Inputs:** `profile/positioning.md` (esp. §11 — anchor cases), `AgentContract.xml` (search), company data.

---

## Goal

Prepare the user so that **they are evaluated AND they evaluate**. They are an interviewer too: checking whether the company aligns with their goals.

## Output

`output/prep-<company>-YYYY-MM-DD.md`:

```md
# Conversation prep — [Company] — YYYY-MM-DD

## Company snapshot (search)
- Product, stage, size, what they say about themselves
- Target audience and the product's impact on people

## Design maturity (read between the lines)
- Is there a design function; who leads; decision process
- Will the role have a seat at the strategy table

## Questions YOU ask (by priority)
1. Mission: what impact on people is the product aimed at?
2. How is success for this role measured at 6/12 months?
3. Autonomy and direct reporting line?
4. How are design decisions made under conflict?
5. Team: size, craft/strategy mix?
6. Hiring timeline and process.

## STAR stories (from positioning.md §11)
- For "tell me about a hard case" → [case] : Situation/Task/Action/Result
- For "how do you lead" → [case]
- For "conflict with a stakeholder" → [case]

## Alignment check for you
- 🟢/🟡/🔴 on this company and why
- What you must find out on the call
```

## Rules

1. **Questions for THEM come first.** Senior level is a two-way evaluation, not just defense.
2. **STAR only from anchor cases** (§11). Don't invent.
3. **API-only search.** Don't scrape the company site; use the search provider.
4. **Honesty about data.** If something wasn't found — mark "unconfirmed," don't infer.
5. Keep the brief short and usable — the user must be able to read it before the call.
