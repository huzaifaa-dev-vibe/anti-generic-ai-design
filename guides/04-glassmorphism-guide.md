# 04 — Glassmorphism Guide

> Glassmorphism is overused by AI and underused well. Most LLM-coded sites slap `backdrop-blur` on a card and call it done. Real glassmorphism is a system: blur, opacity, border, shadow, and noise working together to suggest a physical, frosted surface.

## Why AI glassmorphism fails

The default AI glass effect:

```tsx
<div className="bg-white/10 backdrop-blur-md rounded-2xl border border-white/20 p-6">
  {/* content */}
</div>
```

This fails because:
1. **No backdrop to blur.** `backdrop-blur` needs something *behind* it to blur. On a flat background, it does nothing.
2. **Opacity too low.** `bg-white/10` makes text unreadable.
3. **Border too subtle.** `border-white/20` is barely visible — glass needs a defined edge.
4. **No depth.** No inner highlight, no drop shadow, no layered surfaces.
5. **Same radius everywhere.** Real glass has variation — sharp edges on the bottom, softer on top.

## When to Use Glassmorphism

**Use it when:**
- There's a busy background (photo, gradient mesh, video) that needs layering
- You're building floating UI (sticky nav, command palette, modal)
- The brand voice is "modern / tech / premium"
- You have a strong color story behind the glass

**Don't use it when:**
- The background is flat or near-flat (glass does nothing)
- The site is content-heavy and readability matters most
- The brand is "warm / editorial / paper" — use opaque surfaces instead
- You're building a data-dense dashboard — glass obscures data

**Rule of thumb**: glass should reveal, not decorate. If removing the glass effect doesn't hurt the design, the glass wasn't earning its place.

---

## The 5-Layer Glass System

A real glass surface has 5 layers. Each is independently tunable.

```
┌─────────────────────────────┐
│  1. Backdrop (the thing blurred)│  ← what's behind the glass
├─────────────────────────────┤
│  2. Background tint           │  ← rgba color of the glass itself
├─────────────────────────────┤
│  3. Inner highlight (top)    │  ← 1px lighter line at the top
├─────────────────────────────┤
│  4. Border (subtle)          │  ← 1px defined edge
├─────────────────────────────┤
│  5. Drop shadow              │  ← layered shadow for depth
└─────────────────────────────┘
```

### Layer 1 — Backdrop

The glass needs something to blur. **Always verify there's content behind it.** If the parent has a flat background, the blur does nothing.

```tsx
// ❌ Glass on flat bg — blur is invisible
<section className="bg-white">
  <div className="bg-white/10 backdrop-blur-md" />
</section>

// ✅ Glass over a photo or gradient mesh
<section className="bg-[url('/photo.jpg')]">
  <div className="bg-white/10 backdrop-blur-md" />
</section>
```

### Layer 2 — Background tint

The glass itself has a color. For light glass: `rgba(255, 255, 255, 0.6–0.8)`. For dark glass: `rgba(20, 20, 25, 0.6–0.8)`.

**Opacity below 0.5 is unreadable. Opacity above 0.85 isn't glass, it's a translucent card.**

### Layer 3 — Inner highlight (top edge)

Real glass catches light at the top. Simulate with a `box-shadow: inset 0 1px 0 0 rgba(255,255,255,0.4)` (light mode) or `inset 0 1px 0 0 rgba(255,255,255,0.08)` (dark mode).

### Layer 4 — Border

A 1px border defines the edge. Use `rgba(255, 255, 255, 0.15)` for light glass, `rgba(255, 255, 255, 0.08)` for dark.

### Layer 5 — Drop shadow

Layered shadow for depth:

```css
box-shadow:
  0 1px 2px rgba(0, 0, 0, 0.04),
  0 4px 8px rgba(0, 0, 0, 0.04),
  0 12px 24px rgba(0, 0, 0, 0.06);
```

---

## The Reference Recipe

```css
.glass {
  /* Layer 2: tint */
  background: rgba(255, 255, 255, 0.65);

  /* Layer 1: blur */
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);

  /* Layer 4: border */
  border: 1px solid rgba(255, 255, 255, 0.18);

  /* Layer 3 + 5: inner highlight + outer shadow */
  box-shadow:
    inset 0 1px 0 0 rgba(255, 255, 255, 0.5),
    0 1px 2px rgba(0, 0, 0, 0.04),
    0 8px 24px rgba(0, 0, 0, 0.06);

  border-radius: 16px;
}

.glass-dark {
  background: rgba(20, 20, 25, 0.65);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow:
    inset 0 1px 0 0 rgba(255, 255, 255, 0.06),
    0 1px 2px rgba(0, 0, 0, 0.2),
    0 8px 24px rgba(0, 0, 0, 0.3);
  border-radius: 16px;
}
```

### Why `saturate(180%)`?

When backdrop-filter blurs an image, it can wash out colors. Adding `saturate(180%)` brings them back, making the glass feel like real frosted glass rather than fog. Apple uses this trick in macOS and iOS.

## Tuning for Different Surfaces

| Surface | Blur | Tint opacity | Use |
|---------|------|--------------|-----|
| Modal / dialog | 24px | 0.8 | Strong separation |
| Sticky nav | 16px | 0.7 | Always-visible nav over content |
| Floating card | 16px | 0.65 | Hero feature card |
| Tooltips / popovers | 12px | 0.85 | Readable transient UI |
| Notification toast | 16px | 0.75 | Floating alert |

## Browser Support & Fallbacks

`backdrop-filter` is supported in all modern browsers (Chrome 76+, Firefox 103+, Safari 9+). For older browsers, fall back to a solid background:

```css
.glass {
  /* Fallback for browsers without backdrop-filter */
  background: rgba(255, 255, 255, 0.95);
}

@supports (backdrop-filter: blur(16px)) {
  .glass {
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(16px) saturate(180%);
    -webkit-backdrop-filter: blur(16px) saturate(180%);
  }
}
```

## Performance — Don't Over-Blur

`backdrop-filter: blur()` is expensive. Every glass element repaints its backdrop on every scroll frame.

**Rules:**
- **Maximum 3 glass surfaces visible at once** on a page. More kills scroll performance.
- **Maximum `blur(24px)`**. Higher values tank FPS.
- **Don't animate backdrop-filter.** It re-renders the entire backdrop per frame.
- **Don't put glass inside glass.** The inner glass blurs the outer glass's content, which is already blurred — exponential cost.
- **Test on a low-end device.** If scroll jitters, reduce blur or remove glass.

## The "Noise" Trick

Real frosted glass has a subtle grain. Add it via a tiny SVG noise overlay:

```css
.glass-noise::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.4'/%3E%3C/svg%3E");
  opacity: 0.04;
  pointer-events: none;
  mix-blend-mode: overlay;
  border-radius: inherit;
}
```

This is the difference between "AI glass" and "real glass". Use it sparingly — once per page, max.

## Glass + Color

Tinted glass (e.g. brand-colored glass) follows the same recipe but with a colored tint:

```css
.glass-accent {
  background: rgba(180, 83, 9, 0.15);     /* tinted with accent */
  backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(180, 83, 9, 0.25);
  box-shadow:
    inset 0 1px 0 0 rgba(255, 255, 255, 0.3),
    0 8px 24px rgba(180, 83, 9, 0.1);
}
```

Use tinted glass for hero feature cards — it ties the glass to the brand.

## Anti-Patterns (Auto-Fail)

1. **`backdrop-blur` with no background behind it.** Pointless.
2. **`bg-white/5`** — too transparent, content unreadable.
3. **`backdrop-blur-3xl`** (48px+) — performance killer, looks fake.
4. **Glass on glass** (nested blurred surfaces). Exponential repaint cost.
5. **No border.** Glass without an edge looks like a smudge.
6. **Same border-radius as every other card.** Vary it: `rounded-2xl` for big panels, `rounded-lg` for inputs, `rounded-full` for pills.
7. **Glass nav over a flat-color hero.** No backdrop to blur — does nothing.
8. **Animated glass** (transitioning backdrop-filter). Tank FPS.
9. **Glass as a section background.** Sections should be opaque; glass is for floating elements.

## Variations to Try

### Frosted (classic)
The reference recipe above.

### Crystal (clearer, sharper)
```css
.glass-crystal {
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(8px) saturate(200%);
  border: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
}
```

### Smoked (darker, moodier)
```css
.glass-smoked {
  background: rgba(15, 15, 18, 0.55);
  backdrop-filter: blur(20px) saturate(120%);
  border: 1px solid rgba(255, 255, 255, 0.06);
  box-shadow:
    inset 0 1px 0 0 rgba(255, 255, 255, 0.05),
    0 12px 36px rgba(0, 0, 0, 0.4);
}
```

### Frosted with gradient border (premium)
```css
.glass-premium {
  position: relative;
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px) saturate(180%);
  border-radius: 16px;
}
.glass-premium::before {
  content: '';
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg, rgba(255,255,255,0.6), rgba(255,255,255,0.05));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}
```

## When NOT to Use Glass

- Editorial / publication sites (use opaque surfaces + paper texture)
- Banking / legal / government (use solid, high-trust surfaces)
- E-commerce product pages (use crisp white surfaces for product clarity)
- Any site where readability > aesthetic

Glass is a *flavor*, not a *default*. Use it on 1–2 hero surfaces, not as the primary surface language.

## Output

When you finish this guide, you should have:
- A `.glass` class with all 5 layers defined
- A `.glass-dark` variant for dark mode
- A `@supports` fallback for older browsers
- Maximum 3 glass surfaces on any single page
- A reason written in `DESIGN-RATIONALE.md` for every glass surface ("used on the hero feature card because the card floats over a gradient mesh background")
