# Changelog

All notable changes to the `cofounder-team` skills bundle are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

What the version numbers mean for this bundle:

- **MAJOR** — A skill is removed or renamed, a handoff contract between skills changes in a way that breaks existing usage, or the install/upgrade path changes in a way that requires user action beyond a normal upgrade.
- **MINOR** — A new skill ships, a new section or capability is added to an existing skill, a persona's scope expands, or any backwards-compatible behavior change.
- **PATCH** — Typos, wording polish, small clarifications, internal cross-reference fixes, or other changes that do not alter behavior.

The `humanizer` skill keeps its own `version: 3.0.0` in frontmatter because it predates the bundle and tracks its own internal history. That number is informational; the bundle version in `VERSION` is authoritative for upgrade decisions.

## [Unreleased]

## [0.2.0] - 2026-05-24

### Added

- Cross-skill language contract. Personas (Jack, Maya, Priya, Dan) and coaches (`pitch-deck-coach`, `startup-application-coach`) now respond to the founder in whichever language the founder uses, and generate artifacts (slides, application answers, content drafts, financial narratives, captions, scripts) in that same language by default. The founder can override per artifact ("draft this in English") without changing the conversational language.
- `humanizer` scope clarification. The skill is explicitly English-only and refuses non-English drafts rather than inventing patterns that do not transfer.
- "Non-English copy" exception in every persona's and coach's mandatory humanizer-pass section. Non-English drafts skip the humanizer pass with a short note to the founder.
- Third clause to the cross-skill contract in `CLAUDE.md` so future edits keep language matching consistent across skills.
- `README.md` note about the language behavior.
- `CHANGELOG.md` and `VERSION` files. The bundle now follows Keep a Changelog format and Semantic Versioning.
- "Versioning and CHANGELOG" section in `CLAUDE.md` describing what MAJOR / MINOR / PATCH mean for this bundle and the release process.
- `cofounder-team-upgrade` now shows the curated `CHANGELOG.md` diff in addition to the raw commit log, so users see what actually changed in their words.

## [0.1.0] - 2026-05-24

### Added

- Initial release of the cofounder-team bundle.
- Four co-founder personas: `jack` (sales, marketing, growth), `maya` (product, UX), `priya` (creative, content, social media), `dan` (fundraising, capital strategy, investor relations from pre-seed to Series A).
- Two coaching skills: `pitch-deck-coach` and `startup-application-coach`.
- `humanizer` skill (English-only) called by the personas and coaches before returning user-facing copy.
- `cofounder-team-upgrade` skill that runs the upgrade workflow.
- `setup` and `uninstall` scripts. `setup` symlinks skills into `~/.claude/skills/` on macOS and Linux, copies them with a `.cofounder-team` sentinel file on Windows / Git Bash. `uninstall` only removes entries it created.
- `CLAUDE.md` with the cross-skill contract (lane boundaries, humanizer invocation pattern, persona SKILL.md shape).
- `README.md` and `LICENSE` (MIT).
