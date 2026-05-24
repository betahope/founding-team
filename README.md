# cofounder-team

A set of portable Claude Code skills that give any founder a virtual co-founding team: a sales/marketing/growth co-founder, a product/UX co-founder, a creative/social co-founder, and a fundraising co-founder, plus a pitch deck coach, a startup application coach, and a humanizer that strips AI tells out of any draft.

The skills know about each other. When the conversation moves outside their lane, they hand off cleanly.

## Install

Open a terminal on macOS or Linux and run:

```
git clone --depth 1 https://github.com/betahope/cofounder-team.git ~/.cofounder-team && cd ~/.cofounder-team && bash ./setup
```

That command does three things: it clones this repo to `~/.cofounder-team`, then links each skill into `~/.claude/skills/` (where Claude Code looks for personal skills), then prints a summary.

After it finishes, **start a new Claude Code session** so the skills load.

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

Inside any Claude Code session, run:

```
/cofounder-team-upgrade
```

…or just ask in plain English: "upgrade cofounder-team" or "update my cofounder skills". Claude will pull the latest version from GitHub, re-link any new skills, and show you what changed.

Then start a new Claude Code session so the updated skills load.

**Windows users:** if you installed via Git Bash, setup copied the skill folders instead of linking them (Windows blocks symlinks in many setups). That means an upgrade has to re-copy the latest files. The upgrade skill handles this automatically — just re-run it whenever you want the newest version.

## Uninstall

To remove the skills from `~/.claude/skills/` without deleting the clone:

```
bash ~/.cofounder-team/uninstall
```

The uninstall script only removes links (or copies on Windows) that this repo created. It will not touch any unrelated skill that happens to share a name.

To remove the clone itself as well:

```
rm -rf ~/.cofounder-team
```

## How it works under the hood

Three facts make the whole thing work:

1. A Claude Code skill is just a folder with a `SKILL.md` file in it.
2. Claude Code looks for personal skills in `~/.claude/skills/`.
3. This repo keeps every skill in one folder. The `setup` script symlinks each one into `~/.claude/skills/`.

Because the entries in `~/.claude/skills/` are symlinks back into the repo (on macOS and Linux), running `git pull` inside the clone instantly updates every installed skill. No re-install needed.

On Windows, where symlinks are unreliable, setup falls back to copying the folders. That means you have to re-run setup (or the upgrade skill) after every change to get the new files.

## License

MIT. See `LICENSE`.
