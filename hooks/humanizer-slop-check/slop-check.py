#!/usr/bin/env python3
"""humanizer-slop-check detector. See slop-check.sh and ../README.md.

Reads a Claude Code PostToolUse hook payload as JSON on stdin, finds the edited
file, scans it for a few obvious AI tells, and if any are present prints a short
note for Claude asking it to run the humanizer. Heuristic and conservative on
purpose. Exits quietly on anything unexpected so it never blocks a session.
"""
import json
import os
import re
import sys


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # malformed input: do nothing

    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("path")
    if not path or not os.path.isfile(path):
        return 0

    # Only look at prose files. Code and data files are not our business.
    prose_ext = (".md", ".mdx", ".markdown", ".txt", ".html", ".htm")
    if not path.lower().endswith(prose_ext):
        return 0

    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except Exception:
        return 0

    low = text.lower()
    findings = []

    if "—" in text or "–" in text:
        findings.append("em/en dashes")
    if any(ch in text for ch in ("“", "”", "‘", "’")):
        findings.append("curly quotation marks")
    if re.search(r"\bnot just\b|\bnot only\b", low):
        findings.append('negative parallelism ("not just X, it\'s Y")')
    if re.search(r"\bserves as\b|\bstands as\b", low):
        findings.append('copula avoidance ("serves as")')

    ai_words = [
        "delve", "tapestry", "underscore", "underscores", "testament",
        "vibrant", "nestled", "bustling", "ever-evolving", "seamless",
        "seamlessly", "at its core", "the real question", "let's dive",
        "in order to", "navigating the", "in the realm of",
    ]
    hits = sorted({w for w in ai_words if w in low})
    if hits:
        findings.append("high-frequency AI words: " + ", ".join(hits))

    if not findings:
        return 0

    msg = (
        "humanizer-slop-check flagged possible AI tells in "
        + os.path.basename(path)
        + ": " + "; ".join(findings) + ". "
        "If this file is user-facing copy, run the `humanizer` skill on it and, "
        "when you present it, name the tells you fixed. (This is a heuristic "
        "check; ignore it if the file is not user-facing copy.)"
    )

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
