# Voice calibration

When the user provides a writing sample, use it to match their voice instead of
falling back to the default "natural and opinionated" register.

## When this applies

The user triggered voice calibration if they said something like:

- "Humanize this text. Here's a sample of my writing for voice matching: [sample]"
- "Humanize this text. Use my writing style from [file path] as a reference."
- "Match my voice — I've written like this before: [sample]"

Or they pointed you at a file containing past writing. When in doubt, ask.

## How to analyze the sample

Read the sample before writing anything. Note:

- **Sentence length patterns.** Short and punchy? Long and flowing? Mixed?
- **Word-choice register.** Casual, academic, somewhere between? Specific jargon or
  avoidances?
- **Paragraph openings.** Jump right in, or set context first?
- **Punctuation habits.** Dashes? Parenthetical asides? Semicolons? Lists?
- **Recurring phrases or verbal tics.** Every writer has a few.
- **Transitions.** Explicit connectors ("However", "Furthermore") or just start the
  next point?
- **First-person usage.** How often, and in what register?
- **Opinion density.** Do they state views directly, hedge, or stay neutral?

## How to apply it

Don't just remove AI patterns — replace them with patterns drawn from the sample.

- If the sample has short sentences, don't produce long ones.
- If the sample uses "stuff" and "things," don't upgrade to "elements" and "components."
- If the sample never uses semicolons, don't introduce them.
- If the sample is opinionated, keep opinions. If it's neutral reportage, don't
  manufacture opinions in the rewrite.
- If the sample uses contractions, use them. If it doesn't, don't.

Voice calibration overrides the default "add voice" guidance in SKILL.md. The sample
is the target, not generic humanness.

## When no sample is provided

Fall back to the defaults in SKILL.md — natural, varied rhythm, opinionated where
appropriate, specific over vague. Strip AI patterns. Match the register implied by
the input's context.
