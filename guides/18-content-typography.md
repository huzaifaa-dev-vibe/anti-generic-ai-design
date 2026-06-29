# 18 — Content & Typography

> Content is design. A page with perfect spacing, type, and color, but with placeholder copy, is not a finished page — it's a sketch. AI-coded sites ship "Your headline here", "Lorem ipsum dolor sit amet", and "Powerful, scalable, modern" — the dead language of unfinished work. This guide treats copy as a first-class design material with its own rules, its own rhythm, and its own discipline.

## Why AI fails at content

Five defaults ruin AI copy:

1. **Placeholder text.** "Lorem ipsum" shipped to production. "Your headline here" in the hero. "Feature description goes here" in the cards. These are flags that say "I stopped thinking".
2. **Adjective soup.** "Powerful, scalable, modern, intuitive, seamless." Every word says nothing. Every word could apply to every product. None of them differentiate.
3. **Marketing copy in UX contexts.** "Welcome to the future of project management!" in an empty state. The user is not a prospect here — they're a user, and they need to know what to do next.
4. **No reading-level discipline.** AI writes at a 14th-grade level because that's what its training data rewards. Real users read at a 7th-to-9th-grade level. Long sentences, compound-complex structures, abstract nouns — all death.
5. **No voice.** Every page sounds the same because every page was written by the same averaged-out LLM. A brand has a voice — a stance, a vocabulary, a rhythm. AI default copy has none.

Copy is not what fills the design. Copy **is** the design.

---

## Rule 1 — Copy length per page element

Every element has a target length. Going under is thin. Going over is exhausting.

| Element | Word count | Character count | Why |
|---------|-----------|------------------|-----|
| Hero headline | 4–8 words | 25–50 chars | One breath, one idea |
| Hero subhead | 15–25 words | 80–140 chars | One sentence expanding the headline |
| Hero CTA label | 2–4 words | 10–25 chars | Verb + noun |
| Feature title | 3–6 words | 20–40 chars | Same as headline discipline |
| Feature description | 30–50 words | 180–280 chars | Two short sentences max |
| Testimonial quote | 30–80 words | 180–450 chars | One real sentence with a specific detail |
| Testimonial name + role | 4–8 words | 25–50 chars | Name, title, company |
| Stat | 1–6 words | 5–40 chars | Number + 1-clause provenance |
| Pricing tier name | 1–3 words | 5–20 chars | Noun, not an adjective |
| Pricing tier description | 8–15 words | 50–90 chars | Who it's for |
| Feature list item | 3–8 words | 20–50 chars | Verb + object, parallel structure |
| FAQ question | 6–12 words | 35–70 chars | A real question a user would ask |
| FAQ answer | 40–100 words | 240–600 chars | Direct answer first, then context |
| Footer link label | 1–3 words | 5–20 chars | Noun, not a sentence |
| Empty state headline | 3–6 words | 15–35 chars | What's empty, in plain words |
| Empty state body | 15–30 words | 80–180 chars | Why + what to do |
| Error message | 5–15 words | 30–90 chars | What went wrong + how to fix |

**Test**: count your hero headline. If it's over 12 words, it's not a headline — it's a paragraph pretending to be one. Cut it.

## Rule 2 — Reading level: grade 7–9

Aimed at the average adult reader. The Hemingway App grades your writing; aim for grade 7–9.

Tactics:
- **Short sentences.** Average 14 words. Max 25. If a sentence has three commas, break it in two.
- **Short words.** "Use" not "utilize". "Help" not "facilitate". "Start" not "commence".
- **Active voice.** "We ship daily" not "Daily shipping is performed by us".
- **Concrete nouns.** "Database" not "data persistence layer". "10,000 users" not "a sizable user base".
- **No jargon unless the audience uses it.** A dev tool can say "webhook". A consumer app cannot.

```tsx
// ❌ Grade 14
// "Our comprehensive platform empowers organizations to seamlessly orchestrate
// complex workflows across distributed teams, facilitating unprecedented
// collaboration and operational excellence."

// ✅ Grade 7
// "Plan projects, track work, and ship together — all in one place."
```

Run every block of copy through [Hemingway App](http://www.hemingwayapp.com/) before shipping. If it's above grade 9, rewrite.

## Rule 3 — Voice and tone guidelines

Voice is who you are. Tone is how you sound in a given moment. Voice is constant; tone adapts.

### Define your voice in 3 adjectives

Examples:
- Linear: precise, calm, confident
- Mailchimp: friendly, helpful, witty
- Stripe: clear, technical, authoritative
- Notion: warm, capable, simple

Pick three. Write them at the top of your content guide. Every sentence should pass all three.

### Tone adapts to context

| Context | Tone |
|---------|------|
| Marketing page | Confident, energetic, persuasive |
| Onboarding | Friendly, instructional, encouraging |
| Dashboard | Direct, neutral, efficient |
| Error message | Apologetic, clear, helpful |
| Empty state | Encouraging, helpful |
| Success message | Warm, brief |
| Loading state | Honest, brief |
| Pricing page | Clear, neutral, no pressure |
| Cancel flow | Respectful, no friction, honest |

**The cancel flow test**: when a user cancels, your tone reveals your values. If you become hostile ("Are you sure? You'll lose everything!"), you were never friendly. Be the same brand at the cancel as at the signup.

## Rule 4 — Marketing copy vs UX copy

These are two different disciplines. Don't confuse them.

| Dimension | Marketing copy | UX copy |
|-----------|---------------|---------|
| Goal | Persuade, excite, differentiate | Guide, confirm, explain |
| Length | More words, more room to breathe | Fewer words, maximum efficiency |
| Voice | Projected, energetic | Restrained, neutral |
| Where | Landing pages, ads, emails | App UI, settings, forms, errors |
| Example | "The fastest way to ship code." | "Saved." |

**Marketing copy in a UX context is a category error.** A button that says "Unleash the power of analytics" instead of "View dashboard" is broken. A loading state that says "Whipping up something amazing!" instead of "Loading your dashboard…" is hostile.

## Rule 5 — Long-form typography rules

When the content is the product (blog, docs, long-form article), typography rules the experience.

| Rule | Value | Why |
|------|-------|-----|
| Line length (measure) | 60–80 characters | Optimal reading speed; shorter causes return-sweep fatigue, longer causes line-loss |
| Line height (body) | 1.5–1.7 | Enough air to scan; less causes crowding, more causes disconnect |
| Paragraph spacing | 1–1.5em | Equal to or slightly less than line height |
| Font size (body) | 18–20px on desktop, 16–18px mobile | 16px is the floor; smaller strains reading |
| Heading-to-body gap | Larger above, smaller below | Heading belongs to what follows |
| Justify | Left-aligned, never justified | Justified text creates rivers of whitespace; left-aligned is scannable |

```css
.prose {
  max-width: 65ch;                    /* the only place max-w-prose earns its keep */
  font-size: var(--step-0);
  line-height: 1.65;
  color: var(--text);
}

.prose p {
  margin-bottom: 1.25em;
}

.prose h2 {
  font-size: var(--step-3);
  line-height: 1.15;
  margin-top: 2.5em;
  margin-bottom: 0.6em;
  letter-spacing: -0.02em;
}

.prose h3 {
  font-size: var(--step-2);
  line-height: 1.2;
  margin-top: 2em;
  margin-bottom: 0.5em;
}

.prose h2 + p, .prose h3 + p {
  margin-top: 0;                      /* no double-gap between heading and its body */
}

.prose ul, .prose ol {
  margin: 1.25em 0;
  padding-left: 1.5em;
}

.prose li {
  margin-bottom: 0.5em;
  line-height: 1.6;
}

.prose blockquote {
  margin: 1.5em 0;
  padding-left: 1em;
  border-left: 3px solid var(--accent);
  font-size: var(--step-1);
  line-height: 1.4;
  color: var(--text-muted);
}

.prose code {
  font-family: var(--font-mono);
  font-size: 0.875em;
  padding: 0.15em 0.4em;
  background: var(--surface-hover);
  border-radius: 4px;
}

.prose pre {
  padding: var(--space-4);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow-x: auto;
  font-size: 0.875rem;
  line-height: 1.55;
  margin: 1.5em 0;
}

.prose pre code {
  padding: 0;
  background: none;
}

.prose a {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
}

.prose a:hover {
  text-decoration-thickness: 2px;
}

.prose img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 2em 0;
}
```

## Rule 6 — Links: underline always, color optional

Underlines are the universal signal for "this is a link". Color is a secondary signal — useful, but never the only one (colorblind users, dark mode inversions, etc.).

```css
a {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
}

a:hover {
  text-decoration-thickness: 2px;
}

a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  text-decoration: none;             /* outline replaces underline on focus */
}
```

**In body copy**: always underline. Color is optional but recommended.
**In nav, buttons, or already-obvious interactive contexts**: underline is optional. Color + cursor is enough.

## Rule 7 — Pull quotes, callouts, code blocks, tables, footnotes

### Pull quotes

A pull quote is a sentence from the article, repeated at larger size, used to break up long text and draw scanners into the body.

```css
.pullquote {
  font-size: var(--step-3);
  line-height: 1.2;
  font-family: var(--font-display);
  margin: 2.5em 0;
  padding: 0 0 0 var(--space-5);
  border-left: 3px solid var(--accent);
  color: var(--text);
}
```

Use pull quotes for one or two key sentences per 1500 words. More than that, they lose impact.

### Callouts

A callout is a non-quote emphasized block — a warning, a tip, a note.

```css
.callout {
  margin: 1.5em 0;
  padding: var(--space-4) var(--space-5);
  border-radius: 8px;
  background: var(--accent-soft);
  border-left: 3px solid var(--accent);
}

.callout-title {
  font-weight: 600;
  margin-bottom: 0.25em;
  display: flex;
  align-items: center;
  gap: var(--space-2);
}
```

```html
<aside class="callout">
  <p class="callout-title">
    <InfoIcon aria-hidden /> Note
  </p>
  <p>This API is deprecated. Use the v2 endpoint instead.</p>
</aside>
```

### Code blocks

- Use a real syntax highlighter (Shiki, Prism, Starrynight).
- Always specify the language in the code fence: <code>```ts</code>.
- Line numbers for blocks >10 lines.
- A "copy" button in the top-right.
- Max line length 80 chars (horizontal scroll if exceeded).

### Tables

- Use `<th scope="col">` for column headers, `<th scope="row">` for row headers.
- Zebra striping optional, only for wide tables.
- Right-align numbers, left-align text.
- Use tabular figures (`font-feature-settings: "tnum"`) for numeric columns.

### Footnotes

Use real footnotes, not parenthetical asides. Linked superscript numbers that scroll to a footnote section at the bottom, with a "back" link.

```html
<p>The study<sup><a href="#fn-1" id="fnref-1">1</a></sup> found that…</p>

<footer>
  <ol class="footnotes">
    <li id="fn-1">
      Smith et al., "Cognitive Load in Web Forms", 2023.
      <a href="#fnref-1" aria-label="Back to reference 1">↩</a>
    </li>
  </ol>
</footer>
```

## Rule 8 — Microcopy: the small text that decides everything

Microcopy is the tiny labels, helper text, button text, and error messages that guide users. It's where most copy fails.

| Element | Bad microcopy | Good microcopy |
|---------|---------------|----------------|
| Submit button | "Submit" | "Send invoice" |
| Cancel button | "Cancel" | "Discard changes" |
| Email field helper | "Enter your email" | "We'll send a confirmation to this address." |
| Password requirements | "Must be secure" | "At least 12 characters, including a number." |
| Empty search | "No results" | "No matches for 'query'. Try a different search." |
| Form error | "Invalid input" | "Email must contain @ and a domain." |
| Confirmation dialog | "Are you sure?" | "Delete 'Project Name'? This cannot be undone." |
| Loading button | "Loading…" | "Saving…" (action-specific) |
| Success toast | "Success!" | "Invoice sent to alice@example.com" |
| Opt-in checkbox | "Subscribe" | "Send me product updates (no more than 1 per month)" |

**Rules**:
- Button labels are verbs + objects, not just verbs. "Save" → "Save changes". "Delete" → "Delete file".
- Helper text tells the user what to do or what will happen — not what the field is.
- Errors name the field and the problem. "Email must contain @" beats "Please fix this".
- Confirmation dialogs name the consequence. "Delete project? This cannot be undone." beats "Are you sure?".

## Rule 9 — Numbers, stats, and provenance

Every stat on your page should answer three questions: what, how much, and where did it come from?

```tsx
// ❌ Vague stat
<Stat value="10M+" label="Users" />

// ✅ Stat with provenance
<Stat
  value="10,247,893"
  label="Reviews published"
  source="Source: Internal data, Q3 2025"
/>
```

**Numbers rules**:
- Use exact numbers when they're impressive (1,247,893 not "1M+").
- Use round numbers when they're approximate ("over 10 million").
- Always include a source. No source = made up = no trust.
- Animate the count-up only on the first viewport entry, only once, only if it's a real number.

## Rule 10 — Forbidden copy

These phrases auto-fail a page:

| Forbidden | Why | Use instead |
|-----------|-----|-------------|
| "Lorem ipsum" | Placeholder | Real copy |
| "Your headline here" | Placeholder | Real headline |
| "Powerful" | Empty adjective | Name the specific power |
| "Scalable" | Means nothing concrete | "Handles 10,000 concurrent users" |
| "Modern" | Every product claims this | Describe what's modern about it |
| "Seamless" | Cliché | Describe the seam that's been removed |
| "Leverage" | Corporate speak | "Use" |
| "Robust" | Empty | Name the specific robustness |
| "Cutting-edge" | Marketing speak | Show the edge |
| "Best-in-class" | Vague | "Used by 3 of the Fortune 5" |
| "Empower" | Paternalistic | "Help" or "Let" |
| "Synergy" | Dead word | Delete the sentence |
| "Revolutionary" | Overused | "First to do X" |
| "Game-changer" | Sports cliché | Describe the change |
| "Disruptive" | VC cliché | "Changes how X works by Y" |
| "Unlock" | Marketing cliché | "Access" or "Enable" |
| "Harness" | Vague | "Use" |
| "Next-generation" | Empty | "Built for X" |
| "End-to-end" | Often a lie | Name the start and end |
| "World-class" | Self-praise | "Used by teams at X, Y, Z" |
| "Trusted by" | Often a logo strip with no proof | "Used by teams at X, Y, Z" + case study links |

## Rule 11 — The CTA copy rule

CTA copy is verbs + objects. Not "Get Started" (no object). Not "Learn More" (vague). Not "Click Here" (describes the action, not the destination).

| Bad CTA | Good CTA |
|---------|----------|
| Get Started | Start your free trial |
| Learn More | Read the docs |
| Submit | Send message |
| Click Here | View pricing |
| Read More | Continue reading |
| Buy Now | Start 14-day trial |
| Sign Up | Create your account |
| Contact Us | Email the team |

## Rule 12 — Write a content brief before writing copy

Before you write a single headline, answer:

1. **Who is reading this?** (Person, role, what they care about)
2. **What do they need to understand after reading?** (One sentence)
3. **What do they need to do?** (One action)
4. **What's the emotional state going in?** (Curious, skeptical, frustrated, ready-to-buy)
5. **What's the emotional state going out?** (Confident, reassured, excited, neutral)
6. **What does this page need to say that no competitor's page says?**

If you can't answer all six, you don't have a brief. You have vibes. Write the brief, then write the copy.

## Anti-Patterns (Auto-Fail)

1. **"Lorem ipsum" anywhere.** Banned.
2. **"Your headline here" or "Feature description".** Banned.
3. **Three or more empty adjectives** ("powerful, modern, scalable") in any block.
4. **Hero headline > 12 words.** Cut to 8 or fewer.
5. **Sentences > 25 words** without a deliberate reason.
6. **Reading level > grade 9** on consumer-facing copy.
7. **Marketing copy in a UX context** ("Unleash the power of…" in an empty state).
8. **No source on a stat.** Delete the stat or add the source.
9. **"Get Started" or "Learn More" as CTAs.** Use verb + object.
10. **No voice defined.** Write three adjectives at the top of your content doc.
11. **Cancel flow tone shift.** If you're hostile at cancel, you were never friendly at signup.
12. **Long paragraphs** (>5 sentences). Break them.
13. **Justified text** in any context. Banned.
14. **Body text without underlines on links** in long-form copy.

## Code Example — A Content-Aware Component

```tsx
type Feature = {
  title: string;        // 3–6 words
  description: string;  // 30–50 words, grade 7–9
  icon: React.ReactNode;
};

function FeatureCard({ feature }: { feature: Feature }) {
  // Validate at build time
  if (process.env.NODE_ENV === 'development') {
    if (feature.title.split(' ').length > 6) {
      console.warn(`Feature title too long: "${feature.title}"`);
    }
    if (feature.description.split(' ').length > 60) {
      console.warn(`Feature description too long (${feature.description.split(' ').length} words)`);
    }
  }

  return (
    <article className="feature-card">
      <div className="feature-icon" aria-hidden="true">
        {feature.icon}
      </div>
      <h3 className="feature-title">{feature.title}</h3>
      <p className="feature-description">{feature.description}</p>
    </article>
  );
}
```

## Output

When you finish this guide, you should have:
- A voice defined in three adjectives at the top of `DESIGN-RATIONALE.md`
- A copy length table committed for every page element
- Every block of copy passed through Hemingway App (grade 7–9 for consumer, 9–11 for technical)
- No placeholder text ("Lorem ipsum", "Your headline here") anywhere
- No empty adjectives ("powerful", "scalable", "modern") without a specific claim
- All CTAs as verb + object
- All stats with a source
- Long-form content set with `max-w-prose`, line height 1.5–1.7, line length 60–80 chars
- All links underlined in body copy
- A content brief written for every page before copy was written
