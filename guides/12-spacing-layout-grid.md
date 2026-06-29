# 12 — Spacing, Layout & Grid

> Whitespace is the silent language of design. The eye reads spacing before it reads words. AI-coded sites treat spacing as an afterthought — `py-24` here, `gap-4` there, `max-w-7xl mx-auto` everywhere — and the result is a page that feels like a draft, not a design.

## Why AI fails at spacing and layout

Three defaults ruin every AI layout:

1. **`max-w-7xl mx-auto` for every section.** This is the Tailwind marketing-page reflex. It produces a page where every block is the same width, regardless of content type. A pricing table should not be the same width as a testimonial.
2. **`py-24` between every section.** Vertical rhythm becomes a single boring note — 96px, 96px, 96px, 96px. No cadence, no rest, no emphasis.
3. **Tailwind's default 4px base.** It's not an 8pt system. `gap-3` (12px), `gap-5` (20px), `gap-7` (28px) — these are arbitrary 4px multiples. Real designers use an 8pt grid because 8 divides cleanly into 16, 24, 32, 48, 64, 96, 128 and produces visually harmonious rhythm.

The default AI page is a stack of full-bleed sections, each `max-w-7xl`, each `py-24`, each with `grid md:grid-cols-3 gap-8` inside. That is not a layout. That is a template.

---

## Rule 1 — Adopt the 8pt spacing system

Every spacing value in your design is a multiple of 8. The exceptions are 4 (half-step for tight UI like input padding) and 2 (for hairline gaps between icons and labels).

```css
:root {
  /* 8pt base scale */
  --space-0:  0;
  --space-1:  0.25rem;   /* 4px  — hairline */
  --space-2:  0.5rem;    /* 8px  — tight */
  --space-3:  0.75rem;   /* 12px — input padding */
  --space-4:  1rem;      /* 16px — body text rhythm */
  --space-5:  1.5rem;    /* 24px — component gap */
  --space-6:  2rem;      /* 32px — card padding */
  --space-7:  3rem;      /* 48px — section sub-gap */
  --space-8:  4rem;      /* 64px — section gap */
  --space-9:  6rem;      /* 96px — hero padding */
  --space-10: 8rem;      /* 128px — major section break */
  --space-11: 12rem;     /* 192px — page-level breathing room */
}
```

**Why 8, not 4?** Because at 4px the eye can't perceive the difference between 16 and 20. At 8pt, every step is unambiguous. Designers from Massimo Vignelli onward have used 8pt (or its typographic cousin, the baseline grid) because it produces rhythm that the eye reads as "designed".

Use Tailwind? Map them: `gap-2 = 8px`, `gap-4 = 16px`, `gap-6 = 24px`, `gap-8 = 32px`, `gap-12 = 48px`, `gap-16 = 64px`, `gap-24 = 96px`, `gap-32 = 128px`. **Avoid `gap-3`, `gap-5`, `gap-7`** — they're the 4px system and break rhythm.

## Rule 2 — Use modular vertical rhythm

A page is music. If every section has the same vertical gap, the page is a single note. Real layouts have cadence: small gaps inside components, medium gaps between features in a section, large gaps between major sections, and one or two very large gaps to separate top-level acts.

```css
:root {
  /* Component-internal gaps */
  --gap-tight:   var(--space-2);    /* 8px  — icon-to-label */
  --gap-default: var(--space-4);    /* 16px — element-to-element */
  --gap-loose:   var(--space-5);    /* 24px — between cards */

  /* Section-internal gaps */
  --section-inner: var(--space-7);  /* 48px — header-to-content in a section */

  /* Page-level section gaps */
  --section-gap:  var(--space-8);   /* 64px — default between sections */
  --section-gap-lg: var(--space-9); /* 96px — between major acts */
  --section-gap-xl: var(--space-10);/* 128px — only 1-2 per page */
}

.stack-default > * + * { margin-top: var(--gap-default); }
.stack-loose > * + *   { margin-top: var(--gap-loose); }
.section-stack > * + * { margin-top: var(--section-gap); }
```

A typical page rhythm: hero → 64px → features → 96px → proof → 64px → pricing → 128px → testimonial wall → 64px → footer. Notice the 128px gap once — that's the "act break" that says "we're entering a new phase of the story".

## Rule 3 — Pick a modular scale for type spacing

Type spacing (line-height, paragraph spacing, list gap) should follow the same modular scale as type size (see guide 03). Don't use ad-hoc `mt-6` everywhere.

```css
:root {
  /* Type-aligned paragraph spacing = 1x line height */
  --paragraph-gap: 1.5rem;          /* matches 1.5 line-height at 1rem */
  --list-gap: 0.75rem;
  --heading-to-body: 1.5rem;
  --body-to-heading: 2.5rem;        /* larger gap above a heading than below */
}
```

**Always larger gap above a heading than below it.** The heading belongs to the content that follows it, not the content above. AI sites ship `mt-8 mb-4` symmetrically — wrong. Use `mt-10 mb-3`.

## Rule 4 — Container widths: pick the right max-width

The `max-w-7xl` (1280px) reflex is wrong for 80% of sections. Use this decision table:

| Content type | Max-width | Tailwind | Why |
|--------------|-----------|----------|-----|
| Long-form prose, blog post, docs | 65ch (~680px) | `max-w-prose` | Optimal reading line length |
| Article with sidebar, narrow column | 720px | `max-w-3xl` | Wider than prose for code blocks |
| Marketing section, feature grid | 1152px | `max-w-6xl` | The visual sweet spot |
| Hero, pricing table, dense grid | 1280px | `max-w-7xl` | Wide sections that earn it |
| Logo strip, stats row | 1440px | `max-w-screen-2xl` | Wide, airy |
| Full-bleed image / video / banner | 100% | (none) | Edge-to-edge |
| Pull quote, callout | 880px | `max-w-4xl` | Tighter than prose for emphasis |

**Rule of thumb**: if the content is text, use `max-w-prose` or `max-w-3xl`. If it's a grid of cards, use `max-w-6xl`. Only use `max-w-7xl` when you have a 3+ column grid that needs the room. `max-w-7xl` for a centered hero headline is wrong — it stretches the line past the 65ch reading width.

## Rule 5 — CSS Grid vs Flexbox: pick deliberately

**Use Flexbox** for one-dimensional layouts: a row of buttons, a stack of menu items, a header with logo on the left and nav on the right, a card with an icon and label inline.

**Use CSS Grid** for two-dimensional layouts: a 3-column feature grid, a dashboard with multiple areas, a bento layout, an asymmetric editorial spread.

```css
/* Flexbox: 1D, content-driven */
.button-row {
  display: flex;
  gap: var(--space-3);
  align-items: center;
  justify-content: flex-end;
}

.site-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-6);
}

/* CSS Grid: 2D, structure-driven */
.feature-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

.bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: 200px 200px 200px;
  gap: var(--space-4);
}

.bento-hero { grid-column: span 2; grid-row: span 2; }
.bento-tall { grid-column: span 1; grid-row: span 3; }
```

**The decision test**: "Do I need to control both the rows and the columns?" If yes → Grid. If only one → Flexbox. If you don't know → it's a Grid, because Grid is implicit when both dimensions matter.

## Rule 6 — The 12-column grid (and when to break it)

The 12-column grid comes from print (Jan Tschichold, Müller-Brockmann). 12 divides by 2, 3, 4, 6 — enough flexibility for almost any layout.

```css
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}

.col-3  { grid-column: span 3; }
.col-4  { grid-column: span 4; }
.col-6  { grid-column: span 6; }
.col-8  { grid-column: span 8; }
.col-9  { grid-column: span 9; }
.col-12 { grid-column: span 12; }

/* Editorial 7/5 split */
.editorial-left  { grid-column: 1 / span 7; }
.editorial-right { grid-column: 8 / span 5; }

/* Sidebar + content 3/9 */
.with-sidebar { grid-template-columns: 240px 1fr; }
```

**Break the 12-column grid when**:
- The design is editorial / asymmetric and the grid is fighting you (use named lines or asymmetric `grid-template-columns`).
- The layout is a bento (use `grid-template-areas` instead).
- The page has a single column of prose (use `max-w-prose`, no grid).

**Never break it when**:
- You're building a marketing page with feature cards.
- You're building a dashboard.
- You're not sure — the 12-column grid is the safe default that prevents you from inventing a worse one.

## Rule 7 — Bento layouts: when and how

Bento (named after the Japanese lunch box) is the grid style where cards of different sizes tile a rectangle. Apple's product pages popularized it; Linear's marketing site perfected it.

Use bento when:
- You have 4–8 features of varying importance.
- You want to break out of the "3 equal cards" reflex.
- The brand voice is "premium / crafted".

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  grid-auto-rows: minmax(160px, auto);
  gap: var(--space-4);
}

.bento-grid > *:nth-child(1) { grid-column: span 4; grid-row: span 2; } /* hero */
.bento-grid > *:nth-child(2) { grid-column: span 2; grid-row: span 1; }
.bento-grid > *:nth-child(3) { grid-column: span 2; grid-row: span 1; }
.bento-grid > *:nth-child(4) { grid-column: span 3; grid-row: span 1; }
.bento-grid > *:nth-child(5) { grid-column: span 3; grid-row: span 1; }
```

Bento rules:
- One tile is the "hero" — at least 2× the area of any other.
- No more than 3 distinct tile sizes per bento.
- Equal gap between all tiles. Don't vary the gap to "fix" alignment — vary the tile sizes.
- Each tile has its own visual language (color, texture) but they share a border-radius.

## Rule 8 — Asymmetric layouts: when and how

Symmetry is the AI default. Asymmetry is the senior-designer move — but only when it carries meaning.

```css
/* 7/5 split: editorial */
.split-editorial {
  display: grid;
  grid-template-columns: 7fr 5fr;
  gap: var(--space-9);
  align-items: center;
}

/* 2/10 split: sidebar + content */
.split-sidebar {
  display: grid;
  grid-template-columns: minmax(180px, 2fr) 10fr;
  gap: var(--space-8);
}

/* 5/7 reversed */
.split-reverse {
  display: grid;
  grid-template-columns: 5fr 7fr;
  gap: var(--space-9);
}
```

Use asymmetry when:
- You want one side to dominate (e.g. product screenshot deserves 7/12, headline deserves 5/12).
- You're building an editorial spread.
- The content naturally has a primary and secondary element.

Don't use asymmetry when:
- The two sides are equal in importance.
- The page is a list (use a uniform grid).

## Rule 9 — Container queries: the modern breakpoint

Media queries are viewport-based. Container queries are component-based — they let a card adapt based on its own width, not the viewport. This is the right primitive for design systems.

```css
.card-container { container-type: inline-size; }

.card {
  display: grid;
  gap: var(--space-4);
}

@container (min-width: 480px) {
  .card {
    grid-template-columns: 120px 1fr;
    align-items: start;
  }
}

@container (min-width: 720px) {
  .card {
    grid-template-columns: 200px 1fr auto;
  }
}
```

Use container queries when:
- A component must adapt across multiple contexts (sidebar, full-width, in a grid, in a modal).
- You're building a design system.
- You're tired of writing `@media (min-width: 768px)` for what is really a component-level concern.

Use media queries when:
- The entire page layout needs to change (mobile nav, off-canvas menu).
- You're adjusting the root font-size or page padding.

## Rule 10 — Padding discipline

Component padding follows a rule: the larger the component, the larger the padding. **The same padding across all components is the most common AI mistake.**

```css
.input       { padding: var(--space-2) var(--space-3); }   /* 8px 12px */
.button      { padding: var(--space-2) var(--space-4); }   /* 8px 16px */
.card        { padding: var(--space-5); }                  /* 24px */
.card-lg     { padding: var(--space-6); }                  /* 32px */
.panel       { padding: var(--space-6); }                  /* 32px */
.modal       { padding: var(--space-7); }                  /* 48px */
.section     { padding: var(--space-8) 0; }                /* 64px 0 */
.hero        { padding: var(--space-9) 0; }                /* 96px 0 */
```

**Vertical vs horizontal asymmetry**: section padding is almost always asymmetric — large vertical, smaller horizontal (because horizontal is governed by `max-width` and outer container padding).

## Rule 11 — Whitespace as a design element

Whitespace is not "empty space". It is the design element that creates hierarchy, rest, and emphasis. Massimo Vignelli built an entire career on the principle that what you leave out matters more than what you put in.

Tactics:
- **Isolate the CTA.** A button with 64px of space around it gets more clicks than a button surrounded by 12px of other content.
- **Rest between sections.** Don't fill every gap with content. Let one section breathe before the next.
- **One empty section per page.** A page with no whitespace is exhausting. A page with one deliberately empty area (e.g. a hero with no nav, no badges, just a headline and CTA) feels composed.
- **Use whitespace to create columns where there are none.** Two paragraphs side by side with a 96px gap reads as two columns, even without a divider.

## Rule 12 — Define spacing tokens once, use everywhere

```css
:root {
  /* Page rhythm */
  --page-x-padding: var(--space-5);     /* 24px on mobile */
  --section-y-padding: var(--space-8);  /* 64px default */

  /* Component padding */
  --pad-input:  var(--space-2) var(--space-3);
  --pad-button: var(--space-2) var(--space-4);
  --pad-card:   var(--space-5);
  --pad-modal:  var(--space-7);

  /* Gaps */
  --gap-inline:   var(--space-3);       /* icon + label */
  --gap-stack:    var(--space-4);       /* stacked elements */
  --gap-card:     var(--space-5);       /* between cards in a grid */
  --gap-section:  var(--space-8);       /* between sections */
}

@media (min-width: 768px) {
  :root {
    --page-x-padding: var(--space-8);   /* 32px on desktop */
  }
}
```

## Anti-Patterns (Auto-Fail)

1. **`max-w-7xl mx-auto` on every section.** Variation is mandatory.
2. **`py-24` on every section.** Vary the vertical rhythm.
3. **4px-based spacing** (`gap-3`, `gap-5`, `gap-7`). Use 8pt.
4. **Symmetric padding above and below headings** (`mt-8 mb-8`). Use asymmetric: `mt-10 mb-3`.
5. **Three equal cards** in every section. Vary card sizes; use bento when appropriate.
6. **`gap-4` inside a card AND between cards.** Inner gap should be smaller than outer gap.
7. **Centered everything.** Centered headline + centered subhead + centered CTA + centered logos. Centering is one tool, not a layout strategy.
8. **Fixed pixel widths** (`width: 380px`). Use `fr`, `minmax()`, or percentages.
9. **No `max-width` on body text.** Lines stretch to 1200px and become unreadable.
10. **CSS Grid for a single row** of buttons. Use Flexbox for 1D, Grid for 2D.
11. **Container query overuse.** They're powerful but add cognitive load. Use when a component lives in multiple contexts.
12. **Bento layouts with more than 3 tile sizes.** Becomes chaos.

## Code Example — A Composed Section

```tsx
<section style={{ paddingBlock: 'var(--space-9)' }}>
  <div style={{
    maxWidth: 'var(--max-w-6xl, 72rem)',
    marginInline: 'auto',
    paddingInline: 'var(--page-x-padding)',
  }}>
    <header style={{ marginBottom: 'var(--section-inner)', maxWidth: '48rem' }}>
      <p className="overline">Section overline</p>
      <h2 style={{ marginTop: 'var(--space-3)' }}>A headline that earns the space</h2>
      <p style={{ marginTop: 'var(--space-4)', maxWidth: '52ch' }}>
        A subhead that respects reading width. 52 characters.
      </p>
    </header>

    <div style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
      gap: 'var(--gap-card)',
    }}>
      {/* Cards */}
    </div>
  </div>
</section>
```

## Output

When you finish this guide, you should have:
- An 8pt spacing scale as CSS variables (0, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192)
- A max-width decision table for which `max-w-*` to use per section type
- At least one CSS Grid layout (12-col or bento) and one Flexbox layout, justified in `DESIGN-RATIONALE.md`
- Container queries used for at least one component that lives in multiple contexts
- A vertical rhythm plan: which section gaps are 64px, which are 96px, which are 128px
- Padding tokens for input / button / card / modal / section / hero
- No 4px-based spacing (`gap-3`, `gap-5`, `gap-7`) anywhere in the codebase
- No `max-w-7xl mx-auto` reflex — each section's max-width is justified by content
