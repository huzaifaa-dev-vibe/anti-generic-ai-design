# 17 — Responsive Design

> "Mobile-first" is the most parroted phrase in frontend and the least practiced. AI-coded sites ship `md:grid-cols-3` everywhere, which is desktop-first in reverse — design the desktop layout, then collapse it. Real mobile-first means designing the phone screen first, then progressively enhancing upward. This guide is how to actually do responsive in 2025, with container queries, fluid type, and a thumb-zone-aware touch system.

## Why AI fails at responsive

Five defaults ruin AI responsive design:

1. **`md:grid-cols-3` reflex.** The base styles are for mobile, but they're an afterthought — the LLM designed the desktop layout in its head and broke it down. Mobile users get the crumbs.
2. **Fixed breakpoints with no fluid behavior.** Between `md` (768px) and `lg` (1024px), the layout is whatever it was at 768. No smooth scaling.
3. **Tiny touch targets.** `text-sm` links packed 4px apart. Unusable on a phone.
4. **No thumb-zone thinking.** Primary actions buried at the top of the screen where the thumb can't reach.
5. **Tables that don't transform.** A 6-column data table rendered as-is on mobile, requiring horizontal scroll. AI's solution: `overflow-x-auto` and walk away.

Responsive design is not "make it work on mobile". It is "design three to five distinct experiences that share a soul".

---

## Rule 1 — Mobile-first means write mobile CSS first

Write the base styles for the smallest screen. Enhance upward with `min-width` media queries.

```css
/* ✅ Mobile-first */
.card-grid {
  display: grid;
  grid-template-columns: 1fr;          /* mobile: 1 column */
  gap: var(--space-4);
}

@media (min-width: 640px) {
  .card-grid { grid-template-columns: repeat(2, 1fr); }    /* tablet: 2 cols */
}

@media (min-width: 1024px) {
  .card-grid { grid-template-columns: repeat(3, 1fr); }    /* desktop: 3 cols */
  .card-grid { gap: var(--space-6); }
}

/* ❌ Desktop-first (do not do this) */
.card-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

@media (max-width: 1023px) {
  .card-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 639px) {
  .card-grid { grid-template-columns: 1fr; gap: var(--space-4); }
}
```

Why mobile-first?
- Mobile CSS is the base — every device downloads it. Desktop enhancements layer on top.
- It forces you to design the constraints first. A 3-column card grid is easy; a 1-column card grid that doesn't feel anemic is hard.
- The CSS is shorter. `min-width` queries override the base; `max-width` queries require restating base values.

## Rule 2 — The breakpoint scale

Use the Tailwind default breakpoints. They're well-chosen and battle-tested.

| Name | Width | Device |
|------|-------|--------|
| (base) | 0–639px | Phone portrait |
| `sm` | 640px+ | Phone landscape, small tablet |
| `md` | 768px+ | Tablet portrait (iPad) |
| `lg` | 1024px+ | Tablet landscape, small laptop |
| `xl` | 1280px+ | Desktop |
| `2xl` | 1536px+ | Large desktop, wide monitor |

```css
:root {
  --bp-sm: 640px;
  --bp-md: 768px;
  --bp-lg: 1024px;
  --bp-xl: 1280px;
  --bp-2xl: 1536px;
}

/* Usage */
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
```

**Don't invent new breakpoints** unless you have a specific reason (e.g. a sidebar that needs to collapse at 920px). Custom breakpoints multiply maintenance cost.

## Rule 3 — Container queries: the modern primitive

Media queries are viewport-based. Container queries are component-based. Use them for components that adapt to their container, not the viewport.

```css
/* The card adapts to its container, not the viewport */
.card-container {
  container-type: inline-size;
  container-name: card;
}

.card {
  display: grid;
  gap: var(--space-4);
}

@container card (min-width: 400px) {
  .card {
    grid-template-columns: 120px 1fr;
    align-items: start;
  }
}

@container card (min-width: 640px) {
  .card {
    grid-template-columns: 200px 1fr auto;
  }
}
```

When to use container queries:
- A component lives in multiple contexts (sidebar, full-width, in a modal).
- A reusable card layout adapts to its column.
- You're building a design system.

When to use media queries:
- The entire page layout changes (mobile nav appears).
- Root typography or page padding changes.
- The hero image source changes.

## Rule 4 — Fluid typography with `clamp()`

Stop writing `text-4xl md:text-5xl lg:text-6xl`. Use `clamp()` to scale type smoothly between breakpoints.

```css
:root {
  /* Fluid type scale — scales from 320px to 1536px viewport */
  --step--1: clamp(0.75rem, 0.72rem + 0.15vw, 0.85rem);     /* 12 → 14px */
  --step-0:  clamp(1rem,    0.96rem + 0.2vw,  1.125rem);    /* 16 → 18px */
  --step-1:  clamp(1.125rem, 1.05rem + 0.4vw, 1.35rem);     /* 18 → 22px */
  --step-2:  clamp(1.35rem,  1.2rem + 0.75vw,  1.75rem);    /* 22 → 28px */
  --step-3:  clamp(1.75rem,  1.5rem + 1.25vw,  2.5rem);     /* 28 → 40px */
  --step-4:  clamp(2.25rem,  1.8rem + 2.25vw,  3.5rem);     /* 36 → 56px */
  --step-5:  clamp(3rem,     2.2rem + 4vw,     5rem);       /* 48 → 80px */
}

h1 { font-size: var(--step-4); line-height: 1.05; }
h2 { font-size: var(--step-3); line-height: 1.1; }
h3 { font-size: var(--step-2); line-height: 1.2; }
body { font-size: var(--step-0); line-height: 1.55; }
small { font-size: var(--step--1); }

.hero-headline {
  font-size: var(--step-5);
  line-height: 1.0;
  letter-spacing: -0.04em;
}
```

**How `clamp()` works**: `clamp(MIN, PREFERRED, MAX)`. The preferred value scales with viewport width (`vw`). The min and max cap it.

The formula `0.96rem + 0.2vw` means: start at 0.96rem (≈15.4px), add 0.2% of viewport width. At 320px viewport: 15.4 + 0.64 = 16px. At 1536px viewport: 15.4 + 3.07 = 18.5px (capped at 18px by the max).

**Use the [Utopia.fyi](https://utopia.fyi/type/) calculator** to generate the values for your scale.

## Rule 5 — Fluid spacing

The same trick for spacing. Page padding and section gaps should scale with the viewport.

```css
:root {
  --space-page-x: clamp(1rem, 0.5rem + 2vw, 2rem);          /* 16 → 32px */
  --space-section-y: clamp(3rem, 2rem + 5vw, 6rem);          /* 48 → 96px */
  --space-section-y-lg: clamp(4rem, 2.5rem + 8vw, 8rem);     /* 64 → 128px */
}

.page { padding-inline: var(--space-page-x); }
section { padding-block: var(--space-section-y); }
section.hero { padding-block: var(--space-section-y-lg); }
```

## Rule 6 — Responsive images with `srcset`

```html
<img
  src="/hero-800.jpg"
  srcset="
    /hero-400.jpg   400w,
    /hero-800.jpg   800w,
    /hero-1200.jpg 1200w,
    /hero-1600.jpg 1600w,
    /hero-2400.jpg 2400w
  "
  sizes="(max-width: 768px) 100vw, (max-width: 1280px) 50vw, 1200px"
  alt="Hero image"
  width="1200"
  height="630"
  loading="eager"
  fetchpriority="high"
  decoding="async"
/>
```

**`sizes` is critical.** Without it, the browser doesn't know which image to download and may grab the largest. `sizes` tells the browser: "On mobile this image takes the full viewport width. On desktop, half the viewport width. Never wider than 1200px."

Generate the variants at build time:
- Next.js: `<Image>` handles it automatically.
- Eleventy/Astro: use `@11ty/eleventy-img` or `astro:assets`.
- Static: use Sharp or Squoosh CLI in a build script.

## Rule 7 — Touch targets: 44×44 minimum

Apple HIG and Material Design agree: minimum 44×44 CSS pixels for any tappable element. WCAG 2.5.5 recommends the same (AAA, but should be the default).

```css
.icon-button {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}

/* For inline links in text — ensure at least 24px between targets */
nav a {
  display: inline-block;
  padding: 10px 12px;          /* expands the hit area without making the link look huge */
  min-height: 44px;
  display: inline-flex;
  align-items: center;
}
```

For elements that must be visually small (icon in a dense toolbar), pad the hit area with transparent space:

```css
.dense-icon-button {
  width: 32px;                 /* visual size */
  height: 32px;
  position: relative;
}

.dense-icon-button::before {
  content: '';
  position: absolute;
  inset: -6px;                 /* expands hit area to 44px */
}
```

## Rule 8 — Thumb zones: design for the thumb

On a phone held in one hand, the thumb has a comfort zone (bottom-right for right-handers, bottom-left for left-handers) and a stretch zone (top of screen, far edge opposite the thumb).

| Zone | Where | Use for |
|------|-------|---------|
| Comfort | Bottom 1/3, thumb-side | Primary actions, nav |
| Stretch | Top of screen | Read-only content, headers |
| Dead | Far edge opposite thumb | Avoid placing actions here |

**Practical implications**:
- Bottom nav (mobile) > top nav for primary destinations.
- Floating action button (FAB) bottom-right, not top-right.
- "Submit" button at the bottom of the form, not the top.
- Modals on mobile: action buttons at the bottom, not the header.

```css
/* Mobile bottom nav */
@media (max-width: 767px) {
  .mobile-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: var(--surface);
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding-bottom: env(safe-area-inset-bottom);  /* iOS notch */
  }

  /* Push content up so it isn't hidden behind the nav */
  body { padding-bottom: 60px; }
}
```

## Rule 9 — Responsive navigation patterns

### Mobile: off-canvas / drawer

```tsx
function MobileNav({ open, onClose, items }) {
  return (
    <>
      <div
        className={`overlay ${open ? 'open' : ''}`}
        onClick={onClose}
        aria-hidden={!open}
      />
      <aside
        className={`mobile-drawer ${open ? 'open' : ''}`}
        aria-hidden={!open}
      >
        <nav aria-label="Mobile">
          <ul>
            {items.map(item => (
              <li key={item.href}>
                <a href={item.href} onClick={onClose}>{item.label}</a>
              </li>
            ))}
          </ul>
        </nav>
      </aside>
    </>
  );
}
```

```css
.mobile-drawer {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: min(320px, 85vw);
  background: var(--surface);
  transform: translateX(-100%);
  transition: transform 250ms ease;
  z-index: 60;
  padding: var(--space-6);
}

.mobile-drawer.open { transform: translateX(0); }

.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  opacity: 0;
  pointer-events: none;
  transition: opacity 250ms ease;
  z-index: 55;
}

.overlay.open { opacity: 1; pointer-events: auto; }

@media (min-width: 1024px) {
  .mobile-drawer, .overlay { display: none; }
}
```

### Tablet: bottom nav (mobile-like) or top nav (desktop-like)

Depends on whether the tablet is held (bottom nav) or propped (top nav). Default: top nav at `md`.

### Desktop: top nav, possibly with mega menu

```tsx
function MegaMenu({ label, sections }) {
  const [open, setOpen] = useState(false);
  return (
    <li
      onMouseEnter={() => setOpen(true)}
      onMouseLeave={() => setOpen(false)}
      onFocus={() => setOpen(true)}
      onBlur={() => setOpen(false)}
    >
      <button aria-expanded={open} aria-haspopup="true">
        {label}
      </button>
      {open && (
        <div className="mega-menu" role="menu">
          {sections.map(section => (
            <div key={section.title}>
              <h3>{section.title}</h3>
              <ul>
                {section.links.map(link => (
                  <li key={link.href}>
                    <a href={link.href} role="menuitem">{link.label}</a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </li>
  );
}
```

## Rule 10 — Responsive tables

A 6-column table on a 320px screen is unusable. Three patterns:

### Pattern 1: Card transform (best for simple data)

```css
@media (max-width: 767px) {
  table.responsive { display: block; }
  table.responsive thead { display: none; }
  table.responsive tbody,
  table.responsive tr,
  table.responsive td { display: block; }

  table.responsive tr {
    margin-bottom: var(--space-4);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: var(--space-3);
  }

  table.responsive td {
    display: flex;
    justify-content: space-between;
    padding: var(--space-1) 0;
  }

  table.responsive td::before {
    content: attr(data-label);
    font-weight: 600;
    margin-right: var(--space-3);
  }
}
```

```html
<tr>
  <td data-label="Name">Alice</td>
  <td data-label="Email">alice@example.com</td>
  <td data-label="Role">Admin</td>
</tr>
```

### Pattern 2: Horizontal scroll (acceptable for complex data)

```html
<div class="table-scroll">
  <table>...</table>
</div>
```

```css
.table-scroll {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table-scroll table {
  min-width: 800px;  /* don't let columns squish below readable width */
}
```

### Pattern 3: Hide non-essential columns

```css
@media (max-width: 767px) {
  .col-hide-mobile { display: none; }
}
@media (max-width: 1023px) {
  .col-hide-tablet { display: none; }
}
```

```html
<th class="col-hide-tablet">Last seen</th>
<td class="col-hide-tablet">2 hours ago</td>
```

## Rule 11 — Safe areas (iOS notch, Android gesture nav)

```css
:root {
  --safe-top: env(safe-area-inset-top, 0px);
  --safe-bottom: env(safe-area-inset-bottom, 0px);
  --safe-left: env(safe-area-inset-left, 0px);
  --safe-right: env(safe-area-inset-right, 0px);
}

.fixed-header {
  padding-top: var(--safe-top);
}

.bottom-nav {
  padding-bottom: var(--safe-bottom);
}

.full-bleed {
  /* Account for landscape orientation notches */
  padding-left: var(--safe-left);
  padding-right: var(--safe-right);
}
```

And in HTML:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
```

## Rule 12 — Test on real devices

Browser DevTools device emulation is a starting point, not a finish line. Test on:
- A real iPhone (Safari)
- A real Android (Chrome)
- An iPad (Safari, with rotation)
- A low-end Android (performance test)

You will find issues emulation misses: keyboard behavior, scroll momentum, hover states, viewport units, safe areas.

## Anti-Patterns (Auto-Fail)

1. **Desktop-first CSS with `max-width` overrides.** Use mobile-first with `min-width`.
2. **Fixed pixel widths** (`width: 1200px`) on containers. Use `max-width` or fluid units.
3. **`text-sm` touch targets** with 8px gaps. Use 44×44.
4. **No `srcset` on images** — full-size image downloaded on mobile.
5. **Horizontal scroll on the body** caused by an element wider than viewport. Use `overflow-x: hidden` on `html, body` only as a last resort; fix the offending element.
6. **Hover-only interactions on touch.** No hover on mobile — design tap alternatives.
7. **Tables that don't transform.** Use card pattern or scroll container.
8. **Fixed bottom modals on iOS** that the keyboard covers. Use `dvh` units.
9. **`100vh`** — use `100dvh` (dynamic viewport height) to handle mobile browser chrome correctly.
10. **No `viewport-fit=cover`** — content underflows the notch.
11. **Breakpoints invented per component** — stick to the standard 5.
12. **`position: fixed` nav without safe-area padding** — covered by iOS home indicator.

## Code Example — Fluid Type Scale and Responsive Layout

```css
:root {
  /* Fluid type — generated with Utopia.fyi */
  --step--1: clamp(0.75rem, 0.72rem + 0.15vw, 0.85rem);
  --step-0:  clamp(1rem, 0.96rem + 0.2vw, 1.125rem);
  --step-1:  clamp(1.125rem, 1.05rem + 0.4vw, 1.35rem);
  --step-2:  clamp(1.35rem, 1.2rem + 0.75vw, 1.75rem);
  --step-3:  clamp(1.75rem, 1.5rem + 1.25vw, 2.5rem);
  --step-4:  clamp(2.25rem, 1.8rem + 2.25vw, 3.5rem);
  --step-5:  clamp(3rem, 2.2rem + 4vw, 5rem);

  /* Fluid spacing */
  --space-page-x: clamp(1rem, 0.5rem + 2vw, 2rem);
  --space-section-y: clamp(3rem, 2rem + 5vw, 6rem);
}

.hero {
  padding-block: var(--space-section-y);
  padding-inline: var(--space-page-x);
}

.hero h1 {
  font-size: var(--step-5);
  line-height: 1.0;
  letter-spacing: -0.04em;
  max-width: 16ch;
}

.feature-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--space-4);
}

@container (min-width: 480px) {
  .feature-grid { grid-template-columns: repeat(2, 1fr); }
}

@container (min-width: 800px) {
  .feature-grid { grid-template-columns: repeat(3, 1fr); gap: var(--space-6); }
}

/* Use viewport fallback for browsers without container queries */
@media (min-width: 640px) {
  .feature-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .feature-grid { grid-template-columns: repeat(3, 1fr); }
}
```

## Output

When you finish this guide, you should have:
- Mobile-first CSS as the base, with `min-width` overrides at `sm`/`md`/`lg`/`xl`/`2xl`
- A fluid type scale using `clamp()` for every step
- Fluid page padding and section gaps
- All images with `srcset` and `sizes` (or `<Image>` component)
- Touch targets minimum 44×44px
- A mobile nav (off-canvas drawer) and a desktop nav (top nav or mega menu)
- Tables that transform to cards or scroll horizontally on mobile
- Safe-area padding for iOS notch and Android gesture nav
- `100dvh` instead of `100vh` for full-height layouts
- Container queries for at least one component that lives in multiple contexts
- Tested on a real iPhone, real Android, and an iPad with rotation
