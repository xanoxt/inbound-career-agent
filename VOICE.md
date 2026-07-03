# VOICE — gathering the user's writing to model their voice

> Reference for Ritual A's voice-sample step and for the Brand Engine (playbook 03).
> **Goal:** capture enough of the user's own writing to draft content in THEIR voice, not a generic AI voice.
> **Scope:** this only COLLECTS voice samples. A separate "writing assistant that helps refine voice" is a future project — out of scope here.

## Why

The Brand Engine drafts content. Generic AI prose kills inbound credibility. The fix: ground every draft in the user's actual phrasing, rhythms, and vocabulary, drawn from their own published writing.

## What to collect

Aim for 10–30 representative posts/entries (enough to hear the voice; not so much it drowns the signal). Store raw samples under `profile/voice/`; summarize into `profile/voice-summary.md`.

## Per-platform how-to (easiest first)

### Telegram channel

**PRIMARY (recommended — user-driven, no keys, respects the no-scrape rule):**
- Telegram Desktop → *Settings → Advanced → Export Telegram data*; or open the channel → *⋯ → Export chat history*.
- Choose **JSON** output (machine-readable). Result: `result.json` (schema: <https://core.telegram.org/import-export>). Message objects carry `text` / `text_entities` / `date`.
- Hand the agent the `result.json` (drop it in `profile/voice/`). It extracts the user's posts.
- Caveat (per the schema): exports of public groups/channels contain **only messages by the user requesting the export** — fine for the user's own channel.

**ADVANCED (only if export isn't viable):**
- **MTProto** via Telethon or Pyrogram: read full public/joined channel history. Needs `api_id` + `api_hash` from <https://my.telegram.org>; carries account-flag/ToS risk — use a read-only or bot session, carefully.
- **Bot API:** forward-only — a bot can capture NEW posts if added as admin, but **cannot read history**. Not suitable for voice mining.

### Other platforms (general approach)

- **Substack / standalone blog / Medium:** most have an RSS feed — fetch it (RSS/API is allowed; not scraping). Else paste 10–20 posts as text.
- **LinkedIn posts:** no official export of post history; ask the user to paste their ~10 best posts (or save-page → text).
- **Facebook / Instagram:** use the platform's official data download; else paste samples.
- **Generic fallback (works everywhere):** the user pastes 10–20 representative pieces as text/MD into `profile/voice/`. Always acceptable.

## Hard rule

API / official export / user-provided only. **No scraping.** Same rule as the rest of the pack.

## `voice-summary.md` structure

The agent writes `profile/voice-summary.md` from the samples:
- Register/tone: formal/casual, sentence length, humor, use of emoji/formatting.
- Recurring phrases / vocabulary / pet words.
- Structural habits: how they open and close posts, use of lists, questions, CTAs.
- 5–10 verbatim signature lines (to quote back in drafts).
- Anti-patterns: things they never do (so the agent avoids them).

## Anti-slop check (Brand Engine)

Before a draft reaches the user, run an anti-"AI tell" pass. **Reference (do not copy into this repo):** the *stop-slop* skill — <https://github.com/hardikpandya/stop-slop> — which scores prose on Directness, Rhythm, Trust, Authenticity, Density (revise if <35/50) and bans common AI phrases/structures. Apply its spirit; **the user's `voice-summary.md` overrides any generic rule.**
