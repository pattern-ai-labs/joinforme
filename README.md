<p align="center">
  <img src="assets/logo.png" alt="joinfor.me" width="96" height="96">
</p>

<h1 align="center">joinfor.me</h1>

<p align="center">
  <strong>Send a bot to your meetings from the assistant you already use.</strong><br>
  Google Meet · Zoom · Microsoft Teams — notes, your update, or a second pair of ears — and the transcript back in your chat.
</p>

<p align="center">
  <a href="https://joinfor.me">Website</a> ·
  <a href="docs/platforms.md">Connect your assistant</a> ·
  <a href="skills/joinforme/SKILL.md">Skill</a> ·
  <a href="https://joinfor.me/privacy">Privacy</a> ·
  <a href="https://joinfor.me/terms">Terms</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="MCP: Streamable HTTP" src="https://img.shields.io/badge/MCP-Streamable%20HTTP-black">
  <img alt="Agent Skills" src="https://img.shields.io/badge/Agent%20Skills-SKILL.md-orange">
  <img alt="Status: beta" src="https://img.shields.io/badge/status-beta-yellow">
</p>

---

Ask Claude, ChatGPT, Grok, Gemini or your own agent to *"take notes in my 3 pm call"* or *"go to standup for me
and say the API is done"*. joinfor.me sends a bot into the meeting at the right time, runs it, and gives your
assistant the events and the full transcript. Your assistant doesn't need to stay connected during the meeting.

This repository holds everything an assistant needs to use joinfor.me: the **skill**, the **plugin and extension
manifests** for the main platforms, and **setup guides**. The service itself runs at `api.joinfor.me`.

## What the bot can do

| Mode | What happens |
|---|---|
| **Notes** | Joins quietly and transcribes. Your assistant gets the full transcript and writes the summary. |
| **For me** | Goes instead of you, introduces itself the way you choose and gives your update. It answers only from the brief you gave it and passes anything else back to you. |
| **With me** | Sits in the call with you. Stays quiet unless someone calls it by name, then answers from your brief. Notes what you promised. |

While the meeting runs, your assistant can check what's happening, update the brief, have the bot say
something, answer a question the bot passed on, post in the meeting chat, or make it leave. Bots can be sent
now or scheduled up to 30 days ahead.

## Quick start

1. **Create an account** at https://app.joinfor.me (Google or an email code). It's free during the beta.
2. **Connect your assistant.** Add the remote MCP server
   **`https://api.joinfor.me/mcp`** and sign in when asked, or install the skill with an API key.
3. **Ask for a meeting:**
   - "Take notes in my 3 pm call: https://meet.google.com/abc-defg-hij"
   - "I can't make standup. Go for me: the API is done and I'm on billing today. Don't commit me to dates."
   - "Sit in on my client call with me and answer pricing questions from this brief."
   - "How did the meeting go? Any action items for me?"

## Connect your assistant

| Assistant | How | Details |
|---|---|---|
| **Claude** (web, desktop, mobile) | Settings → Connectors → Add custom connector → `https://api.joinfor.me/mcp` | [Claude](docs/platforms.md#claude) |
| **Claude Code** | `claude plugin marketplace add pattern-ai-labs/joinforme` then `claude plugin install joinforme@joinforme` | [Claude Code](docs/platforms.md#claude) |
| **ChatGPT** | Settings → Apps → Developer mode → Create app with the MCP URL, OAuth | [ChatGPT](docs/platforms.md#chatgpt-and-openai) |
| **Codex** | `codex mcp add joinforme --url https://api.joinfor.me/mcp` | [Codex](docs/platforms.md#chatgpt-and-openai) |
| **Grok** | grok.com/connectors → New Connector → Custom → the MCP URL | [Grok](docs/platforms.md#grok-and-xai) |
| **Grok Bot** | Ask: "Add a custom server named joinforme with the URL https://api.joinfor.me/mcp" | [Grok Bot](docs/platforms.md#grok-and-xai) |
| **Gemini CLI** | `gemini extensions install https://github.com/pattern-ai-labs/joinforme` | [Gemini](docs/platforms.md#google-gemini) |
| **GitHub Copilot** | `copilot plugin install pattern-ai-labs/joinforme`, or the MCP URL in agent mode (VS Code, Visual Studio, JetBrains) | [GitHub Copilot](docs/platforms.md#github-copilot) |
| **Microsoft Copilot Studio** | Add a tool → Model Context Protocol → the MCP URL | [Copilot](docs/platforms.md#microsoft-copilot) |
| **Perplexity, Le Chat** | Add a custom remote connector with the MCP URL | [Perplexity](docs/platforms.md#perplexity) · [Le Chat](docs/platforms.md#mistral-le-chat) |
| **OpenClaw, Hermes, Poke, Meta Muse, Instinct, Dots, Duet** | Skill + API key, or the MCP URL with a Bearer key | [Personal agents](docs/platforms.md#personal-agents) |
| **Cursor, VS Code, Windsurf** | Add the remote MCP server | [Developer tools](docs/platforms.md#developer-tools) |
| **Kimi, Qwen, DeepSeek** | Their developer tools (Kimi Code, Qwen Code, DeepSeek Harness) | [Kimi, Qwen, DeepSeek](docs/platforms.md#kimi-qwen-and-deepseek) |
| **Any other agent** | "Read https://api.joinfor.me/skill.md" plus an API key | [Any other agent](docs/platforms.md#any-other-agent) |

The full step-by-step guide for each one is in **[docs/platforms.md](docs/platforms.md)**.

**Ready-made packages:** every release has `joinforme-skill.zip` (skill uploads) and `joinforme-plugin.zip`
(plugin portals), and the skill installs into any Agent Skills host with `npx skills add pattern-ai-labs/joinforme`.
See [docs/distribution.md](docs/distribution.md) for which package goes where.

## Two ways in, same tools

**Remote MCP**: `https://api.joinfor.me/mcp` (Streamable HTTP). Sign-in uses OAuth 2.1 with PKCE, dynamic
client registration and client ID metadata documents, so most assistants connect with one click. An API key
also works as a Bearer token.

**Skill + HTTPS API**: for agents that follow instructions and call URLs. Create a key at
https://app.joinfor.me/account, save it as `JOINFORME_API_KEY`, and install
[`skills/joinforme`](skills/joinforme/) (or point the agent at https://api.joinfor.me/skill.md). Each tool is
one request:

```bash
curl -s https://api.joinfor.me/api/v1/tools/send_bot \
  -H "Authorization: Bearer $JOINFORME_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"meeting_url": "https://meet.google.com/abc-defg-hij", "mode": "notes"}'
```

Schemas: `GET https://api.joinfor.me/api/v1/tools` and https://api.joinfor.me/openapi.json (OpenAPI 3.1, works
with custom GPT Actions and other tool runners).

## Tools

| Tool | What it does |
|---|---|
| `get_account` | Account, defaults, hours used this month, live meetings |
| `update_defaults` | Default bot name, languages, mode, introduction and passed-on reply |
| `send_bot` | Send a bot now or schedule it, in notes, for_me or with_me mode |
| `list_meetings` | Upcoming, live and past meetings |
| `get_meeting` | Status, who is in the call, open questions the bot passed on |
| `get_events` | The events log: joins and leaves, transcript lines, chat, what the bot said |
| `wait_for_events` | Waits up to 25 s for something new |
| `get_transcript` | Full transcript, attendees and passed-on questions (paged) |
| `update_brief` | Change what the bot knows, during the call |
| `say` | Have the bot say something |
| `answer` | Answer a question the bot passed on |
| `send_chat` | Post in the meeting chat |
| `stop_bot` | Cancel a scheduled bot or make a live one leave |
| `delete_meeting` | Delete a finished meeting and its transcript |

Every tool is annotated (read-only, destructive and open-world hints) and returns structured content plus the
same JSON as text.

## Safety and privacy

- **Only you can send the bot**, from the assistants you connected or with your API key. You can disconnect
  apps and revoke keys at any time.
- **It never commits you.** The bot won't agree to deadlines, money, decisions or promises; it passes them on.
- **The meeting can't take control of it.** People in the call can't change its instructions, and the skill
  tells your assistant never to act on what was said in a meeting without asking you.
- **It leaves when asked**, and after 60 minutes, when it's left alone, or when it isn't admitted.
- **Your data:** transcripts and events are kept for 30 days, then deleted. Delete a meeting or your whole
  account whenever you like. We don't sell your data or train AI models on your meetings. See the
  [privacy policy](https://joinfor.me/privacy).
- **Your responsibility:** tell people in your meetings they're being transcribed where the law or the
  meeting's rules require it.

## Beta limits

Free during the beta. One bot at a time per person, up to 60 minutes per meeting. Usage is counted per month
and a [fair usage policy](https://joinfor.me/fair-use) applies.

## What's in this repository

| Path | For |
|---|---|
| [`skills/joinforme/SKILL.md`](skills/joinforme/SKILL.md) | The skill (Agent Skills format, with OpenClaw metadata) |
| [`.claude-plugin/`](.claude-plugin/) | Claude Code plugin and marketplace (also read by Grok Build and Copilot CLI) |
| [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json) | Codex / ChatGPT plugin manifest |
| [`plugin.json`](plugin.json), [`mcp.json`](mcp.json) | [Agent Plugins](https://agent-plugins.org) manifest, the vendor-neutral standard (read by Copilot CLI) |
| [`.mcp.json`](.mcp.json) | Remote MCP server for Claude Code, Codex and Grok Build |
| [`gemini-extension.json`](gemini-extension.json) | Gemini CLI extension |
| [`server.json`](server.json) | MCP Registry entry |
| [`docs/platforms.md`](docs/platforms.md) | Setup for each assistant |
| [`docs/distribution.md`](docs/distribution.md) | Packages and where each one goes |
| [`scripts/`](scripts/) | `validate.py` (CI checks) and `package.py` (release ZIPs) |
| [`assets/`](assets/) | Logo |

No manifest contains a key or secret: every assistant signs in with OAuth or asks you for your own API key.

## Support

- Questions and problems: info@pattern-ai.com, or open an issue in this repository.
- Security: see [SECURITY.md](SECURITY.md).
- Want your own agent to take part in meetings live, reacting to every line? See
  [AgentCall](https://agentcall.dev), the meeting platform joinfor.me is built on.

## License

The files in this repository are released under the [MIT License](LICENSE). Use of the joinfor.me service is
covered by its [terms](https://joinfor.me/terms) and [privacy policy](https://joinfor.me/privacy).
