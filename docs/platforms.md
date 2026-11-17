# Connecting joinfor.me to your assistant

joinfor.me works with any assistant or agent that can do **one** of these:

| Way in | What the assistant needs | Sign-in |
|---|---|---|
| **Remote MCP** | Support for a custom remote MCP server (Streamable HTTP) | OAuth (the assistant opens a joinfor.me sign-in and consent page), or an API key as `Authorization: Bearer …` |
| **Skill + HTTPS API** | The ability to read instructions and make authenticated HTTPS requests | API key |

- MCP server URL: **`https://api.joinfor.me/mcp`**
- Skill: **`https://api.joinfor.me/skill.md`** (same file as [`skills/joinforme/SKILL.md`](../skills/joinforme/SKILL.md))
- API keys: https://app.joinfor.me/account → API keys

Assistants change their menus often. If a step below doesn't match what you see, look for **Connectors**,
**Apps**, **Integrations**, **Custom connector** or **Add MCP server**. Platforms marked *unverified* haven't
documented the steps publicly yet, so we describe the general route.

**Contents:**
[Claude](#claude) · [ChatGPT and OpenAI](#chatgpt-and-openai) · [Grok and xAI](#grok-and-xai) ·
[Google Gemini](#google-gemini) · [GitHub Copilot](#github-copilot) · [Microsoft Copilot](#microsoft-copilot) · [Perplexity](#perplexity) ·
[Mistral Le Chat](#mistral-le-chat) · [Personal agents](#personal-agents) · [Developer tools](#developer-tools) ·
[Chinese assistants and tools](#chinese-assistants-and-tools) · [Any other agent](#any-other-agent)

---

## Claude

**Claude (web, desktop, mobile):** Settings → Connectors → **Add custom connector** → URL
`https://api.joinfor.me/mcp` → Add → **Connect**. Sign in to joinfor.me and allow access. On the Free plan
you can add one custom connector. On Team and Enterprise plans an owner may need to add it first.

**Claude Duet** *(unverified)*: Duet uses the connectors on your Claude account, so add joinfor.me as
above. If Duet can't see it, give Duet the skill URL and an API key (see [Any other agent](#any-other-agent)).

**Claude Code**, as a plugin (MCP server plus skill):

```bash
claude plugin marketplace add pattern-ai-labs/joinforme
claude plugin install joinforme@joinforme
```

Or only the MCP server:

```bash
claude mcp add --transport http joinforme https://api.joinfor.me/mcp
# with an API key instead of OAuth:
claude mcp add --transport http joinforme https://api.joinfor.me/mcp \
  --header "Authorization: Bearer $JOINFORME_API_KEY"
```

**Claude skills (claude.ai):** zip the [`skills/joinforme`](../skills/joinforme) folder and upload it in Claude's
skills settings (Customize → Skills). The skill calls the HTTPS API, so the connector is the simpler route in
claude.ai.

## ChatGPT and OpenAI

**ChatGPT:** Settings → Apps → Advanced settings → turn on **Developer mode** → **Create app**. Name
`joinfor.me`, MCP server URL `https://api.joinfor.me/mcp`, authentication **OAuth**. Then sign in to
joinfor.me and allow access. Developer mode depends on your plan and workspace settings.

**Custom GPTs (Actions):** import `https://api.joinfor.me/openapi.json`, and set authentication to **API key**,
type **Bearer**, with a key from your account page.

**Dots** *(unverified)*: add a custom connector with the MCP URL `https://api.joinfor.me/mcp` and sign in
with OAuth.

**Codex CLI:**

```bash
codex mcp add joinforme --url https://api.joinfor.me/mcp
codex mcp login joinforme
```

This repository is also a Codex plugin (`.codex-plugin/plugin.json`, with the skill and MCP server).

**OpenAI API (Responses, remote MCP tool):**

```json
{"type": "mcp", "server_label": "joinforme", "server_url": "https://api.joinfor.me/mcp",
 "headers": {"Authorization": "Bearer <JOINFORME_API_KEY>"}, "require_approval": "always"}
```

## Grok and xAI

**Grok (grok.com, iOS, Android):** go to https://grok.com/connectors → **New Connector** → **Custom** → URL
`https://api.joinfor.me/mcp` → sign in to joinfor.me. Custom connectors need a paid Grok plan. On Grok
Business and Enterprise, an admin may need to add it first.

**Grok Bot:** there's no settings field for a server URL. Ask in chat instead:

> Add a custom server named joinforme with the URL https://api.joinfor.me/mcp

Confirm with **Add it**, click **Authorize** on the connect card and sign in, then use it with `@joinforme`.

**Grok Build (CLI):**

```bash
grok mcp add --transport http joinforme https://api.joinfor.me/mcp
```

Grok Build also reads this repository's Claude-style plugin layout (`.claude-plugin/`, `.mcp.json`,
`skills/`).

**xAI API (remote MCP tool):**

```json
{"type": "mcp", "server_url": "https://api.joinfor.me/mcp", "server_label": "joinforme",
 "authorization": "Bearer <JOINFORME_API_KEY>"}
```

## Google Gemini

**Gemini app:** where custom apps are available (rollout limited by country, age and account type), add a
custom app with the MCP URL `https://api.joinfor.me/mcp` and sign in.

**Gemini CLI**, as an extension:

```bash
gemini extensions install https://github.com/pattern-ai-labs/joinforme
```

Then run `/mcp auth joinforme` in a session. Or add it by hand to `~/.gemini/settings.json`:

```json
{"mcpServers": {"joinforme": {"httpUrl": "https://api.joinfor.me/mcp"}}}
```

## GitHub Copilot

**Copilot CLI**, as a plugin (skill plus MCP server):

```bash
copilot plugin install pattern-ai-labs/joinforme
```

If the joinfor.me tools don't appear or you aren't asked to sign in, also add the server to
`~/.copilot/mcp-config.json`:

```json
{"mcpServers": {"joinforme": {"type": "http", "url": "https://api.joinfor.me/mcp"}}}
```

**VS Code, Visual Studio, JetBrains (agent mode):** add the server to your `mcp.json` (in VS Code,
`.vscode/mcp.json` or user settings; in JetBrains, Copilot Chat → Agent → tools icon → Add MCP Tools):

```json
{"servers": {"joinforme": {"type": "http", "url": "https://api.joinfor.me/mcp"}}}
```

Start the server and sign in when asked (in Visual Studio, click **Auth** above the server). On Copilot
Business and Enterprise, an admin must turn on the **MCP servers in Copilot** policy.

## Microsoft Copilot

**Copilot Studio:** Tools → Add a tool → **Model Context Protocol** → URL `https://api.joinfor.me/mcp`.
Authentication is **OAuth 2.0 → Dynamic discovery**, or **API key** with header `Authorization` and value
`Bearer <key>`. Agents built there can be published to Microsoft 365 Copilot and Teams.

**Microsoft 365 Copilot (declarative agent):** reference the remote MCP server
`https://api.joinfor.me/mcp` in the agent manifest, with dynamic client registration for auth.

Consumer Copilot doesn't support custom connectors.

## Perplexity

Settings → Connectors → add a **custom remote connector** with URL `https://api.joinfor.me/mcp`, then sign
in. Perplexity registers itself automatically (OAuth dynamic client registration). Custom connectors need
Pro, Max or Enterprise. Organization accounts depend on admin settings.

## Mistral Le Chat

Connectors → **Add connector** → **Custom MCP connector** → URL `https://api.joinfor.me/mcp` → sign in. In
an organization, an admin may need to add it.

## Personal agents

| Agent | How |
|---|---|
| **OpenClaw** | Install the skill: copy [`skills/joinforme`](../skills/joinforme) into your OpenClaw skills folder and set `JOINFORME_API_KEY`. Or add the remote MCP server with an `Authorization: Bearer` header. |
| **Hermes** | Install the skill the same way (Agent Skills format), or add the remote MCP server `https://api.joinfor.me/mcp`. |
| **Poke** | Add a remote MCP server with URL `https://api.joinfor.me/mcp` and the header `Authorization: Bearer <JOINFORME_API_KEY>`. |
| **Meta Muse** | Add a custom API connection with your API key as a Bearer token, then point Muse at the skill (`https://api.joinfor.me/skill.md`). |
| **Instinct** *(unverified)* | Instinct doesn't document custom MCP servers yet. If it can store an API key and make authenticated HTTPS requests, use the steps in [Any other agent](#any-other-agent). |
| **Dots**, **Claude Duet** | See [ChatGPT and OpenAI](#chatgpt-and-openai) and [Claude](#claude). |

Keep the API key in the agent's credential or secret settings, not in a chat message. You can revoke a key at
any time on your account page.

## Developer tools

| Tool | How |
|---|---|
| **Cursor** | [Install in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=joinforme&config=eyJ1cmwiOiJodHRwczovL2FwaS5qb2luZm9yLm1lL21jcCJ9), or `~/.cursor/mcp.json`: `{"mcpServers": {"joinforme": {"url": "https://api.joinfor.me/mcp"}}}` |
| **VS Code** | `code --add-mcp '{"name":"joinforme","type":"http","url":"https://api.joinfor.me/mcp"}'`, or `.vscode/mcp.json`: `{"servers": {"joinforme": {"type": "http", "url": "https://api.joinfor.me/mcp"}}}` |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json`: `{"mcpServers": {"joinforme": {"serverUrl": "https://api.joinfor.me/mcp"}}}` |
| **Claude Code, Codex, Gemini CLI, Grok Build, GitHub Copilot** | See the sections above. |
| **Anything else** | A remote MCP server at `https://api.joinfor.me/mcp` (Streamable HTTP), OAuth or a Bearer API key. |

## Chinese assistants and tools

What works today:

- **Coding tools and desktop "work" apps** (Kimi Code, Qwen Code, Trae, CodeBuddy, DeepSeek Harness, Doubao Work,
  QwenWork, Kimi Work and others) can add the remote MCP server. Most accept the API key in a header:
  `Authorization: Bearer <JOINFORME_API_KEY>`. Some also support OAuth sign-in.
- **Most also read Agent Skills** (`SKILL.md`): use [`skills/joinforme`](../skills/joinforme) or
  [`joinforme-skill.zip`](distribution.md).
- **Consumer chat apps** (the Doubao, Qwen, DeepSeek, GLM, Yuanbao and Wenxiaoyan apps) can't add custom MCP
  servers yet. Use the vendor's desktop work app, agent platform or coding tool instead.

Create the API key at https://app.joinfor.me/account → API keys.

### ByteDance

**Coze 扣子** (web and desktop): Extensions (扩展) → MCP → **添加自定义 MCP**, paste the JSON below, then
**添加到我的 MCP** and attach it to your agent:

```json
{"mcpServers": {"joinforme": {"url": "https://api.joinfor.me/mcp",
  "headers": {"Authorization": "Bearer <JOINFORME_API_KEY>"}}}}
```

To share it across agents, create an **MCP plugin** instead: Resources (资源库) → + Resource → Plugin, type
MCP, URL `https://api.joinfor.me/mcp`, auth **Service token / API key** in the header `Authorization` with the
value `Bearer <JOINFORME_API_KEY>`.

For the skill, upload [`joinforme-skill.zip`](distribution.md) under Skills (技能). It contains `SKILL.md`.

**Doubao Work 豆包工作** (desktop): 插件·技能·伙伴 → 插件 → **+ 添加** → **新建自定义连接器**. Transport
**HTTP**, URL `https://api.joinfor.me/mcp`, and under 自定义 Headers add `Authorization` =
`Bearer <JOINFORME_API_KEY>`. For the skill: 技能 → + 添加 → 上传技能 → the `joinforme` folder or
`joinforme-skill.zip`.

**Trae**: Settings → MCP → Add → **Create Manually**, or the project file `.trae/mcp.json`:

```json
{"mcpServers": {"joinforme": {"url": "https://api.joinfor.me/mcp",
  "headers": {"Authorization": "Bearer <JOINFORME_API_KEY>"}}}}
```

Skills: copy `skills/joinforme` to `.trae/skills/` (project) or `~/.trae/skills/` (everywhere), or upload it
under Settings → Skills & Commands.

**Doubao app 豆包**: no custom MCP servers or skills yet. Use Doubao Work or Coze.

### Moonshot (Kimi)

**Kimi Code CLI**, with an API key:

```bash
kimi mcp add --transport http joinforme https://api.joinfor.me/mcp \
  --header "Authorization: Bearer $JOINFORME_API_KEY"
```

Or with OAuth sign-in:

```bash
kimi mcp add --transport http --auth oauth joinforme https://api.joinfor.me/mcp
kimi mcp auth joinforme
```

The servers are stored in `~/.kimi/mcp.json`. For the skill, copy `skills/joinforme` to
`~/.config/agents/skills/` (all agents) or `~/.kimi/skills/`, or to `.kimi/skills/` in a project.

**Kimi Work** (desktop): create a personal plugin with **Plugin Builder** and import this repository. Kimi Work
reads `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json` and `server.json`, so the MCP server and the
skill come in together. The plugin then works in Kimi Work and on Kimi web.

**Kimi web**: plugins come from the official market. joinfor.me isn't listed there yet, so use a plugin
created in Kimi Work.

### Alibaba (Qwen)

**Qwen Code**, with an API key:

```bash
qwen mcp add --transport http joinforme https://api.joinfor.me/mcp \
  --header "Authorization: Bearer $JOINFORME_API_KEY"
```

Or in `~/.qwen/settings.json` (all projects) or `.qwen/settings.json` (one project):

```json
{"mcpServers": {"joinforme": {"httpUrl": "https://api.joinfor.me/mcp",
  "headers": {"Authorization": "Bearer <JOINFORME_API_KEY>"}}}}
```

Qwen Code can also sign in with OAuth: leave out the header, and it registers itself with joinfor.me and opens
the sign-in page. For the skill, copy `skills/joinforme` to `~/.qwen/skills/` or `.qwen/skills/`.

**QwenWork 千问办公** (desktop): 扩展 → 连接器 → **+ 添加**, and paste:

```json
{"mcpServers": {"joinforme": {"type": "streamable-http", "url": "https://api.joinfor.me/mcp",
  "headers": {"Authorization": "Bearer <JOINFORME_API_KEY>"}}}}
```

**Bailian 百炼 / Model Studio** (agents built on Alibaba Cloud): MCP management → create a custom MCP service,
install method **http** (`streamableHttp`), URL `https://api.joinfor.me/mcp`, and add
`Authorization: Bearer <JOINFORME_API_KEY>` to the service headers. Custom services are private to your
account.

**Tongyi Lingma 通义灵码**: its manual setup supports STDIO and SSE only. Use a STDIO bridge:

```json
{"mcpServers": {"joinforme": {"command": "npx",
  "args": ["-y", "mcp-remote", "https://api.joinfor.me/mcp", "--header", "Authorization: Bearer <JOINFORME_API_KEY>"]}}}
```

**Qwen app 千问** (chat): no custom MCP servers yet. Use QwenWork or Qwen Code.

### DeepSeek

**DeepSeek Harness** (`dsh`): add an MCP client entry to your profile's `cordis.patch.yml`:

```yaml
- id: mcp-joinforme
  name: '@deepseek-ai/dsh-mcp-client'
  config:
    serverName: joinforme
    transport: streamable-http
    url: https://api.joinfor.me/mcp
    headers:
      Authorization: !!js '`Bearer ${process.env.JOINFORME_API_KEY}`'
```

To use OAuth instead, drop `headers` and set `oauth.credentialKey` without a `clientId`. Harness then registers
itself with joinfor.me, and you sign in through `dsh-mcp-manager`. Skills: copy `skills/joinforme` to
`~/.dsh/skills/` or `~/.agents/skills/`.

**DeepSeek app** (chat): no custom MCP servers yet.

### Zhipu (GLM)

**ZCode** (GLM desktop client): Settings → MCP Servers → **New** → type **HTTP**, URL
`https://api.joinfor.me/mcp`. Click **Open authorization** to sign in with OAuth, or add the header
`Authorization: Bearer <JOINFORME_API_KEY>`.

**Z.ai API** (GLM models): pass joinfor.me as an MCP tool:

```json
{"type": "mcp", "mcp": {"server_label": "joinforme", "server_url": "https://api.joinfor.me/mcp",
  "transport_type": "streamable-http", "headers": {"Authorization": "Bearer <JOINFORME_API_KEY>"}}}
```

**智谱清言 / Z.ai chat, AutoGLM**: no custom MCP servers yet.

### MiniMax

**MiniMax Code**: `~/.minimax/mcp.json`:

```json
{"mcpServers": {"joinforme": {"type": "streamable-http", "url": "https://api.joinfor.me/mcp",
  "headers": {"Authorization": "Bearer ${JOINFORME_API_KEY}"}, "enabled": true}}}
```

**MiniMax Agent** (web): no custom MCP servers yet.

### Tencent

**CodeBuddy**:

```bash
codebuddy mcp add --scope user --transport http joinforme https://api.joinfor.me/mcp \
  --header "Authorization: Bearer $JOINFORME_API_KEY"
```

Or in `~/.codebuddy/.mcp.json` (or `.mcp.json` in a project):

```json
{"mcpServers": {"joinforme": {"type": "http", "url": "https://api.joinfor.me/mcp",
  "headers": {"Authorization": "Bearer ${JOINFORME_API_KEY}"}}}}
```

Skills: copy `skills/joinforme` to `~/.codebuddy/skills/` or `.codebuddy/skills/`.

**WorkBuddy** (desktop): add a **自定义连接器** (custom connector) with the same MCP configuration as CodeBuddy.

**Tencent Cloud ADP 智能体开发平台** (agent platform): add a custom connector, type **streamableHTTP**, URL
`https://api.joinfor.me/mcp`, auth **API key** in the header `Authorization` with the value
`Bearer <JOINFORME_API_KEY>`. ADP replaces Tencent Yuanqi 元器, which shut down on 9 November 2026.

**Yuanbao 元宝** (chat): no custom MCP servers yet.

### Baidu

**Qianfan 千帆 (AppBuilder workflows)** *(partly documented)*: add an **MCP Server** node to the workflow,
enter `https://api.joinfor.me/mcp` as the server address and your key under 鉴权 (auth), connect, then pick the
joinfor.me tool the node should call. Baidu doesn't document the transport or auth format for this node yet.

**Wenxiaoyan 文小言** (chat): no custom MCP servers yet.

Agents built on these models (for example with Qwen-Agent or another framework) can use the MCP server or
the HTTPS API directly.

## Any other agent

If your agent can read a web page and make HTTPS requests with a stored key:

1. Create an API key at https://app.joinfor.me/account and save it in the agent's secret settings as
   `JOINFORME_API_KEY`.
2. Tell the agent:

   > Read https://api.joinfor.me/skill.md and use joinfor.me for my meetings. My API key is saved as
   > JOINFORME_API_KEY.

3. Check it works by asking: "What's my joinfor.me account status?" (it calls `get_account`).

Each tool is one request: `POST https://api.joinfor.me/api/v1/tools/<tool>` with
`Authorization: Bearer <key>` and a JSON body. Schemas: `GET https://api.joinfor.me/api/v1/tools` and
https://api.joinfor.me/openapi.json.
