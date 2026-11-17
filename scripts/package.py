#!/usr/bin/env python3
"""Build ready-to-submit packages into dist/. Run from anywhere: python3 scripts/package.py

dist/joinforme-skill.zip   the skill folder (joinforme/SKILL.md), for skill uploads
dist/joinforme-plugin.zip  the whole plugin (manifests, .mcp.json, skills/, assets/), for plugin portals
dist/SHA256SUMS
Only files tracked by git are packaged, with fixed timestamps, so the same commit gives the same ZIPs.
"""
import hashlib
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
STAMP = (2026, 1, 1, 0, 0, 0)

PLUGIN = [".claude-plugin/", ".codex-plugin/", "plugin.json", "mcp.json", ".mcp.json", "gemini-extension.json",
          "server.json", "skills/", "assets/", "README.md", "LICENSE"]


def tracked():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return sorted(out.split())


def write_zip(path, members):
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, src in members:
            info = zipfile.ZipInfo(arc, STAMP)
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, (ROOT / src).read_bytes())


def main():
    DIST.mkdir(exist_ok=True)
    files = tracked()
    skill = [(f[len("skills/"):], f) for f in files if f.startswith("skills/joinforme/")]
    plugin = [(f, f) for f in files if any(f == p or (p.endswith("/") and f.startswith(p)) for p in PLUGIN)]
    if not skill or not any(a == ".codex-plugin/plugin.json" for a, _ in plugin):
        raise SystemExit("package: expected files are missing")
    write_zip(DIST / "joinforme-skill.zip", skill)
    write_zip(DIST / "joinforme-plugin.zip", plugin)
    sums = []
    for name in ("joinforme-skill.zip", "joinforme-plugin.zip"):
        sums.append(f"{hashlib.sha256((DIST / name).read_bytes()).hexdigest()}  {name}")
        print(f"dist/{name}")
    (DIST / "SHA256SUMS").write_text("\n".join(sums) + "\n")


if __name__ == "__main__":
    main()
