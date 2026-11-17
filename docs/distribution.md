# Packages and distribution

Every release attaches ready-made packages, so joinfor.me can be installed or submitted anywhere without
building anything:

| File | What it is | Latest |
|---|---|---|
| `joinforme-skill.zip` | The skill folder (`joinforme/SKILL.md`) | [download](https://github.com/pattern-ai-labs/joinforme/releases/latest/download/joinforme-skill.zip) |
| `joinforme-plugin.zip` | The whole plugin: every manifest, `.mcp.json`, `skills/`, `assets/` | [download](https://github.com/pattern-ai-labs/joinforme/releases/latest/download/joinforme-plugin.zip) |
| `SHA256SUMS` | Checksums of both | [download](https://github.com/pattern-ai-labs/joinforme/releases/latest/download/SHA256SUMS) |

You can also build them yourself: `python3 scripts/package.py` writes them to `dist/`.

## Which one goes where

| Platform | Use | How |
|---|---|---|
| **Claude** (claude.ai skills) | `joinforme-skill.zip` | Upload it in Claude's skills settings. For the tools, add the connector `https://api.joinfor.me/mcp`. |
| **Claude** (connector) | MCP URL | Settings → Connectors → Add custom connector → `https://api.joinfor.me/mcp` |
| **Claude Code** | This repo | `claude plugin marketplace add pattern-ai-labs/joinforme` then `claude plugin install joinforme@joinforme` |
| **ChatGPT / Codex** (OpenAI plugin portal) | `joinforme-plugin.zip` | Upload the ZIP. It contains `.codex-plugin/plugin.json`, `.mcp.json`, the skill and the logo. |
| **ChatGPT** (one user) | MCP URL | Developer mode → Create app → `https://api.joinfor.me/mcp`, OAuth |
| **GitHub Copilot CLI** | This repo | `copilot plugin install pattern-ai-labs/joinforme` |
| **Gemini CLI** | This repo | `gemini extensions install https://github.com/pattern-ai-labs/joinforme` |
| **Grok Build** | This repo | Install from the repo (Claude-style plugin layout), or `grok mcp add --transport http joinforme https://api.joinfor.me/mcp` |
| **Any Agent Skills host** (OpenClaw, Hermes, Cursor, Codex, Copilot, Gemini CLI and others) | This repo or `joinforme-skill.zip` | `npx skills add pattern-ai-labs/joinforme`, or unzip `joinforme-skill.zip` into the host's skills folder |
| **Agent Plugins hosts** | `joinforme-plugin.zip` | Root `plugin.json` + `mcp.json` follow the [Agent Plugins](https://agent-plugins.org) 1.0.0 standard |
| **MCP Registry** and clients that read it | `server.json` | Listed as `me.joinfor/joinforme` (remote, Streamable HTTP) |
| **Any MCP client** | MCP URL | `https://api.joinfor.me/mcp` (OAuth, or `Authorization: Bearer <key>`) |
| **Any agent that reads URLs** | Skill URL | "Read https://api.joinfor.me/skill.md" plus an API key |

Step-by-step setup for each assistant is in [platforms.md](platforms.md).

## Releasing a new version (maintainers)

1. Bump `version` in every manifest (`.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `plugin.json`,
   `gemini-extension.json`, `server.json`) and add a `CHANGELOG.md` entry. CI fails if they differ.
2. Merge the pull request, then tag `main`: `git tag vX.Y.Z && git push origin vX.Y.Z`.
3. The `release` workflow validates, checks the tag matches the manifests, builds the packages and attaches
   them to the GitHub release.
