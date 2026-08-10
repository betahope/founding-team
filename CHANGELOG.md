# Changelog

All notable changes to the `cofounder-team` skills bundle are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

What the version numbers mean for this bundle:

- **MAJOR** — A skill is removed or renamed, a handoff contract between skills changes in a way that breaks existing usage, or the install/upgrade path changes in a way that requires user action beyond a normal upgrade.
- **MINOR** — A new skill ships, a new section or capability is added to an existing skill, a persona's scope expands, or any backwards-compatible behavior change.
- **PATCH** — Typos, wording polish, small clarifications, internal cross-reference fixes, or other changes that do not alter behavior.

The `humanizer` skill keeps its own version, now under `metadata.version` in frontmatter, because it predates the bundle and tracks its own internal history. That number is informational; the bundle version in `VERSION` is authoritative for upgrade decisions.

## [Unreleased]

## [0.13.0] - 2026-08-10

The "10x" release: two new capabilities (a team skill and shared company memory), a smarter humanizer, and a round of content, tooling, and consistency upgrades across the bundle.

### Added

- **`team` skill.** Convenes the co-founders in a single reply for cross-domain questions and big decisions: the most relevant co-founder leads, only the needed voices join, each is attributed by name, and every session ends in one clear recommendation. Portable, so it ships to Claude.ai, ChatGPT, and every other Agent Skills tool, bringing the multi-voice behavior that previously existed only in the Claude.ai project template to every platform. Added to the README skills list and install steps.
- **Shared company memory (Claude Code only).** The four personas, both coaches, and the team skill now share one memory file, `./.cofounder-team/company.md` in the founder's project, holding the durable basics (stage, ICP, metrics, runway, burn, cap table, top goal). Skills read it at session start instead of re-asking, update it when facts change, and offer once to create it. Defined in `shared/persona/company-memory.md` inside a `{{FLAVOR:claude-code}}` block; the portable build never sees it. Documented as cross-skill contract #4 in `CLAUDE.md`.
- **Humanizer: anti-fabrication rule.** The workflow now forbids introducing facts, numbers, names, or citations not present in the source (placeholder or ask instead), and `references/patterns.md` opens with a note that the invented specifics in its "after" examples are illustrative, not licence to fabricate.
- **Humanizer: density judgment and newer tells.** New "judge density, not presence" rule (count occurrences against length; one em dash is typography, three per paragraph is a tell), a warning that the voice examples are one voice, not the voice (so humanized pieces stop converging on the same casual-blogger sound), and extended watch lists: verb slop (leverage, unlock, streamline, robust, game-changer, holistic, supercharge, elevate, empower, seamless), "here's the thing", and perfectly parallel identical-opener bullet lists.
- **Missing weak/strong examples in `startup-application-coach`.** The competitors, why-now, customer acquisition, and milestones questions in `references/questions.md` now each have a weak/strong pair (fictional companies, labelled as such). `references/moats.md` gains a worked false-moat-to-honest-sequencing example plus two missing moat types: counter-positioning and regulatory/compliance position.
- **Missing slides in `pitch-deck-coach`.** `references/slide-by-slide.md` gains a go-to-market slide section (one concrete channel, evidence it works, why it is hard to copy) and use-of-funds guidance on the ask slide (money-to-milestones lines, 18-to-24-month operating plan, and how to handle forms that demand 5-year projections).
- **Freshness discipline on program facts.** `references/program-specific.md` opens with a standing rule (figures dated mid-2026; trust the program's live application over this file) and notes YC's four-batches-a-year cadence. `references/video.md` hedges the verbatim YC instructions the same way and adds an explicit rule: real founders on camera, no AI avatars or synthetic voiceover, for both video types.

### Changed

- **Humanizer works on non-English drafts now, structurally.** The old contract skipped the humanizer entirely for non-English copy. The new contract: lexical patterns (word lists, English idiom) remain English-only, but structural patterns (forced triplets, stacked hedges, signposting, label-colon-restatement lists, generic endings, chatbot leakage) apply in any language, so non-English drafts get a structural-only pass with a one-line note. Updated in the humanizer's scope section, the shared persona snippet, both coaches, the README, and `CLAUDE.md` contract #3.
- **The build renders every `.md` file, not just `SKILL.md`.** Reference files now go through the same directive pipeline (includes, flavor blocks, variables), enabling shared snippets inside `references/`. Files without directives render byte-identical to a plain copy. Documented in `CLAUDE.md`.
- **Duplicated content moved to `shared/` includes.** The team-bio weak/strong example and the bottom-up TAM strong example (the two examples that had already drifted apart between files), both coaches' conversation-style and humanizer-language sections, and the personas' "no em dashes" / "default to brief" bullets now live in single shared snippets. The vision guidance intentionally stays two-level (summary in SKILL.md, detail in `vision.md`) rather than deduplicated, since the two serve different loading stages.
- **The slop-check hook is quieter and sharper.** It now scans only the text Claude just wrote (pre-existing text no longer re-triggers it on every edit), requires two kinds of tell (or a pile-up of AI words) before speaking, drops the lone en-dash and curly-apostrophe triggers, matches "let's dive" with either apostrophe, and syncs its word list with the humanizer's pattern catalog. `hooks/README.md` updated to match.
- **Persona descriptions trimmed to what-and-when.** The behavior summary sentence ("challenges weak assumptions... takes a clear position") is gone from all four personas' frontmatter descriptions; the domain keywords and triggers stay. The behavior itself is unchanged; it lives in each skill's "How you think" section, which the model now has no shortcut around.
- **Bundle renamed to "The Co-Founder Team" in the README.** Title and tagline now match the folder, skill names, and changelog. The GitHub repo URLs still point at `betahope/founding-team` until the repo itself is renamed (GitHub will redirect once it is).
- **Application coach: replaced the unexplained "$2.5M in revenue" acquisition target** in `references/questions.md` with stage-appropriate phrasing (first 100 users, first 20 paying customers, first $100K).

## [0.12.0] - 2026-08-10

A correctness and consistency release: fixes from a full review of every skill against its own rules and the Agent Skills spec.

### Fixed

- **Bottom-up TAM math error.** The worked example in `startup-application-coach` said 749,404 restaurants at $1,200/year is "roughly $749.4M". The correct product is roughly $899M. Fixed in `references/bottom-up-tam.md` and `references/questions.md`; `pitch-deck-coach`'s copy of the example already had the right figure.
- **Fabricated facts about real companies in example bios.** The strong team-slide and team-answer examples credited "Jordan" with roles at Stripe and Brex, including a Brex acquisition in 2018 that never happened. Both examples now use clearly fictional companies, with a note that real answers should name real, verifiable employers. Fixed in `pitch-deck-coach/references/slide-by-slide.md` and `startup-application-coach/references/questions.md`.
- **Broken repo links in the Claude.ai template.** `claude-ai-project-instructions-template.md` linked to `betahope/cofounder-team`; the repo is `betahope/founding-team`. Both links 404'd.
- **Logo self-contradiction in the design reference.** `design-principles.md` told founders to put the logo on every slide in one section and called that an amateur mistake in another. Resolved to the cover-only rule, matching the skill's red-flag list.
- **Short live pitches now carry the vision beat.** The skill makes vision non-negotiable at every length, but the 1-minute, 3-minute, 5-minute, and 10-minute structures in `deck-types.md` never mentioned it. Each length now says where vision goes.
- **Demo day length corrected.** `audience-asks.md` and `deck-types.md` stated demo days are "usually 3 minutes". Formats vary by program (YC about 1 minute, Techstars about 5); both files now say so and tell founders to confirm with the program.
- **Wrong relative links between reference files.** Files inside `references/` linked to siblings as `references/<file>.md`, which resolves nowhere from there. Now plain sibling filenames, per the Agent Skills spec's file-reference guidance. Fixed in `pitch-deck-coach/references/slide-by-slide.md`, `startup-application-coach/references/questions.md`, and `references/program-specific.md`.
- **Grammar in Jack, Maya, and Priya's descriptions.** "keep things as simple" is now "keeps things as simple" in all three frontmatter descriptions, the text every user sees in their skills list.
- **The humanizer no longer uses em dashes in its own prose.** The skill that flags em-dash overuse (and the repo that bans em dashes) was full of them, including one in a recommended "After" rewrite. Instructional prose in `humanizer/SKILL.md`, `references/patterns.md`, `references/voice-calibration.md`, and `references/example.md` is now em-dash-free; quoted example text that demonstrates AI tells keeps them on purpose.

### Changed

- **Dan's copy delivery is now flavor-aware.** The rule to save final copy to `./drafts/<slug>.md` is Claude Code only; the portable build (Claude.ai, ChatGPT, and other Agent Skills tools) now instead asks for final copy in a clearly separated Markdown block, with no dependence on file paths. Previously the portable build shipped a filesystem instruction that cannot work there.
- **Persona section order unified.** Maya, Priya, and Dan now place "How you talk" before the humanizer section, matching Jack and the canonical shape documented in `CLAUDE.md`. No wording changed; sections moved only.

## [0.11.2] - 2026-07-21

### Added

- **`.gstack/` in `.gitignore`.** Local gstack developer tooling creates this folder inside the repo; it is machine-local state and never part of the bundle, so git now ignores it.

## [0.11.1] - 2026-07-21

Makes the multi-tool story concrete: a hands-on tested ChatGPT install path in the README, and the internal build flavor renamed to match what it really is.

### Added

- **"Install in ChatGPT" section in `README.md`.** ChatGPT supports the Agent Skills standard, and we verified our zips there by hand: open **Plugins** in the sidebar, switch to the **Skills** tab (or go to chatgpt.com/skills), click **+**, choose **Upload from your computer**. Upgrading is re-download and re-upload, the same as on Claude.ai.
- **"Install in other tools" section in `README.md`.** Covers Cursor, OpenAI Codex, GitHub Copilot, Gemini CLI, and other Agent Skills tools, with honest expectations: we test on Claude and ChatGPT, elsewhere the skills are expected to work rather than guaranteed.

### Changed

- **Renamed the `claude-ai` build flavor to `portable`.** The words-only build now lives at `dist/portable/` and the directive is `{{FLAVOR:portable}}`, since the release zips ship to Claude.ai, ChatGPT, and any other Agent Skills tool, not just the Claude website. Internal only: zip names, install steps, and installed skills are unchanged. `build`, the release workflow, and `CLAUDE.md` were updated together; no source skill used the old directive.
- **README reframed as multi-tool.** New tagline, install intro, and a slimmer "Built on an open standard" section that points at the install paths instead of repeating them.

## [0.11.0] - 2026-07-21

Aligns the skill bundle with the Agent Skills spec (https://agentskills.io/specification), the open standard shared by Claude Code, Claude.ai, and other tools.

### Added

- **Spec-compliant frontmatter.** Every skill's frontmatter now carries `license: MIT` and a `metadata` block (`author: betahope`, `bundle-version`). The build reads the version from the `VERSION` file through a new built-in `{{var:BUNDLE_VERSION}}` directive, so a release zip identifies which bundle version it came from.
- **`compatibility` field on `cofounder-team-upgrade`.** Marks it Claude Code only, since it needs git and a local clone. This is the spec's intended use of that field.
- **CI validation gate.** The release workflow now validates every built skill, in both flavors, with the official `skills-ref` validator right after building and before zipping, so an off-spec skill can never ship.
- **"Built on an open standard" section in `README.md`.** The intro now calls the bundle portable Agent Skills, and the new section explains that release zips are plain Agent Skills folders that work in any tool supporting the standard (Cursor, OpenAI Codex, GitHub Copilot, Gemini CLI, and others), not just Claude Code and Claude.ai.
- **Docs.** `CLAUDE.md` documents the built-in `{{var:BUNDLE_VERSION}}` directive, the spec's allowed frontmatter fields, and where the humanizer version now lives.

### Changed

- **`humanizer` frontmatter, made spec-compliant.** The top-level `version: 3.0.0` field, not allowed by the spec and the one thing that failed the official validator, moved to `metadata.version`. `allowed-tools` changed from a YAML list to the spec's space-separated string. The `compatibility` field was dropped, since the skill is words-only and runs anywhere. The description was rewritten without em dashes.
- **Dan's description trimmed.** Down from exactly 1024 characters, the spec's hard limit, to 981, keeping every trigger keyword.

## [0.10.0] - 2026-07-15

Turns the bundle from single-source prose into a source that compiles into two builds, and lands four skill improvements drawn from Paul Bakaus's "The Dark Arts of Skill Engineering." The install and upgrade flow is unchanged for users: still "clone and run setup," and an upgrade still needs no extra action.

### Added

- **A build step (`build`).** Plain bash, no dependencies, runs on macOS's bash 3.2. It compiles each source `SKILL.md` into two flavors: `dist/claude-code/` (the full version, with the Claude-Code-only extras) and `dist/claude-ai/` (a safe, words-and-references-only version for the website). `setup` runs it automatically before linking, and the release workflow runs it before zipping. Supports `{{include}}`, `{{set}}`/`{{var:}}`, and `{{FLAVOR:...}}` directives. This is what lets local-only features ship to Claude Code without ever reaching (or breaking) the Claude.ai build. See "The build system" in `CLAUDE.md`.
- **Shared persona snippets (`shared/persona/`).** The four personas (Jack, Maya, Priya, Dan) now share the co-founder intro, the humanizer workflow steps, and the non-English rule from single files instead of four copies each. Editing the humanizer contract for all four personas is now a one-file change.
- **A "show your work" step in the humanizer pass.** Across all four personas and both coaches, the mandatory humanizer pass now requires naming, in one short line, the AI tells that were found and fixed (or stating none were). That one line is the proof the pass actually ran, which makes the gate much harder for a weaker model to silently skip. Reinforced by a matching item in each coach's final checklist.
- **An optional Claude Code hook (`hooks/humanizer-slop-check/`).** Opt-in, off by default, never installed by `setup`. When a user turns it on, it scans text files after they are written for obvious AI tells and nudges Claude to run the humanizer. It is a heuristic backstop for the case where nobody invoked the humanizer at all. Claude Code only; absent on Claude.ai. See `hooks/README.md`.
- **Cross-session memory for the two coaches (Claude Code only).** `pitch-deck-coach` and `startup-application-coach` now keep a short snapshot per deck or application under `./.cofounder-team/` so a later session picks up where the last left off (the score, the open issues, the standout fact) instead of starting cold. Wrapped in a `{{FLAVOR:claude-code}}` block, so the Claude.ai build does not carry a feature the website cannot support.

### Changed

- **Creative guidance shifts from bans to divergence.** Priya gains a "diverge before you narrow" principle: for creative work, generate several genuinely different options and keep the most distinct, rather than only avoiding the obvious. The pitch-deck palette guidance now offers the founder two or three distinct palette options instead of one default.
- **`setup`, `uninstall`, the release workflow, and `cofounder-team-upgrade`** all now work through the build. `setup` builds then links `dist/claude-code/`; the release workflow builds then zips `dist/claude-ai/`; the upgrade re-links each installed skill at the freshly built version (so users who installed before the build step existed are repointed automatically).
- **Docs updated** (`CLAUDE.md` and `README.md`) to describe the build system, the two flavors, the templating directives, and the golden rule that local-only features must live inside a `{{FLAVOR:claude-code}}` block so the Claude.ai build stays safe.

## [0.9.0] - 2026-06-19

### Changed

- Rebranded the bundle's user-facing name to **The Founding Team**. The README heading and tagline now read "The Founding Team / Your AI founding team, inside Claude." The GitHub repository was renamed from `cofounder-team` to `founding-team`; the clone and release links in the README point at the new URL (GitHub redirects the old one, so existing clones keep pulling). Internal names users depend on are unchanged: the local clone folder stays `~/.cofounder-team`, the upgrade command stays `/cofounder-team-upgrade`, and the Windows `.cofounder-team` sentinel is untouched, so existing installs upgrade with zero action needed.

## [0.8.1] - 2026-06-17

### Changed

- Polished wording in `claude-ai-project-instructions-template.md` and restructured its "Quick Context" section into explicit per-line prompts (the problem, who the customers are, the proposed solution, where the team is based) so founders filling out the template know exactly what to write in each line.

## [0.8.0] - 2026-06-09

### Added

- `startup-application-coach` gained depth on the two questions that sink the most applications, plus a portable assemble step. Adapted from Andres Barreto's published Techstars Application Guide and his Techstars-only skill, generalised to apply across programs and matched to this bundle's voice. The coach stays multi-program (YC, Techstars, a16z Speedrun); this enriches it rather than narrowing it.
  - **`references/bottom-up-tam.md`** — the full bottom-up TAM method (define and count the buyer from real data, set a realistic ACV, segment buyers that pay differently, multiply, sanity-check against a top-down figure), a worked example, the common fatal mistakes, and an optional offer to research the buyer count and price via web search when the environment supports it.
  - **`references/moats.md`** — honest competitive-advantage coaching: the data-moat fallacy and how to pressure-test it, the real durable defensibilities, the chokepoint and workflow-embedding lens for early software, killing the three false moats ("proprietary data," "AI," "first-mover"), and an optional offer to research the customer's workflow chokepoints.
  - **Techstars character limits and structured fields** in `references/program-specific.md` — the per-question character caps the form enforces, and the note that revenue and funding are entered as structured tables rather than prose (so the traction box is for non-revenue signal).
  - **A Markdown assemble step** in `SKILL.md` — once answers are in good shape, the coach can assemble them into a single Markdown document (company header, each question as a heading with its answer, a character count next to each answer where the program enforces a limit). Markdown is the only output format, chosen because it works identically in Claude Code and Claude.ai and the founder can copy it into a doc, a file, or the portal themselves.
  - **An offer to research the hard numbers** — on the market-size and competitive-advantage questions, the coach offers to web-research the inputs (buyer count and price; customer chokepoints) and build the answer from cited figures the founder can correct, degrading gracefully when web search is unavailable.
  - Cross-references added in `questions.md` and `program-specific.md` pointing to the two new reference files at the relevant questions.

### Changed

- Optimised the `README.md` Credits section. Consolidated to one paragraph per skill (the `pitch-deck-coach` and `startup-application-coach` were each described twice with overlapping content), and added a direct link to Andres Barreto's open-source skill repository at [github.com/andresbarreto-techstars/techstars-application-coach-skill](https://github.com/andresbarreto-techstars/techstars-application-coach-skill) to credit the source of the new bottom-up TAM, moat, and Techstars-specific material.

## [0.7.0] - 2026-06-06

### Added

- A "Credits" section in `README.md` attributing the bundle to Charles Hope at Your Startup Advisor, crediting Kevin Hale for the pitch-deck design guidance and Paul Graham, Dalton Caldwell, Andres Barreto, and a16z Speedrun for the application guidance, and crediting the bundled `humanizer` skill to blader ([github.com/blader/humanizer](https://github.com/blader/humanizer), MIT License) and its underlying Wikipedia "Signs of AI writing" source. Docs only, no skill behavior change.

## [0.6.1] - 2026-06-06

### Changed

- Added a "How the team works together" section to `README.md` that makes the team contract explicit at the front door: each co-founder knows the others, knows the edge of its own expertise, and pulls in the right person instead of guessing or bluffing. The behavior was already encoded in every persona's Boundaries section and in the Claude.ai project template; this surfaces it in the README, which previously only hinted at it in one line. Docs only, no skill behavior change.

## [0.6.0] - 2026-05-25

### Changed

- Bumped release workflow actions to Node 24 compatible majors: `actions/checkout@v4` → `@v6`, and `softprops/action-gh-release@v2` → `@v3`. Resolves the deprecation warning flagged in the v0.4.2 notes ahead of GitHub's 2026-06-02 Node 24 default and 2026-09-16 Node 20 removal deadlines. No change to the produced release zips or to either action's input surface.
- Restructured `claude-ai-project-instructions-template.md` so the paste-ready section is wrapped in a fenced code block. On GitHub's rendered view, this gives non-technical users a one-click copy button that captures the raw markdown verbatim, instead of asking them to figure out how to copy unrendered markdown out of a rendered page. The "How to use this" intro was rewritten around the copy button, and a fallback link to the raw file is included for environments where the copy button is unavailable. Template content is unchanged.

## [0.5.0] - 2026-05-25

### Added

- Claude.ai project instructions template (`claude-ai-project-instructions-template.md`) for founders using the skills inside a Claude.ai project. Covers routing between the four co-founders, the "one turn, multiple voices" rule, and project-level defaults.

## [0.4.2] - 2026-05-24

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
