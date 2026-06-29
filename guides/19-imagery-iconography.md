# 19 — Imagery & Iconography

> Imagery is where AI-coded sites go to die. The default stack — unDraw illustrations, emoji feature icons, stock photos of handshakes, Lucide outlines in `rounded-2xl` cards — is the visual equivalent of Lorem ipsum. Real design treats imagery as a system: a chosen visual language, applied consistently, with every asset earning its place.

## Why AI fails at imagery and iconography

Six defaults ruin AI imagery:

1. **Emoji as feature icons.** 🚀 for "fast", ⚡ for "performance", 🎯 for "precision", 🔒 for "secure". Emoji render differently across platforms, can't be styled, can't be themed, and signal "we didn't have a designer".
2. **unDraw illustrations.** The flat, monotone, purple-people illustrations that ship free from unDraw.co. They were novel in 2018. They are now the universal symbol of "we couldn't afford an illustrator".
3. **Stock photos of handshakes.** Two businesspeople shaking hands in front of a glass wall. Or three diverse colleagues laughing at a laptop. These images appear on 50% of B2B sites and signal nothing.
4. **Lucide outline icons in every card.** The same 24px outline icon set on every feature card. Serviceable, but invisible — and identical to every other AI site.
5. **Mixed icon systems.** Lucide here, Heroicons there, a custom SVG somewhere else, all in the same nav. Visual chaos.
6. **No image strategy.** Photos that don't share a color treatment, illustrations that don't share a stroke language, screenshots that don't share a frame style. Each image is an island.

Imagery is a system. Pick one and commit.

---

## Rule 1 — Imagery categories: when to use each

| Category | When to use | When to avoid |
|----------|-------------|---------------|
| **Real photography** | Hero, team, product in use, customer testimonials | When you don't have real photos (don't fake with stock) |
| **Custom illustration** | Brand expression, abstract concepts, onboarding flows | When the budget is zero (don't use unDraw) |
| **3D renders** | Product visualization, hero focal point, brand differentiator | When the product isn't 3D (looks arbitrary) |
| **Generative art** | Decorative backgrounds, abstract hero focal, motion-driven pieces | When it competes with content |
| **Screenshots** | Product pages, "see it in action", docs | Without a browser/chrome frame |
| **Icons** | Navigation, features, UI affordances, status | As decoration (icons must signal function) |
| **No imagery** | Editorial, content-first, minimal sites | Never the cheap option — a deliberate choice |

**Decision tree**:
```
Does the page need imagery at all?
├── No (editorial, docs) → text and whitespace only
├── Yes → What's the focal point?
│   ├── The product → screenshot or 3D render
│   ├── The people → real photography (team, customers)
│   ├── An abstract concept → custom illustration or generative art
│   └── A feature → custom icon, NOT an emoji
```

## Rule 2 — Photography: real > stock

A real photo of your actual product, actual team, or actual customer is worth 10,000 stock photos. Stock photography is the visual equivalent of marketing copy that says "powerful and scalable" — true of every company, distinctive of none.

### When you must use stock

If you have no choice (no budget for a photographer, no real photos yet), follow these rules:

1. **Avoid the cliché shots**. Handshakes, diverse colleagues laughing at laptops, "thinking person with hand on chin", sunsets over cities. If you've seen it on a LinkedIn ad, it's banned.
2. **Pick a single source and a single photographer**. Unsplash, Pexels, or a paid source (Stocksy, Getty). Within that source, find one photographer whose style you like and use only their work for visual consistency.
3. **Apply a color treatment**. A unifying duotone, grain, or contrast curve makes disparate photos feel like a set.
4. **Crop consistently**. Same aspect ratio, same composition style (e.g. all centered, all off-center to the right).

```css
/* Duotone treatment for visual consistency */
.photo-duotone {
  filter: grayscale(100%) contrast(1.1);
  background: var(--accent);
  /* Use mix-blend-mode to apply the tint */
}

.photo-duotone img {
  mix-blend-mode: multiply;
  filter: grayscale(100%) contrast(1.2);
}
```

### Real photography rules

- Hire a photographer for one day. Get 50 photos you'll use for two years.
- Show the actual team, the actual office, the actual product in actual use.
- Never use AI-generated photos of "people" — they look right at first glance and uncanny at second. (See Rule 8 for when AI imagery is acceptable.)
- Always include alt text describing what's in the photo and why it matters.

## Rule 3 — Illustration: custom or nothing

If you cannot commission custom illustrations, do not use illustrations. unDraw and Storyset are banned — they are the AI default, and they signal "we didn't try".

### When illustration is the right choice

- Onboarding flows where the abstract concept needs visual representation
- Empty states (illustration + headline + CTA — see guide 13)
- Brand expression on hero sections where photography doesn't fit
- Explaining multi-step processes (custom diagram > stock photo)

### Custom illustration rules

- **One illustrator per project.** Mixing illustration styles is the cardinal sin.
- **A consistent stroke language.** Same stroke weight, same corner style, same fill strategy across every illustration.
- **A consistent character style.** If you use human figures, they share a face style, body proportion, color palette.
- **Aligned with the brand palette.** Illustrations use the brand accent and supporting colors. Not generic "illustration colors".

```tsx
// ✅ Custom SVG illustration with brand palette
<svg viewBox="0 0 400 300" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="300" fill="var(--bg)" />
  <circle cx="200" cy="120" r="60" fill="var(--accent-soft)" />
  <path
    d="M150 200 Q200 160 250 200 T350 200"
    stroke="var(--accent)"
    stroke-width="3"
    fill="none"
    stroke-linecap="round"
  />
  <text x="200" y="260" text-anchor="middle" fill="var(--text)" font-family="var(--font-display)" font-size="18">
    Your first project
  </text>
</svg>
```

## Rule 4 — 3D renders: earn the budget

3D renders (think Apple's product pages, Linear's hero animations, Vercel's gradient spheres) are the high-end of imagery. They require either a 3D artist or significant tooling (Blender, Spline, R3F).

### When to use 3D

- Hardware products (show the device from every angle)
- Tech brands with a "premium" positioning
- Hero focal points that need to feel "alive"
- Abstract brand expressions (the Vercel triangle, the Stripe gradient orbs)

### When not to use 3D

- You're a content site (3D adds nothing to reading)
- You can't afford to do it well (bad 3D is worse than no 3D)
- The 3D doesn't connect to the product (random gradient orb on a B2B SaaS = decorative noise)

### 3D rules

- Render once, optimize, ship as video (MP4/WebM) or interactive WebGL
- For interactive 3D: use react-three-fiber, budget ≤150KB for the scene, lazy-load below the fold
- Always have a static fallback image for users with reduced motion or no WebGL

## Rule 5 — Screenshots: frame them properly

A raw screenshot floating in a section looks unfinished. Three options:

### Option A: Browser chrome frame

```tsx
<div className="browser-frame">
  <div className="browser-bar">
    <span className="browser-dot red" />
    <span className="browser-dot yellow" />
    <span className="browser-dot green" />
    <div className="browser-url">app.example.com</div>
  </div>
  <img src="/screenshot.png" alt="Product dashboard" />
</div>
```

```css
.browser-frame {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border);
  box-shadow: var(--shadow-card);
  background: var(--surface);
}

.browser-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: var(--surface-hover);
  border-bottom: 1px solid var(--border);
}

.browser-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
}
.browser-dot.red    { background: #FF5F57; }
.browser-dot.yellow { background: #FEBC2E; }
.browser-dot.green  { background: #28C840; }

.browser-url {
  margin-left: 12px;
  padding: 4px 12px;
  background: var(--surface);
  border-radius: 6px;
  font-size: 12px;
  color: var(--text-muted);
  font-family: var(--font-mono);
}
```

### Option B: Device frame

For mobile screenshots, use a phone frame (a CSS-drawn phone, not a stock mockup). For laptop screenshots, use a laptop frame.

### Option C: No frame, full bleed

When the screenshot itself is the hero, crop tight and let it span the full container. No frame, no shadow — just the image.

**Never**: a screenshot with a drop shadow and no frame, floating in the middle of a section. This is the AI default and it looks like a placeholder.

## Rule 6 — Icon systems: pick one, commit

| Icon system | Stroke | Style | Best for |
|-------------|--------|-------|----------|
| **Lucide** | 2px outline | Geometric, neutral | Default for SaaS, dev tools |
| **Phosphor** | Variable (1.5–2px) | Six weights (thin → fill) | When you need weight flexibility |
| **Heroicons** | 1.5px outline | Tailwind-native, simple | Tailwind projects, simple UIs |
| **Tabler Icons** | 2px outline | Open-source, large catalog | Dashboards, dense UIs |
| **Iconoir** | 1.5px outline | Hand-drawn feel | Editorial, creative sites |
| **Custom** | Your choice | Brand-specific | When you have a designer |

**Rules**:
- Pick one system per project. Never mix Lucide and Heroicons on the same page.
- Stroke width is consistent across the entire site. Pick `1.5px` or `2px` and commit.
- Icon size follows the 8pt grid: 16, 20, 24, 32, 48, 64. No 18px icons next to 24px icons.
- Lucide in every feature card is the AI default — readable but invisible. If you go with Lucide, vary the layout (icon left of text, not above) so it doesn't look templated.

## Rule 7 — Custom SVG: when to invest

Custom icons earn their place when:

- The icon represents a brand-specific concept (a unique product feature, a brand mascot).
- The standard library doesn't have a good fit (you're reaching for the 6th-closest icon).
- The icon needs to match an unusual stroke weight or corner radius.
- Brand recognition requires a custom set (think Linear's mark, Vercel's triangle).

```tsx
// ✅ Custom icon for a brand-specific feature
function AsyncTracingIcon({ size = 24 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M4 12h4l2-6 4 12 2-6h4" />
    </svg>
  );
}
```

## Rule 8 — Generative imagery: when, and when not

AI-generated imagery (Midjourney, DALL-E, Stable Diffusion, Flux) has earned a place in the workflow, but it's narrower than AI vendors claim.

### When generative imagery works

- **Abstract textures and backgrounds**. Gradient meshes, noise patterns, organic shapes — generative tools excel here.
- **Mood reference, not final art**. Generate 20 mood images to align the team; commission a human for the final.
- **Surreal / dreamlike brand expression**. When the brand voice is "weird" or "experimental", generative art fits.
- **Internal prototyping**. Generate placeholder imagery for early prototypes; replace before ship.

### When generative imagery fails

- **Faces and people**. AI faces have the uncanny-valley problem. Real customers > AI people, every time.
- **Specific products**. AI can't render your actual product. Use a real screenshot.
- **Hands**. AI still can't do hands reliably. Avoid.
- **Text in images**. AI generates gibberish text. Avoid.
- **Photorealism**. AI photorealism looks "right" at first glance and "wrong" at second. Use real photos.

**Rule**: if a viewer can confidently say "that's AI-generated" within 3 seconds, it's a fail. The best generative imagery is invisible as such.

## Rule 9 — Icon sizing system

| Size | Use | Padding inside |
|------|-----|----------------|
| 16px | Inline with text, dense UI | 0 |
| 20px | Buttons, small feature icons | 2px |
| 24px | Standard feature icons, nav | 4px |
| 32px | Empty state icons | 4px |
| 48px | Large feature illustration | 8px |
| 64px | Hero icon | 12px |

```css
:root {
  --icon-sm: 16px;
  --icon-md: 20px;
  --icon-base: 24px;
  --icon-lg: 32px;
  --icon-xl: 48px;
  --icon-2xl: 64px;
}

.icon {
  width: var(--icon-base);
  height: var(--icon-base);
  flex-shrink: 0;
}
```

## Rule 10 — Icon-in-button alignment

The single most common AI mistake: icon misaligned with button text.

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--step-0);
  line-height: 1;
}

.btn .icon {
  width: 1em;     /* scales with font size */
  height: 1em;
}

.btn .icon-leading  { margin-left: calc(-1 * var(--space-1)); }
.btn .icon-trailing { margin-right: calc(-1 * var(--space-1)); }
```

```tsx
<button className="btn">
  <DownloadIcon className="icon icon-leading" aria-hidden />
  Download
</button>

<button className="btn">
  Continue
  <ArrowRightIcon className="icon icon-trailing" aria-hidden />
</button>
```

**Rules**:
- Icon size matches the text cap height (≈1em), not the line height.
- Gap between icon and text: 6–8px (var(--space-2)).
- Leading icon pulls left by 4px to optically center the icon-text group.
- Trailing icon pulls right by 4px for the same reason.
- Icon is `aria-hidden` — the button text is the accessible name.

## Rule 11 — Accessible icon labels

```tsx
// Icon-only button — needs aria-label
<button className="icon-button" aria-label="Close dialog" onClick={onClose}>
  <XIcon aria-hidden="true" />
</button>

// Decorative icon next to text — icon is aria-hidden
<button className="btn">
  <DownloadIcon aria-hidden="true" />
  Download report
</button>

// Meaningful icon (the icon alone communicates the info) — needs label
<div className="status">
  <CheckCircleIcon aria-label="Success" className="icon text-success" />
  <span>Deploy completed</span>
</div>
```

**Rules**:
- Decorative icons (paired with text): `aria-hidden="true"`.
- Icon-only buttons: `aria-label` on the button, `aria-hidden` on the icon.
- Meaningful icons (status indicators): `aria-label` on the icon, or visually-hidden text.

## Rule 12 — Imagery color treatment: unify

If your page uses multiple images (photos, illustrations, screenshots), unify them with a color treatment:

```css
/* Apply a unifying filter to all hero images */
.hero-image {
  filter: saturate(0.95) contrast(1.05);
}

/* Duotone for editorial photography */
.editorial-photo {
  position: relative;
}
.editorial-photo img {
  filter: grayscale(100%) contrast(1.1);
  mix-blend-mode: multiply;
}
.editorial-photo::after {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--accent);
  mix-blend-mode: screen;
  pointer-events: none;
}

/* Grain overlay for cohesion */
.grain-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.4'/%3E%3C/svg%3E");
  opacity: 0.06;
  pointer-events: none;
  mix-blend-mode: overlay;
}
```

## Rule 13 — Image performance

Imagery is the largest page-weight contributor. See guide 15 for the full treatment. Short rules:

- AVIF first, WebP fallback, JPEG last resort.
- `width` and `height` on every image (prevents CLS).
- `loading="lazy"` for below-the-fold, `loading="eager" fetchpriority="high"` for LCP.
- `srcset` for responsive images.
- Run all SVGs through SVGO.
- Never ship a 4MB image. 200KB max for hero, 80KB for inline.

## Anti-Patterns (Auto-Fail)

1. **Emoji as feature icons** (🚀⚡🎯🔒). Banned.
2. **unDraw or Storyset illustrations**. Banned.
3. **Stock photos of handshakes, diverse-colleagues-at-laptop, sunset-over-city**. Banned.
4. **Mixed icon systems** (Lucide + Heroicons on the same page). Pick one.
5. **Stroke width inconsistency**. Pick `1.5px` or `2px` and commit.
6. **Icon sizes outside the 8pt grid** (18px next to 24px).
7. **Misaligned icon-in-button**. Use `display: inline-flex; align-items: center`.
8. **Icon-only buttons without `aria-label`**.
9. **Raw screenshots with drop shadows and no frame**.
10. **AI-generated faces or people** in production.
11. **No color treatment across disparate images**. Apply a unifying filter.
12. **SVGs not passed through SVGO** — bloated markup, designer metadata.
13. **Stock photos with no alt text**.
14. **Decorative icons without `aria-hidden="true"`**.
15. **3D renders on sites where 3D doesn't connect to the product**.

## Code Example — A Feature Card with Custom Icon

```tsx
import { ShieldCheck } from 'lucide-react';

function FeatureCard() {
  return (
    <article className="feature-card">
      <div className="feature-icon-wrapper">
        <ShieldCheck
          size={24}
          strokeWidth={1.5}
          aria-hidden="true"
          className="feature-icon"
        />
      </div>
      <h3 className="feature-title">SOC 2 Type II certified</h3>
      <p className="feature-description">
        Every API request is logged, encrypted in transit and at rest, and
        audited annually by an independent third party.
      </p>
      <a href="/security" className="feature-link">
        Read the security overview
        <ArrowRight size={16} aria-hidden="true" />
      </a>
    </article>
  );
}
```

```css
.feature-card {
  padding: var(--space-6);
  border: 1px solid var(--border);
  border-radius: 12px;
  background: var(--surface);
}

.feature-icon-wrapper {
  width: 40px;
  height: 40px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  background: var(--accent-soft);
  color: var(--accent);
  margin-bottom: var(--space-4);
}

.feature-icon {
  width: 20px;
  height: 20px;
}

.feature-title {
  font-size: var(--step-1);
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.feature-description {
  font-size: var(--step-0);
  line-height: 1.55;
  color: var(--text-muted);
  margin-bottom: var(--space-4);
}

.feature-link {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: 2px;
  font-weight: 500;
}
```

## Output

When you finish this guide, you should have:
- An imagery category chosen per section (photo / illustration / 3D / screenshot / icon / none)
- A single icon system committed (Lucide, Phosphor, Heroicons, Tabler, Iconoir, or custom)
- A consistent stroke weight (1.5px or 2px) across every icon
- An icon size system on the 8pt grid (16/20/24/32/48/64)
- All icon-in-button pairs aligned with `inline-flex`
- All icon-only buttons with `aria-label`
- All decorative icons with `aria-hidden="true"`
- All screenshots framed (browser chrome, device, or full-bleed — never raw with shadow)
- A unifying color treatment across all images
- No emoji feature icons, no unDraw, no stock handshakes
- A documented decision in `DESIGN-RATIONALE.md`: why this imagery system, what it signals, what it avoids
