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

These skills are designed as a team that knows its own lanes. When editing any persona skill, keep three contracts intact:

1. **Lane boundaries are mutual.** If `jack/SKILL.md` says "visual content sits with Priya" then `priya/SKILL.md` must own that lane. Boundaries described in one skill's "Boundaries" section should be reflected in the other skill's domain. Changing a lane in one place is a multi-file edit.
2. **`humanizer` is called by the others.** Jack, Maya, Priya, Dan, and the two coaches all instruct themselves to run drafts through the `humanizer` skill before returning user-facing copy. If you change humanizer's name, location, or invocation pattern, update every caller.
3. **Language follows the user.** All persona and coach skills detect the founder's language from their messages and respond in that language. Generated artifacts (pitch decks, application answers, content drafts, financial model narratives) are produced in the same language unless the founder explicitly asks for a different language for a specific artifact ("make the deck in English"). Per-artifact overrides do not change the conversational language. Persona names (Jack, Maya, Priya, Dan) stay as-is. `humanizer` is English-only, so non-English drafts skip the humanizer pass and say so briefly. If you add a new persona or coach, it must follow this contract too.

The personas (Jack, Maya, Priya, Dan) follow a consistent SKILL.md shape: persona intro → "How you think" → "Your domain" → "Boundaries" (which names the other co-founders by full name and explicitly hands work off) → "Companion skills" → "How you talk" → "Generating copy: mandatory humanizer pass" → "Context". Preserve this shape when editing — it's how the hand-offs stay reliable.

## Style rules baked into the skills themselves

When editing skill prose, match the existing voice. In particular: **no em dashes** (this is stated explicitly in the persona skills' "How you talk" sections, and `humanizer` flags em-dash overuse as pattern #14). Use commas, parentheses, or two sentences instead.

## Versioning and CHANGELOG

The bundle uses [Semantic Versioning](https://semver.org/). `VERSION` at the repo root is the source of truth for the current version. `CHANGELOG.md` follows the [Keep a Changelog](https://keepachangelog.com/) format.

What the version numbers mean here:

- **MAJOR** — A skill is removed or renamed, a handoff contract between skills changes in a way that breaks existing usage, or the install/upgrade path changes in a way that requires user action beyond a normal upgrade.
- **MINOR** — A new skill ships, a new section or capability is added to an existing skill, a persona's scope expands, or any backwards-compatible behavior change. The language-matching contract added in 0.2.0 is a MINOR example.
- **PATCH** — Typos, wording polish, small clarifications, internal cross-reference fixes, or other changes that do not alter behavior.

Every change goes into the `[Unreleased]` section of `CHANGELOG.md` as it ships. When cutting a release: rename `[Unreleased]` to the new version and date (`[X.Y.Z] - YYYY-MM-DD`), insert a fresh empty `[Unreleased]` at the top, bump `VERSION`, commit, then `git tag vX.Y.Z` and `git push --tags`.

The `humanizer` skill keeps its own `version: 3.0.0` in frontmatter because it predates the bundle. That number is informational; the bundle version is authoritative for upgrade decisions. Do not propagate per-skill versions to the other SKILL.md files.

## The upgrade skill

`cofounder-team-upgrade/SKILL.md` is itself a runbook: `git -C ~/.cofounder-team rev-parse HEAD` (save as OLD) → `git pull` → `bash setup` → `git diff OLD..HEAD -- CHANGELOG.md` → `git log OLD..HEAD`. Do not add steps that edit files or touch anything outside `~/.cofounder-team` and `~/.claude/skills/`.
