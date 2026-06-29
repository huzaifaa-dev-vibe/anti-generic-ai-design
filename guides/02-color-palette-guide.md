# 02 — Color Palette Guide

> Color is the loudest design decision. Get it wrong and no amount of typography or motion will save you. Get it right and the page reads as designed before the user parses a single word.

## Why AI color choices fail

Every LLM-coded site defaults to the same palette: indigo `#6366F1` → violet `#8B5CF6` → pink `#EC4899`. This isn't a coincidence — it's the Tailwind default purple/pink scale, and LLMs have seen it 100,000 times in training data. The result: every AI site looks like every other AI site.

**The fix**: pick from `data/palettes-100.json`, which contains 100 hand-curated palettes with provenance, contrast ratios, and use-cases. Never invent a palette from scratch unless you can defend every hex.

---

## The 5-Role Palette System

Every palette must define 5 roles. No more, no less.

| Role | Variable | Use | Coverage |
|------|----------|-----|----------|
| `bg` | `--bg` | Page background | 60% of pixels |
| `surface` | `--surface` | Cards, panels, raised surfaces | 15% |
| `text` | `--text` | Body copy, headings | 15% |
| `accent` | `--accent` | CTAs, links, key data | 5% |
| `muted` | `--muted` | Secondary text, borders, dividers | 5% |

The 60/15/15/5/5 split is the **60-30-10 rule** adapted for digital. Get the proportions right and even a mediocre palette looks composed. Get them wrong and even a great palette looks chaotic.

## Contrast — Non-Negotiable

| Pairing | Minimum (WCAG AA) | Ideal (AAA) |
|---------|-------------------|-------------|
| Body text on background | 4.5:1 | 7:1 |
| Large text (≥24px / ≥18.66px bold) on background | 3:1 | 4.5:1 |
| UI components (button text, icon strokes) | 3:1 | 4.5:1 |
| Non-text contrast (borders on focus indicators) | 3:1 | 4.5:1 |

**Verify before shipping.** Use the `contrast_ratios` field in `data/palettes-100.json` — it's pre-computed. If you modify a palette, recompute with [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

## Picking a Palette — Decision Tree

```
1. What's the project category?
   ├── SaaS / B2B → cool neutrals + 1 accent (see palettes tagged "professional")
   ├── Portfolio / creative → bold accent + dark or off-white bg ("editorial")
   ├── E-commerce → trust-building + accent for CTAs ("commerce")
   ├── Dashboard / data → low-chroma bg + semantic colors ("data")
   ├── Media / publication → editorial neutrals + 1 strong accent ("editorial")
   └── Personal / blog → warm neutrals + 1 personality accent ("warm")

2. What's the audience's emotional state?
   ├── Calm / trust (finance, healthcare) → desaturated, blue/green/teal
   ├── Energy / excitement (consumer, gaming) → saturated, warm
   ├── Curiosity / learning (education) → mid-saturation, varied
   └── Luxury / exclusivity (premium, fashion) → near-black + 1 metallic or jewel tone

3. Light or dark default?
   ├── Light → bg #FFFFFF or warm off-white (#FAF9F6, #F7F5F0)
   ├── Dark → bg #0A0A0B or warm dark (#0E0E10, #14110F), never pure #000
   └── Toggle → design both, set prefers-color-scheme

4. Pick the accent.
   ├── Not indigo. Not violet. Not the Tailwind purple scale.
   ├── Pick a color with a story: "we chose oxblood (#7B1E1E) because the audience is legal professionals and oxblood reads gravitas without being funereal"
   └── Test the accent on both bg and surface — it must pop on both

5. Verify contrast and ship.
```

## Color Theory Crash Course

### Hue relationships

| Relationship | Example | Effect |
|--------------|---------|--------|
| Monochromatic | All blues, varied lightness | Calm, unified, easy |
| Analogous | Blue → teal → green | Harmonious, natural |
| Complementary | Blue + orange | High contrast, energetic |
| Triadic | Red + yellow + blue | Playful, complex |
| Split-complementary | Blue + yellow-orange + red-orange | Balanced tension |

**For UI**: monochromatic or analogous is almost always right. Complementary is for one accent vs one base (e.g. blue site with orange CTAs). Triadic is for brands that need playfulness (children's products, gaming).

### Saturation discipline

Most AI sites are too saturated. **Desaturate your accent by 15–20%** and the page instantly looks more designed.

- Bad: `#FF0000` (pure red)
- Better: `#C73232` (slightly desaturated red)
- Best: `#A82828` (muted, editorial red)

### Temperature

Warm colors (red/orange/yellow) advance — they feel closer, more energetic, more urgent. Cool colors (blue/green/violet) recede — they feel calmer, more distant, more professional.

A page that's all cool will feel sterile. A page that's all warm will feel aggressive. **Pair them**: cool base + warm accent, or vice versa.

### The "off-white" rule

Pure white `#FFFFFF` is harsh. For light themes, prefer:
- `#FAFAFA` — neutral cool off-white
- `#F7F5F0` — warm off-white (paper)
- `#F4F4F1` — warm gray off-white

For dark themes, pure black `#000000` is equally harsh. Prefer:
- `#0A0A0B` — near-black, slight cool
- `#0E0E10` — neutral near-black
- `#14110F` — warm near-black (luxury)

## Dark Mode Specifics

See `guides/16-dark-mode-guide.md` for the full treatment. Short rules:

- Don't invert a light palette 1:1. Dark mode needs its own palette.
- Surfaces should be **lighter** than the bg, not darker. (`surface: #18181B` over `bg: #0A0A0B`.)
- Text on dark should be `#E4E4E7` or similar — pure `#FFFFFF` is too bright.
- Drop shadows don't work on dark. Use `border: 1px solid rgba(255,255,255,0.08)` for separation.
- Saturated colors glow on dark. Desaturate accents by 10–15% for dark mode.

## Semantic Colors

Every palette needs semantic colors for status:

| Status | Hex range | Example |
|--------|-----------|---------|
| Success | Green, slightly desaturated | `#16A34A` or `#15803D` |
| Warning | Amber/orange, not pure yellow | `#D97706` or `#CA8A04` |
| Error | Red, slightly desaturated | `#DC2626` or `#B91C1C` |
| Info | Blue, slightly desaturated | `#2563EB` or `#1D4ED8` |

These should harmonize with the accent — pick green/amber/red/blue from the same hue family as your accent where possible.

## The "One Accent" Rule

Most sites need exactly **one accent color**. The accent is for:
- Primary CTAs
- Links in body copy
- Active nav state
- Key data points in charts

Everything else is a neutral or a semantic. If you have two accents (e.g. brand orange + a secondary teal), one is the primary accent and the other is a **supporting color** — used 1/10th as often.

## Forbidden Palettes (Auto-Fail)

1. **Indigo → violet → pink gradient** (the AI default). Banned.
2. **Pure RGB primaries** (`#FF0000`, `#00FF00`, `#00FFFF`). Looks like MS Paint.
3. **Tailwind default `slate` + `indigo`** combo. The most common AI palette.
4. **Pure black on pure white** with no off-whites. Harsh, unedited.
5. **Grayscale + any saturated color** that hasn't been tuned. Looks like a developer picked it.

## CSS Variable Setup

```css
:root {
  /* Light theme */
  --bg: #FAFAFA;
  --surface: #FFFFFF;
  --text: #18181B;
  --accent: #B45309;        /* amber-700 — warm, editorial */
  --muted: #71717A;
  --border: rgba(24, 24, 27, 0.08);

  /* Semantic */
  --success: #15803D;
  --warning: #B45309;
  --error: #B91C1C;
  --info: #1D4ED8;

  /* Tints of accent (precomputed, not opacity) */
  --accent-soft: #FDE68A;
  --accent-strong: #92400E;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0A0A0B;
    --surface: #18181B;
    --text: #E4E4E7;
    --accent: #F59E0B;      /* brighter amber for dark bg */
    --muted: #A1A1AA;
    --border: rgba(255, 255, 255, 0.08);
  }
}
```

## Tooling

- [Realtime Colors](https://realtimecolors.com/) — live preview palette + fonts on a real layout
- [Coolors](https://coolors.co/) — palette generator (use for inspiration, not as your source of truth)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — verify ratios
- [Tailwind CSS Color Picker](https://uicolors.app/) — generate Tailwind shades from a single hex

## Output

When you finish this guide, you should have:
- A palette object with all 5 roles + 4 semantic colors + 2–3 accent tints
- CSS variables defined for both light and dark
- Contrast ratios verified for body/surface, body/bg, accent/surface, accent/bg
- A `vibe` and `rationale` written into `DESIGN-RATIONALE.md`
- **No** forbidden palettes
