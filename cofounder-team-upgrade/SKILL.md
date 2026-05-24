---
name: cofounder-team-upgrade
description: "Upgrade the cofounder-team skills to the latest version. Use when the user wants to update or upgrade their cofounder-team skills, get the newest versions of Jack, Maya, Priya, Dan, pitch-deck-coach, startup-application-coach, or humanizer, or asks to run /cofounder-team-upgrade. Triggers include 'upgrade cofounder-team', 'update my cofounder skills', 'pull latest cofounder-team', or running /cofounder-team-upgrade."
---

# Upgrade the cofounder-team skills

When the user asks to upgrade, do exactly this. Do not edit any files. Only run shell commands.

1. **Set the repo folder.** Default is `~/.cofounder-team`. If that folder does not exist, ask the user where they cloned the repo and use that path instead for the rest of the steps.

2. **Record the current version** so we can show the user what changed:
   ```
   git -C ~/.cofounder-team rev-parse HEAD
   ```
   Remember this value as `OLD`.

3. **Pull the latest version:**
   ```
   git -C ~/.cofounder-team pull
   ```

4. **Re-run the installer** so any new skills get linked into `~/.claude/skills/`:
   ```
   bash ~/.cofounder-team/setup
   ```

5. **Show what changed since `OLD`.** First the curated changelog, then the raw commit log as a fallback.

   Changelog diff (this is the human-readable summary of what shipped):
   ```
   git -C ~/.cofounder-team diff OLD..HEAD -- CHANGELOG.md
   ```
   If the user was on a version before `CHANGELOG.md` existed (anything older than v0.2.0), the diff will show the whole changelog as added. That is correct: everything in it is new to them.

   Raw commit log (covers anything not captured in the changelog):
   ```
   git -C ~/.cofounder-team log --oneline OLD..HEAD
   ```
   (Replace `OLD` with the value from step 2 in both commands.)

   If there are no new commits, tell the user they are already up to date.

6. **Tell the user the new version and to start a new Claude Code session** so the updated skills load. Read the version from `~/.cofounder-team/VERSION` if it exists; otherwise just tell them to restart.

That is the entire upgrade workflow. Do not run additional commands, do not edit files, do not modify anything outside `~/.cofounder-team` and `~/.claude/skills/`.
