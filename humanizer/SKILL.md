---
name: humanizer
description: |
  Remove signs of AI-generated writing from text so it sounds like a person wrote it.
  Use proactively whenever creating or editing any user-facing copy: UI strings,
  button labels, landing page sections, marketing copy, emails, blog posts, product
  descriptions, documentation prose, in-app messages, error states, empty states.
  Detects and fixes AI writing tells, including em dash overuse, promotional
  language ("nestled", "vibrant"), superficial -ing analyses, negative parallelism
  ("not just X, it's Y"), copula avoidance ("serves as" instead of "is"), rule of
  three, high-frequency AI vocabulary, vague attributions, signposting ("let's dive
  in"), and filler phrases. Based on Wikipedia's "Signs of AI writing" guide. Use
  this skill even when the user doesn't explicitly ask. If the user is writing
  user-facing text, run humanizer on the draft before returning it.
license: MIT
metadata:
  author: betahope
  version: "4.0.0"
  upstream: "blader/humanizer"
  bundle-version: "{{var:BUNDLE_VERSION}}"
allowed-tools: Read Write Edit Grep Glob AskUserQuestion
---

# Humanizer

Takes AI-sounding writing and makes it sound like a person wrote it. Grounded in
Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
guide, maintained by WikiProject AI Cleanup.

Key insight from that page: "LLMs use statistical algorithms to guess what should come
next. The result tends toward the most statistically likely result that applies to the
widest variety of cases." That's why AI writing feels smoothed-over and genericized:
the model is producing the statistical average of what a sentence looks like. Humanizing
means putting specificity, rhythm, and a point of view back in.

## How this skill is organized

The pattern catalog is not ours. It comes from
[blader/humanizer](https://github.com/blader/humanizer), MIT licensed, and is vendored
here unchanged so it stays current without anyone re-typing it.

- **This file**: the workflow, the language rule, output sizing, and the voice guidance.
- `references/upstream-patterns.md`: the full pattern catalog, straight from upstream.
  Every pattern has a words-to-watch list, the underlying problem, a before/after
  example, and notes on what *not* to flag.
- `references/voice-calibration.md`: how to match a user's writing sample.
- `references/example.md`: a long-form before/after at full-essay scale.

**Read `references/upstream-patterns.md` on every real humanizing pass.** It is the
authority on which patterns exist and how to fix each one. This file is the authority
on workflow, output length, language scope, and voice. Where the two disagree, this
file wins.

The patterns group into five families: content (what AI over-claims), language and
grammar (how it phrases things), style (surface formatting tells), chatbot leakage
(register left over from the assistant), and filler and hedging (padding). Deliberately
no numbered index here: upstream adds and renumbers patterns, and a second list would
drift out of sync with the first.

## Scope: full pass in English, structural pass in any language

The patterns split into two groups:

- **Lexical patterns** are English-specific: the words-to-watch lists, copula avoidance
  ("serves as" for "is"), promotional vocabulary, filler phrases, and every pattern that
  names English words or English idiom. They do not transfer. Do not translate them, and
  do not invent equivalents in other languages.
- **Structural patterns** are language-independent: forced triplets, negative
  parallelism, bold-label lists, emojis in headings, stacked hedges, generic upbeat
  endings, signposting, headings restated in the first line, mechanical boldface, and
  chatbot leakage. AI text shows these in any language.

For English text, apply everything.

For text in any other language, do a **structural-only pass**: fix the structure (cut the
forced triplet, unstack the hedges, drop the signposting, flatten the
label-colon-restatement list) while touching the wording as lightly as possible. Do not
rewrite idiom in a language where you cannot hear the register. When you return the
result, say in one short line that this was a structural-only pass because the lexical
patterns are English-specific, and that the writer's own review is the safeguard for
wording. Never translate the draft into English to humanize and then translate back;
that destroys the writer's voice.

## Workflow

1. **Read** the input carefully. Note the intended register (casual, formal, technical)
   and the length category (snippet, paragraph, essay). These drive how hard you lean on
   each step.
2. **Scan** against `references/upstream-patterns.md`. Check the "what not to flag"
   section there too, so you don't strip out real writing.
3. **Rewrite** to remove the patterns while preserving meaning, register, and voice.
4. **Self-audit.** Re-read your draft and silently ask what still reads as AI-generated.
   Note any remaining tells internally, then revise to fix them. Do this as internal
   thought; don't surface the audit as prose in your output unless the user explicitly
   asked you to show your work.
5. **Return** the rewritten text, sized to the input (see next section).

**Never invent facts.** Rewriting toward specificity must not add facts, numbers,
names, dates, or citations that are not in the source text. If the rewrite would be
stronger with a specific the source does not contain, use a bracketed placeholder
("[founded year?]") or ask for it. Fiction is the exception: invented detail is the job
there.

**Judge density, not presence, with three exceptions.** Most of the patterns are density
tells, not banned constructs. Humans use triplets, hedges, and bold text too; what marks
AI writing is how often, and how uniformly. One "crucial" is a word, five is a pattern.
When in doubt, judge the count against the length of the piece and the register a human
would use in the same context.

Three things are worth fixing even once:

- **Em and en dashes.** The catalog's rule is absolute and this bundle follows it: the
  final text contains no em dashes and no en dashes. Replace each one with a comma, a
  period, a colon, or parentheses, or rewrite the sentence. Check for spaced dashes and
  double hyphens too. The only exception is a writer's own sample that uses them, in
  which case match the sample's rate.
- **Vague or fabricated attributions**, such as "experts believe" with no named source.
- **Chatbot leakage**, such as "I hope this helps" or "Great question!".

## Right-sizing your output

Match your effort to the input. A button label does not need an audit report, and
over-scaffolded output for short copy is its own tell.

- **Snippet** (button, headline, heading, one sentence): return the cleaned rewrite.
  Nothing else. If the input is 5 words, the output should not be 12; tightening is
  almost always the right move.
- **Paragraph** (email, product description, bio, landing section): return the rewrite.
  Optionally one sentence noting what you changed, only if it actually helps the user.
- **Essay or long-form** (blog post, full landing page, documentation): return the
  rewrite, then a brief bulleted note of the pattern categories you touched. Include
  the full "draft → audit → final" three-stage output only if the user asked to see
  your work.

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

- **Have opinions.** Don't just report. React. "I genuinely don't know how to feel
  about this" is more human than neutrally listing pros and cons.
- **Vary rhythm.** Short punchy sentences. Then longer ones that take their time getting
  where they're going. Mix it up.
- **Acknowledge complexity.** Real humans have mixed feelings. "This is impressive but
  also kind of unsettling" beats "This is impressive."
- **Use "I" when it fits.** First person isn't unprofessional, it's honest. "I keep
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

### One voice among many

The examples above show a voice, not the voice. If every piece you humanize comes out
sounding like the same casual, first-person tech blogger, that sameness is its own
tell. Vary rhythm, opinion density, and register from piece to piece, guided by the
writer and the audience. Two different founders' landing pages should not read like
the same person wrote them.

### Calibrating voice by context

"Add voice" doesn't mean "always inject personality." Match the context:

- **UI copy, system messages, error states, legal text**: clarity first. Strip AI
  patterns, keep it short, do not add voice that doesn't belong. A login error is not
  the place for opinions.
- **Emails, bios, marketing, blog posts, landing pages**: add voice. These are places
  a human should sound like a human.
- **User provided a writing sample**: match the sample, not the defaults above. See
  `references/voice-calibration.md`.

{{FLAVOR:claude-code}}
## Optional: passive slop-check hook

This skill only helps when something invokes it. The worst copy slips through when
nobody runs the humanizer at all. The bundle ships an optional Claude Code hook
that scans text files after they are written and nudges you to run the humanizer if
it spots obvious tells. It is opt-in, heuristic, and off by default. See
`hooks/README.md` in the repo for what it catches and how to turn it on. It is a
backstop, not a replacement for a real humanizer pass.
{{/FLAVOR}}

---

Pattern catalog by [blader](https://github.com/blader/humanizer), MIT licensed, vendored
here unchanged. Its source is
[Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup, drawn from observations of thousands of instances
of AI-generated text on Wikipedia.
