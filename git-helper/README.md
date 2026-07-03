# git-helper — установка git шаг за шагом (запасной путь)

> Нужен **только** если вы хотите пойти git-путём (клонировать репозиторий).
> Зелёный путь (вставить `LAUNCHER.md` агенту) **не требует git вообще**.
> RU ниже, EN — дальше.

---

## RU — настройка git

### 1. Установите git
- **macOS:** откройте Терминал и введите `git --version`. Если git не установлен, система предложит установить «Command Line Developer Tools» — согласитесь. Либо через Homebrew: `brew install git`.
- **Windows:** скачайте с git-scm.com и установите (можно оставить настройки по умолчанию).
- **Linux:** `sudo apt install git` (Debian/Ubuntu) или аналог вашего пакетного менеджера.

Проверка: `git --version` — должна показать версию.

### 2. Первичная настройка (один раз)
```
git config --global user.name "Ваше Имя"
git config --global user.email "you@example.com"
```

### 3. Клонируйте репозиторий навыков
```
git clone https://github.com/xanoxt/inbound-career-agent.git inbound-career-agent
cd inbound-career-agent
```
# ссылка уже подставлена; для форка замените URL.

### 4. Запустите агента
Откройте эту папку в вашем агенте (Claude Code) и скажите: «прочитай `AGENTS.md` и настрой рабочее пространство по `SETUP.md`». Дальше агент всё сделает сам.

> Если репозиторий приватный и запрашивает логин — используйте персональный токен (PAT) вместо пароля. Где его взять, подскажет хостинг (GitHub/GitLab).

---

## EN — set up git

> Only needed if you choose the git path (clone the repo).
> The green path (paste `LAUNCHER.md` to your agent) needs **no git**.

### 1. Install git
- **macOS:** in Terminal run `git --version`; if missing, accept the "Command Line Developer Tools" prompt. Or `brew install git`.
- **Windows:** download from git-scm.com, default settings are fine.
- **Linux:** `sudo apt install git` (or your distro's equivalent).

Verify: `git --version`.

### 2. First-time config (once)
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 3. Clone the skill pack
```
git clone https://github.com/xanoxt/inbound-career-agent.git inbound-career-agent
cd inbound-career-agent
```

### 4. Launch the agent
Open this folder in your agent (Claude Code) and say: "read `AGENTS.md` and set up the workspace per `SETUP.md`." The agent takes it from there.

> Private repo asking for credentials? Use a personal access token (PAT) instead of a password — your host (GitHub/GitLab) explains how to create one.
