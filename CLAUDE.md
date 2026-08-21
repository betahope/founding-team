# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Response style (critical)

Every response in every session must be as concise as possible. As clear as possible. In simple, plain English. This applies to Claude and to every invoked persona (Maya, Jack, Priya, Dan, or any other co-founder skill).

Generated artefacts (drafts, plans, copy) may run as long as the artefact genuinely needs. Conversation may not.

## Git workflow

Work directly on `main`. All commits and pushes go to `main` — do not create feature branches, do not open PRs against a different base, do not push to any other branch. If a task seems to call for a branch, default to `main` unless the user explicitly says otherwise.

## What this repo is

A bundle of portable Claude Code skills. There is no application, no test suite, no lint. Every "deliverable" is a `SKILL.md` (plus optional `references/`) that Claude Code loads at session start.

There is one small build step. The source `SKILL.md` files use a few templating directives, and `build` (plain bash, no dependencies) compiles them into two finished flavors under `dist/`. See "The build system" below. `setup` runs the build for you, so the day-to-day loop is still just "clone and run setup."

## Repo layout

Each top-level directory containing a `SKILL.md` is a skill:

- `jack`, `maya`, `priya`, `dan` — the four co-founder personas
- `team` — convenes the personas in one multi-voice reply for cross-domain questions and big decisions
- `pitch-deck-coach`, `startup-application-coach` — coaching skills
- `humanizer` — called by the other skills before they return user-facing copy. Its pattern catalog is vendored from upstream, not written here (see "The vendored humanizer catalog" below)
- `cofounder-team-upgrade` — runs the upgrade workflow

Supporting pieces:

- `build` — bash script that compiles source skills into `dist/claude-code/` and `dist/portable/`.
- `shared/` — snippets included by more than one skill (for example `shared/persona/` holds the co-founder intro, the shared style rules, the humanizer steps, and the non-English rule). Not a skill.
- `hooks/` — optional, opt-in Claude Code hooks (currently `humanizer-slop-check`). Not a skill, not installed by `setup`, absent on Claude.ai.
- `dist/` — build output. Git-ignored. Never edit by hand; rebuild instead.

`setup` and `uninstall` are bash scripts. `setup` runs `build`, then links every skill in `dist/claude-code/` into `~/.claude/skills/` (or copies it on Windows / Git Bash, leaving a `.cofounder-team` sentinel file). `uninstall` removes only the links or copies this repo created.

## Distribution channels

The bundle ships through two channels that work very differently. Both are equally supported.

**Claude Code (local install).** Users `git clone` this repo to `~/.cofounder-team` and run `bash ./setup`. `setup` builds the skills, then on macOS and Linux makes `~/.claude/skills/<name>` a **symlink** into `dist/claude-code/<name>`. Because the installed skill points at the build, editing a source `SKILL.md` does **not** change the live skill until you rebuild (run `bash ./build`, or just `bash ./setup` again) and start a new Claude Code session. On Windows, entries are copies, so changes never reach the installed skill until `bash ./setup` (or `/cofounder-team-upgrade`) is re-run. The installed Claude Code skill is the `claude-code` flavor, so it carries the Claude-Code-only extras (the coach memory sections, the humanizer hook note).

**Claude.ai (release zips).** Every `v*` tag push triggers `.github/workflows/release.yml`, which runs `build` and attaches one `.zip` per skill (the `portable` flavor) to a GitHub Release. Users download the zips and upload them via Claude.ai's **Customize → Skills** UI (in the left sidebar). There is no in-app upgrade path on Claude.ai; users re-download newer zips and re-upload to update. Note: Skills on Claude.ai live under Customize in the sidebar, not under Settings — easy to get wrong when writing docs. The `portable` flavor omits everything that only works in Claude Code, so it is always safe words-and-references only. The release zips are what ship this flavor: to Claude.ai, to ChatGPT, or to any other tool that supports the Agent Skills standard.

The release workflow discovers skills by scanning `dist/portable/` after the build. It excludes any skill listed in the workflow's `EXCLUDED_SKILLS` env var. Currently only `cofounder-team-upgrade` is excluded (it touches local filesystem paths that do not exist on Claude.ai).

The Claude.ai distribution starts at v0.3.0. Earlier tags (v0.1.0, v0.2.0) only ship through the Claude Code install path.

## The build system

One source, two builds. The same skill ships to Claude Code (which can run hooks, save memory files, and more) and to any Agent Skills tool such as Claude.ai or ChatGPT (which can only read the skill text and its bundled references). So `build` compiles each source `SKILL.md` into two flavors:

- `dist/claude-code/<skill>/` — the full version, including Claude-Code-only extras.
- `dist/portable/<skill>/` — the portable version: words and reference notes only, nothing that needs a running program. Ships in the release zips, uploaded to Claude.ai, ChatGPT, or any other Agent Skills tool.

`build` is plain bash and needs nothing installed (it runs on macOS's bash 3.2). Every `.md` file in a skill folder is rendered through the directive pipeline: the `SKILL.md`, every file under `references/`, and shared snippets. So includes and flavor blocks work in reference files too, not just in `SKILL.md`. Non-markdown assets are copied as-is. The directives:

- `{{include: shared/persona/foo.md}}` — insert another file here (also processed). Path is relative to the repo root. Must be alone on its line.
- `{{set:NAME=value}}` — define a variable (the line is removed from output). Read from the source `SKILL.md` only.
- `{{var:NAME}}` — replaced by the value set above. `{{var:BUNDLE_VERSION}}` is a built-in exception: `build` always defines it from the repo's `VERSION` file, so no skill needs its own `{{set:BUNDLE_VERSION=...}}` line. The name is reserved: if a skill sets it anyway, the built-in value still wins.
- `{{FLAVOR:claude-code}} ... {{/FLAVOR}}` — keep this block only in the Claude Code build.
- `{{FLAVOR:portable}} ... {{/FLAVOR}}` — keep this block only in the portable build.

A source file with no directives renders byte-identical to a plain copy, so most edits need no knowledge of the build at all. One caveat: `{{set:NAME=value}}` variables are read only from the skill's `SKILL.md`, but they apply everywhere in that skill (including reference files and includes).

**Golden rule: never break the portable build.** Anything that needs a hook, a helper agent, a script, or persistent memory is Claude Code only. Put it inside a `{{FLAVOR:claude-code}}` block so the portable build never sees it. Universal, words-only improvements need no flavor wrapper.

Every skill's frontmatter must stay within the Agent Skills spec fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`; spec at https://agentskills.io/specification). Anything outside that set fails `skills-ref` validation in the release workflow.

After any change to a source skill or a shared snippet, run `bash ./build` and confirm no `{{` directives leak into `dist/` (`grep -rn "{{" dist/` should be empty except in intended literal cases). `setup` runs the build automatically.

## Adding a new skill

1. Create `<skill-name>/SKILL.md` at the repo root with valid frontmatter (`name`, `description`, optionally `license`, `compatibility`, `metadata`, `allowed-tools`). You can use the build directives (includes, flavor blocks) if useful, but a plain `SKILL.md` with no directives works too.
2. Run `bash ./setup` to build and link it into `~/.claude/skills/`.
3. Update `README.md`'s "The skills" list (and the "Install in Claude.ai" step list if the skill should ship to Claude.ai too).
4. If other skills should hand off to it, add it to their **Companion skills** / **Boundaries** sections.
5. Decide whether the skill should ship to Claude.ai. If it touches local filesystem paths, machine-specific state, or anything else that does not exist on Claude.ai, add it to `EXCLUDED_SKILLS` in `.github/workflows/release.yml`. Otherwise no workflow change is needed — auto-discovery picks it up on the next tagged release.

`setup` will skip any path under `~/.claude/skills/<name>` that is a real folder it didn't create (no symlink, no sentinel file), so don't try to overwrite a user's existing skill of the same name.

## The cross-skill contract

These skills are designed as a team that knows its own lanes. When editing any persona skill, keep five contracts intact:

1. **Lane boundaries are mutual.** If `jack/SKILL.md` says "visual content sits with Priya" then `priya/SKILL.md` must own that lane. Boundaries described in one skill's "Boundaries" section should be reflected in the other skill's domain. Changing a lane in one place is a multi-file edit.
2. **`humanizer` is called by the others.** Jack, Maya, Priya, Dan, and the two coaches all instruct themselves to run drafts through the `humanizer` skill before returning user-facing copy. If you change humanizer's name, location, or invocation pattern, update every caller. The four personas now share the humanizer workflow steps and the non-English rule from `shared/persona/humanizer-steps.md` and `shared/persona/humanizer-non-english.md`, so editing those two snippets updates all four personas at once. The two coaches keep their own inline copies (their structure differs), so they still need separate edits.
3. **Language follows the user.** All persona and coach skills detect the founder's language from their messages and respond in that language. Generated artifacts (pitch decks, application answers, content drafts, financial model narratives) are produced in the same language unless the founder explicitly asks for a different language for a specific artifact ("make the deck in English"). Per-artifact overrides do not change the conversational language. Persona names (Jack, Maya, Priya, Dan) stay as-is. `humanizer` runs in full on English drafts; on non-English drafts it does a structural-only pass (its lexical patterns are English-specific) and the caller notes that briefly. If you add a new persona or coach, it must follow this contract too.
4. **Style rules are shared.** Jack, Maya, Priya, Dan, and the `team` skill all include `shared/persona/talk-rules.md`, which holds the four rules every co-founder voice follows: simple plain language (in whatever language the founder is using), concise, organised, and no em dashes. It also draws the line on scope: conciseness applies to conversation, while plain language and organisation apply to artifacts too. Edit that one file to change how every co-founder communicates. Do not restate these rules inside a persona; add only what is specific to that persona (Dan's fundraising vocabulary note is the example).
5. **Company memory is shared (Claude Code only).** The personas, the coaches, and the `team` skill all include `shared/persona/company-memory.md`, which defines one shared memory file (`./.cofounder-team/company.md` in the founder's project) holding the company basics. It is wrapped in a `{{FLAVOR:claude-code}}` block, so the portable build never sees it. A new skill that advises the company should include the same snippet.

The personas (Jack, Maya, Priya, Dan) follow a consistent SKILL.md shape: persona intro → "How you think" → "Your domain" → "Boundaries" (which names the other co-founders by full name and explicitly hands work off) → "Companion skills" → "How you talk" → "Generating copy: mandatory humanizer pass" → "Context". Preserve this shape when editing — it's how the hand-offs stay reliable. A few of these blocks are now `{{include}}` directives resolved at build time (the co-founder intro, the style rules, the humanizer steps, the non-English rule); the rendered shape is unchanged.

## Style rules baked into the skills themselves

When editing skill prose, match the existing voice. In particular: **no em dashes** (this is stated explicitly in `shared/persona/talk-rules.md`, which every persona's "How you talk" section includes, and `humanizer` flags em dashes). Use commas, parentheses, or two sentences instead.

## Versioning and CHANGELOG

The bundle uses [Semantic Versioning](https://semver.org/). `VERSION` at the repo root is the source of truth for the current version. `CHANGELOG.md` follows the [Keep a Changelog](https://keepachangelog.com/) format.

What the version numbers mean here:

- **MAJOR** — A skill is removed or renamed, a handoff contract between skills changes in a way that breaks existing usage, or the install/upgrade path changes in a way that requires user action beyond a normal upgrade.
- **MINOR** — A new skill ships, a new section or capability is added to an existing skill, a persona's scope expands, or any backwards-compatible behavior change. The language-matching contract added in 0.2.0 is a MINOR example.
- **PATCH** — Typos, wording polish, small clarifications, internal cross-reference fixes, or other changes that do not alter behavior.

Every change goes into the `[Unreleased]` section of `CHANGELOG.md` as it ships. When cutting a release: rename `[Unreleased]` to the new version and date (`[X.Y.Z] - YYYY-MM-DD`), insert a fresh empty `[Unreleased]` at the top, bump `VERSION`, commit, then `git tag vX.Y.Z` and `git push --tags`.

The `humanizer` skill keeps its own version, now under `metadata.version` in frontmatter, because it predates the bundle. That number is informational; the bundle version is authoritative for upgrade decisions. Do not propagate per-skill versions to the other SKILL.md files.

## The vendored humanizer catalog

The humanizer's pattern catalog is not ours. It belongs to blader
(https://github.com/blader/humanizer, MIT) and is vendored, unmodified, as
`humanizer/references/upstream-patterns.md`. We used to keep a hand-written copy that
slowly fell behind upstream; this replaces it.

Rules:

- **Never hand-edit `humanizer/references/upstream-patterns.md`.** It is generated. Any
  edit is lost on the next sync.
- **`humanizer/SKILL.md` is our layer only**: workflow, output sizing, the non-English
  rule, and the voice guidance. It must not restate the pattern list. Upstream renumbers
  and renames patterns between releases, so any second list here would drift, and so
  would any prose that cites a pattern by number. Do not reintroduce pattern numbers into
  `SKILL.md`, the shared snippets, or the hook comments.
- **`sync-humanizer`** (repo root, plain bash) fetches upstream's latest tagged release
  and rewrites the vendored file. `bash ./sync-humanizer --check` reports without writing.
  It refuses to vendor anything containing `{{`, since the build would treat that as a
  template directive.
- **`.github/workflows/sync-humanizer.yml`** runs the sync weekly, rebuilds, validates
  against the Agent Skills spec, and opens a pull request when upstream has moved. Nothing
  merges automatically. The repo needs "Allow GitHub Actions to create and approve pull
  requests" enabled under Settings -> Actions -> General.
- Reviewing a sync PR means checking that no renumbering broke prose elsewhere, deciding
  whether the slop-check hook's word list needs additions, and adding a `CHANGELOG.md`
  entry before the next release.

## The upgrade skill

`cofounder-team-upgrade/SKILL.md` is itself a runbook: `git -C ~/.cofounder-team rev-parse HEAD` (save as OLD) → `git pull` → `bash setup` → `git diff OLD..HEAD -- CHANGELOG.md` → `git log OLD..HEAD`. Do not add steps that edit files or touch anything outside `~/.cofounder-team` and `~/.claude/skills/`.
