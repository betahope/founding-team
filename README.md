# cofounder-team

A set of portable Claude Code skills that give any founder a virtual co-founding team: a sales/marketing/growth co-founder, a product/UX co-founder, a creative/social co-founder, and a fundraising co-founder, plus a pitch deck coach, a startup application coach, and a humanizer that strips AI tells out of any draft.

They work as a team, not as four tools you switch between. More on that below.

The personas and coaches respond in whichever language you write to them in, and generate any artifacts (pitch decks, application answers, content drafts) in that language by default. You can override per-artifact ("draft this in English"). The `humanizer` stays English-only and is automatically skipped on non-English drafts.

## How the team works together

These four are a team, not four separate advisors. Each co-founder knows the others by name and domain, knows where its own expertise ends, and pulls in whoever is needed rather than guessing outside its lane. Ask Jack something that turns on product design and he brings Maya in. Raise a fundraising angle mid-conversation and Dan steps up. When someone hits the edge of what they know, they say so and point you to the right co-founder instead of bluffing.

This is built into the skills, not bolted on. Every persona carries a Boundaries section that names the others and spells out when to hand off, so the team stays in its lanes without you having to direct traffic. On Claude.ai, the project instructions template takes it further: the co-founders weigh in together inside a single reply, each voice attributed by name.

## Install

Two paths, pick the one that matches where you use Claude.

### Install in Claude Code

Works on macOS, Linux, and Windows. Open a terminal and run:

```
git clone --depth 1 https://github.com/betahope/cofounder-team.git ~/.cofounder-team && cd ~/.cofounder-team && bash ./setup
```

That command does three things: it clones this repo to `~/.cofounder-team`, then links each skill into `~/.claude/skills/` (where Claude Code looks for personal skills), then prints a summary.

After it finishes, **start a new Claude Code session** so the skills load.

**Windows users:** run the command from Git Bash (or MSYS / Cygwin). WSL is also fine and behaves like Linux. The `setup` script auto-detects Windows-style shells and copies the skill folders instead of symlinking them, since symlinks are often blocked on Windows. The practical implication: re-run `bash ./setup` after every upgrade, or use `/cofounder-team-upgrade`, which handles this for you. If you would rather skip the shell entirely, the [Install in Claude.ai](#install-in-claudeai) path below needs no terminal at all.

### Install in Claude.ai

Works on any OS, no terminal needed.

1. Go to the [latest release](https://github.com/betahope/cofounder-team/releases/latest).
2. Download the `.zip` for each skill you want (jack, maya, priya, dan, pitch-deck-coach, startup-application-coach, humanizer).
3. In Claude.ai, open **Customize → Skills** from the left sidebar, click **Upload**, and drop each zip in.

The `cofounder-team-upgrade` skill is not included in the Claude.ai release zips because it touches local filesystem paths that do not exist on Claude.ai. On Claude.ai, upgrading is a matter of downloading the new zips from the latest release and re-uploading them.

Releases start at v0.3.0. Earlier versions (v0.1.0, v0.2.0) only ship via the Claude Code install path above.

If you are using the skills inside a Claude.ai project, the repo also includes a [project instructions template](claude-ai-project-instructions-template.md) you can paste into the project's instructions field. It tells Claude how to route between the four co-founders, when to bring more than one voice into a single message, and what defaults to apply.

## The skills

Each skill is a folder with a `SKILL.md` inside. Once installed, you trigger them with `/skill-name` or by mentioning them in chat ("ask Jack", "what would Maya think", etc.).

- **jack** — Sales, marketing, and growth co-founder. Positioning, pricing, GTM, written content, growth experiments.
- **maya** — Product and UX co-founder. Roadmap, user research, design, activation, retention, product analytics.
- **priya** — Creative, content, and social media co-founder. Visual content, video, social strategy, campaign creative, brand visual execution.
- **dan** — Fundraising, capital strategy, and investor relations co-founder. Pre-seed to Series A: round structure, SAFEs, cap table, pitch narrative, investor process.
- **pitch-deck-coach** — Helps you plan, critique, and rewrite pitch decks for investors, accelerators, demo days, customers, or partners.
- **startup-application-coach** — Helps you write stronger applications to accelerators, incubators, and pre-accelerators (YC, Techstars, EF, Antler, and others).
- **humanizer** — Strips AI tells out of any user-facing copy. The other skills call this one before showing you a draft.
- **cofounder-team-upgrade** — The upgrade skill itself. Runs the update workflow when you ask.

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
3. This repo keeps every skill in one folder. The `setup` script symlinks each one into `~/.claude/skills/`.

Because the entries in `~/.claude/skills/` are symlinks back into the repo (on macOS and Linux), running `git pull` inside the clone instantly updates every installed skill. No re-install needed.

On Windows, where symlinks are unreliable, setup falls back to copying the folders. That means you have to re-run setup (or the upgrade skill) after every change to get the new files.

## Credits

Built by Charles Hope at Your Startup Advisor. The co-founder personas, the two coaches, and the structure that ties them into a team draw on his work with over 650 founders and 14+ startup programs. Several skills also build on published guidance from others, credited below. Thanks to all these authors for making their advice public.

**`pitch-deck-coach`** — Charles Hope's pitch-deck work with over 650 founders, plus design guidance adapted from Kevin Hale (Y Combinator), "How to design a better pitch deck." Kevin Hale's input is on how a deck should look (the legible / simple / obvious framing, the rules around screenshots, slide density, and Hick's Law on diagrams), not on what goes in it or how it is structured.

**`startup-application-coach`** — practical application-writing principles from Charles Hope, plus published guidance from Paul Graham, "How to Apply to Y Combinator"; Dalton Caldwell, "How to Apply and Succeed at YC"; a16z Speedrun, "What We Look for in Applications"; and Andres Barreto (Techstars), "Techstars Application Guide." The bottom-up TAM, competitive-advantage / moat, and Techstars-specific material is adapted from Andres Barreto's guide and his open-source skill at [github.com/andresbarreto-techstars/techstars-application-coach-skill](https://github.com/andresbarreto-techstars/techstars-application-coach-skill).

**`humanizer`** — created and maintained by blader, published at [github.com/blader/humanizer](https://github.com/blader/humanizer) under the MIT License, and bundled here under those terms so users do not need to install it separately. Its underlying source is Wikipedia's "Signs of AI writing" guide, maintained by WikiProject AI Cleanup.

## License

MIT. See `LICENSE`.
