#!/usr/bin/env python3
"""Check the plugin manifests and the skill. Run from the repo root: python3 scripts/validate.py"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MCP_URL = "https://api.joinfor.me/mcp"
NAME = "joinforme"
errors = []


def err(msg):
    errors.append(msg)


def load(rel):
    try:
        return json.loads((ROOT / rel).read_text())
    except Exception as e:  # noqa: BLE001
        err(f"{rel}: invalid JSON ({e})")
        return None


# 1. Every tracked JSON file parses.
files = subprocess.run(["git", "ls-files", "*.json"], cwd=ROOT, capture_output=True, text=True).stdout.split()
docs = {f: load(f) for f in files}

# 2. Agent Plugins schemas.
try:
    import jsonschema
    from urllib.request import urlopen

    for rel, kind in (("plugin.json", "plugin"), ("mcp.json", "mcp")):
        schema = json.load(urlopen(f"https://agent-plugins.org/schemas/1.0.0/{kind}.schema.json", timeout=20))
        for e in jsonschema.Draft202012Validator(schema).iter_errors(docs.get(rel) or {}):
            err(f"{rel}: {e.message}")
except ImportError:
    print("note: jsonschema not installed, skipping Agent Plugins schema check")

# 3. Names and versions agree.
versions = {}
for rel, key in ((".claude-plugin/plugin.json", None), (".codex-plugin/plugin.json", None),
                 ("plugin.json", None), ("gemini-extension.json", None), ("server.json", None)):
    d = docs.get(rel) or {}
    versions[rel] = d.get("version")
    if rel != "server.json" and d.get("name") != NAME:
        err(f"{rel}: name should be {NAME!r}, got {d.get('name')!r}")
if len(set(versions.values())) != 1:
    err(f"versions differ: {versions}")
market = docs.get(".claude-plugin/marketplace.json") or {}
if [p.get("name") for p in market.get("plugins", [])] != [NAME]:
    err(".claude-plugin/marketplace.json: expected one plugin named joinforme")

# 4. MCP endpoints: the one URL, no headers or secrets.
servers = []
for rel in (".mcp.json", "mcp.json"):
    servers += list(((docs.get(rel) or {}).get("mcpServers") or {}).items())
servers += list(((docs.get("gemini-extension.json") or {}).get("mcpServers") or {}).items())
for name, cfg in servers:
    url = cfg.get("url") or cfg.get("httpUrl")
    if url != MCP_URL:
        err(f"MCP server {name}: url should be {MCP_URL}, got {url!r}")
    if cfg.get("headers"):
        err(f"MCP server {name}: manifests must not carry headers")
for r in (docs.get("server.json") or {}).get("remotes", []):
    if r.get("url") != MCP_URL:
        err(f"server.json: remote url should be {MCP_URL}")
secret = re.compile(r"(jfm_[A-Za-z0-9]{16,}|ak_ac_|sk-[A-Za-z0-9]{20,}|clientSecret|Bearer [A-Za-z0-9_\-]{20,})")
for rel in files:
    if secret.search((ROOT / rel).read_text()):
        err(f"{rel}: looks like it contains a secret")

# 5. Skills: frontmatter name matches the folder, description present and short enough.
for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(f"{skill.relative_to(ROOT)}: missing YAML frontmatter")
        continue
    front = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line and not line.startswith(" "))
    name = front.get("name", "").strip()
    desc = front.get("description", "").strip()
    if name != skill.parent.name:
        err(f"{skill.relative_to(ROOT)}: name {name!r} should match folder {skill.parent.name!r}")
    if not desc or len(desc) > 1024:
        err(f"{skill.relative_to(ROOT)}: description must be 1-1024 characters (has {len(desc)})")

if errors:
    print("\n".join("✗ " + e for e in errors))
    sys.exit(1)
print(f"✓ {len(files)} JSON files, {len(servers)} MCP entries, skills and versions OK")
