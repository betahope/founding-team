# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Git workflow

Work directly on `main`. All commits and pushes go to `main` — do not create feature branches, do not open PRs against a different base, do not push to any other branch. If a task seems to call for a branch, default to `main` unless the user explicitly says otherwise.

## What this repo is

A bundle of portable Claude Code skills. There is no application, no build, no test suite, no lint. Every "deliverable" is a `SKILL.md` (plus optional `references/`) that Claude Code loads at session start.

## Repo layout

Each top-level directory containing a `SKILL.md` is a skill:

- `jack`, `maya`, `priya`, `dan` — the four co-founder personas
- `pitch-deck-coach`, `startup-application-coach` — coaching skills
- `humanizer` — called by the other skills before they return user-facing copy
- `cofounder-team-upgrade` — runs the upgrade workflow

`setup` and `uninstall` are bash scripts. `setup` walks every top-level dir that contains a `SKILL.md` and links it into `~/.claude/skills/` (or copies it on Windows / Git Bash, leaving a `.cofounder-team` sentinel file).

## How edits land in Claude Code

On macOS and Linux, `~/.claude/skills/<name>` is a **symlink** back into this repo. That means editing a `SKILL.md` here changes the live, installed skill immediately — no re-install needed, but the user still has to start a new Claude Code session for the loader to pick it up.

On Windows the entries are copies, so changes here do **not** reach the installed skill until `bash ./setup` (or `/cofounder-team-upgrade`) is re-run.

## Adding a new skill

1. Create `<skill-name>/SKILL.md` at the repo root with valid frontmatter (`name`, `description`, optionally `version`, `license`, `allowed-tools`).
2. Run `bash ./setup` to link it into `~/.claude/skills/`.
3. Update `README.md`'s "The skills" list.
4. If other skills should hand off to it, add it to their **Companion skills** / **Boundaries** sections.

`setup` will skip any path under `~/.claude/skills/<name>` that is a real folder it didn't create (no symlink, no sentinel file) — so don't try to overwrite a user's existing skill of the same name.

## The cross-skill contract

These skills are designed as a team that knows its own lanes. When editing any persona skill, keep two contracts intact:

1. **Lane boundaries are mutual.** If `jack/SKILL.md` says "visual content sits with Priya" then `priya/SKILL.md` must own that lane. Boundaries described in one skill's "Boundaries" section should be reflected in the other skill's domain. Changing a lane in one place is a multi-file edit.
2. **`humanizer` is called by the others.** Jack, Maya, Priya, Dan, and the two coaches all instruct themselves to run drafts through the `humanizer` skill before returning user-facing copy. If you change humanizer's name, location, or invocation pattern, update every caller.

The personas (Jack, Maya, Priya, Dan) follow a consistent SKILL.md shape: persona intro → "How you think" → "Your domain" → "Boundaries" (which names the other co-founders by full name and explicitly hands work off) → "Companion skills" → "How you talk" → "Generating copy: mandatory humanizer pass" → "Context". Preserve this shape when editing — it's how the hand-offs stay reliable.

## Style rules baked into the skills themselves

When editing skill prose, match the existing voice. In particular: **no em dashes** (this is stated explicitly in the persona skills' "How you talk" sections, and `humanizer` flags em-dash overuse as pattern #14). Use commas, parentheses, or two sentences instead.

## The upgrade skill

`cofounder-team-upgrade/SKILL.md` is itself a runbook: `git -C ~/.cofounder-team rev-parse HEAD` (save as OLD) → `git pull` → `bash setup` → `git log OLD..HEAD`. Do not add steps that edit files or touch anything outside `~/.cofounder-team` and `~/.claude/skills/`.
