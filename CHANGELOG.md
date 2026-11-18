# Changelog

## Unreleased

- Calendar rules can **skip** as well as join, and limit by the number of people on the invite (`action`,
  `min_people`, `max_people`), e.g. "skip 1:1s"; `position` sets the order (first match wins).
- `get_calendar refresh: true` reads the calendar again first, for a meeting just added.

## 1.3.0 — 2026-11-18

- **Calendar auto-join:** connect Google Calendar (read-only) and joinfor.me sends bots by itself to the meetings
  your rules pick. New tools `get_calendar`, `save_calendar_rule`, `delete_calendar_rule`.
- New tool `update_meeting`: change a scheduled bot (mode, brief, the update) or skip it before it joins.
- `get_account` shows the calendar status; `list_meetings` shows each bot's `source` and calendar title.

## 1.2.0 — 2026-11-18

- Skill: `update_defaults` takes `time_zone` (e.g. `Asia/Kolkata`); joinfor.me shows meeting times in the user's
  zone and learns it from `start_at` offsets if not set. `list_meetings` lists upcoming bots soonest first and
  returns `start_local`.
- Skill: new `bot_chat` event (the bot's own chat posts); transcript lines are in time order, chat posts marked
  `"chat": true`.

## 1.1.1 — 2026-11-18

- `server.json`: icon for the MCP Registry and the directories that read it.
- `server.json`: description shortened to the registry's 100-character limit; CI checks it.
- `glama.json` to claim the Glama listing; 400×400 logo for directory submissions.

## 1.1.0 — 2026-11-18

- Setup for **GitHub Copilot**: Copilot CLI plugin install, and agent mode in VS Code, Visual Studio and JetBrains.
- New **Chinese assistants and tools** guide:
  - ByteDance: Coze, Doubao Work, Trae
  - Moonshot: Kimi Code CLI, Kimi Work
  - Alibaba: Qwen Code, QwenWork, Bailian, Tongyi Lingma
  - DeepSeek Harness; Zhipu: ZCode, Z.ai API; MiniMax Code
  - Tencent: CodeBuddy, WorkBuddy, ADP; Baidu: Qianfan
- **Agent builders and chat clients**: Manus, Dify, Cherry Studio, LobeHub, ChatWise.
- **Release packages**: `joinforme-skill.zip` and `joinforme-plugin.zip` attached to every release; see
  `docs/distribution.md`.
- CI checks the manifests and the skill on every change. Issue and pull request templates.

## 1.0.0 — 2026-11-18

First release.

- Skill `skills/joinforme/SKILL.md` (Agent Skills format, OpenClaw metadata), also served at
  https://api.joinfor.me/skill.md.
- Plugin and extension manifests: Claude Code (`.claude-plugin/`, `.mcp.json`), Codex / ChatGPT
  (`.codex-plugin/`), Agent Plugins (`plugin.json`, `mcp.json`), Gemini CLI (`gemini-extension.json`) and the MCP
  Registry (`server.json`).
- Setup guide for each assistant in `docs/platforms.md`.
