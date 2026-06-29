# Templates

Drop-in React + TypeScript + Tailwind components and CSS utilities. Use these as your starting point — never start from `<div className="container">`.

## Structure

```
templates/
├── hero/
│   ├── hero-split.tsx              ← Split hero (text left, product right) — SaaS default
│   ├── hero-asymmetric.tsx         ← Editorial-style, breaks the grid
│   ├── hero-product-first.tsx      ← Terminal/code hero with headline below — dev tools
│   └── hero-video-bg.tsx           ← Cinematic video background
├── components/
│   ├── glass-card.tsx + .css       ← Real glassmorphism (5-layer system)
│   ├── animated-nav.tsx            ← Sticky glass nav that shrinks on scroll
│   ├── gradient-text.tsx + .css    ← Non-default gradient text (8 presets, no AI purple)
│   ├── bento-grid.tsx              ← Asymmetric bento layout (replaces 3-card grids)
│   ├── magnetic-button.tsx         ← Cursor-attracting button (hero CTA only)
│   ├── counter.tsx                 ← Animated number counter
│   └── scroll-reveal.tsx           ← Triggered fade/slide-in (use sparingly!)
└── styles/
    ├── tokens.css                  ← Design tokens (CSS variables for palette + type + spacing)
    ├── glassmorphism.css           ← Glass utility classes
    └── animations.css              ← Animation utility classes
```

## Setup

### 1. Import the tokens

```tsx
// app/layout.tsx or _app.tsx
import '../templates/styles/tokens.css';
```

### 2. Customize the tokens

Open `templates/styles/tokens.css` and replace the palette + font values with your chosen ones from `data/palettes-100.json` and `data/font-pairs-100.json`.

### 3. Load the fonts

Update the `<link>` tag in your HTML head with your font pairing's `loading_html` from `data/font-pairs-100.json`.

### 4. Use the components

```tsx
import { HeroSplit } from '../templates/hero/hero-split';
import { GlassCard } from '../templates/components/glass-card';
import { BentoGrid } from '../templates/components/bento-grid';
import { Counter } from '../templates/components/counter';

export default function HomePage() {
  return (
    <>
      <HeroSplit
        eyebrow="Now in public beta"
        headline="Ship design reviews 4× faster"
        subhead="Frameable cuts review cycles from 5 days to 4 hours."
        primaryCta={{ label: 'Start free trial →', href: '/signup' }}
        secondaryCta={{ label: 'Watch demo', href: '/demo' }}
        proof={{ stat: '1,247,893', label: 'reviews shipped', source: 'Stripe Q3 2025' }}
        productMockup={<ProductPreview />}
      />

      <BentoGrid cells={[
        { id: '1', title: 'Frame-perfect annotations', description: '...', size: 'large' },
        { id: '2', title: 'Slack sync', description: '...', size: 'square' },
        // ...
      ]} />
    </>
  );
}
```

## Dependencies

The components assume:
- React 18+
- TypeScript 5+
- Tailwind CSS 3+ (for utility classes used in className)
- The CSS variables defined in `styles/tokens.css`
- A modern browser (Chrome 90+, Firefox 88+, Safari 14+)

No external animation library required — all motion uses native CSS / Web APIs.

## Anti-Patterns (Auto-Fail)

- Do NOT use `scroll-reveal.tsx` on every section. It's for product flows and data reveals only.
- Do NOT use `magnetic-button.tsx` on every button. Hero CTA only, 1 per page max.
- Do NOT use `glass-card.tsx` over a flat background. Glass needs something to blur.
- Do NOT mix `gradient-text.tsx` presets. Pick one per page.
- Do NOT skip `tokens.css`. The components depend on the CSS variables.

## See Also

- `guides/05-hero-section-guide.md` — when to use each hero variant
- `guides/04-glassmorphism-guide.md` — when glass is appropriate
- `guides/06-advanced-css-components.md` — advanced CSS techniques
- `examples/demo-saas-landing.html` — standalone HTML demo using these patterns
