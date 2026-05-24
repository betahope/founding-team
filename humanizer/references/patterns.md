# AI writing patterns — full catalog

Full reference for the 28 patterns indexed in `SKILL.md`. Each entry has a watch list,
the underlying problem, and a before/after example.

Numbering matches the index in SKILL.md.

---

## Content patterns

### 1. Significance inflation

**Watch for:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key
role/moment, underscores/highlights its importance/significance, reflects broader,
symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for,
marking/shaping the, represents/marks a shift, key turning point, evolving landscape,
focal point, indelible mark, deeply rooted.

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary
aspects represent or contribute to a broader topic. The sentence sounds weighty but
adds no information.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a
> pivotal moment in the evolution of regional statistics in Spain. This initiative was
> part of a broader movement across Spain to decentralize administrative functions and
> enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish
> regional statistics independently from Spain's national statistics office.

---

### 2. Notability puffery

**Watch for:** independent coverage, local/regional/national media outlets, written by
a leading expert, active social media presence, has been featured in [list of outlets].

**Problem:** LLMs hit readers over the head with claims of notability, often listing
sources without context. This reads like a press kit.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu.
> She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on
> outcomes rather than methods.

---

### 3. Superficial -ing analyses

**Watch for:** highlighting..., underscoring..., emphasizing..., ensuring..., reflecting...,
symbolizing..., contributing to..., cultivating..., fostering..., encompassing...,
showcasing...

**Problem:** AI tacks present-participle ("-ing") phrases onto the end of sentences to
add fake depth. The phrase restates the sentence in vaguer, weightier terms.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural
> beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan
> landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold. The architect said these were chosen to
> reference local bluebonnets and the Gulf coast.

---

### 4. Promotional language

**Watch for:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing,
exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking
(figurative), renowned, breathtaking, must-visit, stunning.

**Problem:** LLMs have serious trouble keeping a neutral tone, especially on
culture/heritage/travel topics. The voice defaults to a tourism brochure.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands
> as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly
> market and 18th-century church.

---

### 5. Vague attributions

**Watch for:** Industry reports, Observers have cited, Experts argue, Some critics argue,
several sources/publications (when few are actually cited).

**Problem:** AI attributes opinions to vague authorities without specific sources. The
effect is that nobody said it, but it sounds authoritative.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and
> conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey
> by the Chinese Academy of Sciences.

---

### 6. Formulaic "Challenges and Future Prospects" sections

**Watch for:** Despite its... faces several challenges..., Despite these challenges,
Challenges and Legacy, Future Outlook.

**Problem:** Many LLM-generated articles include a formulaic "Challenges" section that
names generic challenges and then dismisses them with a "despite" pivot to a hopeful
conclusion. The section says nothing specific.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas,
> including traffic congestion and water scarcity. Despite these challenges, with its
> strategic location and ongoing initiatives, Korattur continues to thrive as an integral
> part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal
> corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## Language and grammar patterns

### 7. High-frequency AI vocabulary

**Watch for:** actually, additionally, align with, crucial, delve, emphasizing, enduring,
enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key
(adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun),
testament, underscore (verb), valuable, vibrant.

**Problem:** These words appear far more frequently in post-2023 text. They often
co-occur in the same sentence, compounding the effect.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel
> meat. An enduring testament to Italian colonial influence is the widespread adoption
> of pasta in the local culinary landscape, showcasing how these dishes have integrated
> into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes,
> introduced during Italian colonization, remain common, especially in the south.

---

### 8. Copula avoidance

**Watch for:** serves as, stands as, marks, represents [a], boasts, features, offers.

**Problem:** LLMs substitute elaborate constructions for simple copulas ("is"/"are"/"has").
Every "X serves as Y" is a candidate for "X is Y."

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features
> four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. It has four rooms
> totaling 3,000 square feet.

---

### 9. Negative parallelism and tailing negations

**Problem:** Constructions like "Not only... but..." or "It's not just about..., it's..."
are overused. So are clipped tailing-negation fragments like "no guessing" or "no wasted
motion" tacked onto the end of a sentence.

**Before (negative parallelism):**
> It's not just about the beat riding under the vocals; it's part of the aggression
> and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item, so the user doesn't have to guess.

---

### 10. Rule of three overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive. Any time a
sentence has exactly three adjectives, three parallel clauses, or three bullet categories
suspiciously often, suspect this.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities.
> Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between
> sessions.

---

### 11. Elegant variation

**Problem:** AI has repetition-penalty code that causes excessive synonym substitution
for the same referent. Humans usually just reuse the word.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles.
> The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

---

### 12. False ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful
scale. The shape of the phrase suggests a spectrum when none exists.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to
> the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark
> matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

---

### 13. Passive voice and subjectless fragments

**Problem:** LLMs hide the actor or drop the subject entirely with lines like "No
configuration file needed" or "The results are preserved automatically." Rewrite these
when active voice makes the sentence clearer and more direct. Contractions help — they
also cut the formal AI register.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You don't need a config file — the system saves results automatically.

---

## Style patterns

### 14. Em dash overuse

**Problem:** LLMs use em dashes (—) more than humans, mimicking "punchy" sales writing.
Most of these can be rewritten more cleanly with commas, periods, or parentheses. A few
em dashes per document are fine — three per paragraph aren't.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You
> don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in
> official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves.
> You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in
> official documents.

---

### 15. Mechanical boldface emphasis

**Problem:** AI bolds phrases reflexively — usually the first noun phrase or an
acronym expansion. In published prose, boldface should be rare.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**,
> and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced
> Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and
> Balanced Scorecard.

---

### 16. Inline-header vertical lists

**Problem:** AI outputs lists where items start with a bolded label, a colon, and then
a sentence that restates the label.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms,
> and adds end-to-end encryption.

---

### 17. Title Case Headings

**Problem:** AI capitalizes all main words in headings by default. Most modern
editorial styles use sentence case for headings.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

---

### 18. Emojis in headings and bullets

**Problem:** AI decorates headings and bullet points with emojis as a reflex. In most
professional contexts this reads as a tell.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next
> step: schedule a follow-up meeting.

---

### 19. Curly quotation marks

**Problem:** ChatGPT outputs curly quotes (“ ” ‘ ’) instead of straight quotes (" " ' ').
Straight quotes are the norm in code, plain text, and most web copy.

**Before:**
> He said “the project is on track” but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

---

## Communication patterns

### 20. Collaborative artifacts and sycophancy

**Watch for:** I hope this helps, Of course!, Certainly!, You're absolutely right!,
Would you like..., let me know, here is a..., Great question!, That's an excellent
point, What a thoughtful question.

**Problem:** Text meant as chatbot correspondence leaks into content — either openers
("Here is an overview...") or flattery ("Great question!"). Both mark the text as
machine-emitted.

**Before (mixed artifacts + sycophancy):**
> Great question! Here is an overview of the French Revolution. You're absolutely right
> that this is a complex topic. I hope this helps! Let me know if you'd like me to
> expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to
> widespread unrest.

---

### 21. Knowledge-cutoff disclaimers

**Watch for:** as of [date], Up to my last training update, While specific details are
limited/scarce..., based on available information..., I don't have information on...

**Problem:** AI disclaimers about incomplete information get left in the text when it's
pasted as content. Strip them.

**Before:**
> While specific details about the company's founding are not extensively documented
> in readily available sources, it appears to have been established sometime in the
> 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

---

## Filler and hedging patterns

### 22. Filler phrases

**Problem:** Multi-word phrases where one word would do. Cut them.

Substitutions:
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"
- "With regards to" → "About"
- "For the purpose of" → "To"

---

### 23. Excessive hedging

**Problem:** Over-qualifying statements with stacks of modals ("could potentially
possibly"). One hedge is enough. Usually zero is enough.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on
> outcomes.

**After:**
> The policy may affect outcomes.

---

### 24. Generic positive conclusions

**Problem:** Vague upbeat endings that commit to nothing. "The future is bright" means
"I have nothing specific to say about the future."

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue
> their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

---

### 25. Too-perfect compound-modifier hyphenation

**Watch for:** identical hyphenation of the same compound modifier every single time it
appears across a document — "cross-functional", "high-quality", "data-driven",
"decision-making", "real-time", "long-term", "end-to-end".

**Problem:** AI hyphenates compound modifiers with machine consistency. Real writers
drift — sometimes they hyphenate, sometimes they don't, sometimes they rewrite around
the construction entirely. This is a *variation* tell, not a grammar rule. Hyphenating
compound modifiers before a noun is correct in edited prose — the issue is doing it
identically every time.

**How to fix:** don't globally un-hyphenate. Instead, vary usage across the piece.
Rewrite some instances to avoid the compound entirely. A few open compounds in predicate
position ("the team was cross functional") or recast as verbs or clauses ("updates in
real time" instead of "real-time updates") break the pattern without breaking grammar.

**Before (AI pattern — every compound hyphenated identically):**
> The cross-functional team delivered a high-quality, data-driven report on our
> client-facing tools. Their decision-making process was well-known for being thorough
> and detail-oriented.

**After (varied, some rewritten):**
> The team pulled people from engineering, design, and ops. They delivered a thorough
> report on the tools customers touch, grounded in actual usage data. Their process was
> careful, if slow.

---

### 26. Persuasive authority tropes

**Watch for:** The real question is, at its core, in reality, what really matters,
fundamentally, the deeper issue, the heart of the matter.

**Problem:** LLMs use these phrases to pretend they're cutting through noise to some
deeper truth. The sentence that follows usually just restates an ordinary point with
extra ceremony.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is
> organizational readiness.

**After:**
> The question is whether teams can adapt. That mostly depends on whether the
> organization is ready to change its habits.

---

### 27. Signposting

**Watch for:** Let's dive in, let's explore, let's break this down, here's what you
need to know, now let's look at, without further ado.

**Problem:** LLMs announce what they're about to do instead of doing it. This
meta-commentary slows the writing down and gives it a tutorial-script feel.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at multiple layers, including request memoization, the data
> cache, and the router cache.

---

### 28. Fragmented headers

**Signs to watch:** a heading followed by a one-line paragraph that restates the heading
before the real content begins.

**Problem:** LLMs add a generic sentence after a heading as a rhetorical warm-up. It
usually adds nothing and makes the prose feel padded.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.
