# The Co-Founder Team

*Your AI co-founder team, wherever you work: Claude, ChatGPT, and any tool that supports Agent Skills.*

A set of portable [Agent Skills](https://agentskills.io) that give any founder a virtual co-founding team: a sales/marketing/growth co-founder, a product/UX co-founder, a creative/social co-founder, and a fundraising co-founder, plus a pitch deck coach, a startup application coach, and a humanizer that strips AI tells out of any draft.

They work as a team, not as four tools you switch between. More on that below.

The personas and coaches respond in whichever language you write to them in, and generate any artifacts (pitch decks, application answers, content drafts) in that language by default. You can override per-artifact ("draft this in English"). The `humanizer` runs in full on English drafts; on other languages it does a lighter structural-only pass, since its wording patterns are English-specific.

## How the team works together

These four are a team, not four separate advisors. Each co-founder knows the others by name and domain, knows where its own expertise ends, and pulls in whoever is needed rather than guessing outside its lane. Ask Jack something that turns on product design and he brings Maya in. Raise a fundraising angle mid-conversation and Dan steps up. When someone hits the edge of what they know, they say so and point you to the right co-founder instead of bluffing.

This is built into the skills, not bolted on. Every persona carries a Boundaries section that names the others and spells out when to hand off, so the team stays in its lanes without you having to direct traffic. And when a question deserves more than one voice, the `team` skill convenes them: say "ask the team" (or `/team` in Claude Code) and the right co-founders answer together in a single reply, each voice attributed by name, ending in one clear recommendation. On Claude.ai, the project instructions template adds the same behavior at the project level.

## Install

Pick the path that matches where you work.

### Install in Claude Code

Works on macOS, Linux, and Windows. Open a terminal and run:

```
git clone --depth 1 https://github.com/betahope/cofounder-team.git ~/.cofounder-team && cd ~/.cofounder-team && bash ./setup
```

That command does three things: it clones this repo to `~/.cofounder-team`, then builds the skills and links each one into `~/.claude/skills/` (where Claude Code looks for personal skills), then prints a summary. The build is plain bash and needs nothing extra installed.

After it finishes, **start a new Claude Code session** so the skills load.

**Windows users:** run the command from Git Bash (or MSYS / Cygwin). WSL is also fine and behaves like Linux. The `setup` script auto-detects Windows-style shells and copies the skill folders instead of symlinking them, since symlinks are often blocked on Windows. The practical implication: re-run `bash ./setup` after every upgrade, or use `/cofounder-team-upgrade`, which handles this for you. If you would rather skip the shell entirely, the [Install in Claude.ai](#install-in-claudeai) path below needs no terminal at all.

### Install in Claude.ai

Works on any OS, no terminal needed.

1. Go to the [latest release](https://github.com/betahope/cofounder-team/releases/latest).
2. Download the `.zip` for each skill you want (jack, maya, priya, dan, team, pitch-deck-coach, startup-application-coach, humanizer).
3. In Claude.ai, open **Customize → Skills** from the left sidebar, click **Upload**, and drop each zip in.

The `cofounder-team-upgrade` skill is not included in the Claude.ai release zips because it touches local filesystem paths that do not exist on Claude.ai. On Claude.ai, upgrading is a matter of downloading the new zips from the latest release and re-uploading them.

Releases start at v0.3.0. Earlier versions (v0.1.0, v0.2.0) only ship via the Claude Code install path above.

If you are using the skills inside a Claude.ai project, the repo also includes a [project instructions template](claude-ai-project-instructions-template.md) you can paste into the project's instructions field. It tells Claude how to route between the four co-founders, when to bring more than one voice into a single message, and what defaults to apply.

### Install in ChatGPT

ChatGPT supports the same Agent Skills standard, so the release zips work there too. Tested with this bundle.

1. Go to the [latest release](https://github.com/betahope/cofounder-team/releases/latest) and download the `.zip` for each skill you want.
2. In ChatGPT, open **Plugins** in the sidebar and switch to the **Skills** tab, or go straight to [chatgpt.com/skills](https://chatgpt.com/skills).
3. Click the **+** button, choose **Upload from your computer**, and pick a zip. ChatGPT scans each skill on upload and it becomes available right after.

To upgrade later, download the newer zips and upload them again, the same as on Claude.ai. The `cofounder-team-upgrade` skill is Claude Code only and is not part of the zips.

### Install in other tools

Cursor, OpenAI Codex, GitHub Copilot, Gemini CLI, and dozens of other tools also support Agent Skills. Download the zips from the [latest release](https://github.com/betahope/cofounder-team/releases/latest), unzip them, and put each skill folder where your tool keeps skills (its docs will say where, and [agentskills.io](https://agentskills.io) links each tool's setup guide). We build and test on Claude and ChatGPT, so in other tools treat the skills as expected to work rather than guaranteed. If one misbehaves, [open an issue](https://github.com/betahope/cofounder-team/issues).

## The skills

Each skill is a folder with a `SKILL.md` inside. Once installed, trigger them by mentioning them ("ask Jack", "what would Maya think"). In Claude Code you can also type `/skill-name`.

- **jack** — Sales, marketing, and growth co-founder. Positioning, pricing, GTM, written content, growth experiments.
- **maya** — Product and UX co-founder. Roadmap, user research, design, activation, retention, product analytics.
- **priya** — Creative, content, and social media co-founder. Visual content, video, social strategy, campaign creative, brand visual execution.
- **dan** — Fundraising, capital strategy, and investor relations co-founder. Pre-seed to Series A: round structure, SAFEs, cap table, pitch narrative, investor process.
- **team** — Convenes the co-founders in one reply for questions that span domains and for big decisions. Each voice named, one recommendation at the end.
- **pitch-deck-coach** — Helps you plan, critique, and rewrite pitch decks for investors, accelerators, demo days, customers, or partners.
- **startup-application-coach** — Helps you write stronger applications to accelerators, incubators, and pre-accelerators (YC, Techstars, EF, Antler, and others).
- **humanizer** — Strips AI tells out of any user-facing copy. The other skills call this one before showing you a draft. Its pattern catalog is [blader's humanizer](https://github.com/blader/humanizer), vendored here unchanged and re-synced automatically, so upgrading the bundle also gets you the latest patterns.
- **cofounder-team-upgrade** — The upgrade skill itself. Runs the update workflow when you ask.

## Built on an open standard

Every skill here follows the [Agent Skills](https://agentskills.io) format, an open standard started by Anthropic and now supported by dozens of AI tools. That is why the same release zips install cleanly in Claude, ChatGPT, and other tools, with nothing Claude-specific inside. See the [Install](#install) section above for the path that matches your tool.

## Upgrade

### Upgrade in Claude Code

Inside any Claude Code session, run:

```
/cofounder-team-upgrade
```

…or just ask in plain English: "upgrade cofounder-team" or "update my cofounder skills". Claude will pull the latest version from GitHub, re-link any new skills, show you the curated changelog of what shipped, and remind you to start a new session.

**Windows users:** if you installed via Git Bash, setup copied the skill folders instead of linking them (Windows blocks symlinks in many setups). That means an upgrade has to re-copy the latest files. The upgrade skill handles this automatically, just re-run it whenever you want the newest version.

### Upgrade in Claude.ai

Claude.ai has no in-app upgrade flow for personal skills. To get the newest version:

1. Go to the [latest release](https://github.com/betahope/cofounder-team/releases/latest) and check the version number against what you have installed.
2. Download the updated zips and re-upload them in **Customize → Skills** (in the left sidebar). Claude.ai will replace the existing skill of the same name.
3. The release notes on each release list what changed, pulled from `CHANGELOG.md`.

## Uninstall

The uninstall script applies to Claude Code installs only.

To remove the skills from `~/.claude/skills/` without deleting the clone:

```
bash ~/.cofounder-team/uninstall
```

The uninstall script only removes links (or copies on Windows) that this repo created. It will not touch any unrelated skill that happens to share a name.

To remove the clone itself as well:

```
rm -rf ~/.cofounder-team
```

On Claude.ai, remove skills individually under **Customize → Skills** in the left sidebar.

## How it works under the hood

Three facts make the whole thing work:

1. A Claude Code skill is just a folder with a `SKILL.md` file in it.
2. Claude Code looks for personal skills in `~/.claude/skills/`.
3. `setup` compiles the source skills into finished skills under `dist/claude-code/`, then symlinks each one into `~/.claude/skills/`.

There is a small build step because the same source ships to two places: Claude Code (which can run the local-only extras like hooks and cross-session memory) and Claude.ai (which gets a simpler, words-only version). The build is plain bash, so "clone and run setup" is all you do.

Because the entries in `~/.claude/skills/` are symlinks into the build (on macOS and Linux), an upgrade rebuilds and re-links in one step. After a `git pull`, run `bash ./setup` again (or use `/cofounder-team-upgrade`, which does it for you) so the latest source is rebuilt. A bare `git pull` on its own updates the source but not the built skill.

On Windows, where symlinks are unreliable, setup falls back to copying the folders. Either way, re-run setup (or the upgrade skill) after a pull to get the new files.

## Credits

Built by Charles Hope at Your Startup Advisor. The co-founder personas, the two coaches, and the structure that ties them into a team draw on his work with over 650 founders and 14+ startup programs. Several skills also build on published guidance from others, credited below. Thanks to all these authors for making their advice public.

**`pitch-deck-coach`** — Charles Hope's pitch-deck work with over 650 founders, plus design guidance adapted from Kevin Hale (Y Combinator), "How to design a better pitch deck." Kevin Hale's input is on how a deck should look (the legible / simple / obvious framing, the rules around screenshots, slide density, and Hick's Law on diagrams), not on what goes in it or how it is structured.

**`startup-application-coach`** — practical application-writing principles from Charles Hope, plus published guidance from Paul Graham, "How to Apply to Y Combinator"; Dalton Caldwell, "How to Apply and Succeed at YC"; a16z Speedrun, "What We Look for in Applications"; and Andres Barreto (Techstars), "Techstars Application Guide." The bottom-up TAM, competitive-advantage / moat, and Techstars-specific material is adapted from Andres Barreto's guide and his open-source skill at [github.com/andresbarreto-techstars/techstars-application-coach-skill](https://github.com/andresbarreto-techstars/techstars-application-coach-skill).

**`humanizer`** — created and maintained by blader, published at [github.com/blader/humanizer](https://github.com/blader/humanizer) under the MIT License, and bundled here under those terms so users do not need to install it separately. blader's pattern catalog ships unmodified as `humanizer/references/upstream-patterns.md`; our `SKILL.md` adds only the workflow, output sizing, non-English rule, and voice guidance on top. A weekly job re-syncs the catalog whenever blader publishes a new version. Its underlying source is Wikipedia's "Signs of AI writing" guide, maintained by WikiProject AI Cleanup.

## License

MIT. See `LICENSE`.
