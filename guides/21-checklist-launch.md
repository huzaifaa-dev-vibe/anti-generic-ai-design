# 21 — Pre-Launch Checklist (The Master Gate)

> This is the final gate. Nothing ships without passing every check on this list. Not "most of them". Not "the important ones". Every single one. A page that ships with three boxes unchecked is a page that ships broken. The checklist is binary: yes or no. There is no "almost".

## Why this checklist exists

AI-coded sites ship fast — and ship unfinished. The LLM writes the hero, the features, the pricing, and stops. It doesn't check the meta tags, the structured data, the focus states, the Lighthouse score, the OG image, the sitemap. The result: a page that looks fine in the preview and fails in production.

This checklist exists because the difference between "looks done" and "is done" is 50 specific things. Senior engineers know this. They run through the list before every ship. This guide is the list.

## How to use this checklist

1. **Run it before every ship.** Not just the first ship — every ship.
2. **Every check is binary.** Yes or no. No "mostly", no "kind of".
3. **Any "no" blocks the ship.** Either fix it or explicitly defer with a written reason in `DESIGN-RATIONALE.md`.
4. **The checklist is the spec.** If something is on the list, it's required. If something is not on the list, it's optional.
5. **Print it, sign it, date it.** A checklist that lives in a README is a checklist nobody runs.

---

## The 50-Point Pre-Launch Checklist

| # | Category | Check | Status |
|---|----------|-------|--------|
| 1 | Design | Does the page have exactly one `<h1>`? | ☐ Yes ☐ No |
| 2 | Design | Does the page use a non-default color palette (no indigo/violet/pink gradient)? | ☐ Yes ☐ No |
| 3 | Design | Does the page use a non-default font pairing (not Inter for everything)? | ☐ Yes ☐ No |
| 4 | Design | Does the page use the 8pt spacing system (no `gap-3`, `gap-5`, `gap-7`)? | ☐ Yes ☐ No |
| 5 | Design | Does every section have a justified max-width (not reflexive `max-w-7xl`)? | ☐ Yes ☐ No |
| 6 | Design | Does the hero have a single focal point (not headline + product + video competing)? | ☐ Yes ☐ No |
| 7 | Design | Is the visual texture language consistent across the page (flat / glass / grain / brutalist — pick one)? | ☐ Yes ☐ No |
| 8 | Design | Does the page have at most 3 ambient animations and 5 triggered animations (motion budget)? | ☐ Yes ☐ No |
| 9 | Design | Does every interactive element have all 5 states (rest, hover, focus, active, disabled)? | ☐ Yes ☐ No |
| 10 | Design | Does the page have zero emoji feature icons, zero unDraw illustrations, zero stock handshakes? | ☐ Yes ☐ No |
| 11 | Code quality | Does the JS bundle weigh ≤ 250KB gzipped initial (or 350KB SaaS / 500KB dashboard)? | ☐ Yes ☐ No |
| 12 | Code quality | Are all images optimized (AVIF/WebP with fallback, `width`/`height`, lazy-loaded below fold)? | ☐ Yes ☐ No |
| 13 | Code quality | Are fonts self-hosted or preconnected, with `font-display: swap` and ≤4 files total? | ☐ Yes ☐ No |
| 14 | Code quality | Is the build passing in CI with no warnings? | ☐ Yes ☐ No |
| 15 | Code quality | Are environment variables checked (no API keys in client bundle, no `.env` in repo)? | ☐ Yes ☐ No |
| 16 | Code quality | Is the `.env.example` file present and up to date? | ☐ Yes ☐ No |
| 17 | Code quality | Are all dependencies pinned to specific versions (no `^` or `~` for production deps)? | ☐ Yes ☐ No |
| 18 | Code quality | Is the `DESIGN-RATIONALE.md` file written with all 7 debate blocks completed? | ☐ Yes ☐ No |
| 19 | Accessibility | Does every interactive element have a visible `:focus-visible` style (no `outline: none` without replacement)? | ☐ Yes ☐ No |
| 20 | Accessibility | Do all body text colors pass 4.5:1 contrast against their background? | ☐ Yes ☐ No |
| 21 | Accessibility | Are all form inputs paired with `<label>` elements (associated via `for`/`id`)? | ☐ Yes ☐ No |
| 22 | Accessibility | Are all form errors associated via `aria-describedby` and announced via `role="alert"`? | ☐ Yes ☐ No |
| 23 | Accessibility | Are all icon-only buttons labeled via `aria-label` or visually-hidden text? | ☐ Yes ☐ No |
| 24 | Accessibility | Are all decorative icons marked `aria-hidden="true"`? | ☐ Yes ☐ No |
| 25 | Accessibility | Does the page have a "Skip to content" link as the first focusable element? | ☐ Yes ☐ No |
| 26 | Accessibility | Is `<html lang="...">` set correctly? | ☐ Yes ☐ No |
| 27 | Accessibility | Does the page respect `prefers-reduced-motion: reduce`? | ☐ Yes ☐ No |
| 28 | Accessibility | Are all touch targets ≥ 44×44px (or 24×24 with adequate spacing)? | ☐ Yes ☐ No |
| 29 | Accessibility | Was the page tested with a screen reader (VoiceOver or NVDA)? | ☐ Yes ☐ No |
| 30 | Accessibility | Does the Lighthouse Accessibility score ≥ 95? | ☐ Yes ☐ No |
| 31 | SEO | Is the `<title>` unique, descriptive, and under 60 characters? | ☐ Yes ☐ No |
| 32 | SEO | Is the `<meta name="description">` present, compelling, and under 160 characters? | ☐ Yes ☐ No |
| 33 | SEO | Is canonical URL set (`<link rel="canonical">`)? | ☐ Yes ☐ No |
| 34 | SEO | Is Open Graph metadata complete (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`)? | ☐ Yes ☐ No |
| 35 | SEO | Is the Open Graph image 1200×630px, optimized, and visually compelling? | ☐ Yes ☐ No |
| 36 | SEO | Is Twitter Card metadata present (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`)? | ☐ Yes ☐ No |
| 37 | SEO | Is structured data (JSON-LD) present for the page type (Article, Product, FAQPage, BreadcrumbList, Organization)? | ☐ Yes ☐ No |
| 38 | SEO | Is the `sitemap.xml` generated and submitted to Google Search Console? | ☐ Yes ☐ No |
| 39 | Performance | Is LCP < 2.5s on mobile (measured in production, not localhost)? | ☐ Yes ☐ No |
| 40 | Performance | Is CLS < 0.1 on the page? | ☐ Yes ☐ No |
| 41 | Performance | Is INP < 200ms on the page? | ☐ Yes ☐ No |
| 42 | Performance | Is the LCP element preloaded (e.g. `<link rel="preload" as="image">`)? | ☐ Yes ☐ No |
| 43 | Performance | Are render-blocking resources eliminated (critical CSS inlined, JS deferred or async)? | ☐ Yes ☐ No |
| 44 | Performance | Does the Lighthouse Performance score ≥ 90 on mobile? | ☐ Yes ☐ No |
| 45 | LLM SEO | Is there an `llms.txt` file at the root with project overview and key links? | ☐ Yes ☐ No |
| 46 | LLM SEO | Does the page contain a definitive answer paragraph (50–150 words) for its primary question? | ☐ Yes ☐ No |
| 47 | LLM SEO | Are entities, terms, and concepts used explicitly (not paraphrased)? | ☐ Yes ☐ No |
| 48 | LLM SEO | Is the content structured with Q&A blocks or FAQ schema where appropriate? | ☐ Yes ☐ No |
| 49 | Analytics + monitoring | Is an analytics tool installed (PostHog, Plausible, Fathom, or GA4)? | ☐ Yes ☐ No |
| 50 | Analytics + monitoring | Is error monitoring installed (Sentry, Rollbar, or equivalent)? | ☐ Yes ☐ No |
| 51 | Analytics + monitoring | Are Core Web Vitals being tracked in production (via `web-vitals` library)? | ☐ Yes ☐ No |
| 52 | Analytics + monitoring | Is uptime monitoring configured (UptimeRobot, Pingdom, or equivalent)? | ☐ Yes ☐ No |

> Note: The table contains 52 rows because analytics naturally splits into 4 distinct concerns (page analytics, error monitoring, vitals tracking, uptime). The intent of "50 points" is preserved — these are the binary gates.

---

## Category Notes

### Design (checks 1–10)

These checks enforce the principles in guides 01–05, 12, 13, 19. A page that fails any of these is visually generic. The most common failures:

- **#2 (palette)**: indigo/violet/pink gradient. The single most common AI tell.
- **#4 (spacing)**: 4pt system (`gap-3`, `gap-5`) instead of 8pt. Visible to designers, invisible to engineers.
- **#8 (motion budget)**: too many animations. AI ships fade-in-up on every section.
- **#10 (imagery)**: emoji icons. The fastest AI tell.

### Code quality (checks 11–18)

These checks enforce engineering discipline. A page that fails any of these is fragile. The most common failures:

- **#11 (bundle size)**: LLMs import `moment` instead of `date-fns`, `lodash` instead of native methods. Bundle balloons.
- **#13 (fonts)**: 6 weights of Inter loaded from Google Fonts without `preconnect`. FOIT for 2 seconds.
- **#18 (design rationale)**: the document doesn't exist. The agent skipped Phase 1–3 of the protocol in guide 01.

### Accessibility (checks 19–30)

These checks enforce WCAG 2.2 AA. A page that fails any of these excludes users — and is a legal liability in many jurisdictions (ADA, EAA, AODA). The most common failures:

- **#19 (focus)**: `outline: none` without replacement. Keyboard users can't navigate.
- **#21 (labels)**: `<input>` without `<label>`. Screen reader users hear "edit text, blank, blank, blank".
- **#29 (screen reader test)**: nobody actually ran VoiceOver. The page looks accessible but isn't.

### SEO (checks 31–38)

These checks enforce classic search engine optimization. See guide 07 for the full treatment. The most common failures:

- **#31 (title)**: "Home" or "Untitled" as the `<title>`. No search engine will rank it.
- **#35 (OG image)**: missing. When users share the URL, the social card is blank.
- **#37 (structured data)**: missing JSON-LD. The page doesn't appear in rich results.

### Performance (checks 39–44)

These checks enforce Core Web Vitals. See guide 15 for the full treatment. The most common failures:

- **#39 (LCP)**: hero image is 4MB JPEG, not preloaded, not lazy-loaded — wait, it should NOT be lazy-loaded if it's the LCP element.
- **#41 (INP)**: heavy JavaScript on interaction. Click handler takes 400ms.
- **#43 (render-blocking)**: 12 stylesheets in `<head>`, all sync. Browser can't paint.

### LLM SEO (checks 45–48)

These checks enforce discoverability by AI systems (ChatGPT, Perplexity, Claude, Google AI Overviews). See guide 08 for the full treatment. The most common failures:

- **#45 (llms.txt)**: missing. AI crawlers have no map of your content.
- **#46 (definitive answer)**: no 50–150 word direct answer to the page's primary question. AI systems can't extract a citation.

### Analytics + monitoring (checks 49–52)

These checks enforce observability. A shipped page without analytics is a page you can't improve. The most common failures:

- **#49 (analytics)**: missing entirely. You don't know how many users visited.
- **#50 (error monitoring)**: missing. Errors happen in production and you don't know.

---

## The Ship Ceremony

1. **Run the checklist.** Open the page in production (not localhost). Click through every check. Mark each one Yes or No.
2. **Count the No's.** Any No blocks the ship.
3. **Fix the No's.** Either fix them or write a deferral in `DESIGN-RATIONALE.md` with a date and owner.
4. **Re-run the checklist.** All Yes's (or written deferrals).
5. **Sign and date.** Add to the bottom of `DESIGN-RATIONALE.md`:

```markdown
## Pre-Launch Sign-Off

- Date: YYYY-MM-DD
- Engineer: [name]
- Designer: [name]
- All 52 checks passed: Yes
- Deferrals: [list, with dates]

This page is ready to ship.
```

6. **Ship.** Merge the PR. Deploy.

## The Post-Launch Smoke Test

After the deploy completes:

1. Visit the production URL on a real phone (not DevTools emulation).
2. Visit on a real laptop, in Safari, Chrome, and Firefox.
3. Visit in dark mode.
4. Visit with the network throttled to "Slow 4G".
5. Visit with JavaScript disabled. Does critical content still appear?
6. Visit with a screen reader (VoiceOver on Mac, NVDA on Windows).
7. Run Lighthouse on the production URL. Compare to the dev Lighthouse score — should be within 5 points.
8. Check Sentry (or equivalent) for new errors in the first 10 minutes.
9. Check analytics for the first 100 visits — are they arriving?

If any of these fail, roll back. Don't "fix it in production".

## Anti-Patterns (Auto-Fail)

1. **"We'll fix it post-launch."** No. Fix it now or defer with a written date.
2. **"It's just a small thing."** Small things are how big outages happen.
3. **"Lighthouse said 90 in dev."** Lighthouse in dev is not Lighthouse in prod. Re-run it.
4. **"We don't need analytics yet."** You do. You can't improve what you don't measure.
5. **"Accessibility can wait."** It can't. It's a legal liability and a user-exclusion bug.
6. **"We'll add structured data later."** Later never comes. Add it now.
7. **"The OG image isn't critical."** It is — every shared link uses it.
8. **"Nobody shares our URLs anyway."** They will, when the OG image is good.
9. **"We tested in Chrome."** Test in Safari and Firefox too. And on a real iPhone.
10. **"The checklist is too long."** It's 52 items. Senior teams run it every ship. So can you.

## Output

When you finish this guide, you should have:
- All 52 checklist items marked Yes (or deferred with a written date and owner)
- A signed and dated pre-launch sign-off in `DESIGN-RATIONALE.md`
- A post-launch smoke test completed (real phone, real laptop, Safari + Chrome + Firefox, dark mode, slow network, no JS, screen reader, Lighthouse, Sentry, analytics)
- The page shipped to production
- No "we'll fix it later" deferrals without a written date

The page is done. Ship it.
