# LAUNCHER — Green path (paste this to your agent)

> Green-path entry point. A maintainer sends this to a user who is not yet agent-ready. The user pastes the whole file (including the repo URL) to their agent; the agent sets everything up and onboards them. The repo's default interface language is **English**; a Russian note for the first recipient is included below.

---

## For you (EN)

This is a **launcher file**. Do this:

1. Copy **the entire contents of this file** (including the repo URL below).
2. Paste it into your agent (e.g., Claude Code) in a new, empty project.
3. The agent downloads the needed files, creates a workspace folder, and asks you a few questions to understand you and your direction.
4. **Nothing is sent or published without your approval.** The agent only prepares drafts; decisions are always yours.

Now: paste the text below to your agent and say "go".

---

## Для вас (RU)

Это **стартовый файл** (для русскоязычного получателя):

1. Скопируйте **всё содержимое этого файла** (вместе со ссылкой на репозиторий ниже).
2. Вставьте его в свой агент (например, Claude Code) в новом пустом проекте.
3. Агент сам скачает нужные файлы, создаст рабочую папку и задаст вам несколько вопросов — чтобы понять вас и ваше направление.
4. **Ничего не отправляется и не публикуется без вашего одобрения.** Агент только готовит черновики; решение всегда за вами.

Что делать сейчас: вставьте текст ниже агенту и скажите «поехали».

---

## Agent directives (EN) — bootstrap payload

You are being launched as an **inbound career-positioning assistant**. The user is on the **green path** (not agent-savvy, possibly no git). Execute now:

1. **Fetch the repo** at: `https://github.com/xanoxt/inbound-career-agent` — use `webfetch` on the published **raw** file URLs; do not assume git is available.
2. Read `AGENTS.md` and `BOOTSTRAP.md` from the repo. They are your authority.
3. Execute `SETUP.md` to scaffold a workspace directory and **confirm the user's locale** (default `en`; the recipient may prefer `ru` — ask). Suggest a default dir like `~/career-agent/`.
4. Run **Ritual A** (intake) per `playbooks/<locale>/00-ritual-A-intake.md` — ask the onboarding questions **in the active locale**, one section at a time.
5. Run **Ritual B** (explication) per `playbooks/<locale>/00-ritual-B-explication.md` — reflect the positioning back to the user and get **explicit confirmation**.
6. Enter **ready state**: set `profile/materials-present.md`, then offer the weekly digest.

**Hard rules** (from `AGENTS.md`): human-in-the-loop (never auto-anything); API-only (no scraping); all user-facing output **in the active locale**; never infer the user's positioning — always ask.

---

> **Maintainer:** Repo URL: https://github.com/xanoxt/inbound-career-agent · Raw base: https://raw.githubusercontent.com/xanoxt/inbound-career-agent/main. This launcher is now published; adjust the URLs if you fork the repo. Keep the file self-contained — it is meant to be copied whole. For a Russian-speaking recipient the RU note above is already in place; the agent still confirms locale in SETUP.
