# Changelog

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
