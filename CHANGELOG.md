# Changelog

All notable changes to the `cofounder-team` skills bundle are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

What the version numbers mean for this bundle:

- **MAJOR** — A skill is removed or renamed, a handoff contract between skills changes in a way that breaks existing usage, or the install/upgrade path changes in a way that requires user action beyond a normal upgrade.
- **MINOR** — A new skill ships, a new section or capability is added to an existing skill, a persona's scope expands, or any backwards-compatible behavior change.
- **PATCH** — Typos, wording polish, small clarifications, internal cross-reference fixes, or other changes that do not alter behavior.

The `humanizer` skill keeps its own `version: 3.0.0` in frontmatter because it predates the bundle and tracks its own internal history. That number is informational; the bundle version in `VERSION` is authoritative for upgrade decisions.

## [Unreleased]

### Fixed

- Trimmed `dan/SKILL.md` description to fit Claude.ai's 1024-character limit on the `description` frontmatter field. Was 1382 characters, which caused Claude.ai's skill loader to reject the upload with `field 'description' in SKILL.md must be at most 1024 characters`. The trim collapsed two enumerated sub-lists into compact parentheticals (cap table mechanics; grants and accelerator programs), dropped a few non-trigger details, and preserved all term-sheet vocabulary, program names, and persona credibility that drive triggering.

### Notes

- **Workflow maintenance TODO (before 2026-06-02):** the release workflow at `.github/workflows/release.yml` uses `actions/checkout@v4` and `softprops/action-gh-release@v2`, both currently running on Node.js 20. GitHub Actions will force Node.js 24 as the default starting **2026-06-02** and will remove Node.js 20 from runners on **2026-09-16**. Bump these actions to versions that ship Node.js 24 builds before then, or set `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24=true` on the runner as a temporary opt-in. Background: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/

## [0.4.1] - 2026-05-24

### Fixed

- README install sections now explicitly call out Windows support. "Install in Claude Code" leads with "Works on macOS, Linux, and Windows" and explains the Git Bash / MSYS / WSL specifics where they matter. "Install in Claude.ai" notes that the path works on any OS with no terminal needed. Previously a Windows reader could mistake the Claude Code path for Mac/Linux only because the first line said "Open a terminal on macOS or Linux."

## [0.4.0] - 2026-05-24

### Added

- Each persona gained one high-leverage instinct in their "How you think" section. Small additions, chosen because each one closes the single biggest blind spot in that persona's domain.
  - **Jack** — "Strategy before tactics." Before recommending any channel, campaign, pricing change, or growth experiment, name the ICP in one sentence and the buyer's specific job in one sentence, then check whether the proposed tactic matches both. The most common failure in his domain is well-executed marketing for a poorly positioned product.
  - **Maya** — "Stay close to users." Before suggesting a flow change, a feature cut, an onboarding redesign, or a new experiment, ask the founder when they last talked to a user and what those users said. If it has been more than a week, push for a conversation before the decision.
  - **Priya** — "Anchor on references early." Before generating concepts or producing assets, ask for three to five visual references that capture what the founder is picturing. Closes the gap between what the founder imagines and what gets produced.
  - **Dan** — "The five facts to anchor on." On first contact about any fundraising decision, get current runway, current burn, last milestone hit, next milestone with target date and definition of done, and a cap table snapshot. Without these, every recommendation is generic.
- All four personas now close their "How you think" section with a "Name what would change your mind" instinct: when taking a strong position, state the concrete falsifiable evidence that would update it. Signals real thinking instead of stubborn templating and gives the founder a clear bar to push back on.
- Both coaches gained operational reflexes that turn existing principles into specific reader-simulation outputs.
  - **pitch-deck-coach** — "Answer the audience's question." Added as a non-negotiable. Names the specific question this audience is asking (seed investor: "is this a fund-returner?"; YC reviewer: "is this an interesting founder with an interesting wedge?"; customer: "should I buy this?") and checks every slide against it before reviewing or planning anything else.
  - **pitch-deck-coach** — Title-only narrative, operationalized. Critique mode's first review pass now produces three explicit reader-simulation outputs for the founder (one-line takeaway, vision check, title-only narrative) and shares them before any slide-by-slide critique.
  - **startup-application-coach** — First-sentence test, operationalized. Critique mode now reads only the first sentence of each answer, states it verbatim, and reports what landed. Simulates the actual reader's stop-at-weak-first-sentence skim.
  - **startup-application-coach** — "Surface the one obvious fact." Added as a non-negotiable. Asks the founder for their single most impressive concrete fact and checks that it appears in the first 30 words of some answer, not buried in paragraph three.
- Cross-skill voice rule: default to brief in conversation. The four personas had their "Concise and accurate" and "Match the depth of your response" bullets replaced with a sharper default-to-brief pair (shortest answer that still says why; take a position, give one or two reasons, stop; expand only if the founder asks). The two coaches gained a new "How you respond in conversation" section saying the same thing. Both versions are explicit that the rule applies to chat replies only: slide-by-slide content, application drafts, founder bios, and other produced artifacts stay as long as they need to be.

### Fixed

- Corrected the Claude.ai UI path in install/upgrade docs. Skills on Claude.ai live under **Customize → Skills** in the left sidebar, not under Settings. The wrong path appeared in `README.md`, `CLAUDE.md`, the release workflow's release-notes template, and the [0.3.0] section below. The v0.3.0 release notes on GitHub were also patched in place via `gh release edit`.

## [0.3.0] - 2026-05-24

### Added

- Claude.ai distribution path. Each persona and coach is now packaged as a standalone `.zip` and attached to every GitHub Release for upload through Claude.ai's **Customize → Skills** UI (in the left sidebar).
- `.github/workflows/release.yml`. Builds the per-skill zips automatically on `v*` tag push and supports manual re-runs via `workflow_dispatch`. Auto-discovers skills by scanning for top-level directories with a `SKILL.md`. Excludes anything in `EXCLUDED_SKILLS` (currently just `cofounder-team-upgrade`). Release notes are pulled from the matching section of this changelog.
- "Install in Claude.ai" and "Upgrade in Claude.ai" sections in `README.md` linking to the latest release and explaining the re-upload upgrade flow.
- "Distribution channels" section in `CLAUDE.md` describing the two install surfaces (Claude Code via local install, Claude.ai via release zips) and what to do when adding a new skill.

### Notes

- The `cofounder-team-upgrade` skill is intentionally excluded from Claude.ai release zips. It touches local filesystem paths (`~/.cofounder-team`, `~/.claude/skills/`) that do not exist on Claude.ai. On Claude.ai, "upgrade" means downloading the newer release zips and re-uploading them.
- Earlier versions (v0.1.0, v0.2.0) do not have release zips attached. The Claude.ai distribution starts at v0.3.0.

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
