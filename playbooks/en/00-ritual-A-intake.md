# Playbook 00 — Ritual A: Intake (onboarding + materials)

> **When to run:** on first launch, after `SETUP.md`, IF `profile/materials-present.md` is absent.
> **Language:** everything the user sees is in the **active locale** (this file: English).
> **Goal:** understand the user as a person — ask, never infer from a single line.

---

## 0. Rules (strict)

1. **Ask, do not infer.** Assume nothing about direction, domain, or level. Even if the user hints — confirm.
2. **One block at a time.** Never dump 36 questions. Go section by section; let the person think.
3. **Record verbatim.** Store answers as quotes in `profile/intake-answers.md` — Ritual B returns them in the user's own words.
4. **Flag contradictions.** If a goal conflicts with the situation — don't silently "fix" it; surface it in a "⚠️ Contradictions" block and discuss.
5. **Don't rush.** Allow skipping ("not sure yet / later"). An honest "I don't know" beats a fabricated answer.
6. **Respect boundaries.** The user may decline any question.

---

## 1. Materials intake (before questions)

Ask the user to provide (in parts is fine — links or files in `profile/materials/`):

- Resume / CV (EN + local language if any).
- Portfolio link.
- 2–3 key cases: **role / process / outcome / metrics** (link, text, or PDF).
- Current profile links: LinkedIn, Behance/Dribbble, personal site, any local boards, blog/channel — whatever exists.
- Any notes on "what I want to do" (if any).

**Store everything in `profile/materials/`; list paths in the "Materials" block of `profile/intake-answers.md`.**

---

## 1b. Voice samples (for content)

The Brand Engine (playbook 03) writes posts in the user's voice, not a generic "AI voice." For that it needs samples of how the user already writes.

- Ask where the user publishes: Telegram channel, Substack, personal blog, LinkedIn, local blog platforms, Facebook, etc.
- Collect 10–30 representative posts. Methods in `VOICE.md` (from a Telegram export to pasting text).
- Store raw samples in `profile/voice/`; write `profile/voice-summary.md` (register/tone, recurring phrases, structural habits, 5–10 verbatim signature lines, anti-patterns).
- If they have no publications yet — note it in `voice-summary.md` ("voice being formed"); the Brand Engine then leans on intake quotes and flags this to the user.

---

## 2. Questionnaire (adapted for senior level)

Ask by section. Soften phrasing to conversational; keep intent.

### Block 1. Current situation
- Current role and how long in it?
- What do you enjoy most right now?
- What drains you / frustrates you most?

### Block 2. Career goals
- Short-term goals (1–2 yrs)?
- Long-term aspirations (3–5 yrs)?
- Any specific industries or product types pulling you?

### Block 3. Skills & strengths
- What are you most confident about as your strongest skills?
- What do you want to develop?

### Block 4. Barriers & fears
- What's holding you back right now?
- Any concerns about changing/searching?

### Block 5. Work-life & capacity
- How much time per week can you realistically give to active positioning/search? (calibrates the plan — e.g., content takes effort)

### Block 6. Motivation & values
- What genuinely drives you in work?
- Rank what matters most in the next place: money / mission / team / autonomy / growth / recognition.

### Block 7. Expectations of the assistant
- What do you expect from our work? What should be different in 3 months?

### Block 8. Open
- What else is important to know about you and your situation?

---

## 3. Senior/Lead level — mandatory clarifications (do NOT skip)

This is what separates a lead intake from a generic one:

- **Craft ↔ strategy axis:** where do you want to sit — more hands-on in the craft, or more function-building/strategy?
- **People vs craft:** do you want to manage a team, or stay a strong IC lead? What team size is comfortable?
- **Design-function maturity:** join a place where design exists, or build from zero (founding/first design lead)?
- **Mission — filter or nice-to-have?** Is "helping people" a hard requirement or desirable? (clarifies how much to narrow the market)
- **Geography:** local only? Remote from your country? Open to relocation? Foreign employers? (affects a tax/payment block)
- **Compensation:** target/floor? In what currency? Format (employee/contractor/freelance)?
- **Best cases:** 2–3 you're proudest of — and **why** (this is the core of positioning and content).
- **Company archetypes:** what attracts you, what's a definite no (examples and anti-examples).
- **Inbound channels:** which do you already have, which are you willing to build (LinkedIn, blog/talks, personal site, newsletter/community).

---

## 4. Flagged contradictions — what to look for

Examples of tension to surface (not judge — discuss):
- "want deep in the craft" **AND** "want to manage a big team."
- "work-life balance matters" **AND** "want to join a startup launch."
- "mission matters" **AND** "money is the top priority."
- "want global inbound" **AND** "not willing to relocate and weak English."

Each contradiction → a line in "⚠️ Contradictions" with a question for the user.

---

## 5. Closing the ritual

1. Write everything to `profile/intake-answers.md` (structured by block, with the user's quotes).
2. Briefly replay to the user in 5–7 lines how you understood them (their words).
3. Say you'll proceed to **Ritual B (explication)** — you'll assemble positioning from answers + materials and return it for confirmation.
4. Launch `playbooks/en/00-ritual-B-explication.md` (or `playbooks/<locale>/...`).
