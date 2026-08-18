#!/usr/bin/env python3
"""humanizer-slop-check detector. See slop-check.sh and ../README.md.

Reads a Claude Code PostToolUse hook payload as JSON on stdin, pulls out the text
Claude just wrote (not the whole file, so pre-existing text never re-triggers it),
scans that text for obvious AI tells, and prints a short note for Claude asking it
to run the humanizer. It stays quiet unless it sees at least two kinds of tell, or
a pile-up of high-frequency AI words. Heuristic and conservative on purpose. Exits
quietly on anything unexpected so it never blocks a session.
"""
import json
import os
import re
import sys

# High-frequency AI vocabulary, kept in sync with the humanizer skill's
# references/upstream-patterns.md (the sales-language and overused-word lists).
# Single words are matched on word boundaries; phrases are matched as substrings.
AI_WORDS = [
    "bustling", "crucial", "delve", "elevate", "empower", "fostering",
    "game-changer", "garner", "holistic", "interplay", "intricate", "leverage",
    "nestled", "pivotal", "robust", "seamless", "showcase", "streamline",
    "supercharge", "tapestry", "testament", "underscore", "unlock", "vibrant",
]
AI_PHRASES = [
    "at its core", "the real question", "here's the thing", "let's dive",
    "in order to", "ever-evolving", "navigating the", "in the realm of",
]

PROSE_EXT = (".md", ".mdx", ".markdown", ".txt", ".html", ".htm")


def new_text_from(tool_input):
    """Return only the text this tool call wrote, or None if unknown."""
    if isinstance(tool_input.get("content"), str):        # Write
        return tool_input["content"]
    parts = []
    if isinstance(tool_input.get("new_string"), str):     # Edit
        parts.append(tool_input["new_string"])
    for edit in tool_input.get("edits") or []:            # MultiEdit
        if isinstance(edit, dict) and isinstance(edit.get("new_string"), str):
            parts.append(edit["new_string"])
    return "\n".join(parts) if parts else None


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # malformed input: do nothing

    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("path")
    if not path or not path.lower().endswith(PROSE_EXT):
        return 0  # only prose files are our business

    text = new_text_from(tool_input)
    if not text:
        return 0  # nothing new written, or a tool shape we do not know

    # Normalise curly apostrophes so "let's dive" matches either apostrophe.
    low = text.lower().replace("’", "'")
    findings = []

    # Density, not presence: one em dash is normal typography.
    if text.count("—") >= 2:
        findings.append("multiple em dashes")
    if re.search(r"\bnot just\b|\bnot only\b", low):
        findings.append('negative parallelism ("not just X, it\'s Y")')
    if re.search(r"\bserves as\b|\bstands as\b", low):
        findings.append('copula avoidance ("serves as")')

    word_hits = sorted(
        {w for w in AI_WORDS if re.search(r"\b" + re.escape(w), low)}
        | {p for p in AI_PHRASES if p in low}
    )
    if word_hits:
        findings.append("high-frequency AI words: " + ", ".join(word_hits))

    # Quiet unless there is a real signal: two kinds of tell, or a word pile-up.
    if len(findings) < 2 and len(word_hits) < 3:
        return 0

    msg = (
        "humanizer-slop-check flagged possible AI tells in the text just written to "
        + os.path.basename(path)
        + ": " + "; ".join(findings) + ". "
        "If this is user-facing copy, run the `humanizer` skill on it and, "
        "when you present it, name the tells you fixed. (This is a heuristic "
        "check; ignore it if the text is not user-facing copy.)"
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
