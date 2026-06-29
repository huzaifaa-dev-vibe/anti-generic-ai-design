# 03 — Font Pairing Guide

> Typography is 95% of web design. Get it right and the page reads as designed even with no color. Get it wrong and no palette saves you.

## Why AI typography fails

Three defaults ruin AI sites:

1. **Inter everywhere.** Inter is a great UI face. It is not a display face. Using it for H1s makes every page feel like a SaaS dashboard.
2. **Single-weight everything.** LLMs ship `font-normal` for body and `font-bold` for headings. Real typography uses 4–6 weights deliberately.
3. **No numeric or mono variants.** Dashboards, pricing tables, and code blocks need tabular numerals and a mono face. AI ships Inter for everything, and the numbers wobble.

**The fix**: pick from `data/font-pairs-100.json`, which contains 100 curated pairings with rationale, fallbacks, and loading strategy.

---

## The 4-Role Type System

| Role | Variable | Use | When required |
|------|----------|-----|---------------|
| `--font-display` | Display face | H1, hero, large numbers | Always (for non-dashboard sites) |
| `--font-body` | Body face | Paragraphs, lists, captions | Always |
| `--font-numeric` | Numeric face | Stats, prices, dates | Dashboards, SaaS, e-commerce |
| `--font-mono` | Monospace face | Code, kbd, technical labels | Dev tools, docs, dashboards |

A simple blog might use only `display + body`. A SaaS dashboard needs all four. Pick the right number of roles for the project.

## Pairing Principles

### 1. Contrast in classification

Pair a **serif** display with a **sans-serif** body, or vice versa. Two sans-serifs can work if they're stylistically different (e.g. geometric display + humanist body), but two serifs of similar classification look muddy.

| Display | Body | Works? | Why |
|---------|------|--------|-----|
| Serif (Playfair) | Sans (Inter) | ✅ | High contrast in classification |
| Sans (Geist) | Sans (Inter) | ⚠️ | Low contrast — only works with strong weight difference |
| Mono (JetBrains) | Sans (Inter) | ✅ | Strong contrast, dev-tool vibe |
| Serif (Tiempos) | Serif (Source Serif) | ❌ | Too similar, muddies hierarchy |

### 2. Contrast in weight

If display and body are the same family, they MUST differ by at least 2 weights. Display `900` + body `400` works. Display `500` + body `400` does not.

### 3. x-height compatibility

The body face's x-height should be **similar to or larger than** the display face's. If the body face has a tiny x-height (e.g. Georgia) paired with a display face that has a huge x-height (e.g. Söhne), the body looks anemic.

### 4. Mood alignment

A playful display (e.g. a rounded face like Quicksand) fights a serious body (e.g. IBM Plex Sans). The two faces must agree on mood:
- **Editorial / serious**: Tiempos, Source Serif, Crimson Pro + Inter, IBM Plex Sans
- **Tech / precise**: Geist, Söhne, Inter + JetBrains Mono for accents
- **Warm / humanist**: Söhne, Inter + Lora, Source Serif
- **Playful / brand**: Fraunces (with optical sizing), Bricolage Grotesque + Inter

## Font Categories — When to Use Each

### Sans-serif body faces (the safe default)

| Font | Vibe | Best for |
|------|------|----------|
| Inter | Neutral, modern, slightly clinical | SaaS, dashboards, dev tools |
| Geist | Geometric, precise, slightly warmer | Modern dev tools (Vercel aesthetic) |
| IBM Plex Sans | Technical, humanist | Enterprise, docs, technical content |
| Söhne (paid) | Editorial, premium | High-end SaaS, agencies |
| Manrope | Geometric, friendly | Consumer SaaS, marketing |
| DM Sans | Geometric, neutral | Marketing pages, blogs |
| General Sans | Geometric, modern | Editorial SaaS |

### Serif body faces (for reading-heavy sites)

| Font | Vibe | Best for |
|------|------|----------|
| Source Serif | Neutral, readable | Long-form articles, docs |
| Lora | Warm, slightly calligraphic | Blogs, magazines |
| Crimson Pro | Old-style, readable | Long-form reading |
| Newsreader | Editorial, contemporary | Publications, journalism |
| PT Serif | Workhorse serif | Generic long-form |

### Display faces (the differentiator)

| Font | Vibe | Best for |
|------|------|----------|
| Playfair Display | High-contrast, fashion | Luxury, fashion, editorial |
| Fraunces (with optical) | Variable, expressive | Brand sites, portfolios |
| Bricolage Grotesque | Modern, expressive | Creative agencies, portfolios |
| Tiempos (paid) | Editorial, premium | High-end publications |
| Söhne (paid) | Modern grotesque | Premium SaaS |
| Big Shoulders | Condensed, impactful | News, sports, bold brands |
| Instrument Serif | Free, expressive | Editorial SaaS |

### Mono faces (for code / technical UI)

| Font | Vibe | Best for |
|------|------|----------|
| JetBrains Mono | Ligatures, readable | Dev tools, code blocks |
| Geist Mono | Variable, modern | Modern dev tools |
| IBM Plex Mono | Technical, humanist | Enterprise, technical |
| Berkeley Mono (paid) | Editorial, premium | High-end dev tools |
| Space Mono | Distinctive, retro | Creative / brand |

## Numeric Faces — The Forgotten Role

For dashboards, pricing tables, and stat-heavy hero sections, use **tabular figures**. Without them, numbers shift width as they change, which looks broken.

```css
.stat-number {
  font-family: var(--font-numeric);
  font-feature-settings: "tnum" 1, "lnum" 1;  /* tabular + lining nums */
}
```

If your body face supports `tnum` (Inter, IBM Plex, Geist all do), you can use it for numerics. Otherwise pair a dedicated numeric face like **Söhne Mono** or **JetBrains Mono**.

## The Default Forbidden Pairing

**Inter (display) + Inter (body)** is forbidden. If you must use Inter for body, pair with:
- A real display face (Fraunces, Bricolage, Playfair, Instrument Serif), OR
- Inter Display (the optical variant) at a much heavier weight

## Loading Strategy

### Google Fonts (free, easy, slightly slow)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Fraunces:opsz,wght@9..144,500;9..144,700&display=swap" rel="stylesheet">
```

### Fontsource (self-hosted, faster, more reliable)

```bash
npm install @fontsource/inter @fontsource/fraunces
```

```tsx
import '@fontsource/inter/400.css';
import '@fontsource/inter/500.css';
import '@fontsource/inter/600.css';
import '@fontsource/fraunces/500.css';
import '@fontsource/fraunces/700.css';
```

### Self-hosted (premium fonts)

For paid fonts (Söhne, Tiempos, Berkeley Mono), self-host with `@font-face` and subset to the character sets you actually need.

### Performance rules

- **Preload** only the body face's regular weight. Display weights load on demand.
- **Subset** to `latin` + `latin-ext` unless you need CJK / Cyrillic / Arabic.
- **`font-display: swap`** for body (avoid FOIT), `optional` for display (avoid layout shift if it loads slow).
- **Maximum 4 web font files** total. Each file is a network request.

## Type Scale

Use a **modular scale**, not arbitrary sizes. Pick a ratio and stick to it.

| Ratio | Name | Use case |
|-------|------|----------|
| 1.125 | Major second | Dense dashboards, docs |
| 1.2 | Minor third | General SaaS, balanced |
| 1.25 | Major third | Marketing, editorial |
| 1.333 | Perfect fourth | Editorial, blog |
| 1.5 | Perfect fifth | Bold hero, big type |

```css
:root {
  --step--1: 0.833rem;   /* 13.33px */
  --step-0:  1rem;       /* 16px */
  --step-1:  1.2rem;     /* 19.2px */
  --step-2:  1.44rem;    /* 23px */
  --step-3:  1.728rem;   /* 27.6px */
  --step-4:  2.074rem;   /* 33.2px */
  --step-5:  2.488rem;   /* 39.8px */
  --step-6:  2.986rem;   /* 47.8px */
  --step-7:  3.583rem;   /* 57.3px */
}
```

## Line Height & Tracking

| Element | Line height | Letter tracking |
|---------|-------------|-----------------|
| Body (16–20px) | 1.5–1.7 | 0 |
| Small body (≤14px) | 1.45 | +0.01em |
| H1 (≥40px) | 1.05–1.15 | -0.02em to -0.04em |
| H2 | 1.15–1.25 | -0.01em to -0.02em |
| H3 | 1.25–1.35 | 0 to -0.01em |
| Display (≥60px) | 1.0–1.1 | -0.03em to -0.05em |
| Caption / overline | 1.4 | +0.05em to +0.1em, uppercase |

**Big type needs tight tracking. Small type needs loose tracking.** LLMs ship everything at `tracking-normal` which makes headlines look amateur.

## Anti-Patterns (Auto-Fail)

1. **Inter for everything** (display + body + numeric). Forbidden.
2. **One weight only.** Need at least 3 weights (regular, medium, bold).
3. **`tracking-normal` on a 60px headline.** Tighten to -0.03em.
4. **`leading-relaxed` (1.625) on a 48px H1.** Tighten to 1.1.
5. **Roboto + Open Sans.** Both overused, both bland.
6. **Pure system font stack** (`-apple-system, BlinkMacSystemFont`). Fine for an internal tool, banned for a marketing site.
7. **Mixed rendering** — some text anti-aliased, some not. Set `-webkit-font-smoothing: antialiased` globally.
8. **More than 4 web font files.** Performance killer.

## CSS Variable Setup

```css
:root {
  --font-display: 'Fraunces', 'Times New Roman', serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-numeric: 'Inter', sans-serif;  /* supports tnum */
  --font-mono: 'JetBrains Mono', 'Courier New', monospace;

  --font-body-weight: 400;
  --font-body-weight-medium: 500;
  --font-body-weight-bold: 600;

  --font-display-weight: 500;
  --font-display-weight-bold: 700;
}

body {
  font-family: var(--font-body);
  font-weight: var(--font-body-weight);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: var(--font-display-weight);
  letter-spacing: -0.02em;
  line-height: 1.1;
}
```

## Tooling

- [Google Fonts](https://fonts.google.com/) — free fonts
- [Fontsource](https://fontsource.org/) — self-host the Google Fonts catalog
- [Typ.io](https://typ.io/) — real-world font pairings on live sites
- [Typescale](https://typescale.com/) — modular scale calculator
- [Font Pair](https://www.fontpair.co/) — pairing inspiration

## Output

When you finish this guide, you should have:
- A 4-role type system (or 2–3 roles for simpler projects)
- Fonts loaded via Google Fonts, Fontsource, or self-hosted (max 4 files)
- CSS variables for each role + weights
- A modular type scale committed
- Line-height and tracking rules per element
- No anti-patterns present
