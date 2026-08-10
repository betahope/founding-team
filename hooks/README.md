# Optional hooks (Claude Code only)

These are extras for Claude Code. They are **opt-in**: nothing here runs until you
turn it on yourself. None of it is installed by `setup`, and none of it exists on
Claude.ai (the website has no hooks). If you never touch this folder, the skills
work exactly the same.

## humanizer-slop-check

A safety net for the humanizer pass. The persona and coach skills already tell
Claude to run the `humanizer` skill on user-facing copy. But a skill only helps
when it is invoked. This hook runs automatically after Claude writes or edits a
text file and scans **only the text Claude just wrote** (never the rest of the
file, so old text does not re-trigger it on every edit). It looks for a few
obvious AI tells: multiple em dashes, "not just X" openers, "serves as" / "stands
as", and a list of high-frequency AI words kept in sync with the humanizer's
pattern catalog. It speaks up only when it sees at least two kinds of tell (or a
pile-up of AI words), and then asks Claude to run the humanizer and say what it
fixed.

It is a **heuristic**, not the humanizer skill. It catches easy surface tells only.
It is deliberately conservative to avoid false alarms, and it exits quietly if
anything is off, so it never blocks your work. It needs `python3` on your machine;
if that is missing, it does nothing.

### Turn it on

Add a `PostToolUse` hook to your Claude Code settings (either your global
`~/.claude/settings.json` or a project `.claude/settings.json`). Point it at the
script in this repo:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.cofounder-team/hooks/humanizer-slop-check/slop-check.sh"
          }
        ]
      }
    ]
  }
}
```

If you cloned the repo somewhere other than `~/.cofounder-team`, use that path.
Start a new Claude Code session after editing settings. To turn it off, remove the
block.

### Turn it off

Delete the block you added. That is all. It leaves no other trace.
