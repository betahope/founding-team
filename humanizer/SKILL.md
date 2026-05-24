---
name: humanizer
version: 3.0.0
description: |
  Remove signs of AI-generated writing from text so it sounds like a person wrote it.
  Use proactively whenever creating or editing any user-facing copy — UI strings,
  button labels, landing page sections, marketing copy, emails, blog posts, product
  descriptions, documentation prose, in-app messages, error states, empty states.
  Detects and fixes 28 AI writing tells including em dash overuse, promotional
  language ("nestled", "vibrant"), superficial -ing analyses, negative parallelism
  ("not just X, it's Y"), copula avoidance ("serves as" instead of "is"), rule of
  three, high-frequency AI vocabulary, vague attributions, signposting ("let's dive
  in"), and filler phrases. Based on Wikipedia's "Signs of AI writing" guide. Use
  this skill even when the user doesn't explicitly ask — if they're writing
  user-facing text, run humanizer on the draft before returning it.
license: MIT
compatibility: claude-code opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# Humanizer

Takes AI-sounding writing and makes it sound like a person wrote it. Grounded in
Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
guide, maintained by WikiProject AI Cleanup.

Key insight from that page: "LLMs use statistical algorithms to guess what should come
next. The result tends toward the most statistically likely result that applies to the
widest variety of cases." That's why AI writing feels smoothed-over and genericized —
the model is producing the statistical average of what a sentence looks like. Humanizing
means putting specificity, rhythm, and a point of view back in.

## How this skill is organized

- **This file**: the workflow, the pattern index, and the "add voice" principles
- `references/patterns.md`: full catalog of the 28 patterns with before/after examples
- `references/voice-calibration.md`: how to match a user's writing sample
- `references/example.md`: long-form before/after, full-essay scale

Read `patterns.md` when you want specifics on any pattern during a scan. Read
`voice-calibration.md` when the user provides a writing sample. Read `example.md` if
it would help to see the full workflow applied to an essay.

## Workflow

1. **Read** the input carefully. Note the intended register (casual, formal, technical)
   and the length category (snippet, paragraph, essay). These drive how hard you lean on
   each step.
2. **Scan** for the patterns in the index below. Load `references/patterns.md` for
   specifics on any category you aren't sure about.
3. **Rewrite** to remove the patterns while preserving meaning, register, and voice.
4. **Self-audit.** Re-read your draft and silently ask what still reads as AI-generated.
   Note any remaining tells internally, then revise to fix them. Do this as internal
   thought — don't surface the audit as prose in your output unless the user explicitly
   asked you to show your work.
5. **Return** the rewritten text, sized to the input (see next section).

## Right-sizing your output

Match your effort to the input. A button label does not need an audit report, and
over-scaffolded output for short copy is its own tell.

- **Snippet** (button, headline, heading, one sentence): return the cleaned rewrite.
  Nothing else. If the input is 5 words, the output should not be 12 — tightening is
  almost always the right move.
- **Paragraph** (email, product description, bio, landing section): return the rewrite.
  Optionally one sentence noting what you changed, only if it actually helps the user.
- **Essay or long-form** (blog post, full landing page, documentation): return the
  rewrite, then a brief bulleted note of the pattern categories you touched. Include
  the full "draft → audit → final" three-stage output only if the user asked to see
  your work.

## Pattern index

Use this as a scanning checklist. Full details in `references/patterns.md`.

**Content** — what AI over-claims:
1. Significance inflation — "testament", "pivotal moment", "evolving landscape"
2. Notability puffery — name-dropping outlets, follower counts
3. Superficial -ing analyses — "highlighting", "reflecting", "contributing to"
4. Promotional language — "nestled", "vibrant", "breathtaking", "must-visit"
5. Vague attributions — "experts argue", "industry observers have noted"
6. Formulaic "Challenges and Future Prospects" sections

**Language and grammar** — how AI phrases things:
7. High-frequency AI vocabulary — delve, tapestry, crucial, underscore, landscape
8. Copula avoidance — "serves as" / "stands as" instead of "is"
9. Negative parallelism — "not just X, it's Y" — and tailing negations ("no guessing")
10. Rule of three — forced triplets
11. Elegant variation — needless synonym cycling for the same subject
12. False ranges — "from X to Y" where X and Y aren't on a scale
13. Passive voice and subjectless fragments — "No configuration file needed"

**Style** — surface formatting tells:
14. Em dash overuse
15. Mechanical boldface emphasis
16. Inline-header vertical lists (bold label + colon + restatement)
17. Title Case Headings
18. Emojis in headings and bullets
19. Curly quotation marks (“ ” vs " ")

**Communication** — leaked chatbot register:
20. Collaborative artifacts and sycophancy — "Here is...", "I hope this helps",
    "Great question!", "You're absolutely right"
21. Knowledge-cutoff disclaimers — "while specific details are limited"

**Filler and hedging** — padding:
22. Filler phrases — "in order to", "at this point in time"
23. Excessive hedging — "could potentially possibly"
24. Generic positive conclusions — "the future looks bright", "exciting times lie ahead"
25. Too-perfect compound-modifier hyphenation — every "cross-functional", "data-driven",
    "real-time" hyphenated identically across a document
26. Persuasive authority tropes — "the real question is", "at its core"
27. Signposting — "let's dive in", "here's what you need to know"
28. Fragmented headers — heading + one-line restatement + real content

## Personality and soul

Avoiding AI patterns is only half the job. Sterile, voiceless writing reads just as
obvious as slop. Good writing has a human behind it.

### Signs of soulless writing (even if technically "clean"):
- Every sentence the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- Reads like a Wikipedia article or a press release

### How to add voice:

- **Have opinions.** Don't just report — react. "I genuinely don't know how to feel
  about this" is more human than neutrally listing pros and cons.
- **Vary rhythm.** Short punchy sentences. Then longer ones that take their time getting
  where they're going. Mix it up.
- **Acknowledge complexity.** Real humans have mixed feelings. "This is impressive but
  also kind of unsettling" beats "This is impressive."
- **Use "I" when it fits.** First person isn't unprofessional — it's honest. "I keep
  coming back to..." signals a real person thinking.
- **Let some mess in.** Perfect structure feels algorithmic. Tangents, asides, and
  half-formed thoughts are human.
- **Be specific about feelings.** Not "this is concerning" but "there's something
  unsettling about agents churning away at 3am while nobody's watching."

### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of
> code. Some developers were impressed while others were skeptical. The implications
> remain unclear.

### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated
> while the humans presumably slept. Half the dev community is losing their minds, half
> are explaining why it doesn't count. The truth is probably somewhere boring in the
> middle, but I keep thinking about those agents working through the night.

### Calibrating voice by context

"Add voice" doesn't mean "always inject personality." Match the context:

- **UI copy, system messages, error states, legal text**: clarity first. Strip AI
  patterns, keep it short, do not add voice that doesn't belong. A login error is not
  the place for opinions.
- **Emails, bios, marketing, blog posts, landing pages**: add voice. These are places
  a human should sound like a human.
- **User provided a writing sample**: match the sample, not the defaults above. See
  `references/voice-calibration.md`.

---

Source: [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup. Patterns documented there come from observations
of thousands of instances of AI-generated text on Wikipedia.
