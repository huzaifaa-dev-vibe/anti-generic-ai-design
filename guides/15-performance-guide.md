# 15 — Performance Guide

> Performance is design. A page that loads in 3.5s vs 1.2s feels like a different product, even if the pixels are identical. AI-coded sites ship 2MB JS bundles, 12 render-blocking stylesheets, unoptimized images at 4K, and `font-display: block` because the LLM didn't think about it. This guide is the performance budget that ships.

## Why AI fails at performance

Five defaults ruin AI performance:

1. **No bundle budget.** LLMs import libraries without weighing them. `lodash` for one function, `moment` instead of `date-fns`, a 200KB charting library for a 4-bar chart.
2. **Unoptimized images.** `<img src="hero.jpg" />` with no `srcset`, no `width`/`height`, no lazy loading, no modern format. The browser downloads a 4MB JPEG and renders it at 400px wide.
3. **Render-blocking everything.** Every CSS file in `<head>`, every JS file sync. The browser can't paint until all of them download.
4. **No font strategy.** Google Fonts loaded without `preconnect`, without `font-display: swap`, loading 6 weights of one family. The text is invisible for 2 seconds (FOIT).
5. **Client-side everything.** Every page is a SPA. The user waits for HTML, then waits for JS, then waits for hydration, then waits for the API call. Four waterfalls instead of one.

Performance is not an optimization you do later. It is a constraint you design against from line one.

---

## Rule 1 — Core Web Vitals are the targets

| Metric | Target | What it measures |
|--------|--------|------------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | When the largest visible element finishes rendering |
| **CLS** (Cumulative Layout Shift) | < 0.1 | How much the layout shifts during load |
| **INP** (Interaction to Next Paint) | < 200ms | Latency of the first user interaction |
| **TTFB** (Time to First Byte) | < 800ms | Server response time |
| **FCP** (First Contentful Paint) | < 1.8s | When the first content appears |

**Measure with**: Chrome DevTools → Lighthouse, PageSpeed Insights, WebPageTest, or `web-vitals` library in production.

```ts
// Production monitoring
import { onLCP, onCLS, onINP, onFCP, onTTFB } from 'web-vitals';

function sendToAnalytics({ name, value, id }) {
  // Send to your analytics platform
  navigator.sendBeacon('/api/vitals', JSON.stringify({ name, value, id }));
}

onLCP(sendToAnalytics);
onCLS(sendToAnalytics);
onINP(sendToAnalytics);
onFCP(sendToAnalytics);
onTTFB(sendToAnalytics);
```

The targets are the **75th percentile of page loads on mobile devices on 4G**. Not your dev machine on fiber. Test on a mid-range Android with throttled CPU and network.

## Rule 2 — Set a JS bundle budget

Industry standard: **250KB initial JS gzipped** for a marketing page, **350KB** for a SaaS app, **500KB** for a complex dashboard. Every KB above this needs justification.

```json
// package.json — bundle budget enforcement
{
  "scripts": {
    "analyze": "ANALYZE=true next build",
    "size-check": "bundlesize"
  },
  "bundlesize": [
    { "path": ".next/static/chunks/main-*.js", "maxSize": "80KB" },
    { "path": ".next/static/chunks/framework-*.js", "maxSize": "45KB" },
    { "path": ".next/static/chunks/pages/_app-*.js", "maxSize": "50KB" },
    { "path": ".next/static/chunks/pages/index-*.js", "maxSize": "40KB" }
  ]
}
```

**Rules**:
- Audit dependencies with `npm ls` and `bundlephobia.com` before installing.
- Replace `lodash` with `lodash-es` (tree-shakeable) or native methods.
- Replace `moment` with `date-fns` or `Intl.DateTimeFormat` (built-in).
- Replace `axios` with native `fetch` (smaller, no overhead).
- One charting library per project. If you need 3 charts, use one library.
- No `react-html-parser`, no `dangerouslySetInnerHTML` for static content.

## Rule 3 — Code splitting: load only what's needed

```tsx
import { lazy, Suspense } from 'react';

// ❌ Eagerly loaded — adds to initial bundle
import HeavyChart from './HeavyChart';

// ✅ Lazy loaded — only fetched when needed
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  return (
    <Suspense fallback={<ChartSkeleton />}>
      <HeavyChart data={data} />
    </Suspense>
  );
}
```

**Route-level code splitting** (Next.js does this automatically with the App Router):
- Each route is its own chunk.
- Shared modules are extracted into common chunks.
- Prefetch links on hover/viewport-in for instant navigation.

**Component-level code splitting**:
- Below-the-fold components (modals, settings panels, charts).
- Heavy libraries (video players, editors, 3D renderers).
- A/B-tested variants.

## Rule 4 — Tree shaking: kill unused exports

```ts
// ❌ Imports the entire lodash
import _ from 'lodash';
_.get(obj, 'a.b.c');

// ✅ Imports only what's used
import get from 'lodash-es/get';
get(obj, 'a.b.c');

// ✅ Even better — native
obj?.a?.b?.c;
```

Verify with `npm run analyze` (Next.js bundle analyzer or webpack-bundle-analyzer). If you see large chunks of a library you don't recognize, you're not tree-shaking.

**Side-effect flag**: in your `package.json`, set `"sideEffects": false` (or list files with side effects) so bundlers can tree-shake aggressively.

## Rule 5 — Image optimization: the largest lever

Images are usually 60–80% of page weight. Optimize them and LCP drops by 2 seconds.

### Format

| Format | Use case | Support |
|--------|----------|---------|
| **AVIF** | First choice, ~50% smaller than JPEG | All modern browsers (92%+) |
| **WebP** | Fallback, ~30% smaller than JPEG | 96%+ |
| **JPEG** | Fallback for legacy | 100% |
| **PNG** | Transparent images, screenshots | 100% |
| **SVG** | Icons, illustrations, logos | 100% |

```tsx
// Next.js handles this automatically
import Image from 'next/image';

<Image
  src="/hero.jpg"
  alt="Product dashboard"
  width={1200}
  height={630}
  priority  // above the fold
  sizes="(max-width: 768px) 100vw, 50vw"
/>

// Below the fold — lazy loaded by default
<Image src="/feature.jpg" alt="Feature" width={800} height={600} />
```

### The picture element (no Next.js)

```html
<picture>
  <source srcset="/hero.avif" type="image/avif" />
  <source srcset="/hero.webp" type="image/webp" />
  <img
    src="/hero.jpg"
    alt="Product dashboard"
    width="1200"
    height="630"
    loading="eager"
    fetchpriority="high"
    decoding="async"
  />
</picture>
```

### Sizing

```html
<!-- Responsive images with srcset -->
<img
  src="/hero-1200.jpg"
  srcset="
    /hero-400.jpg   400w,
    /hero-800.jpg   800w,
    /hero-1200.jpg 1200w,
    /hero-1600.jpg 1600w
  "
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="Hero"
  width="1200"
  height="630"
/>
```

**Always set `width` and `height`** (or `aspect-ratio` in CSS). Without them, the browser doesn't know the image's aspect ratio until it downloads, causing CLS.

### Blur-up placeholder

```tsx
// Pre-computed LQIP (low-quality image placeholder)
<Image
  src="/hero.jpg"
  alt="Hero"
  width={1200}
  height={630}
  placeholder="blur"
  blurDataURL="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD..." // tiny base64
/>
```

## Rule 6 — Font loading: no invisible text

Fonts are the second-largest cause of slow LCP. Strategy:

1. **Preload** the body font's regular weight.
2. **`font-display: swap`** for body — show fallback instantly, swap when loaded (no FOIT).
3. **`font-display: optional`** for display — if it loads slow, never swap (avoid late layout shift).
4. **Subset** to latin + the languages you support.
5. **Max 4 web font files** total.

```html
<!-- Preconnect to font CDN -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

<!-- Preload the body font regular weight -->
<link
  rel="preload"
  as="style"
  href="https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap"
/>

<!-- Load the stylesheet (non-blocking) -->
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Fraunces:wght@500;700&display=swap"
/>
```

### Self-hosted (better)

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-latin-400.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
```

Use [Fontsource](https://fontsource.org/) for self-hosted Google Fonts — they handle subsetting and `font-display` for you.

### Avoid layout shift on font swap

```css
/* Size-adjust the fallback to match the web font */
@font-face {
  font-family: 'Inter-fallback';
  src: local('Arial');
  size-adjust: 100.5%;
  ascent-override: 90%;
}

body {
  font-family: 'Inter', 'Inter-fallback', sans-serif;
}
```

## Rule 7 — Critical CSS: inline above-the-fold styles

The browser can't paint until CSS downloads. Inline the CSS needed for the first paint; load the rest async.

```html
<style>
  /* Critical CSS — inline in <head> */
  :root { --bg: #FAFAFA; --text: #18181B; /* ... */ }
  body { font-family: var(--font-body); background: var(--bg); color: var(--text); }
  .hero { padding: 96px 0; }
  .hero h1 { font-size: clamp(2.5rem, 5vw, 4rem); line-height: 1.05; }
  /* ... only what's needed for first paint */
</style>

<link rel="preload" href="/styles/main.css" as="style" onload="this.rel='stylesheet'" />
<noscript><link rel="stylesheet" href="/styles/main.css" /></noscript>
```

Next.js does this automatically. For raw HTML/React, use [critical](https://github.com/addyosmani/critical) or Critters.

## Rule 8 — Defer and async non-critical JS

```html
<!-- Critical JS — inline or sync -->
<script>/* tiny inline script for first paint */</script>

<!-- Non-critical JS — defer -->
<script src="/js/app.js" defer></script>

<!-- Analytics — async, low priority -->
<script src="https://analytics.example.com/script.js" async></script>
```

| Attribute | When to use |
|-----------|-------------|
| (none) | Never — blocks parsing |
| `defer` | Default for non-critical scripts. Executes in order, after HTML parses. |
| `async` | Third-party scripts (analytics, ads). Executes whenever it loads. |
| `module` | ES modules — defer by default |

## Rule 9 — Rendering strategy: RSC vs CSR vs SSG vs ISR

```
Is the page the same for every user, every visit?
├── Yes → SSG (Static Site Generation)
│         Built at deploy time. Fastest. Best for marketing pages, docs.
├── No, but updates infrequently → ISR (Incremental Static Regeneration)
│         Built at request time, cached. Best for blogs, catalogs.
├── No, updates per request → SSR (Server-Side Rendering)
│         Built per request. Best for personalized dashboards.
└── No, highly interactive → CSR (Client-Side Rendering)
         Built in browser. Best for apps with heavy state (Figma, sheets).

Hybrid: RSC (React Server Components) — render on server, stream HTML, hydrate selectively.
Best of SSR + CSR. Default for Next.js App Router.
```

| Strategy | TTFB | FCP | LCP | SEO | Use case |
|----------|------|-----|-----|-----|----------|
| SSG | Best | Best | Best | Best | Marketing, docs, blog |
| ISR | Good | Good | Good | Good | Catalogs, news |
| SSR | Fair | Fair | Fair | Good | Personalized dashboards |
| CSR | Poor | Poor | Poor | Poor | Highly interactive apps |
| RSC | Good | Good | Good | Good | Default for modern Next.js |

**Default**: SSG for everything you can. ISR for content that updates. SSR only when you must. CSR only for the parts that need it (drag-and-drop, real-time, canvas).

## Rule 10 — CDN and edge delivery

```
User → Edge (closest PoP) → Origin server
```

- **Static assets** (images, JS, CSS) on a CDN. Cloudflare, Vercel Edge, AWS CloudFront.
- **HTML** cached at the edge when possible. Next.js ISR does this automatically.
- **Edge functions** for personalization, A/B testing, auth — run closer to the user than the origin.

```ts
// Next.js edge middleware — runs at the edge
export const config = { runtime: 'edge' };

export default function middleware(req: NextRequest) {
  const country = req.geo?.country || 'US';
  const res = NextResponse.next();
  res.headers.set('x-user-country', country);
  return res;
}
```

## Rule 11 — HTTP/3 and modern protocols

HTTP/3 (over QUIC) reduces connection setup time, especially on flaky networks. All major CDNs support it. Enable it.

```nginx
# Nginx HTTP/3
server {
  listen 443 quic reuseport;
  listen 443 ssl;
  http2 on;
  http3 on;
  add_header Alt-Svc 'h3=":443"; ma=86400';
}
```

## Rule 12 — The Lighthouse 90+ Recipe

A reliable path to Lighthouse Performance ≥ 90 on a marketing page:

1. **SSG the page** (Next.js `output: 'export'` or `generateStaticParams`).
2. **Inline critical CSS**. Defer the rest.
3. **Optimize the LCP image**:
   - AVIF/WebP with JPEG fallback.
   - `priority` on the `<Image>`.
   - Sized with `width`/`height` to prevent CLS.
   - Preload: `<link rel="preload" as="image" href="/hero.aviv" fetchpriority="high" />`.
4. **Font strategy**: self-host, preload body regular, `font-display: swap`, subset to latin.
5. **JS budget**: ≤ 150KB initial gzipped. Code-split everything below the fold.
6. **No render-blocking third-party scripts**. Analytics async, deferred, loaded after `load`.
7. **Compress everything**: Brotli for HTML/CSS/JS, gzip fallback.
8. **Cache headers**: `Cache-Control: public, max-age=31536000, immutable` for hashed assets.

```ts
// next.config.ts
const nextConfig = {
  reactStrictMode: true,
  poweredByHeader: false,
  compress: true,
  images: {
    formats: ['image/avif', 'image/webp'],
    minimumCacheTTL: 60 * 60 * 24 * 365,
  },
  experimental: {
    optimizePackageImports: ['lucide-react', 'framer-motion'],
  },
};
```

## Anti-Patterns (Auto-Fail)

1. **JS bundle > 350KB gzipped** without justification.
2. **Images without `width`/`height`** — causes CLS.
3. **`<img>` without `loading="lazy"`** for below-the-fold images.
4. **`font-display: block`** — invisible text during font load (FOIT).
5. **Render-blocking CSS** in `<head>` not inlined.
6. **Synchronous third-party scripts** (analytics, chat widgets) in `<head>`.
7. **Moment.js** anywhere. Use `date-fns` or `Intl`.
8. **Entire lodash** when one function suffices.
9. **No CDN** for static assets.
10. **No cache headers** — every visit re-downloads everything.
11. **CSR for marketing pages** — kills SEO and LCP.
12. **Animated GIFs** — convert to MP4 (10× smaller) or WebP.
13. **`<video autoplay>` with no `preload="metadata"`** — downloads the full video.
14. **Unoptimized SVGs** — run through SVGO. Strip metadata, collapse paths.
15. **Polyfilling for modern browsers** — use `<script type="module">` / `nomodule` pattern, or build for evergreen browsers and skip polyfills.

## Code Example — Performance Budget Config

```json
// .lighthouserc.json
{
  "ci": {
    "assert": {
      "preset": "lighthouse:no-pwa",
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.9 }],
        "categories:accessibility": ["error", { "minScore": 0.95 }],
        "categories:seo": ["error", { "minScore": 0.95 }],
        "first-contentful-paint": ["error", { "maxNumericValue": 1800 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["error", { "maxNumericValue": 200 }],
        "unused-javascript": ["warn", { "maxNumericValue": 50000 }],
        "unused-css-rules": ["warn", { "maxNumericValue": 20000 }],
        "render-blocking-resources": ["error", { "maxNumericValue": 0 }]
      }
    }
  }
}
```

## Output

When you finish this guide, you should have:
- Lighthouse Performance ≥ 90 on mobile (4G, mid-range device)
- LCP < 2.5s, CLS < 0.1, INP < 200ms — measured in production
- JS bundle ≤ 250KB initial gzipped (or 350KB SaaS, 500KB dashboard)
- All images AVIF/WebP with fallback, lazy-loaded below the fold, with `width`/`height`
- Self-hosted fonts with `font-display: swap` and preloaded body weight
- Critical CSS inlined, non-critical deferred
- SSG/ISR for all public pages; SSR/CSR only where justified
- CDN for static assets with immutable cache headers
- A `web-vitals` monitoring script sending real user metrics to analytics
- Lighthouse CI config in repo, blocking PRs that regress scores
- Documented in `DESIGN-RATIONALE.md`: the bundle size, the Lighthouse scores, the date measured
