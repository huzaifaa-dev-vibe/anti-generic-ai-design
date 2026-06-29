# 07 — Technical SEO Guide

> SEO is the part of the project AI agents skip because it's "boring infrastructure." Then the site launches, gets zero traffic, and the user blames the design. SEO is design. A beautiful page Google can't crawl is a failed page.

## Why AI SEO fails

Every LLM-coded site ships the same five SEO mistakes:

1. **No meta description** — or worse, a generic one like "Welcome to our website."
2. **Title tag is the page H1** — ignored that titles and H1s serve different audiences (SERP vs reader).
3. **No structured data** — zero JSON-LD, meaning Google has to guess what the page is about.
4. **Images with no `alt`, no `width`/`height`, no `loading="lazy"`** — guaranteeing CLS and zero image search traffic.
5. **No `sitemap.xml`, no `robots.txt`, no canonicals** — orphan pages, duplicate content, crawl budget wasted.

The fix is mechanical. SEO is mostly a checklist. Get the checklist right and you'll outrank 90% of competitors who didn't.

---

## The 7 Pillars of Technical SEO

### Pillar 1 — The `<head>` Document

Every page needs these tags, in this order, in the `<head>`:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">

  <!-- Primary meta -->
  <title>Ship Design Reviews 4× Faster | Frameable</title>
  <meta name="description" content="Frameable cuts design review cycles from 5 days to 4 hours with async video annotations. Built for product teams of 5–50. Try it free.">
  <link rel="canonical" href="https://frameable.app/">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">

  <!-- OpenGraph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://frameable.app/">
  <meta property="og:title" content="Ship Design Reviews 4× Faster | Frameable">
  <meta property="og:description" content="Async video annotations for product teams. 5-day cycles become 4-hour cycles.">
  <meta property="og:image" content="https://frameable.app/og/default.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Frameable">
  <meta property="og:locale" content="en_US">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@frameable">
  <meta name="twitter:creator" content="@frameable">
  <meta name="twitter:title" content="Ship Design Reviews 4× Faster">
  <meta name="twitter:description" content="Async video annotations for product teams.">
  <meta name="twitter:image" content="https://frameable.app/og/default.png">

  <!-- Performance -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="image" href="https://frameable.app/hero.webp" fetchpriority="high">

  <!-- Structured data -->
  <script type="application/ld+json">{ "@context": "https://schema.org", ... }</script>
</head>
```

### Title tag — the most important 60 characters on the page

- **Length**: 50–60 characters (Google truncates at ~580 pixels, ≈60 chars at default font).
- **Structure**: `[Primary keyword] | [Brand]` or `[Benefit + keyword] | [Brand]`.
- **Each page has a unique title.** If two pages have the same title, Google picks one and ignores the other.
- **No keyword stuffing.** "Frameable | Design Review | Async Review | Video Review" is garbage. Google demotes.

```html
<!-- Bad -->
<title>Home | Frameable</title>
<title>Welcome to Frameable</title>

<!-- Good -->
<title>Ship Design Reviews 4× Faster | Frameable</title>
<title>Async Video Annotations — Frameable Features</title>
<title>Frameable vs Linear: Design Review Showdown</title>
```

### Meta description — the SERP ad you don't pay for

- **Length**: 150–160 characters.
- **Goal**: maximize click-through from the SERP. Treat it like ad copy.
- **Include the primary keyword** early (Google bolds matches).
- **Include a CTA or value prop**: "Try free", "See how it works", "Read the case study".
- **If you don't write one, Google auto-generates from page content.** Usually worse.

### Canonical — your duplicate-content protection

Every page must self-canonical. Paginated pages canonical to themselves (not page 1 — that's an old myth). Cross-domain duplicates canonical to the original.

```html
<link rel="canonical" href="https://frameable.app/features/annotations">
```

If you have `frameable.app/features/annotations` and `frameable.app/features/annotations?ref=newsletter`, both should canonical to the clean URL. Otherwise Google indexes both and splits ranking signals.

### Pillar 2 — Structured Data (JSON-LD)

JSON-LD is how you tell Google what your page *is*. Without it, Google guesses. With it, Google can show rich results (stars, prices, FAQ accordions, breadcrumbs in the SERP).

**Always use JSON-LD** (not microdata, not RDFa). It's a `<script type="application/ld+json">` block — invisible to users, machine-readable.

#### Article schema (blogs, news)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How we cut design review cycles from 5 days to 4 hours",
  "description": "A case study in async-first design review workflow.",
  "image": "https://frameable.app/blog/case-study-stripe/cover.png",
  "datePublished": "2025-03-14",
  "dateModified": "2025-03-16",
  "author": {
    "@type": "Person",
    "name": "Maya Patel",
    "url": "https://frameable.app/team/maya"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Frameable",
    "logo": {
      "@type": "ImageObject",
      "url": "https://frameable.app/logo.png",
      "width": 512,
      "height": 512
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://frameable.app/blog/case-study-stripe"
  }
}
```

#### Product schema (SaaS, e-commerce)

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Frameable Team Plan",
  "description": "Async video design review for product teams of 5–50.",
  "brand": { "@type": "Brand", "name": "Frameable" },
  "image": ["https://frameable.app/og/product.png"],
  "offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "USD",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "29.00",
      "priceCurrency": "USD",
      "referenceQuantity": { "@type": "QuantitativeValue", "value": 1, "unitCode": "MON" }
    },
    "availability": "https://schema.org/InStock",
    "url": "https://frameable.app/pricing"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127"
  }
}
```

**Don't fake ratings.** Google manually reviews and will penalize.

#### FAQPage schema (gets you the FAQ accordion in SERP)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long is the free trial?",
      "acceptedAnswer": { "@type": "Answer", "text": "14 days, no credit card required." }
    },
    {
      "@type": "Question",
      "name": "Do you offer student discounts?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes — 50% off with a valid .edu email." }
    }
  ]
}
```

FAQ schema is one of the highest-leverage wins in SEO. Every pricing page and product page should have 4–8 FAQ items. They render as accordions in Google's SERP, taking real estate from competitors.

#### BreadcrumbList schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://frameable.app/" },
    { "@type": "ListItem", "position": 2, "name": "Features", "item": "https://frameable.app/features" },
    { "@type": "ListItem", "position": 3, "name": "Annotations", "item": "https://frameable.app/features/annotations" }
  ]
}
```

#### Organization schema (site-wide, in the layout)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Frameable",
  "url": "https://frameable.app/",
  "logo": "https://frameable.app/logo.png",
  "sameAs": [
    "https://twitter.com/frameable",
    "https://github.com/frameable",
    "https://www.linkedin.com/company/frameable"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-555-0100",
    "contactType": "customer service",
    "areaServed": "US",
    "availableLanguage": ["English"]
  }
}
```

#### LocalBusiness schema (if you have a physical location)

```json
{
  "@context": "https://schema.org",
  "@type": "CafeOrCoffeeShop",
  "name": "Daydream Coffee",
  "image": "https://daydream.coffee/shop.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "143 Bell St",
    "addressLocality": "Seattle",
    "addressRegion": "WA",
    "postalCode": "98121",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 47.6149, "longitude": -122.3459 },
  "telephone": "+1-555-0100",
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "07:00",
    "closes": "18:00"
  }],
  "priceRange": "$$",
  "servesCuisine": "Coffee, Pastries",
  "url": "https://daydream.coffee"
}
```

### Pillar 3 — URL Structure

**Rules:**
- Lowercase, hyphen-separated, no query strings for canonical URLs.
- Short and keyword-rich: `/features/annotations` not `/products/our-amazing-annotation-tool-v2`.
- No date in URL for evergreen content (`/blog/async-design-reviews`, not `/blog/2025/03/14/async-design-reviews`).
- No file extensions: `/pricing` not `/pricing.html`.
- One URL = one page. No `?session=...` URLs indexed. Use `rel="canonical"` to collapse.

```text
✅ /features/annotations
✅ /blog/async-design-reviews
✅ /pricing
✅ /case-studies/stripe
❌ /blog/2025/03/14/async-design-reviews
❌ /index.php?page=features&id=12
❌ /Features/Annotations  (uppercase)
❌ /the-ultimate-guide-to-async-design-reviews-that-actually-works  (keyword stuffing)
```

### Pillar 4 — Semantic HTML

Google reads the DOM, not the design. A page where every section is a `<div class="section">` is harder to parse than a page using `<main>`, `<article>`, `<section>`, `<aside>`, `<nav>`, `<header>`, `<footer>`.

```html
<body>
  <header>
    <nav aria-label="Primary">...</nav>
  </header>

  <main>
    <article>
      <h1>Async design reviews cut cycle time 4×</h1>
      <p class="lede">A case study from Stripe's design team.</p>

      <section>
        <h2>The problem</h2>
        <p>...</p>
      </section>

      <section>
        <h2>The workflow</h2>
        <p>...</p>
      </section>

      <aside aria-label="Related reading">
        <h2>Related</h2>
        <ul>...</ul>
      </aside>
    </article>
  </main>

  <footer>...</footer>
</body>
```

**Heading hierarchy**: one `<h1>` per page, then `<h2>` for major sections, `<h3>` for subsections. **Never skip levels** (no `<h4>` directly under an `<h2>`). Google uses heading hierarchy to understand page structure for featured snippets.

### Pillar 5 — Internal Linking

Every page should have:
- **3+ internal links pointing to it** (so it's not orphaned).
- **3+ internal links pointing out** (so users and crawlers can navigate deeper).
- **Descriptive anchor text** — "how async reviews work" not "click here".

```html
<!-- Bad -->
<a href="/features">Learn more</a>
<a href="/pricing">Click here</a>

<!-- Good -->
<a href="/features/annotations">how async video annotations work</a>
<a href="/pricing/team-plan">see Team Plan pricing</a>
```

Internal links pass PageRank. A new blog post should link to 2–3 existing pillar pages, and those pillars should link back to the new post. Build a hub-and-spoke structure: one pillar page per topic, multiple supporting pages linking to it.

### Pillar 6 — Image Optimization

```html
<img
  src="/hero-dashboard.webp"
  alt="Frameable dashboard showing three pending design reviews with video annotation markers"
  width="1200"
  height="630"
  loading="lazy"
  decoding="async"
  fetchpriority="low"
>
```

**Rules:**
- **`alt` text**: describe the image in 100 chars or less. Decorative images get `alt=""` (empty, not omitted). Never keyword-stuff.
- **`width` and `height`**: always set. Prevents CLS (layout shift) while the image loads.
- **`loading="lazy"`** on every image below the fold. Hero image gets `fetchpriority="high"` and **no** lazy loading.
- **`decoding="async"`**: lets the browser decode off the main thread.
- **Format**: WebP (universally supported) or AVIF (better compression, 95% browser support). No JPEG/PNG unless you need transparency or animation.
- **Size**: serve responsive images with `srcset`.

```html
<img
  src="/hero-1200.webp"
  srcset="/hero-400.webp 400w, /hero-800.webp 800w, /hero-1200.webp 1200w, /hero-1600.webp 1600w"
  sizes="(max-width: 600px) 100vw, (max-width: 1200px) 50vw, 800px"
  alt="..."
  width="1200" height="630"
  fetchpriority="high"
>
```

### Pillar 7 — Core Web Vitals

Google measures three metrics for ranking:

| Metric | Target | Measures |
|--------|--------|----------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Perceived load speed |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Visual stability |
| **INP** (Interaction to Next Paint) | < 200ms | Interactivity / responsiveness |

**LCP optimization:**
- Identify the LCP element (usually the hero headline, hero image, or hero video poster).
- Preload it: `<link rel="preload" as="image" href="/hero.webp" fetchpriority="high">`.
- Serve it from a CDN. No third-party host for the LCP image.
- Compress to < 200KB.
- Use `font-display: swap` or `optional` so text doesn't wait on fonts.

**CLS optimization:**
- Always set `width` and `height` on images, videos, iframes.
- Reserve space for ads and embeds with `min-height`.
- Don't inject banners/toasts above existing content.
- Use CSS `aspect-ratio` for responsive media containers.

```css
.media-frame {
  aspect-ratio: 16 / 9;
  background: var(--surface);
}
```

**INP optimization:**
- Avoid long main-thread tasks (>50ms). Break them up with `requestIdleCallback` or `setTimeout(..., 0)`.
- Debounce input handlers (`input`, `scroll`, `mousemove`).
- Use `content-visibility: auto` on off-screen sections to skip rendering.

```css
.offscreen-section {
  content-visibility: auto;
  contain-intrinsic-size: 1px 5000px;
}
```

---

## International — `hreflang`

Multi-language sites need `hreflang` tags so Google serves the right language version:

```html
<link rel="alternate" hreflang="en" href="https://frameable.app/en/pricing">
<link rel="alternate" hreflang="es" href="https://frameable.app/es/pricing">
<link rel="alternate" hreflang="de" href="https://frameable.app/de/pricing">
<link rel="alternate" hreflang="x-default" href="https://frameable.app/en/pricing">
```

`x-default` is the fallback for users whose locale you don't have. Always include it. Use ISO 639-1 language codes, optionally with region (`en-GB`, `en-US`). Don't put `hreflang` on a page that doesn't have translations — it's noise.

URL structure options (pick one, be consistent):
- Subdirectory: `frameable.app/es/pricing` (recommended — single domain, all link equity pooled)
- Subdomain: `es.frameable.app/pricing` (Google treats as separate sites, splits equity)
- ccTLD: `frameable.es/pricing` (strongest geo-signal, expensive to maintain)

## Pagination vs Infinite Scroll

**Use pagination for indexable content** (blog lists, product category pages). Each page is a separate URL Google can crawl and rank.

```html
<!-- Page 2 -->
<link rel="prev" href="https://frameable.app/blog?page=1">
<link rel="next" href="https://frameable.app/blog?page=3">
```

(Note: Google deprecated `rel="prev"/"next"` as a ranking signal, but Bing still uses it and it doesn't hurt.)

**If you must use infinite scroll**, implement it as pushState history — each "page" of loaded content gets a unique URL (`?page=2`, `?page=3`) so Google can crawl it. Otherwise only the first page gets indexed.

For product listings: pagination. For feeds (Twitter-style): infinite scroll with proper pushState.

## `robots.txt` and `sitemap.xml`

### `robots.txt`

```text
User-agent: *
Allow: /

# Block crawl of internal/search pages
Disallow: /search
Disallow: /admin
Disallow: /*?session=
Disallow: /*?utm_

# Block AI training crawlers (optional — see guide 08)
User-agent: GPTBot
Disallow: /

Sitemap: https://frameable.app/sitemap.xml
```

**Don't block CSS/JS.** Googlebot renders pages with Chrome — if you block your stylesheet, Google sees the unstyled version and may misjudge the page.

### `sitemap.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://frameable.app/</loc>
    <lastmod>2025-03-14</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://frameable.app/features/annotations</loc>
    <lastmod>2025-03-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <!-- ... -->
</urlset>
```

For multi-language sites, use `xhtml:link` for hreflang in the sitemap:

```xml
<url>
  <loc>https://frameable.app/en/pricing</loc>
  <xhtml:link rel="alternate" hreflang="en" href="https://frameable.app/en/pricing"/>
  <xhtml:link rel="alternate" hreflang="es" href="https://frameable.app/es/pricing"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://frameable.app/en/pricing"/>
</url>
```

Generate sitemaps at build time. Don't serve them dynamically — Google wants a static XML file.

## OpenGraph and Twitter Cards — the SERP preview that matters on social

OG images are what show when someone shares your link in Slack, Twitter, LinkedIn, iMessage, Discord. A great OG image gets clicks; a missing one gets ignored.

- **Size**: 1200×630 pixels (1.91:1 ratio). Larger is fine but won't show more.
- **Format**: PNG or JPG. < 1MB.
- **Content**: brand mark + headline + a single visual hook. Don't cram.
- **Per-page**: every important page gets its own OG image. Don't share one across the site.

Build an OG image generation pipeline:

```ts
// app/og/[slug]/route.tsx (Next.js example)
import { ImageResponse } from 'next/og';

export async function GET(req: Request, { params }: { params: { slug: string } }) {
  const post = await getPost(params.slug);
  return new ImageResponse(
    (
      <div style={{ display: 'flex', flexDirection: 'column', width: 1200, height: 630, background: '#0E0E10', color: '#F4F4F1', padding: 80 }}>
        <div style={{ fontSize: 28, color: '#A1A1AA', marginBottom: 24 }}>{post.eyebrow}</div>
        <div style={{ fontSize: 72, fontWeight: 700, lineHeight: 1.1, maxWidth: 1000 }}>{post.title}</div>
        <div style={{ display: 'flex', marginTop: 'auto', alignItems: 'center', gap: 16 }}>
          <div style={{ fontSize: 32 }}>Frameable</div>
          <div style={{ fontSize: 24, color: '#A1A1AA' }}>frameable.app/blog/{post.slug}</div>
        </div>
      </div>
    ),
    { width: 1200, height: 630 }
  );
}
```

Then in the page `<head>`:

```html
<meta property="og:image" content="https://frameable.app/og/async-design-reviews">
```

---

## The 30-Point Pre-Launch SEO Checklist

Print this. Run it before every launch.

### Document fundamentals (1–7)
1. [ ] Each page has a unique `<title>` (50–60 chars)
2. [ ] Each page has a unique `<meta name="description">` (150–160 chars)
3. [ ] Each page has a self-referential `<link rel="canonical">`
4. [ ] `<html lang="...">` is set correctly
5. [ ] `<meta name="viewport">` is present
6. [ ] `<meta name="robots">` is set (default: `index, follow`)
7. [ ] Favicon, apple-touch-icon, theme-color are present

### Structured data (8–13)
8. [ ] Organization schema on the home page
9. [ ] Article / Product / LocalBusiness schema on relevant pages
10. [ ] BreadcrumbList schema on inner pages
11. [ ] FAQPage schema on pricing / product pages (where applicable)
12. [ ] All JSON-LD validates in [Schema.org Validator](https://validator.schema.org/)
13. [ ] All JSON-LD has zero errors in Google Rich Results Test

### Social / sharing (14–17)
14. [ ] OpenGraph tags on every page (og:url, og:title, og:description, og:image)
15. [ ] OG image is 1200×630, < 1MB, branded
16. [ ] Twitter card tags (`summary_large_image` for hero pages)
17. [ ] OG image per-page on top 10 landing pages (not one shared)

### Images (18–22)
18. [ ] Every image has `alt` text (decorative images get `alt=""`)
19. [ ] Every image has `width` and `height`
20. [ ] All below-fold images have `loading="lazy"`
21. [ ] All images are WebP or AVIF (no JPEG/PNG unless needed)
22. [ ] Hero/LCP image has `fetchpriority="high"` and is preloaded

### Crawl / index (23–27)
23. [ ] `robots.txt` is live, allows all important pages, blocks `/admin`, `/search`
24. [ ] `sitemap.xml` is live and submitted in Google Search Console
25. [ ] All canonical URLs return HTTP 200
26. [ ] 404 page exists and is helpful (links to popular pages, search)
27. [ ] 301 redirects for any renamed URLs

### Performance / Core Web Vitals (28–30)
28. [ ] LCP < 2.5s on mobile (test with PageSpeed Insights, not just desktop Lighthouse)
29. [ ] CLS < 0.1 (all images have width/height, no late-loading banners)
30. [ ] INP < 200ms (debounce handlers, break up long tasks)

### Bonus (run if you have time)
- Submit to Bing Webmaster Tools (free, Bing indexes faster than Google for new sites)
- Test with Google's [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- Run a Screaming Frog crawl — catches broken links, missing alts, duplicate titles
- Set up Google Search Console email alerts for indexing issues

---

## Anti-Patterns (Auto-Fail)

1. **No `<title>` or `<meta name="description">`.** Site is invisible in SERP.
2. **Same `<title>` on every page.** Google picks one, ignores the rest.
3. **JSON-LD with errors.** Schema.org validator must pass clean.
4. **`<img>` with no `alt`, no `width`, no `height`.** Accessibility and CLS failure.
5. **JPEG hero images at 1.5MB+.** Tank LCP.
6. **No sitemap.xml.** Pages take weeks to get indexed.
7. **`robots.txt` blocking CSS/JS.** Googlebot can't render your page properly.
8. **Infinite scroll with no pushState.** Only first page gets indexed.
9. **Duplicate content with no canonical.** Splits ranking across URLs.
10. **Keyword-stuffed titles** (`Best Design Review Tool | Top Design Review | #1 Review Tool`). Demoted by Google.
11. **Hidden text / cloaking** (text same color as background). Manual penalty.
12. **Buying backlinks.** Eventual penalty, not worth the short-term gain.
13. **AI-generated content published without human review.** Google's "helpful content" system can demote. Edit every AI-drafted page.
14. **No internal links from new content back to pillar pages.** New pages stay orphaned.
15. **Pop-ups covering the screen on mobile first load.** Google's "intrusive interstitials" penalty.

## Tooling

- [Google Search Console](https://search.google.com/search-console) — the source of truth for indexing, queries, click-through rate
- [Bing Webmaster Tools](https://www.bing.com/webmasters) — faster indexing, smaller reach
- [Schema.org Validator](https://validator.schema.org/) — validates JSON-LD
- [Rich Results Test](https://search.google.com/test/rich-results) — Google's official structured-data tester
- [PageSpeed Insights](https://pagespeed.web.dev/) — Core Web Vitals + Lighthouse
- [Screaming Frog](https://www.screamingfrog.co.uk/seo-spider/) — site crawler (free up to 500 URLs)
- [Ahrefs / Semrush](https://ahrefs.com) — keyword research and backlink tracking (paid)
- [OpenGraph.xyz](https://www.opengraph.xyz/) — preview OG cards across platforms

## Output

When you finish this guide, you should have:
- A complete `<head>` template applied to every page (title, description, canonical, OG, Twitter, robots)
- JSON-LD for Organization on the home page, plus Article / Product / FAQPage / BreadcrumbList where relevant
- All JSON-LD passing the Schema.org Validator
- `robots.txt` and `sitemap.xml` at the site root, sitemap submitted to Google Search Console
- All images with `alt`, `width`, `height`, `loading`, `fetchpriority`
- LCP < 2.5s, CLS < 0.1, INP < 200ms verified on mobile
- A per-page OG image pipeline (not one shared image)
- A 404 page that links to popular content
- 301 redirects for any renamed URLs
- The 30-point checklist signed off, every box ticked
