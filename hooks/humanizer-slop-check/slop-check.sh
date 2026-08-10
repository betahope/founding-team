#!/usr/bin/env bash
# humanizer-slop-check — an OPTIONAL Claude Code PostToolUse hook.
#
# What it does: after Claude writes or edits a text file, this scans the text
# Claude just wrote (not the whole file) for a handful of obvious "AI tells":
# multiple em dashes, negative-parallelism openers, "serves as", and a list of
# high-frequency AI words synced with the humanizer's pattern catalog. If it sees
# at least two kinds of tell, it hands Claude a short note listing them and asks
# it to run the `humanizer` skill. This is the safety net for the case the article
# calls out: the worst copy slips through when nobody invoked the humanizer at all.
#
# This is a HEURISTIC, not the humanizer skill. It only catches easy, surface-level
# tells. The real cleanup is still the humanizer skill's job.
#
# It is OPT-IN. It does nothing until you register it yourself (see hooks/README.md).
# It only runs in Claude Code. Claude.ai has no hooks, so this is irrelevant there.
# If anything goes wrong, it exits quietly and never blocks your work.

set -euo pipefail

# Never break the session: if python3 is missing, do nothing.
if ! command -v python3 >/dev/null 2>&1; then
  exit 0
fi

# Run the detector, passing this hook's stdin (the JSON payload) straight through.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/slop-check.py"
