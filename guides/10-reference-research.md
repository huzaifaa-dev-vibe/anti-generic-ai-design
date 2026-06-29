# 10 — Reference Research (How to Steal Like an Artist)

> Every senior designer you've ever worked with keeps a mental (or Notion) library of 200+ reference sites. Before they start a project, they pull 5–10 references, analyze what works, and borrow specific elements. AI agents skip this step entirely — they go from "build a SaaS landing page" to `<div className="max-w-7xl mx-auto">` with zero research. This is why every AI site looks the same. This guide is the fix.

## Why AI research fails

Three defaults kill AI design research:

1. **AI agents don't read `data/websites-100.json`.** The repo ships with 100 hand-curated reference sites, organized by category. The agent doesn't know to open it. So it builds from training-data defaults — which are the most generic possible output.
2. **AI agents don't analyze references before borrowing.** When they do cite a reference, they copy the surface (the gradient, the rounded corner) without understanding why it worked in the original context. A direct copy without context is a generic copy.
3. **AI agents confuse "reference" with "clone".** Borrowing a hero layout from Linear is fine. Borrowing Linear's exact headline + screenshot + proof layout, just changing the words, is a clone. The user notices.

**The fix**: a mandatory research phase before any code is written. Pull 3 references. Analyze them. Borrow specific elements. Document the borrows. Build only after.

This is the same Phase 1 from `01-thinking-redesign.md`. This guide goes deeper on the *how*.

---

## The 5-Step Research Methodology

### Step 1 — Identify the project category

Before researching, name what you're building. Not in vague terms — in specific ones.

```text
Category: B2B SaaS (project management for design teams)
Sub-category: Async collaboration tool
Target audience: Product designers at startups (50–500 employees)
Vibe: Editorial-professional (not playful, not corporate)
Reference category: "saas-collab-editorial"
```

The category determines which references to pull. A "B2B SaaS" without sub-category is too broad — you'll end up with the AI-default SaaS look (indigo gradient, Inter, centered hero).

**Reference category taxonomy** (match against `data/websites-100.json` categories):

- `saas-collab` — Linear, Notion, Figma, Coda
- `saas-devtools` — Vercel, Supabase, Railway, Bun
- `saas-finance` — Stripe, Mercury, Ramp, Brex
- `editorial-publication` — The Verge, Pentagram, It's Nice That
- `portfolio-creative` — Mucho, Lusion, studio sites
- `ecommerce-fashion` — Aesop, Buck Mason, Everlane
- `ecommerce-dtc` — Allbirds, Glossier, Outdoor Voices
- `agency-studio` — Pentagram, IDEO, Huge
- `media-magazine` — New Yorker, Bloomberg
- `docs-developer` — Stripe Docs, Vercel Docs, MDN
- `personal-blog` — Maggie Appleton, Andy Matuschak
- `product-launch` — Apple Vision Pro, OpenAI DevDay

Pick the closest match. If you're between two, pull references from both.

### Step 2 — Search `data/websites-100.json`

Open the file. Filter by `category`. Pick **3 references** that match the vibe. For each, read the `design_notes` field — it contains the specific element worth borrowing.

```bash
# Example: filter for saas-collab references
jq '.[] | select(.category == "saas-collab")' data/websites-100.json
```

If your category isn't in the file, search the web for "best [category] websites 2025" and pull 3 yourself. Add them to your local copy of `websites-100.json` (PRs welcome — see `CONTRIBUTING.md`).

### Step 3 — Analyze each reference (6 dimensions)

For each of the 3 references, write a structured analysis across 6 dimensions. This is the work AI agents skip. Don't skip it.

#### Dimension 1 — Layout

- Is the hero split, centered, asymmetric, video-bg, product-first?
- What's the grid? 12-column? Asymmetric? Editorial 3-column?
- How dense is the content? Sparse / balanced / dense?
- What's the section rhythm? (e.g. hero → logos → features → testimonial → pricing → CTA)

```text
Reference: Linear (linear.app)
Layout: Split hero, text-left, product UI right. 12-col grid.
        Sparse — lots of whitespace. Section rhythm:
        hero → logo strip → 3 feature cards (alternating) →
        testimonial → CTA → footer.
Borrow: The alternating feature cards (image-left, image-right)
Avoid: The "Trusted by" logo strip — overused
```

#### Dimension 2 — Palette

- What are the 5 roles (bg, surface, text, accent, muted)?
- Light or dark? Both?
- What's the accent? Is it saturated or muted?
- Are there semantic colors? How are they used?

```text
Reference: Linear
Palette: Dark default (#08090A bg, #1C1D20 surface, #F7F8F8 text,
         #5E6AD2 accent — a slightly-desaturated indigo, warmer than
         Tailwind indigo)
         Light mode available (#FBFAFF bg, accent same)
Borrow: The accent (#5E6AD2) — it's indigo done right (slightly muted,
        slightly warm)
Avoid: I won't use it directly — too identifiable as "Linear blue".
       I'll pick a different accent and use Linear's *desaturation
       approach* on it.
```

#### Dimension 3 — Type

- Display face? Body face? Numeric? Mono?
- Weights used?
- Type scale ratio?
- Any custom letter-spacing or line-height treatments?

```text
Reference: Linear
Type: Inter Variable for everything. Display weight 580 (not standard),
      body 420. Tight tracking on headlines (-0.02em).
      Numeric: same Inter with tabular-nums.
Borrow: The non-standard weights (580 / 420) — feels intentional
        rather than default 400/600.
Avoid: Single-family system — I'll pair Inter body with a display
       serif to differentiate.
```

#### Dimension 4 — Motion

- What animates on page load?
- What animates on scroll?
- What are the hover micro-interactions?
- How long is the hero choreography?
- What's the easing curve?

```text
Reference: Linear
Motion: Hero choreography ~2.5s. Eyebrow → headline (1 line) →
        subhead → CTAs → product UI. Easing feels like ease-out
        with a slight overshoot. Scroll: feature cards fade-up
        individually (staggered 80ms). Hover: cards lift 2px with
        shadow.
Borrow: The choreography sequence and ~2.5s total duration.
Avoid: The fade-up-on-scroll — too generic. I'll use a different
       reveal (clip-path wipe or mask-image reveal).
```

#### Dimension 5 — Copy

- Voice: formal / casual / technical / editorial?
- Headline formula?
- CTA copy style?
- Sentence length distribution?

```text
Reference: Linear
Copy: Technical-editorial. Headlines are short statements of fact
      ("The issue tracking tool you'll enjoy using"). Subheads expand
      with mechanism. CTAs are imperative + outcome ("Get started —
      it's free"). Sentence length: short.
Borrow: The headline-as-statement-of-fact formula. Short.
Avoid: Their voice is too dry for my audience — I'll add warmth
       in the subhead without losing the directness.
```

#### Dimension 6 — Information Architecture

- What pages does the site have? (sitemap)
- What's the nav structure?
- Where are CTAs placed?
- What links from the footer?
- What's the URL structure?

```text
Reference: Linear
IA: Pages: / (home), /features (overview), /features/{feature} (8
    sub-pages), /method (their methodology blog), /customers (case
    studies), /pricing, /changelog, /docs (separate subdomain),
    /careers, /security, /privacy, /terms.
    Nav: Product (dropdown), Customers, Pricing, Changelog, Docs,
    "Log in", "Get started".
Borrow: The /features/{feature} pattern — one page per feature.
Avoid: Their "method" section — too marketing-heavy for me.
```

### Step 4 — Borrow specific elements (not whole designs)

This is the critical step. AI agents skip directly to "build something like Linear" and end up cloning Linear. The senior-designer move is to borrow **specific elements** from each reference, not the whole design.

**A borrow looks like:**
> "I'm borrowing Linear's hero choreography timing (2.5s total, 80ms stagger between elements) but not their headline fade-up. I'll use a clip-path wipe reveal instead."

**A clone looks like:**
> "I'm using a split hero like Linear, with the same eyebrow + headline + subhead + 2 CTAs + product UI on the right."

The borrow names what's taken and what's left. The clone takes everything.

**Borrow library** — for each reference, list 2–3 specific borrows:

```text
Reference 1: Linear (linear.app)
  Borrow A: Hero choreography timing (2.5s total, 80ms stagger)
  Borrow B: Alternating image-left / image-right feature cards
  Borrow C: The "Get started — it's free" CTA copy pattern
  Avoid X: Their logo strip ("Trusted by")
  Avoid Y: Their exact accent color (#5E6AD2)
  Avoid Z: Their single-family Inter system

Reference 2: Stripe (stripe.com)
  Borrow A: The diagonal section divider (clip-path)
  Borrow B: Their tab-switcher for "personal vs business" use cases
  Borrow C: The animated background gradient mesh (subtle)
  Avoid X: Their exact gradient colors
  Avoid Y: Their photography style (too fintech)

Reference 3: Vercel (vercel.com)
  Borrow A: Terminal-typewriter hero pattern (for dev-tool variant)
  Borrow B: Their mono font for code blocks (Geist Mono)
  Borrow C: The "deployment in 60 seconds" stat-card style
  Avoid X: Their pure black + white palette (too stark for my audience)
  Avoid Y: Their headline gradient-text effect
```

### Step 5 — Document borrows in `DESIGN-RATIONALE.md`

Every borrow must be written down. If you can't point to a line in `DESIGN-RATIONALE.md` explaining where an element came from, you're not borrowing — you're defaulting.

```markdown
## References and borrows

### Reference 1: Linear (linear.app)
- **Borrow A — Hero choreography timing (2.5s, 80ms stagger)**
  Reason: Linear's hero feels deliberate but not slow. The 2.5s total
  matches the user's "this page has loaded and is ready" expectation.
  Source: data/websites-100.json#linear

- **Borrow B — Alternating image-left / image-right feature cards**
  Reason: Alternating layout creates rhythm; same-direction cards
  feel monotonous. Linear executes this with 5:7 ratio columns.
  Source: data/websites-100.json#linear

- **Borrow C — CTA copy pattern ("action — outcome")**
  Reason: "Get started — it's free" is more clickable than "Get
  Started" alone. The em-dash adds the outcome ("it's free")
  without padding the button width.
  Source: data/websites-100.json#linear

### Reference 2: Stripe (stripe.com)
- **Borrow A — Diagonal section divider via clip-path**
  Reason: Diagonal dividers break the monotony of horizontal
  section breaks. Used once between the hero and the feature
  section, not on every section.
  Source: data/websites-100.json#stripe

[...]
```

This document is your defense when the user says "this looks like X". You can say: "Yes, I borrowed X's section divider because it solves Y problem. Here's the rationale."

---

## Where to Find References (beyond `websites-100.json`)

The repo ships 100 references. You'll outgrow it. Use these design-archive sites to find more:

### Awwwards (awwwards.com)
The largest collection of award-winning sites. Filter by:
- **Site of the Day** — current best-in-class
- **Site of the Month** — recent winners
- **Developer Award** — technically impressive
- **Honorable Mentions** — solid, not flashy

Use for: creative / agency / portfolio / fashion / luxury.

Don't use for: B2B SaaS (Awwwards skews toward visual showcase; SaaS sites rarely win).

### Siteinspire (siteinspire.com)
Curated gallery of editorial / portfolio / studio sites. Less flashy than Awwwards, more refined. Updated daily.

Use for: editorial, portfolios, design studios, typography-driven sites.

### Httpster (httpster.net)
Hand-picked, no-algorithm gallery. Less volume, higher curation. Strong on European and Japanese design.

Use for: international design sensibility, type-driven layouts.

### Land-book (land-book.com)
Categorized gallery specifically for landing pages. Filter by category (apps, e-commerce, portfolios, etc.).

Use for: SaaS, startups, product launch pages.

### Codrops (tympanus.net/codrops)
Reference for **technique**, not visual style. Each article has a working demo with code. Use when you need to figure out how to build a specific interaction.

### One Page Love (onepagelove.com)
Single-page sites specifically. Good for product launches, event pages, portfolio one-pagers.

### Direct from the source
- **Apple** — for cinematic hero, scroll choreography, precision typography
- **Stripe** — for technical-editorial SaaS, animated diagrams
- **Linear** — for product UI showcase, motion design
- **Vercel** — for dev-tool aesthetics, terminal-first hero
- **Aesop** — for editorial e-commerce, typography-led
- **Pentagram** — for studio / brand work, asymmetric editorial
- **Bloomberg Businessweek** — for editorial typography, magazine layouts

### Pinterest / Are.na
For mood-boarding (color, texture, photography style). Not for layout — too many generic AI-styled mockups pollute the results.

---

## How to Read a Site's Design Language

When you open a reference site, you have 10 seconds to capture what works. Train your eye to scan in this order:

### 1. First impression (0–2 seconds)

Don't analyze. Just feel. Is the site calm? Energetic? Premium? Friendly? Write down the one-word vibe. This is the gestalt — what the user experiences before they parse anything.

### 2. Focal point (2–4 seconds)

Where does your eye land first? That's the focal point. Is it the headline? The product UI? A photo? A logo? The focal point tells you what the site is selling.

### 3. Color story (4–6 seconds)

What's the dominant color? The accent? How much of each? A great site has a clear color story — "this is a teal site with cream surfaces and a coral accent" — not a confusing rainbow.

### 4. Typography (6–8 seconds)

What's the display face? The body face? Are the weights deliberate (3–5 weights) or lazy (regular + bold only)? Is the headline tight-tracked and large, or loose-tracked and medium?

### 5. Motion (8–10 seconds)

What's moving? What's still? Does the motion reveal information or decorate? Does it respect your time or make you wait?

### 6. Information hierarchy (10+ seconds)

After the first impression, parse the hierarchy. What's the H1? What's the H2? What's the CTA? What's secondary? A great site has 3 levels of hierarchy max — primary, secondary, tertiary. More levels = visual chaos.

---

## What to Steal vs What to Invent

### Steal (specific elements)

- **Layout patterns** — split hero, alternating feature cards, sticky-stack
- **Motion patterns** — choreography timing, easing curves, stagger
- **Copy formulas** — headline structures, CTA patterns, subhead mechanisms
- **Color relationships** — "warm accent on cool neutral" not "the exact hex #5E6AD2"
- **Type pairings** — "serif display + sans body" not "Tiempos + Söhne" (unless you have the license)
- **Information architecture** — page list, nav structure, footer organization
- **Interaction patterns** — tab-switcher, accordion, command-K palette

### Invent (the whole composition)

- **The exact palette** — never copy all 5 hexes from one reference
- **The exact headline copy** — formula yes, words no
- **The exact product UI** — your product is different
- **The exact photography** — your audience and product are different
- **The combination of borrows** — no one else should have Linear's choreography + Stripe's dividers + Vercel's terminal hero. That combination is yours.

### Never steal

- The brand identity (logo, exact brand mark, exact brand color)
- The exact photography
- The exact copy
- A reference site's signature interaction (e.g. Apple's "scrollytelling" product pages — too identifiable)

---

## Screenshot Tools

To analyze a reference, you'll need to capture it. Use these:

- **Full-page screenshot**: macOS `Cmd+Shift+4` then spacebar on the window; or use [GoFullPage](https://gofullpage.com/) Chrome extension. Captures the entire scroll height as one PNG.
- **Region screenshot**: macOS `Cmd+Shift+4`; Windows `Win+Shift+S`; Linux `gnome-screenshot -a`.
- **Video capture**: macOS `Cmd+Shift+5` for screen recording; [Loom](https://loom.com) for sharing.
- **Code inspection**: Chrome DevTools → Elements. Toggle device toolbar (`Cmd+Shift+M`) to see mobile layout.
- **Color picker**: macOS Digital Color Meter; [Sip](https://sipapp.io) for palette capture.
- **Font inspector**: [WhatFont](https://chrome.google.com/webstore/detail/whatfont/jabopobgcpjmedljpbcaablpmlmfcogm) Chrome extension; or DevTools → Computed → font-family.
- **Animation inspector**: DevTools → Animations tab. Records CSS animations and transitions on the page.

Save screenshots in a `/research/screenshots/` folder. Name them: `linear-home.png`, `stripe-pricing.png`, etc. Reference them in `DESIGN-RATIONALE.md`.

---

## The Research Worksheet Template

Print this. Fill it for every project. Don't start coding until it's complete.

```markdown
# Research Worksheet — [Project Name]

## Project brief
- Category: [saas-collab / portfolio / ecommerce / ...]
- Sub-category: [e.g. "async design review for product teams"]
- Target audience: [who they are, what they care about]
- Primary goal: [sign up / contact / buy / read]
- Vibe: [editorial / playful / premium / technical / ...]
- Reference category (from websites-100.json): [match key]

## Reference 1: [Site name] ([URL])
### Vibe (one word)
[e.g. "editorial-precise"]

### Layout
- Hero type: [split / centered / asymmetric / ...]
- Grid: [12-col / asymmetric / editorial 3-col]
- Density: [sparse / balanced / dense]
- Section rhythm: [hero → logos → features → ...]

### Palette
- bg: [#hex]
- surface: [#hex]
- text: [#hex]
- accent: [#hex] — [muted / saturated], [warm / cool]
- Light or dark default: [light / dark / toggle]

### Type
- Display: [family] [weight]
- Body: [family] [weight]
- Numeric / Mono: [if applicable]
- Type scale: [ratio]
- Letter-spacing treatments: [e.g. "-0.03em on H1"]

### Motion
- Hero choreography: [duration, sequence]
- Scroll animations: [list]
- Hover micro-interactions: [list]
- Easing curve: [estimate, e.g. "ease-out with slight overshoot"]

### Copy
- Voice: [formal / casual / technical / editorial]
- Headline formula: [e.g. "statement of fact, 6-8 words"]
- CTA pattern: [e.g. "action — outcome"]
- Sentence length: [short / medium / varied]

### IA
- Pages: [list]
- Nav structure: [list]
- Footer: [list]

### Borrows
- Borrow A: [specific element] — reason: [why]
- Borrow B: [specific element] — reason: [why]
- Borrow C: [specific element] — reason: [why]

### Avoids
- Avoid X: [what + why]
- Avoid Y: [what + why]

## Reference 2: [Site name] ([URL])
[same structure]

## Reference 3: [Site name] ([URL])
[same structure]

## Synthesis

### What I'm borrowing (combined list)
1. [from R1] — element — reason
2. [from R2] — element — reason
3. [from R3] — element — reason
[... 6–10 total borrows]

### What I'm inventing (the combination that's mine)
- The palette: [my specific 5-role palette, distinct from any one reference]
- The type pairing: [my specific 4-role system]
- The hero: [my specific layout, distinct from any one reference]
- The motion: [my specific choreography + interactions]
- The signature moment: [the one thing no reference has]

### What I'm explicitly NOT doing
- Not [reference 1's signature]: [why]
- Not [reference 2's signature]: [why]
- Not [the AI default]: [why]

## Files to consult
- /research/screenshots/ — saved reference screenshots
- /research/notes.md — this worksheet
- DESIGN-RATIONALE.md — the final committed borrows + rationales
```

---

## Anti-Patterns (Auto-Fail)

1. **No research phase.** Agent goes from "build a SaaS site" straight to code. Forbidden.
2. **Pulling references from training data instead of `websites-100.json`.** Training data is biased toward the most generic examples.
3. **Citing a reference without analyzing it.** "Inspired by Linear" with no breakdown of what's borrowed = clone.
4. **Borrowing the surface (the gradient, the radius) without understanding the why.** A direct copy without context is a generic copy.
5. **Borrowing a reference's exact palette.** Steal the relationship, not the hex.
6. **Borrowing a reference's exact headline formula AND words.** Formula yes, words no.
7. **Cloning a reference's signature interaction.** Apple's scrollytelling, Stripe's animated diagrams, Linear's hero — too identifiable.
8. **Not documenting borrows in `DESIGN-RATIONALE.md`.** No doc = no borrow = default.
9. **Pulling references that don't match the project vibe.** Awwwards-style portfolio references for a B2B SaaS will produce a confusing site.
10. **Using only one reference.** Three is the minimum. With one, you clone. With three, you synthesize.
11. **Skipping the "avoid" column.** Knowing what to avoid is as important as knowing what to borrow.
12. **Treating references as gospel.** References are starting points, not destinations. Disagree with them where they're wrong for your audience.

## Anti-Pattern: "I'll just use Dribbble"

Dribbble is for inspiration, not reference. Dribbble shots are concept work — they're not built, they don't ship, they don't get used. Reference real, shipped websites that real users interact with.

The same goes for Behance, Mobbin (better — those are real shipped apps), and most Pinterest mockups. The web is your reference library. Use it.

---

## Anti-Pattern: Trend-chasing

A reference from 2018 may still be great. A trend from 2024 may already be tired. Don't pick references because they're new — pick them because they work for your audience.

Trends that are already tired (avoid copying):
- Bento grids for everything (Apple did it great in 2023, everyone copied in 2024, it's now a cliché)
- Animated gradient text on hero headlines
- 3D scrolling product reveals
- Glassmorphism cards on flat backgrounds
- "Spinning globe" hero animations

Trends that are still fresh (use sparingly):
- Scroll-driven animations (CSS native, low cost)
- View Transitions API for route changes
- Editorial-magazine layouts in SaaS
- Asymmetric grids (when done deliberately)
- Real photography over illustrations

---

## Output

When you finish this guide, you should have:
- A `Research Worksheet` filled in with 3 references analyzed across 6 dimensions each
- 6–10 specific borrows documented in `DESIGN-RATIONALE.md`, each with a reason
- 3–6 explicit avoids documented
- A "synthesis" section stating what you're inventing (the combination that's yours)
- Screenshots saved in `/research/screenshots/` for each reference
- A clear sense of what the AI default for this category is, and why you're deviating
- No more than one element borrowed from any single reference (otherwise it's a clone)
- A written answer to: "If the user says 'this looks like X', what do I say?"
