# 09 — Animation Guide

> Animation is the difference between a site that feels alive and a site that feels dead. It's also the difference between a site that feels designed and a site that feels AI-generated. The AI default — `fade-in-up` on every section, `linear` easing, 1000ms durations — is the loudest possible "this was made by a robot" signal.

## Why AI animation fails

Four defaults ruin AI animation:

1. **`fade-in-up` on every section.** Every LLM-coded site does this. It's the most-overused motion on the web. After the second section, the user has stopped noticing it. After the fifth, they're annoyed.
2. **`linear` easing.** Linear easing feels mechanical. Real motion has acceleration and deceleration. Linear says "I am a robot animating this."
3. **1000ms+ durations.** A real micro-interaction is 100–200ms. A real section reveal is 400–800ms. 1000ms+ makes the user wait — they think the page is broken.
4. **Animating layout properties.** `width`, `height`, `top`, `left`, `margin`, `padding` all trigger layout recalculation. Frame drops. Use `transform` and `opacity` only.

This guide is the cure. By the end you'll know which easing curve to use when, how long each interaction should take, and how to choreograph a hero that feels like Apple, not like an AI.

---

## The 3 Layers of UI Animation

### Layer 1 — Micro-interactions (100–200ms)

Things a user directly triggers: button hover, button press, toggle, link hover, focus ring. The user caused this animation, so it must feel **instant**. >200ms feels laggy.

```css
.btn {
  transition: transform 150ms var(--ease-out),
              background-color 150ms var(--ease-out),
              box-shadow 150ms var(--ease-out);
}
.btn:hover { transform: translateY(-1px); }
.btn:active { transform: translateY(0); transition-duration: 50ms; }
```

The `:active` transition is faster (50ms) than the `:hover` transition (150ms) — pressing should feel snappier than hovering.

### Layer 2 — Small transitions (200–400ms)

Things that respond to user action but aren't directly the user's gesture: modal opening, dropdown expanding, accordion expanding, tab switching, toast sliding in. The user expects these to take a moment but not feel slow.

```css
.modal {
  transition: opacity 280ms var(--ease-in-out),
              transform 280ms var(--ease-in-out);
}
.modal[data-open="false"] { opacity: 0; transform: scale(0.96) translateY(8px); pointer-events: none; }
.modal[data-open="true"]  { opacity: 1; transform: scale(1)    translateY(0);   pointer-events: auto; }
```

### Layer 3 — Large / choreographed (400–800ms)

Things the user didn't trigger: hero entrance, page transition, scroll reveal of a major section, onboarding choreography. 800ms is the upper limit. Anything longer and the user thinks the page is loading.

```css
@keyframes hero-enter {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero-headline {
  animation: hero-enter 700ms var(--ease-out) 200ms both;
}
```

**Total choreography cap: 3 seconds.** A hero that takes 5 seconds to fully reveal is making the user wait. See the "Hero Choreography" section below.

---

## Timing Curves — the `cubic-bezier` reference

CSS ships with `ease`, `ease-in`, `ease-out`, `ease-in-out`, `linear`. Throw them all away except `ease-out` for most things. For real control, use `cubic-bezier(x1, y1, x2, y2)`.

A cubic-bezier curve describes how the animation's progress (y-axis) maps to time (x-axis). The first control point `(x1, y1)` is the start of the curve; the second `(x2, y2)` is the end.

### The 7 curves you actually need

```css
:root {
  /* Linear — mechanical, robotic. Almost never use. */
  --ease-linear: linear;

  /* Standard ease-out — starts fast, slows at end. Default for most things. */
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);

  /* Standard ease-in — starts slow, accelerates. Use for elements leaving the screen. */
  --ease-in: cubic-bezier(0.7, 0, 0.84, 0);

  /* Ease-in-out — slow start and end. Use for state transitions (modal open). */
  --ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);

  /* Material standard "decelerate" — Material Design's default. */
  --ease-material: cubic-bezier(0.4, 0, 0.2, 1);

  /* "Back" / overshoot — slightly overshoots the target. Use for playful entrances (pop-in). */
  --ease-back: cubic-bezier(0.34, 1.56, 0.64, 1);

  /* "Anticipate" — pulls back before moving forward. Use for emphasized motion. */
  --ease-anticipate: cubic-bezier(0.5, -0.5, 0.5, 1.5);
}
```

### When to use each

| Curve | Use for | Don't use for |
|-------|---------|---------------|
| `--ease-out` | Element entering the viewport, hover states, press states | Elements leaving the screen |
| `--ease-in` | Element leaving the viewport, dismissing a modal | Element entering — feels like it's "running away" |
| `--ease-in-out` | State transitions (modal open/close, panel expand) | Micro-interactions (too slow) |
| `--ease-material` | General-purpose UI motion (Material Design default) | When you want personality |
| `--ease-back` | Playful entrances: popovers, badges, notification toasts | Serious / corporate UI |
| `--ease-anticipate` | Emphasized motion: hero choreography, big reveals | Frequent interactions (gets exhausting) |
| `--ease-linear` | Nothing except mechanical progress (loading bars, spinners) | Almost anything else |

**Critical rule**: never animate `linear`. Linear feels like a robot. Every real-world motion has acceleration. The only valid uses of linear are: continuous loops (spinners), mechanical progress bars, and raster-line drawing.

---

## The 12 Principles of Animation, applied to UI

Disney's 12 principles from "The Illusion of Life" (1981) translate to UI. Here are the ones that matter:

### 1. Squash and stretch

An object changes shape as it moves to suggest weight and flexibility. In UI: a button compresses on press.

```css
.btn { transform-origin: center; }
.btn:active { transform: scale(0.96, 0.94); transition: transform 80ms var(--ease-out); }
```

Don't over-do it. A 4% squash is enough. More looks like a toy.

### 2. Anticipation

Before a major motion, the element briefly moves in the opposite direction. In UI: a card lifts slightly before expanding into a modal.

```css
@keyframes modal-expand {
  0%   { transform: scale(1); }
  15%  { transform: scale(0.98); }      /* anticipate */
  100% { transform: scale(1); }
}
```

15% of the duration spent on anticipation. The user doesn't consciously see it, but the motion feels alive.

### 3. Staging

One thing at a time. Don't animate 5 elements simultaneously — the eye doesn't know where to look. Stagger them.

### 4. Slow in, slow out (ease-in-out)

Already covered. Real motion doesn't start or stop instantly.

### 5. Follow-through

After the main motion stops, secondary elements continue briefly. In UI: a modal stops moving but its shadow takes another 80ms to settle.

```css
.modal { transition: transform 280ms var(--ease-out); }
.modal-shadow { transition: box-shadow 360ms var(--ease-out); }
```

### 6. Timing

Covered in the 3 layers above. Get the duration right.

### 7. Exaggeration

Real motion is subtle; animation needs to be 10–20% more to be readable. A button that lifts 1px on hover feels flat. Lift it 2–3px.

### 8. Solid drawing

In UI: respect the physics of the surface. A card has weight. A shadow implies depth. A blur implies glass. Don't mix metaphors.

### 9. Appeal

The motion should feel good. If a user does the same action 100 times, the animation should still feel satisfying on the 100th. Snappy is satisfying. Sluggish is not.

---

## Scroll-Triggered Animations (IntersectionObserver)

For browsers without scroll-driven animations support (Firefox and older Safari as of 2025), fall back to IntersectionObserver.

```ts
// hooks/useInView.ts
import { useEffect, useRef, useState } from 'react';

export function useInView<T extends HTMLElement = HTMLDivElement>(
  options: IntersectionObserverInit = { threshold: 0.15, rootMargin: '0px 0px -10% 0px' }
) {
  const ref = useRef<T>(null);
  const [inView, setInView] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;

    // Respect reduced motion — just show it
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      setInView(true);
      return;
    }

    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setInView(true);
        observer.unobserve(entry.target); // animate once
      }
    }, options);

    observer.observe(el);
    return () => observer.disconnect();
  }, []);

  return { ref, inView };
}
```

```tsx
function Section({ children }: { children: React.ReactNode }) {
  const { ref, inView } = useInView<HTMLDivElement>();
  return (
    <section
      ref={ref}
      className={`section ${inView ? 'section--in' : ''}`}
    >
      {children}
    </section>
  );
}
```

```css
.section {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 600ms var(--ease-out), transform 600ms var(--ease-out);
}
.section--in {
  opacity: 1;
  transform: translateY(0);
}
```

**Better yet — use CSS scroll-driven animations** (guide 06). Zero JS, runs on the compositor, respects reduced-motion automatically when wrapped. Fall back to IntersectionObserver for unsupported browsers.

---

## Spring Physics — when to use Framer Motion

CSS transitions are tweened: they go from A to B along an easing curve over a fixed duration. Spring physics are different: the element is pulled toward a target by a virtual spring, with mass, stiffness, and damping.

Springs feel more natural for: **draggable elements, swipe-to-dismiss, gesture-driven bottom sheets, anything the user manipulates physically.** CSS can't do springs natively (proposed but not shipped).

```tsx
import { motion, useDrag } from 'framer-motion';

function Card() {
  const { ref } = useDrag({
    onDragEnd: (e, info) => {
      if (Math.abs(info.offset.x) > 100) {
        // dismiss
      }
    }
  });

  return (
    <motion.div
      ref={ref}
      drag="x"
      dragConstraints={{ left: 0, right: 0 }}
      dragElastic={0.6}
      whileTap={{ scale: 0.95 }}
      transition={{ type: 'spring', stiffness: 300, damping: 24 }}
    >
      Swipe me
    </motion.div>
  );
}
```

**When to use springs vs tweens:**

| Use case | Tween | Spring |
|----------|-------|--------|
| Hover state | ✅ | ❌ |
| Modal open | ✅ | ⚠️ (acceptable if subtle) |
| Draggable card | ❌ | ✅ |
| Swipe-to-dismiss | ❌ | ✅ |
| Scroll-triggered reveal | ✅ | ❌ |
| Page transition | ✅ | ⚠️ |
| Bottom sheet | ❌ | ✅ |

**Framer Motion spring presets:**

```ts
{ stiffness: 300, damping: 24 }  // snappy — buttons, toggles
{ stiffness: 200, damping: 26 }  // balanced — modals, sheets
{ stiffness: 100, damping: 18 }  // loose — playful, child-like
{ stiffness: 500, damping: 30 }  // tight — precise, technical
```

Don't ship springs without tuning. Default `stiffness: 100, damping: 10` is too bouncy for production UI.

---

## Stagger Patterns

When multiple elements enter together, stagger them. Don't stagger by a fixed interval — stagger with **diminishing intervals** so the later elements catch up.

```css
/* Bad: equal stagger */
.item:nth-child(1) { animation-delay: 0ms; }
.item:nth-child(2) { animation-delay: 100ms; }
.item:nth-child(3) { animation-delay: 200ms; }
.item:nth-child(4) { animation-delay: 300ms; }
/* Total: 300ms — feels mechanical */

/* Good: diminishing stagger */
.item:nth-child(1) { animation-delay: 0ms; }
.item:nth-child(2) { animation-delay: 80ms; }
.item:nth-child(3) { animation-delay: 140ms; }
.item:nth-child(4) { animation-delay: 190ms; }
/* Total: 190ms — feels organic */
```

The diminishing-stagger formula: `delay_n = base * (1 - 0.5^n)`. Cap the total stagger at 250ms — beyond that, the user thinks the page is loading.

```tsx
// Framer Motion variant
const stagger = {
  animate: {
    transition: {
      staggerChildren: 0.06,        // 60ms base interval
      delayChildren: 0.1,
    },
  },
};

const item = {
  initial: { opacity: 0, y: 16 },
  animate: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.4, ease: [0.16, 1, 0.3, 1] },
  },
};

<ul>
  <motion.div variants={stagger} initial="initial" animate="animate">
    {items.map(i => <motion.li variants={item} key={i.id}>{i.label}</motion.li>)}
  </motion.div>
</ul>
```

---

## Hero Choreography

A hero entrance is the most-choreographed moment on the page. It should take 2–3 seconds total, with elements entering in sequence.

```css
/* Reference: Frameable hero entrance */
.hero-eyebrow {
  opacity: 0;
  animation: fade-up 600ms var(--ease-out) 200ms forwards;
}

.hero-headline-line-1 {
  opacity: 0;
  animation: fade-up 800ms var(--ease-out) 350ms forwards;
}

.hero-headline-line-2 {
  opacity: 0;
  animation: fade-up 800ms var(--ease-out) 480ms forwards;
}

.hero-subhead {
  opacity: 0;
  animation: fade-up 600ms var(--ease-out) 700ms forwards;
}

.hero-cta {
  opacity: 0;
  animation: fade-up 500ms var(--ease-out) 900ms forwards;
}

.hero-cta-secondary {
  opacity: 0;
  animation: fade-up 500ms var(--ease-out) 1000ms forwards;
}

.hero-product-ui {
  opacity: 0;
  animation: fade-up-soft 800ms var(--ease-out) 600ms forwards;
}

.hero-proof {
  opacity: 0;
  animation: fade-in 600ms var(--ease-out) 1400ms forwards;
}

@keyframes fade-up {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes fade-up-soft {
  from { opacity: 0; transform: translateY(40px) scale(0.98); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

@keyframes fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
  .hero-eyebrow,
  .hero-headline-line-1,
  .hero-headline-line-2,
  .hero-subhead,
  .hero-cta,
  .hero-cta-secondary,
  .hero-product-ui,
  .hero-proof {
    opacity: 1;
    animation: none;
  }
}
```

**Timeline:**

```
0.0s ──────────────────────────────────────────────── 3.0s
  │                                                    
  ├─ eyebrow ──────────────────┐                     
  │                            ├─ headline L1 ────── 
  │                            │  ├─ product UI ──── 
  │                            │  │            ├─ headline L2 ─
  │                            │  │            │           ├─ subhead ─
  │                            │  │            │           │       ├─ CTA ─
  │                            │  │            │           │       │     ├─ CTA2 ─
  │                            │  │            │           │       │     │       ├─ proof ─
```

The total is 2.0s (proof arrives at 1.4s + 0.6s duration = 2.0s). Under 3s. The user is not waiting.

**Rules:**
- Stagger by **75–150ms** between related elements (eyebrow → headline).
- Stagger by **200–400ms** between sections (headline → subhead → CTA).
- The **product UI** enters mid-choreography (600ms in) so it doesn't compete with the headline.
- The **proof element** enters last (after 1.4s) — it's the closing argument.

---

## Page Transitions — View Transitions API

For SPA route changes, use the View Transitions API (guide 06 has the full recipe). For app-level transitions, the pattern is:

```tsx
// On route change
function navigate(href: string) {
  if (!document.startViewTransition) {
    location.href = href;
    return;
  }
  document.startViewTransition(() => {
    flushSync(() => {
      // React router or similar: update the route
      router.push(href);
    });
  });
}
```

```css
::view-transition-old(root) {
  animation: 280ms var(--ease-in) both fade-out;
}
::view-transition-new(root) {
  animation: 280ms var(--ease-out) both fade-in;
}

@keyframes fade-out { to { opacity: 0; transform: translateY(-8px); } }
@keyframes fade-in  { from { opacity: 0; transform: translateY(8px); } }
```

For named transitions (so a card "expands" into a modal):

```tsx
<button style={{ viewTransitionName: 'card-1' }}>Open</button>

<Modal style={{ viewTransitionName: 'card-1' }}>...</Modal>
```

```css
::view-transition-old(card-1) {
  animation: 320ms var(--ease-in-out) both shrink;
}
::view-transition-new(card-1) {
  animation: 320ms var(--ease-in-out) both grow;
}

@keyframes shrink { to { opacity: 0; } }
@keyframes grow   { from { opacity: 0; transform: scale(0.95); } }
```

---

## Reduced-Motion Handling — non-negotiable

Every animation must respect `prefers-reduced-motion: reduce`. Some users have vestibular disorders, motion sensitivity, or simply prefer less motion. The spec is your legal and ethical obligation.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

But this nukes everything. **Better:** write the override per-component so essential state changes (focus rings, button presses) still happen instantly.

```css
@media (prefers-reduced-motion: reduce) {
  .section {
    opacity: 1 !important;
    transform: none !important;
    animation: none !important;
  }
  .btn {
    transition: background-color 100ms ease-out;
    /* keep color transition, drop transform */
  }
  .hero-headline {
    opacity: 1 !important;
    animation: none !important;
  }
}
```

For Framer Motion:

```tsx
import { useReducedMotion } from 'framer-motion';

function Section() {
  const reduce = useReducedMotion();
  return (
    <motion.div
      initial={reduce ? false : { opacity: 0, y: 24 }}
      whileInView={reduce ? undefined : { opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
    >
      Content
    </motion.div>
  );
}
```

---

## Performance — `transform` and `opacity` only

The browser compositor can animate `transform` and `opacity` cheaply (GPU). Animating `width`, `height`, `top`, `left`, `margin`, `padding`, `border-width`, `background-position`, `box-shadow` triggers layout and paint — frames drop.

**Layer promotion**: only promote to a GPU layer when animating. Don't slap `will-change: transform` on every element — it eats memory.

```css
/* Good — promoted only when needed */
.card {
  transition: transform 250ms var(--ease-out);
}
.card:hover {
  transform: translateY(-4px);
  will-change: transform;  /* apply only on hover */
}

/* Bad — promoted forever, memory leak */
.card {
  will-change: transform;
  transition: transform 250ms var(--ease-out);
}
```

**Property cost ranking** (cheapest → most expensive):

1. `opacity` — compositor only
2. `transform: translate / scale / rotate` — compositor only
3. `filter: blur / hue-rotate / saturate` — paint only, GPU-accelerated
4. `background-color`, `color` — paint
5. `box-shadow` — paint
6. `border-radius` — paint
7. `width`, `height`, `padding`, `margin` — **layout** (most expensive)
8. `top`, `left`, `right`, `bottom` (when `position` is set) — **layout**

If you must animate a layout property (rare), wrap it in `contain: layout` to limit the blast radius:

```css
.expanding-panel {
  contain: layout;
  transition: height 300ms var(--ease-in-out);
}
```

Or better: use `transform: scaleY()` instead of `height`.

---

## Reference: `data/animations-100.json`

The repo's `data/animations-100.json` lists 100 curated animations with timing curves, durations, and use-cases. When you're stuck for an animation idea, scan it. Don't reinvent.

Each entry looks like:

```json
{
  "id": "fade-up",
  "name": "Fade Up",
  "type": "entrance",
  "duration_ms": 600,
  "easing": "cubic-bezier(0.16, 1, 0.3, 1)",
  "properties": ["opacity", "transform: translateY"],
  "best_for": "Section reveals, hero choreography",
  "reduced_motion_fallback": "show without animation",
  "tags": ["subtle", "professional"]
}
```

Filter by `type` (entrance / hover / state-change / loop), by `best_for`, or by `tags`. Use 5–8 animations per project, not 30. Repetition builds identity.

---

## Anti-Patterns (Auto-Fail)

1. **`fade-in-up` on every section.** The most-overused animation on the web. Banned.
2. **`linear` easing.** Mechanical. Use any other curve.
3. **1000ms+ durations on micro-interactions.** 150–250ms is the range.
4. **Animating `width` / `height` / `top` / `left` / `margin`.** Triggers layout. Use `transform`.
5. **`will-change: transform` on every animated element.** Eats memory. Apply on hover/active only.
6. **Stagger of 100ms+ per element.** Total stagger exceeds 250ms and feels slow.
7. **No `prefers-reduced-motion` fallback.** Accessibility failure.
8. **Multiple heavy animations on screen at once.** Frame drops. Limit to 1 heavy animation (blur, large transform, filter) at a time.
9. **Hero choreography > 3 seconds total.** User thinks the page is broken.
10. **Springs on every interaction.** Bouncy UI gets exhausting. Reserve for physical / draggable elements.
11. **Background gradient position animation.** Triggers paint on the entire viewport. Use `@property --angle` + `transform: rotate()` on a blurred pseudo-element instead.
12. **`backdrop-filter` animations.** Tank FPS.
13. **Parallax on mobile.** Breaks the touch experience. Disable on touch devices.
14. **Auto-playing video / canvas animations** the user can't pause. Accessibility failure.
15. **Animation that hides content.** If a user has to wait for an animation to finish to read the text, kill the animation.

---

## Animation Budget — pick one

Per project, commit to an animation energy level. See guide 01.

| Level | Count | Examples |
|-------|-------|----------|
| Calm | 1–2 | Page-load only (hero entrance) |
| Measured | 3–5 | Hero + 2–3 scroll-triggered reveals + 1 hover micro-interaction |
| Energetic | 6–10 | Hero + scroll reveals + hover + tab transitions + counter |
| Cinematic | 10+ | Hero choreography + scroll reveals + draggable + transitions + ambient |

Most SaaS sites should be **measured**. Portfolios and creative-agency sites can be **energetic** or **cinematic**. Don't pick "cinematic" for a B2B SaaS — it distracts from the message.

---

## Output

When you finish this guide, you should have:
- A `tokens.css` with `--ease-out`, `--ease-in`, `--ease-in-out`, `--ease-back`, `--ease-material` defined
- A duration system: 150ms (micro), 280ms (small), 600ms (large), with `--dur-fast / --dur-base / --dur-slow` tokens
- An animation budget committed (calm / measured / energetic / cinematic) and written in `DESIGN-RATIONALE.md`
- Every animation using `transform` and `opacity` only (no layout-property animations)
- `prefers-reduced-motion` fallbacks on every animated component
- Hero choreography that completes in under 3 seconds
- Stagger patterns using diminishing intervals (max total stagger 250ms)
- Framer Motion (or equivalent) only where spring physics are needed (draggable, swipe)
- `will-change` applied on hover/active only, never permanently
- 5–8 animations from `data/animations-100.json` selected, not 30
- No anti-patterns present
