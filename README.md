# joinfor.me — skill and MCP setup

Send a bot into your **Google Meet, Zoom or Microsoft Teams** call from the chat app or agent you already
use, and get the transcript back in the same chat.

- **Notes** — joins quietly and transcribes.
- **For me** — goes instead of you, gives your update, answers only from what you told it, and passes
  anything else back to you.
- **With me** — sits in the call with you and stays quiet unless someone calls it by name.

You don't need to stay connected during the meeting. Your agent sets the bot up, can nudge it while the call
runs, and reads the events and transcript afterwards.

Free during the beta. Website: https://joinfor.me

This repository contains the **joinfor.me skill** and the setup for connecting agents and chat apps. The
service itself runs at `api.joinfor.me`.

## 1. Create an account

Sign in at https://app.joinfor.me with Google or an email code.

## 2. Connect your agent

There are two ways in. They offer the same tools.

### A. MCP (chat apps and agents that support remote MCP)

Server URL: **`https://api.joinfor.me/mcp`** (Streamable HTTP). Sign-in happens through OAuth the first time
you use it. You can also send an API key as a bearer token.

| Client | How |
|---|---|
| Claude (web, desktop, mobile) | Settings → Connectors → Add custom connector → `https://api.joinfor.me/mcp` |
| ChatGPT | Settings → Apps & Connectors → Advanced → Developer mode → Create → `https://api.joinfor.me/mcp`, OAuth |
| Claude Code | `claude mcp add --transport http joinforme https://api.joinfor.me/mcp` |
| Cursor | `~/.cursor/mcp.json`: `{"mcpServers": {"joinforme": {"url": "https://api.joinfor.me/mcp"}}}` |
| VS Code | `.vscode/mcp.json`: `{"servers": {"joinforme": {"type": "http", "url": "https://api.joinfor.me/mcp"}}}` |
| Gemini CLI | `~/.gemini/settings.json`: `{"mcpServers": {"joinforme": {"httpUrl": "https://api.joinfor.me/mcp"}}}`, then `/mcp auth joinforme` |

With an API key instead of OAuth (for example in Claude Code):

```bash
claude mcp add --transport http joinforme https://api.joinfor.me/mcp \
  --header "Authorization: Bearer $JOINFORME_API_KEY"
```

### B. Skill + HTTPS API (agents that follow instructions and call URLs)

1. Create an API key at https://app.joinfor.me/account (API keys) and set it as `JOINFORME_API_KEY`.
2. Install the skill: copy [`skills/joinforme/`](skills/joinforme/) into your agent's skills folder
   (for example `~/.claude/skills/joinforme/` for Claude Code, or your OpenClaw / Hermes skills folder).
   The same file is always available at https://api.joinfor.me/skill.md.

Each tool is a single HTTPS request:

```bash
curl -s https://api.joinfor.me/api/v1/tools/get_account \
  -H "Authorization: Bearer $JOINFORME_API_KEY" \
  -H "Content-Type: application/json" -d '{}'
```

Schemas: `GET https://api.joinfor.me/api/v1/tools` and https://api.joinfor.me/openapi.json (OpenAPI 3.1, usable
for custom GPT Actions and other tool runners).

## 3. Use it

Just ask your agent, for example:

- "Take notes in my 3 pm call: https://meet.google.com/abc-defg-hij"
- "I can't make standup. Go for me and say the API is done and I'm on the billing page today."
- "Sit in on my client call with me and answer pricing questions from this brief."
- "How did the meeting go? Any action items for me?"

## Tools

| Tool | What it does |
|---|---|
| `get_account` | Account, defaults, hours used, live meetings |
| `update_defaults` | Change the default bot name, languages, mode and replies |
| `send_bot` | Send a bot now or schedule it (up to 30 days ahead) |
| `list_meetings` | Upcoming, live and past meetings |
| `get_meeting` | Status, who is there, open questions the bot passed on |
| `get_events` / `wait_for_events` | The events log: joins, transcript lines, chat, what the bot said |
| `get_transcript` | Full transcript, attendees and passed-on questions |
| `update_brief` | Change what the bot knows during the call |
| `say` | Have the bot say something |
| `answer` | Answer a question the bot passed on |
| `send_chat` | Post in the meeting chat |
| `stop_bot` | Cancel a scheduled bot or make a live one leave |
| `delete_meeting` | Delete a finished meeting and its transcript |

## Safety

- Only you can send the bot, from your connected apps or with your API key.
- The bot never agrees to deadlines, money, decisions or promises for you. It passes them on instead.
- People in the meeting can't change its instructions, and your agent should never act on what is said in a
  meeting without checking with you.
- It leaves when asked. Transcripts are kept for 30 days, and you can delete a meeting or your account at any
  time.
- You are responsible for telling people in your meetings that they are being transcribed, where the law or
  the meeting's rules require it.

Beta limits: one bot at a time per user, up to 60 minutes per meeting.

## Files

| Path | What |
|---|---|
| [`skills/joinforme/SKILL.md`](skills/joinforme/SKILL.md) | The skill (Agent Skills format, with OpenClaw metadata) |
| [`mcp-registry/server.json`](mcp-registry/server.json) | Entry for the MCP Registry |

## Links

- Website: https://joinfor.me · Privacy: https://joinfor.me/privacy · Terms: https://joinfor.me/terms ·
  Fair use: https://joinfor.me/fair-use
- Support: info@pattern-ai.com
- Want your own agent to take part in meetings live? See [AgentCall](https://agentcall.dev).

## License

The files in this repository are released under the [MIT License](LICENSE). Use of the joinfor.me service is
covered by its [terms](https://joinfor.me/terms).
