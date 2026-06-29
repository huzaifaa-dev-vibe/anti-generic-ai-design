# 05 — Hero Section Guide (Top-Class Required)

> The hero is 80% of the first impression. If it's generic, the entire site feels generic — no matter how good the rest is. This guide is the longest in the skill because the hero deserves it.

## Why AI heroes fail

The default AI hero:

```tsx
<section className="py-24 text-center">
  <h1 className="text-6xl font-bold">The Modern Way to [Verb] [Noun]</h1>
  <p className="mt-6 text-xl text-gray-600 max-w-2xl mx-auto">
    [Generic subhead about productivity, collaboration, or scaling]
  </p>
  <div className="mt-8 flex gap-4 justify-center">
    <Button>Get Started</Button>
    <Button variant="outline">Learn More</Button>
  </div>
  <div className="mt-16">
    <ProductScreenshot className="rounded-2xl shadow-2xl" />
  </div>
</section>
```

This is the most-shipped layout in the history of the web. Every AI builds it. Every user has seen it 10,000 times. **It is invisible.**

This guide exists to make sure your hero is not invisible.

---

## The 7 Rules of a Top-Class Hero

### Rule 1 — One Focal Point

A hero has exactly one thing the eye lands on first. Pick one:
- The headline (editorial / publication)
- The product UI (SaaS / dev tools)
- A single hero image (e-commerce / fashion)
- A video (cinematic brands)
- A 3D element (cutting-edge tech brands)

**Never two.** A headline AND a product screenshot AND a video competing for attention = visual chaos. Pick one, support it with the others.

**Test**: Show the hero to someone for 2 seconds. Ask "what did you look at first?" If they say "I don't know", you have two focal points. Fix it.

### Rule 2 — Show the Real Product

The fastest way to look generic is to ship a hero with a stock illustration or an unDraw vector. **Show the actual product.**

- SaaS? Show the dashboard, with real data, even if mocked.
- Dev tool? Show the terminal / IDE view.
- E-commerce? Show the hero product in a real setting.
- Service? Show the work (case study preview, before/after, real photo).
- Mobile app? Show the app on a real device, not a stock phone mockup.

If you can't show the real product, show a **real moment**: the team, the workshop, the work in progress. Never a stock illustration.

### Rule 3 — Motion Reveals Information

Every animation in the hero must reveal information, not decorate.

| Animation | Information revealed | Verdict |
|-----------|----------------------|---------|
| Counter animates 0 → 1,247,893 | Scale of customer base | ✅ |
| Product UI unrolls a real flow | How the product works | ✅ |
| Chart line draws across the screen | Trend / growth | ✅ |
| Headline fades in word-by-word | Nothing | ❌ Decoration |
| Background gradient slowly shifts | Nothing | ❌ Decoration |
| Cards stagger-fade-in on scroll | Nothing | ❌ Decoration |

If an animation doesn't reveal information, remove it.

### Rule 4 — Proof Within the Fold

The hero must contain proof. Not below the fold. **In it.**

Pick one:
- **One stat with provenance**: "1,247,893 reviews shipped · Source: Stripe data, Q3 2025"
- **Three logos with case-study links**: clickable logos, not a grayscale strip
- **One testimonial**: a real quote, named, with photo and role
- **One award / press mention**: "Featured in The Verge" with a link to the article

A hero without proof reads as marketing copy. A hero with proof reads as truth.

### Rule 5 — Maximum 7 Elements Above the Fold

Count them:
1. Nav (logo, links, CTA) — counts as 1 even if it has 8 links
2. Eyebrow / overline (optional)
3. H1
4. Subhead
5. Primary CTA
6. Secondary CTA (or proof element)
7. Visual (product / image / video)

**Seven.** If you have 8+, the hero is cluttered. Cut.

(Backgrounds, gradients, and decorative elements don't count if they're truly background. If they fight for attention, they count.)

### Rule 6 — Headline is Specific

Generic headlines:
- ❌ "The Modern Way to Build Software"
- ❌ "Design Without Limits"
- ❌ "Scale Your Business with AI"
- ❌ "The All-in-One Platform"

Specific headlines:
- ✅ "Ship design reviews 4× faster"
- ✅ "The Stripe for India's UPI rails"
- ✅ "Stop losing 30% of your tickets to spam"
- ✅ "Vercel for databases"

The formula: **[Outcome] + [Specificity]**. Outcome = what the user gets. Specificity = a number, a comparison, or a constraint that makes it real.

If your headline could appear on 100 different SaaS sites unchanged, it's generic. Rewrite.

### Rule 7 — CTA Copy is Action + Outcome

- ❌ "Get Started"
- ❌ "Learn More"
- ❌ "Sign Up Free"

- ✅ "Start free trial → build your first review in 2 min"
- ✅ "Book a 20-min demo · See the dashboard live"
- ✅ "Read the docs · 5-min quickstart"
- ✅ "Install with `npm i @scope/pkg`"

CTA copy should tell the user **what happens next** and **how long it takes**. Vague CTAs get vague clicks.

---

## Hero Layout Patterns

### Pattern A — Split Hero (SaaS default, but make it yours)

```
┌─────────────────────────────────────────┐
│  ┌──────────────┐  ┌──────────────────┐ │
│  │  EYEBROW     │  │                  │ │
│  │              │  │   PRODUCT UI     │ │
│  │  Headline    │  │   (real data)    │ │
│  │  that wraps  │  │                  │ │
│  │  to 3 lines  │  │                  │ │
│  │              │  │                  │ │
│  │  Subhead     │  │                  │ │
│  │              │  │                  │ │
│  │  [CTA] [2nd] │  │                  │ │
│  │              │  │                  │ │
│  │  ★ proof     │  │                  │ │
│  └──────────────┘  └──────────────────┘ │
└─────────────────────────────────────────┘
```

When done right: Linear, Vercel, Resend, Cal.com.
When done wrong: every generic AI SaaS.

**Make it yours by**:
- Asymmetric split (55/45 instead of 50/50)
- Product UI has a real cursor that moves, real data that updates
- Tilted product UI with a soft drop shadow
- Eyebrow with a status dot ("● Now in beta" / "● v2.0 shipped")

### Pattern B — Asymmetric Editorial (portfolio / agency)

```
┌─────────────────────────────────────────┐
│ ┌─────────────────────────────────────┐ │
│ │                                     │ │
│ │  MASSIVE HEADLINE                   │ │
│ │  that breaks the grid               │ │
│ │  on purpose                         │ │
│ │                                     │ │
│ │       ┌──────────────┐              │ │
│ │       │  hero image  │              │ │
│ │       │              │              │ │
│ │       └──────────────┘              │ │
│ │                                     │ │
│ │  Subhead              [CTA →]       │ │
│ └─────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

When done right: Pentagram, Mucho, studio sites.
When done wrong: looks broken.

**Make it yours by**:
- Headline at 8–12rem (128–192px) — true editorial scale
- Break the grid intentionally (image extends past the column)
- Mix weights within the headline (regular + italic + bold)
- Use a real display face (Fraunces, Bricolage, Tiempos)

### Pattern C — Product-First (dev tools)

```
┌─────────────────────────────────────────┐
│  ┌─────────────────────────────────────┐ │
│  │  $ npm install @scope/pkg           │ │
│  │  $ scope init                       │ │
│  │  ✓ Project created                  │ │
│  │  $ scope deploy                     │ │
│  │  → https://my-app.scope.sh          │ │
│  └─────────────────────────────────────┘ │
│                                         │
│         Ship in 60 seconds.             │
│  The database that scales with you.     │
│                                         │
│         [Get Started] [Docs →]          │
└─────────────────────────────────────────┘
```

When done right: Vercel, Supabase, Railway, Bun.
When done wrong: looks like a code block.

**Make it yours by**:
- The terminal actually types itself out (real characters, real timing)
- Use the project's actual CLI syntax (not made-up commands)
- The headline BELOW the terminal — uncommon, gets attention
- Mono font throughout the hero

### Pattern D — Video Background (cinematic brands)

```
┌─────────────────────────────────────────┐
│  [background video plays, muted]        │
│                                         │
│                                         │
│         HEADLINE OVERLAY                │
│         Subhead                         │
│         [CTA]                           │
│                                         │
│                                         │
│  [scroll indicator ↓]                   │
└─────────────────────────────────────────┘
```

When done right: Apple, Tesla, Nike.
When done wrong: looks like a stock video site.

**Make it yours by**:
- Video is original, not stock
- Dark overlay (rgba(0,0,0,0.4)) for text legibility
- Muted, autoplay, loop, playsinline (mobile-friendly)
- Subtitles / captions burned in or via WebVTT
- Poster image for the 200ms before video loads

### Pattern E — 3D / Interactive (cutting-edge)

```
┌─────────────────────────────────────────┐
│  ┌──────────────┐  ┌──────────────────┐ │
│  │              │  │                  │ │
│  │  Headline    │  │   [3D object     │ │
│  │  Subhead     │  │    that rotates  │ │
│  │  [CTA]       │  │    with mouse]   │ │
│  │              │  │                  │ │
│  └──────────────┘  └──────────────────┘ │
└─────────────────────────────────────────┘
```

When done right: Apple Vision Pro, Spline, Lusion.
When done wrong: gimmicky, slow, distracting.

**Use only if**:
- The product is genuinely 3D / spatial / interactive
- You can hit 60fps on mid-range hardware
- You have a fallback static image for low-power devices
- The 3D supports the message (doesn't just spin for fun)

### Pattern F — Centered Editorial (use sparingly)

```
┌─────────────────────────────────────────┐
│                                         │
│            EYEBROW                      │
│                                         │
│         Massive Headline                │
│         that earns the center           │
│                                         │
│            Subhead                      │
│                                         │
│         [CTA]  [2nd CTA]                │
│                                         │
│  ────────────────────────────────────   │
│         proof / logos                   │
└─────────────────────────────────────────┘
```

**Banned by default.** Only allowed if:
- The brand is editorial (publication, magazine)
- The headline is genuinely striking (not "The Modern Way to...")
- The visual rhythm of the rest of the page is asymmetric (so this centered hero is a deliberate beat)
- You can defend it in the debate phase

---

## Hero Motion Patterns

### Pattern 1 — Choreographed Reveal (3 seconds max)

```
0.0s: Background appears
0.2s: Eyebrow fades in
0.4s: Headline first line draws in
0.7s: Headline second line draws in
1.0s: Subhead fades in
1.3s: CTAs slide up
1.6s: Product UI fades in
2.0s: Proof element appears
2.5s: Hero is fully settled, ready for interaction
```

Total: under 3 seconds. Anything longer is making the user wait.

### Pattern 2 — Live Product Demo

The product UI in the hero is alive. A cursor moves and clicks. Real data updates. A chart line draws.

**Make sure**:
- The demo loops every 8–15 seconds (not too fast, not too slow)
- It pauses on hover so users can read
- It respects `prefers-reduced-motion` (static state instead of animation)

### Pattern 3 — Counter Reveal

A single big number animates from 0 to its final value.

```tsx
<Counter from={0} to={1_247_893} duration={2_000} format={n => n.toLocaleString()} />
```

**Use when**: you have one killer stat. Not when you have 4 mediocre stats.

### Pattern 4 — Typewriter (use sparingly)

The headline types itself out character by character.

**Use only when**:
- The brand voice is technical / dev-focused
- The headline is short (≤ 40 chars)
- You have a real reason (e.g. showcasing a CLI tool)

**Avoid when**: it's just decoration. Typewriter headlines get old fast.

---

## Hero Anti-Patterns (Auto-Fail)

1. **Centered hero with stacked H1 + subhead + 2 buttons + product screenshot below.** The default AI hero. Banned.
2. **"Trusted by" grayscale logo strip below the hero.** Replace with 3 case-study cards.
3. **Indigo→violet→pink gradient background.** Banned.
4. **Stock illustration / unDraw vector as the hero visual.** Show real product instead.
5. **Headline that says "The [Adjective] [Noun] for [Audience]"** — formulaic.
6. **Two CTAs that say "Get Started" and "Learn More".** Be specific.
7. **Animated gradient text on the headline.** Overused AI tell.
8. **Floating 3D shapes / abstract blobs in the background.** Visual noise.
9. **Hero is 100vh+ tall with barely any content.** Wasted space.
10. **Hero is 50vh tall with cramped content.** Worse.
11. **Headline above 80px without an editorial reason.** Big type for the sake of big type.
12. **Headline below 36px on desktop.** Too small to lead.
13. **No proof element in the hero.** Reads as unverified marketing.
14. **Hero with 8+ elements.** Cluttered.
15. **Background image with no overlay, text on top unreadable.** Accessibility failure.

---

## Hero Copywriting

### Eyebrow / Overline (optional but powerful)

A small line above the H1, usually uppercase, with a status dot or category label:
- `● v2.0 just shipped`
- `● Now in public beta`
- `FOR TEAMS · NOT FOR SOLOS`
- `CASE STUDY · STRIPE`

The eyebrow sets context before the headline lands. Use it.

### Headline formulas that work

| Formula | Example |
|---------|---------|
| Outcome + specificity | "Ship design reviews 4× faster" |
| Comparison (the X for Y) | "The Stripe for India's UPI rails" |
| Negative outcome + negation | "Stop losing 30% of tickets to spam" |
| Direct category claim | "The fastest database for serverless apps" |
| Question | "What if your database had sub-ms latency?" |
| Statement of fact | "1 in 3 startups use us by Series A" |

### Subhead formulas

| Formula | Example |
|---------|---------|
| Expand the headline | "Frameable cuts design review cycles from 5 days to 4 hours with async video annotations." |
| Who it's for | "Built for product teams of 5–50 who ship daily." |
| Mechanism + outcome | "AI-powered annotations + Slack integration = reviews that don't block shipping." |

### CTA copy

| Bad | Good |
|-----|------|
| Get Started | Start free trial → ship your first review today |
| Learn More | See how it works (2-min video) |
| Sign Up Free | Create account · No credit card |
| Contact Us | Book a 20-min call · Get a custom demo |
| Try It Now | Open the live demo · No signup needed |

---

## Hero Responsive Behavior

| Breakpoint | Hero treatment |
|------------|----------------|
| ≥1280px (xl) | Full split or asymmetric layout, side-by-side elements |
| 1024–1279px (lg) | Split layout may narrow, but stays side-by-side |
| 768–1023px (md) | Stack vertically: text first, visual below. Reduce headline size. |
| 640–767px (sm) | Single column. Headline 36–44px. One CTA (move secondary to text link). |
| <640px (xs) | Single column. Headline 32–40px. Remove eyebrow if it crowds. |

**Critical**: the mobile hero is NOT the desktop hero with smaller text. It's a different composition. Plan it deliberately.

## Hero Performance Budget

- LCP element (usually the headline or product image) must load in < 2.5s on 4G
- Hero image: WebP or AVIF, ≤ 200KB
- Hero video: ≤ 2MB total, mp4 with h264 + AAC, poster image required
- Fonts: preload body weight, swap display weight
- JS for hero animation: ≤ 30KB gzipped

If your hero violates these, simplify. A fast generic hero beats a slow beautiful one.

## Accessibility Checklist for the Hero

- [ ] H1 is the first heading on the page (no H1 in the nav or above)
- [ ] H1 is exactly one (not zero, not multiple)
- [ ] All CTAs are real buttons or links with accessible names
- [ ] Background video has a pause control (or respects prefers-reduced-motion)
- [ ] Background images have sufficient contrast with text (4.5:1 minimum)
- [ ] All animations respect `prefers-reduced-motion`
- [ ] Focus order through the hero is logical (nav → H1 → subhead → CTAs)
- [ ] Hero is keyboard-navigable (no mouse-only interactions)

## Output

When you finish this guide, you should have:
- A hero with exactly one focal point
- A real product moment (not a stock illustration)
- Motion that reveals information
- Proof within the fold
- Maximum 7 elements
- A specific, non-generic headline
- CTAs with action + outcome copy
- A responsive plan for mobile
- A performance budget met
- An accessibility checklist signed off

The hero is the first thing the user sees. Make it the best thing on the page.
