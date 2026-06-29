# 06 — Advanced CSS Components (Beyond Utility Soup)

> Modern CSS can do everything Tailwind tells you it can't. The problem isn't that AI agents lack the syntax — it's that they default to `flex gap-4 rounded-2xl bg-white/5 p-6` because that's what's in the training data. This guide is the cure: 10 recipes that ship real, opinionated, hand-tuned CSS components instead of utility-class soup.

## Why AI CSS fails

Open any LLM-generated component. You'll see one of two patterns:

**Pattern A — Tailwind soup:**
```tsx
<div className="relative flex flex-col items-start gap-4 rounded-2xl border border-white/10 bg-white/5 p-6 shadow-lg backdrop-blur-md transition-all duration-300 hover:scale-105 hover:border-white/20 hover:bg-white/10 hover:shadow-xl">
```
That's 13 utility classes doing what 6 lines of scoped CSS would do better. It's unreadable, untunable, unthemeable, and identical across every AI codebase.

**Pattern B — Inline-styled divs:**
```tsx
<div style={{ background: 'linear-gradient(...)', borderRadius: 16, padding: 24 }}>
```
No hover states, no responsive behavior, no reduced-motion, no theming. A dead-end component.

**The fix**: write actual CSS. Use `@property`, `:has()`, container queries, scroll-driven animations, `clip-path`, `mask-image`, conic gradients, and view transitions — features that 95% of AI-generated sites never touch because they require deliberate thought, not autocomplete.

Tailwind is allowed as a layout helper (`grid`, `flex`, spacing). It is **not** allowed as your only styling strategy. Every component in this guide uses Tailwind for layout primitives and a real stylesheet for everything visual.

---

## The 5 Rules of Advanced CSS Components

### Rule 1 — Use `@property` for animatable custom properties

CSS custom properties (`--foo`) are not animatable by default. Register them with `@property` and they become first-class animatable values. This unlocks gradient-angle animations, color morphs, and count-ups — all in CSS, no JS.

```css
@property --angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

@property --hue {
  syntax: '<angle>';
  initial-value: 220deg;
  inherits: false;
}

@property --count {
  syntax: '<integer>';
  initial-value: 0;
  inherits: false;
}
```

Without `@property`, `transition: --angle 1s` does nothing. With it, the browser interpolates the angle smoothly. This is the difference between "AI CSS that won't compile" and "real CSS that works."

### Rule 2 — Reach for `:has()` before reaching for state libraries

`parent:has(child)` is the parent selector CSS has waited 20 years for. It removes 80% of the cases where you'd otherwise reach for `useState` + conditional className.

```css
/* Style the form when any input is invalid */
form:has(input:invalid) .submit-btn {
  opacity: 0.5;
  pointer-events: none;
}

/* Hide the label when the card is selected */
.card-grid:has(.card[data-selected="true"]) .card-default-label {
  opacity: 0;
}

/* Highlight a card when its checkbox is checked */
label.card:has(input:checked) {
  border-color: var(--accent);
  background: var(--accent-soft);
}
```

Browser support: Chrome 105+, Safari 15.4+, Firefox 121+. That's 93%+ global. Use it.

### Rule 3 — Container queries before media queries for component-level responsiveness

Media queries ask "how wide is the viewport?" Container queries ask "how wide is my container?" — which is the question components actually need answered. A card in a 3-column grid and the same card in a sidebar have different needs regardless of viewport.

```css
.card-container { container-type: inline-size; }

@container (min-width: 400px) {
  .card { display: grid; grid-template-columns: 1fr 2fr; }
}

@container (max-width: 399px) {
  .card { display: flex; flex-direction: column; }
}
```

Use media queries for **page layout** (nav, sidebar, page grid). Use container queries for **component layout** (cards, lists, form rows).

### Rule 4 — `mask-image` for reveals, `clip-path` for shapes

Both are GPU-acomposited and can be animated. They're faster than SVG filters and more flexible than `border-radius`.

`mask-image` reveals parts of an element based on an alpha mask. Use for: text-fill gradients with hard edges, image reveals on scroll, soft-fade edges.

`clip-path` cuts an element into a shape. Use for: angular cards, diagonal section dividers, hexagon avatars, blob shapes.

### Rule 5 — Scroll-driven animations over scroll-listener JS

For the love of performance, stop writing `window.addEventListener('scroll', ...)`. CSS scroll-driven animations (Chrome 115+, Safari 26+, Firefox shipping) handle 90% of scroll effects natively — they run off the compositor, never trigger layout, and survive `prefers-reduced-motion` automatically when you wrap them right.

```css
@keyframes fade-in-on-enter {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.section-reveal {
  animation: fade-in-on-enter linear forwards;
  animation-timeline: view();
  animation-range: entry 0% entry 60%;
}
```

That's a scroll-triggered reveal with zero JS. Combine with `@media (prefers-reduced-motion: reduce)` to disable.

---

## Recipe 1 — Animated Gradient Mesh Background

The "AI default" gradient is `bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500` — a 1-axis linear gradient with three saturated stops. Banned. A real gradient mesh has 4–6 radial gradients blended together and a slow angle animation.

```css
@property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }

.mesh-bg {
  position: relative;
  isolation: isolate;
  background:
    radial-gradient(40vw 40vw at 20% 30%, hsl(280 60% 40% / 0.7), transparent 60%),
    radial-gradient(35vw 35vw at 80% 20%, hsl(190 70% 45% / 0.6), transparent 65%),
    radial-gradient(50vw 50vw at 60% 80%, hsl(15 75% 50% / 0.55), transparent 60%),
    radial-gradient(30vw 30vw at 30% 70%, hsl(150 55% 40% / 0.5), transparent 55%),
    var(--bg);
  filter: saturate(1.1) contrast(1.05);
}

.mesh-bg::after {
  content: '';
  position: absolute;
  inset: -20%;
  background: inherit;
  filter: blur(60px);
  transform: rotate(var(--angle));
  animation: spin-mesh 30s linear infinite;
  z-index: -1;
}

@keyframes spin-mesh {
  to { --angle: 360deg; }
}

@media (prefers-reduced-motion: reduce) {
  .mesh-bg::after { animation: none; }
}
```

This is what Apple's marketing pages do. It is not `bg-gradient-to-br from-violet-500 to-fuchsia-500`. Don't ship that.

## Recipe 2 — Conic Gradient Border Card

```css
@property --border-angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }

.conic-card {
  position: relative;
  border-radius: 20px;
  background: var(--surface);
  padding: 2rem;
  isolation: isolate;
}

.conic-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.5px;
  background: conic-gradient(
    from var(--border-angle),
    transparent 0deg,
    var(--accent) 60deg,
    transparent 120deg,
    transparent 240deg,
    var(--accent-2, hsl(280 70% 60%)) 300deg,
    transparent 360deg
  );
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  animation: rotate-border 6s linear infinite;
  z-index: -1;
}

@keyframes rotate-border {
  to { --border-angle: 360deg; }
}

@media (prefers-reduced-motion: reduce) {
  .conic-card::before { animation: none; }
}
```

This is the animated gradient-border trick — a thin conic gradient rotates around the card edge. The `mask-composite: exclude` trick is what creates a hollow border. Use it on hero feature cards, never on every card.

## Recipe 3 — Mask-Image Text Reveal

A scroll-driven reveal where text fills with color from bottom to top as it enters the viewport. No JS.

```css
@keyframes fill-in {
  from { --reveal: 0%; }
  to   { --reveal: 100%; }
}

.reveal-text {
  --reveal: 0%;
  background: linear-gradient(
    to bottom,
    var(--accent) 0%,
    var(--accent) var(--reveal),
    var(--muted) var(--reveal),
    var(--muted) 100%
  );
  -webkit-background-clip: text;
          background-clip: text;
  color: transparent;
  animation: fill-in linear forwards;
  animation-timeline: view();
  animation-range: entry 10% cover 40%;
}
```

Pair with a heading that's already on screen — the heading text starts muted and "fills" with accent color as the user scrolls. Cheap, elegant, no JS, respects reduced-motion if you wrap with the media query.

## Recipe 4 — Clip-Path Angular Section Divider

```css
.section-divider {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 calc(100% - 4vw));
  padding-bottom: 8vw;
}

/* Or a slanted section break */
.section-slant {
  clip-path: polygon(0 4vw, 100% 0, 100% calc(100% - 4vw), 0 100%);
}

/* Hexagon avatar */
.avatar-hex {
  clip-path: polygon(25% 5%, 75% 5%, 100% 50%, 75% 95%, 25% 95%, 0 50%);
}

/* Blob shape (use sparingly — can read as 2019 Dribbble) */
.shape-blob {
  clip-path: path('M 100,20 C 180,20 220,80 220,140 C 220,210 160,260 100,260 C 40,260 0,210 0,140 C 0,80 20,20 100,20 Z');
}
```

Use `clip-path` for one or two signature moments per site. Don't clip everything — it makes the page feel like a 2018 portfolio.

## Recipe 5 — Scroll-Snap Carousel (no library)

```css
.snap-carousel {
  display: flex;
  gap: 1.5rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 1rem;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none; /* Firefox */
}
.snap-carousel::-webkit-scrollbar { display: none; } /* Chromium/Safari */

.snap-carousel > * {
  scroll-snap-align: center;
  scroll-snap-stop: always;
  flex: 0 0 min(80vw, 420px);
}

@media (min-width: 768px) {
  .snap-carousel > * { flex-basis: 360px; }
}
```

```tsx
<section className="snap-carousel" aria-label="Customer stories">
  {stories.map(s => <StoryCard key={s.id} story={s} />)}
</section>
```

No `embla-carousel`, no `swiper`, no 40KB of JS. Native scroll-snap, native touch, native keyboard when you add `tabindex="0"` to the cards. Add `scroll-snap-stop: always` so the carousel doesn't skip cards on fast flicks.

## Recipe 6 — Container-Query Card (responsive without media queries)

```css
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: 1.5rem;
  container-type: inline-size;
}

.product-card {
  display: grid;
  gap: 0.75rem;
}

@container (min-width: 320px) {
  .product-card { grid-template-columns: 100px 1fr; grid-template-areas: 'img body'; }
  .product-card .card-img { grid-area: img; }
  .product-card .card-body { grid-area: body; }
}

@container (max-width: 319px) {
  .product-card { grid-template-columns: 1fr; grid-template-areas: 'img' 'body'; }
}
```

The same component adapts based on its column width, not the viewport. Drop it in a sidebar, in a hero, in a grid — it always lays out correctly. This is what container queries were built for.

## Recipe 7 — `:has()`-Powered Form Validation State

```css
.form-field {
  position: relative;
}

.form-field input {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 0.625rem 0.875rem;
  transition: border-color 0.15s ease;
}

/* When the input is focused and valid, accent the border */
.form-field:has(input:focus:valid) input {
  border-color: var(--success);
}

/* When the input is invalid (and has been touched via :not(:placeholder-shown)), red border */
.form-field:has(input:not(:placeholder-shown):invalid) input {
  border-color: var(--error);
}

/* Show the error message only when the field is invalid + touched */
.form-field .error-msg {
  display: none;
  color: var(--error);
  font-size: 0.8125rem;
  margin-top: 0.25rem;
}

.form-field:has(input:not(:placeholder-shown):invalid) .error-msg {
  display: block;
}

/* Disable submit when the form has any invalid field */
form:has(input:not(:placeholder-shown):invalid) .submit-btn {
  opacity: 0.5;
  pointer-events: none;
}
```

No React state. No `useState` for "touched". No `useForm` library. The browser already knows whether the input is valid (via `required`, `type="email"`, `pattern`) — let CSS react to it.

## Recipe 8 — View Transitions API (cross-document or same-document)

Same-document view transition (SPA route change):

```tsx
// On click of a nav link
function navigate(href: string) {
  if (!document.startViewTransition) {
    location.href = href;
    return;
  }
  document.startViewTransition(() => {
    location.href = href;
  });
}
```

```css
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 0.35s;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

/* Named transition — only the hero image morphs */
.hero-img {
  view-transition-name: hero-image;
}

::view-transition-old(hero-image) {
  animation: 0.35s ease-out both fade-out;
}
::view-transition-new(hero-image) {
  animation: 0.35s ease-out both fade-in;
}

@keyframes fade-out { to { opacity: 0; } }
@keyframes fade-in  { from { opacity: 0; } }
```

Use view transitions for: route changes, opening modals from a card (the card "expands" into the modal), image-gallery zoom. Don't use for: every interaction. The transition should feel like continuity, not a magic trick.

For cross-document (MPA) view transitions, add `<meta name="view-transition" content="same-origin">` and the browser handles it across full page loads.

## Recipe 9 — Scroll-Driven Progress Bar (sticky reading progress)

```css
.reading-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  width: 100%;
  background: var(--accent);
  transform: scaleX(var(--progress, 0));
  transform-origin: left;
  z-index: 100;
  animation: progress linear;
  animation-timeline: scroll(root);
}

@keyframes progress {
  from { transform: scaleX(0); }
  to   { transform: scaleX(1); }
}
```

That's a sticky reading-progress bar — zero JavaScript, zero scroll listeners, runs on the compositor. Add a `@media (prefers-reduced-motion: reduce) { .reading-progress { animation: none; transform: scaleX(1); } }` fallback if you want it always visible.

## Recipe 10 — Animated Counter with `@property`

```css
@property --num {
  syntax: '<integer>';
  initial-value: 0;
  inherits: false;
}

.counter {
  counter-reset: num var(--num);
  animation: count-up 2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  animation-timeline: view();
  animation-range: entry 0% cover 30%;
}

.counter::after {
  content: counter(num);
}

@keyframes count-up {
  to { --num: 1247893; }
}
```

The `counter-reset: num var(--num)` reads the custom property into a CSS counter, and `::after { content: counter(num) }` displays it. As `--num` animates from 0 to 1,247,893 (which only works because we registered it with `@property`), the displayed counter updates with no layout cost.

Add thousand separators by post-processing: `content: counter(num, decimal); /* or use a JS formatter for grouped digits */`. For tabular figures, set `font-variant-numeric: tabular-nums`.

## Recipe 11 — Sticky Stack (`position: sticky` cards)

```css
.stack-section {
  position: relative;
}

.stack-card {
  position: sticky;
  top: 4rem;
  margin-bottom: 4rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 12px 32px rgba(0,0,0,0.06);
}

/* Each card sticks slightly below the previous one */
.stack-card:nth-child(1) { top: 4rem; }
.stack-card:nth-child(2) { top: 6rem; }
.stack-card:nth-child(3) { top: 8rem; }
.stack-card:nth-child(4) { top: 10rem; }
```

A stack of cards that pile up as you scroll — each new card slides up and rests below the previous. Apple's product pages use this constantly. No JS. Just `position: sticky` and incremental `top` values.

## Recipe 12 — Custom Property Theme Tokens (real design-token system)

Stop hardcoding `text-[#7B1E1E]` in your JSX. Build a real token layer.

```css
:root {
  /* Color tokens — semantic, not raw */
  --color-bg: #FAFAFA;
  --color-surface: #FFFFFF;
  --color-text: #18181B;
  --color-text-muted: #71717A;
  --color-accent: #B45309;
  --color-accent-soft: #FDE68A;
  --color-border: rgb(24 24 27 / 0.08);

  /* Spacing tokens — 4px scale */
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-12: 3rem;
  --space-16: 4rem;
  --space-24: 6rem;

  /* Radius tokens */
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-xl: 24px;
  --radius-pill: 999px;

  /* Shadow tokens — layered */
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.04);
  --shadow-md: 0 1px 2px rgb(0 0 0 / 0.04), 0 4px 12px rgb(0 0 0 / 0.06);
  --shadow-lg: 0 1px 2px rgb(0 0 0 / 0.04), 0 8px 24px rgb(0 0 0 / 0.08);
  --shadow-glow: 0 0 0 4px var(--color-accent-soft);

  /* Motion tokens */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
  --dur-fast: 150ms;
  --dur-base: 250ms;
  --dur-slow: 400ms;
}

[data-theme="dark"] {
  --color-bg: #0A0A0B;
  --color-surface: #18181B;
  --color-text: #E4E4E7;
  --color-text-muted: #A1A1AA;
  --color-border: rgb(255 255 255 / 0.08);
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.4);
  --shadow-md: 0 1px 2px rgb(0 0 0 / 0.4), 0 4px 12px rgb(0 0 0 / 0.5);
  --shadow-lg: 0 1px 2px rgb(0 0 0 / 0.4), 0 8px 24px rgb(0 0 0 / 0.6);
}
```

Now your component is:

```tsx
<button className="btn-primary">Save changes</button>
```

```css
.btn-primary {
  background: var(--color-accent);
  color: white;
  border: none;
  border-radius: var(--radius-md);
  padding: var(--space-3) var(--space-6);
  font-weight: 500;
  box-shadow: var(--shadow-sm);
  transition: transform var(--dur-fast) var(--ease-out),
              box-shadow var(--dur-fast) var(--ease-out);
}
.btn-primary:hover { transform: translateY(-1px); box-shadow: var(--shadow-md); }
.btn-primary:active { transform: translateY(0); }
.btn-primary:focus-visible { outline: none; box-shadow: var(--shadow-glow); }
```

Three lines of JSX, twelve lines of CSS, infinitely themeable. That's a real component.

---

## Browser Support Reality Check

| Feature | Chrome | Safari | Firefox | Use today? |
|---------|--------|--------|---------|-----------|
| `@property` | 85+ | 16.4+ | 128+ | ✅ Yes |
| `:has()` | 105+ | 15.4+ | 121+ | ✅ Yes |
| Container queries | 105+ | 16+ | 110+ | ✅ Yes |
| Scroll-driven animations | 115+ | 26+ | in-development | ⚠️ Progressive enhancement |
| View Transitions API | 111+ (same-doc) | 18+ | in-development | ⚠️ Progressive enhancement |
| `mask-composite` | 120+ | 15.4+ | 53+ | ✅ Yes (with `-webkit-`) |
| `clip-path: path()` | 88+ | 13.1+ | 71+ | ✅ Yes |

For features marked "progressive enhancement": the page must work without them. The animation is bonus polish, not core functionality. Always wrap in `@supports`:

```css
@supports (animation-timeline: view()) {
  .section-reveal { animation: fade-in-on-enter linear forwards; animation-timeline: view(); }
}
@supports not (animation-timeline: view()) {
  .section-reveal { opacity: 1; /* show by default */ }
}
```

## Forbidden Patterns (Auto-Fail)

1. **Tailwind utility soup with 12+ classes per element.** If you can't read the className and know what it does in 3 seconds, it's soup. Extract to a component CSS class.
2. **`@apply` everywhere.** `@apply` is not "real CSS" — it's Tailwind in disguise. Use it sparingly for one-off utilities, never as a primary styling strategy.
3. **Animated `background-position` for gradient shifts.** Triggers paint on every frame. Use `@property --angle` + a `transform: rotate()` of a blurred pseudo-element instead.
4. **JavaScript scroll listeners for progress bars / reveals / parallax.** Replace with scroll-driven animations. Falls back to no-animation for older browsers.
5. **Inline `style={{...}}` for anything beyond dynamic values (e.g. `--x` from a drag).** Inline styles can't be themed, can't respond to `:hover`, can't be reduced-motion-aware.
6. **`backdrop-filter` on more than 3 elements per page.** Performance killer.
7. **`filter: blur()` on large elements (full-width sections).** GPU-expensive. Use SVG `feGaussianBlur` or pre-baked blurred images.
8. **Conic gradients with 8+ color stops.** Looks like a rainbow wheel. 2–3 stops max.
9. **`clip-path: polygon(...)` with more than 6 points.** Becomes a jagged mess. Use `path()` for curves instead.
10. **Forgetting `prefers-reduced-motion`.** Every animation in this guide must have a reduced-motion fallback.
11. **Forgetting `:focus-visible`.** Keyboard users need to see where they are. Don't rely on `:focus` (it shows for mouse clicks too).
12. **`will-change: transform` on everything.** The browser will hate you. Apply only to elements currently animating, then remove.

## Anti-Pattern: "I'll just use Framer Motion"

Framer Motion is great. It's also 60KB gzipped and shipped to every user for what is often a 30-line CSS animation. Before reaching for it:

- **Scroll reveals** → CSS scroll-driven animations (0KB)
- **Hover micro-interactions** → CSS `transition` (0KB)
- **Page transitions** → View Transitions API (0KB)
- **Spring physics on a draggable card** → Framer Motion (worth it)
- **Gesture-based bottom sheets** → Framer Motion (worth it)

Reach for JS animation libraries when you need **physics** (springs, momentum, gestures) or **orchestration** (complex staggered sequences with branching). For 80% of UI animation, CSS is enough.

## Output

When you finish this guide, you should have:
- At least 3 components written in real CSS (not utility soup), each using one advanced feature: `@property`, `:has()`, container queries, scroll-driven animations, view transitions, `mask-image`, or `clip-path`
- A `tokens.css` file with color, spacing, radius, shadow, and motion tokens
- `@supports` fallbacks for every progressive-enhancement feature
- `prefers-reduced-motion` media queries on every animation
- No JS scroll listeners for animations that CSS can handle
- A documented reason in `DESIGN-RATIONALE.md` for each advanced technique ("used conic-gradient border on the hero feature card because the brand is high-tech and the rotating accent draws the eye without distracting from the headline")
