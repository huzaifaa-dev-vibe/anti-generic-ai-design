# 20 — Conversion Principles

> Conversion is not a dark art. It is applied psychology with a feedback loop. AI-coded landing pages ship the same seven sections in the same order with the same CTAs because the LLM has seen Stripe's pricing page 10,000 times. The result is a page that looks like every SaaS page — invisible, unconverting, indistinguishable from the next. This guide is the senior-growth-designer's playbook for designing pages that convert without resorting to dark patterns.

## Why AI fails at conversion

Five defaults ruin AI landing pages:

1. **Same section order every time.** Hero → logos → features → testimonials → pricing → CTA → footer. Every LLM ships this. Every user has seen it 10,000 times. It no longer converts — it scrolls past.
2. **No hierarchy of intent.** Every CTA is identical in weight. "Get Started" appears six times. The user has no signal which one matters.
3. **Fake urgency.** "Limited time offer!" "Only 3 left!" "Sale ends in 02:14:33!" Countdown timers that reset on page reload. Users have learned to ignore these — and to distrust sites that use them.
4. **No proof, just claims.** "Trusted by 10,000+ companies" with a grayscale logo strip that links to nothing. No case studies. No numbers. No named customers.
5. **Pricing designed by engineers.** Three tiers, "Most Popular" badge on the middle one, feature comparison table with 40 rows. The decoy effect absent. The anchor absent. Annual toggle that gives 20% off — same as every competitor.

Conversion design is psychology + clarity. Not pressure.

---

## Rule 1 — Apply Cialdini's seven principles (ethically)

Robert Cialdini's *Influence* (1984) identified seven principles of persuasion. Each maps to a design pattern.

| Principle | Ethical design pattern | Dark pattern (banned) |
|-----------|------------------------|----------------------|
| **Reciprocity** | Free trial, free tool, free guide — give value first | "Free" that requires a credit card to access |
| **Commitment & consistency** | Multi-step form, micro-yes before macro-yes | Forced continuity (can't cancel) |
| **Social proof** | Real customer logos with links, named testimonials, case studies, real usage stats | Fake testimonials, purchased reviews, inflated user counts |
| **Authority** | "As featured in" with real press links, expert endorsements, certifications | Fake awards, invented expert quotes |
| **Liking** | Real team photos, founder's note, authentic voice | Stock photos of "the team", AI-generated personas |
| **Scarcity** | "Beta access for first 100 teams", real limited inventory | Fake countdowns that reset, "only 3 left" that's been 3 for weeks |
| **Unity** | "Join 2,000 builders like you", community-driven marketing | In-group exclusion designed to manipulate |

**The ethical test**: would a user who understood the pattern still feel respected? If yes, ethical. If they'd feel manipulated, dark pattern.

## Rule 2 — Hierarchy of intent: awareness → consideration → decision → retention

Every page serves one primary intent. Design for that intent; don't try to serve all four.

| Stage | User's question | Page type | Primary CTA |
|-------|-----------------|-----------|-------------|
| **Awareness** | "What is this? Why should I care?" | Homepage, blog post, ad landing | "Read more" / "Watch demo" |
| **Consideration** | "Could this work for me? How does it compare?" | Features page, comparison page, docs | "Start free trial" / "Talk to sales" |
| **Decision** | "Should I buy? Which plan?" | Pricing page, signup page | "Start trial" / "Buy now" |
| **Retention** | "How do I get more value? Should I upgrade?" | Dashboard, in-app messages, email | "Upgrade" / "Explore feature" |

**A homepage trying to sell is a homepage that fails.** The user isn't ready. Match the CTA to the stage: awareness pages get "Learn more", decision pages get "Buy".

## Rule 3 — CTA placement: four mandatory locations

A landing page needs CTAs at four points, each tuned to a different reader:

1. **Above the fold.** For the user who already knows they want this. "Start free trial" — high contrast, primary button.
2. **After the value props.** For the user who needed to read the features. "Start free trial" — same button, repeated.
3. **After social proof.** For the user who needed the validation. "Join 2,000+ teams" + CTA. This is the highest-converting placement.
4. **In the footer.** For the user who scrolled all the way down looking for it. "Start free trial" + secondary links.

```tsx
<LandingPage>
  <Hero>
    <h1>...</h1>
    <p>...</p>
    <CTA variant="primary">Start free trial</CTA>     {/* 1. Above fold */}
  </Hero>

  <Features>
    <FeatureCard />
    <FeatureCard />
    <FeatureCard />
  </Features>

  <CTASection>
    <CTA variant="primary">Start free trial</CTA>     {/* 2. After value props */}
  </CTASection>

  <SocialProof>
    <Testimonial />
    <Testimonial />
    <StatBar />
    <CTA variant="primary">Join 2,000+ teams</CTA>    {/* 3. After social proof */}
  </SocialProof>

  <Pricing />

  <FooterCTA>
    <CTA variant="primary">Start free trial</CTA>     {/* 4. In footer */}
  </FooterCTA>
</LandingPage>
```

**Rules**:
- All four CTAs use the same label and same color. Variation confuses.
- The above-the-fold CTA is the largest. The footer CTA can be smaller.
- Never more than one primary CTA per section. Secondary CTAs ("Talk to sales", "Read docs") are visually subordinate.

## Rule 4 — Social proof patterns: pick the right one for the stage

| Pattern | Strength | Use case |
|---------|----------|----------|
| **Logo strip** | Weak | Awareness — establishes "real companies use this" |
| **Stat with provenance** | Medium | Awareness, consideration — "1M+ users" with source |
| **Single testimonial (named, with photo)** | Strong | Consideration, decision — one real story |
| **Testimonial wall (3–6 quotes)** | Strong | Consideration — shows range of customers |
| **Case study (linked)** | Strongest | Decision — full story with metrics |
| **User count ("Join 2,000+ teams")** | Medium | Awareness — only if the number is real |
| **Star rating (G2, Capterra)** | Strong | Decision — third-party verified |
| **Press mentions ("As seen in")** | Medium | Awareness — authority transfer |
| **Live activity ("14 people signed up today")** | Medium | Decision — only if honest, not "anonymized" |

### Logo strip rules

- **Real logos with real links.** Each logo should link to a case study. A grayscale logo strip with no links is decoration.
- **5–7 logos, not 30.** More looks desperate; less looks under-adopted.
- **Equal visual weight.** All logos at the same height (e.g. 28px), same opacity (e.g. 50% default, 100% on hover).
- **Sort by recognizability**, not alphabetically. The most famous logo goes first.

```tsx
<section className="logo-strip">
  <p className="logo-strip-label">Trusted by teams at</p>
  <ul className="logo-grid">
    {customers.map(c => (
      <li key={c.name}>
        <a href={c.caseStudyUrl} aria-label={`${c.name} case study`}>
          <img src={c.logo} alt="" width={120} height={28} />
        </a>
      </li>
    ))}
  </ul>
</section>
```

### Testimonial rules

- Named: real name, real role, real company.
- Photo: a real headshot, not a stock photo, not an AI face.
- Specific: "We cut our deployment time from 40 minutes to 90 seconds" beats "This product is amazing".
- Linked: clicking the testimonial opens the full case study.
- One long, specific quote beats three short generic ones.

```tsx
<figure className="testimonial">
  <blockquote>
    "We cut our deployment time from 40 minutes to 90 seconds. The team
    shipped 3x more features last quarter without adding headcount."
  </blockquote>
  <figcaption>
    <img src="/jane-doe.jpg" alt="" width={48} height={48} />
    <div>
      <p className="name">Jane Doe</p>
      <p className="role">VP Engineering, Acme Corp</p>
    </div>
  </figcaption>
  <a href="/case-studies/acme" className="case-study-link">
    Read the full case study →
  </a>
</figure>
```

## Rule 5 — Pricing page psychology

The pricing page is the highest-leverage page in conversion design. Six principles:

### 1. The three-tier structure (with optional enterprise)

- **Free / Starter** — for solo users, evaluation. Low price or free.
- **Pro / Team** — the target. Most users should land here.
- **Business / Enterprise** — for power users, large teams. Premium price, "Contact sales".

### 2. The anchor

Show the most expensive plan first (left-to-right reading, or visually largest). The middle plan then looks reasonable by comparison. This is the **anchor effect**.

### 3. The decoy

A pricing tier that exists to make the target tier look like a better deal. Classic example: a "Pro" tier at $99 and a "Pro Plus" tier at $149 with marginally more features. Most users pick Pro Plus because the upgrade feels worth it. The decoy is the $99 tier that's just barely worse than $149.

### 4. The "Most Popular" badge

Place it on the target tier (usually the middle one). This combines social proof with the decoy effect.

### 5. Monthly vs annual toggle

Default to annual (with the savings shown), but make monthly easy to find. The "save 20%" anchor works — but only if the monthly price is shown for comparison.

```tsx
<div className="pricing-toggle">
  <button aria-pressed={cycle === 'monthly'} onClick={() => setCycle('monthly')}>
    Monthly
  </button>
  <button aria-pressed={cycle === 'annual'} onClick={() => setCycle('annual')}>
    Annual <span className="savings">Save 20%</span>
  </button>
</div>
```

### 6. Feature comparison table

- Group features by category (Core, Collaboration, Security, Support).
- Use checkmarks for included, dashes for not included, "Add-on" for paid extras.
- Keep it under 20 rows. Anything more, link to a "full comparison" page.
- The target tier's column is visually emphasized (background tint, "Most Popular" badge, slightly larger).

```tsx
<div className="pricing-grid">
  <PricingCard
    name="Starter"
    price={0}
    description="For solo builders"
    cta="Start for free"
  />
  <PricingCard
    name="Pro"
    price={cycle === 'annual' ? 24 : 30}
    description="For growing teams"
    cta="Start 14-day trial"
    popular  // visually emphasized
  />
  <PricingCard
    name="Business"
    price={cycle === 'annual' ? 60 : 75}
    description="For scaling organizations"
    cta="Start 14-day trial"
  />
  <PricingCard
    name="Enterprise"
    price="Custom"
    description="For large teams with custom needs"
    cta="Talk to sales"
  />
</div>
```

### Pricing page anti-patterns

- **Hiding the price** behind a "Contact us" form. Banned for any plan under $1,000/month.
- **Per-seat pricing with no calculator**. Users need to know the total before they buy.
- **No monthly option**. Annual-only signals "we want to lock you in".
- **Feature comparison with 40 rows**. Decision paralysis.
- **No FAQ on the pricing page**. The 5 most common questions belong here.

## Rule 6 — Urgency without dark patterns

Real urgency converts. Fake urgency destroys trust.

### Ethical urgency

- **Real scarcity**: "Beta access for first 100 teams" — and you actually cap it.
- **Time-bound discounts**: "20% off through Friday" — and the price actually goes up Friday.
- **Inventory**: "3 seats left in this cohort" — when there really are 3 seats.
- **Live activity**: "14 people signed up today" — when it's actually today's signups.

### Dark patterns (banned)

- Countdown timers that reset on page reload.
- "Only 3 left in stock!" that's been 3 for weeks.
- "47 other people are viewing this" with no basis in fact.
- Confirmshaming ("No thanks, I don't want to grow my business").
- Forced continuity (free trial that auto-charges with no reminder).
- Roach motel (easy to sign up, hard to cancel).

**The test**: would a journalist writing about your site find the urgency honest? If yes, ship it. If they'd catch you in a lie, kill it.

## Rule 7 — Form optimization: fewer fields, progressive disclosure

Every field in a form reduces conversion by ~10%. Cut fields ruthlessly.

### Field reduction rules

| Field | Required? | Why |
|-------|-----------|-----|
| Email | Yes | The only field you truly need |
| First name | Maybe | Only if you personalize the next step |
| Last name | No | Ask later |
| Company | No | Ask later (or never) |
| Job title | No | Ask later |
| Phone | No | Unless you genuinely need to call |
| Password | Yes (if no magic link) | Or use magic link instead |
| Country | Maybe | Only for tax/shipping |
| How did you hear about us? | No | Marketing curiosity ≠ conversion |

```tsx
// ❌ Bad: 7 fields
<form>
  <input name="firstName" required />
  <input name="lastName" required />
  <input name="email" required />
  <input name="company" required />
  <input name="jobTitle" required />
  <input name="phone" required />
  <input name="country" required />
  <button>Sign up</button>
</form>

// ✅ Good: 1 field
<form>
  <input name="email" type="email" required />
  <button>Send magic link</button>
</form>
```

### Progressive disclosure

Collect additional information across the user's journey, not at signup:

1. **Signup**: email only. Send magic link.
2. **First login**: ask for name + workspace name.
3. **Onboarding step 2**: ask about their use case (informs product).
4. **Onboarding step 3**: invite teammates (optional).
5. **Settings, later**: company name, billing address, team roles.

Each step asks for what's needed to take the next step. Nothing more.

### Multi-step forms

For long forms (checkout, application), break into 3–5 steps with a progress indicator. Each step asks for related info. Conversion improves 15–30% versus one long form.

```tsx
function MultiStepForm() {
  const [step, setStep] = useState(1);
  const total = 4;

  return (
    <form>
      <progress max={total} value={step} aria-label={`Step ${step} of ${total}`} />

      {step === 1 && <AccountStep />}
      {step === 2 && <ProfileStep />}
      {step === 3 && <TeamStep />}
      {step === 4 && <ConfirmStep />}

      <div className="form-nav">
        {step > 1 && <button type="button" onClick={() => setStep(step - 1)}>Back</button>}
        {step < total ? (
          <button type="button" onClick={() => setStep(step + 1)}>Continue</button>
        ) : (
          <button type="submit">Create account</button>
        )}
      </div>
    </form>
  );
}
```

## Rule 8 — The landing page section order decision tree

There is no single right order — but there are wrong orders. Here's the decision tree:

```
1. Hero
   Always first. One focal point, one CTA, proof within the fold.

2. Social proof (logo strip)
   Immediately after hero. Establishes "real companies use this".

3. Problem / context
   For awareness-stage audiences: "Here's the problem we solve".
   For consideration-stage audiences: SKIP — they know the problem.

4. Solution / value props
   3–6 features, each with a specific benefit (not a feature list).

5. How it works
   3-step visual: connect → configure → ship. Reduces perceived complexity.

7. Social proof (testimonials / case studies)
   Strongest proof placement. Deeper than the logo strip.

8. Comparison / "vs alternative"
   Only for crowded markets. Honest comparison beats pretending competitors don't exist.

9. Pricing
   Decision-stage content. Place after the user understands the value.

10. FAQ
   Handles objections. Place near the pricing or at the bottom.

11. Final CTA section
   One last ask, before the footer. Big, simple, one button.

12. Footer
   Links to everything else.
```

### When to deviate

- **Dev tools**: skip the "problem" section. Developers know the problem. Lead with the product.
- **Consumer products**: lead with the product (photo/video) before the problem. Show, don't tell.
- **Premium / luxury**: lead with the brand story. Pricing is hidden or "Contact us".
- **Commodity**: lead with price. The decision is mostly price.

## Rule 9 — A/B test what matters, not what's easy

Don't A/B test button colors. Test:

| Test | Impact | How |
|------|--------|-----|
| Headline angle (benefit vs identity vs fear) | High | 3 variants, 1,000 visits each |
| CTA placement (above fold only vs repeated) | High | 2 variants |
| CTA copy ("Start trial" vs "See plans" vs "Get demo") | High | 3 variants |
| Pricing display (monthly vs annual default) | Medium | 2 variants |
| Social proof (logos vs testimonials vs stats) | High | 3 variants |
| Hero visual (product screenshot vs illustration vs none) | High | 3 variants |
| Form length (1 field vs 3 vs 5) | High | 3 variants |

Don't test:
- Button color (unless you're at >10,000 conversions/month, the effect is noise).
- Minor copy tweaks.
- Anything where you can't reach statistical significance in 30 days.

## Rule 10 — Measure conversion properly

Conversion rate is the percentage of visitors who complete the goal. But "the goal" is rarely one thing. Track:

| Metric | Definition |
|--------|------------|
| **Primary conversion rate** | Visitors → primary action (signup, purchase) |
| **Micro-conversion rate** | Visitors → intermediate action (clicked CTA, started trial) |
| **Funnel drop-off** | Step N → Step N+1 (where do users leave?) |
| **Visitor → SQL** | Marketing qualified lead → sales qualified lead |
| **CAC** | Customer acquisition cost (spend / new customers) |
| **LTV** | Lifetime value (revenue per customer × retention) |
| **LTV:CAC ratio** | Should be ≥ 3:1 for sustainable growth |

Tools: PostHog, Plausible, Fathom, Google Analytics 4, Mixpanel. Pick one. Don't run three.

## Anti-Patterns (Auto-Fail)

1. **Same section order as every other SaaS site.** Banned.
2. **Countdown timers that reset on reload.** Banned.
3. **"Only X left!" that doesn't decrement.** Banned.
4. **Grayscale logo strip with no links.** Banned.
5. **Fake testimonials** (stock photos, made-up quotes). Banned.
6. **Confirmshaming** ("No thanks, I hate saving time"). Banned.
7. **Forced continuity** (free trial auto-charges with no reminder). Banned.
8. **Roach motel** (easy signup, hard cancel). Banned.
9. **"Most Popular" badge on the cheapest tier** (signals misunderstanding of the decoy effect).
10. **7-field signup form.** Cut to 1.
11. **No FAQ on pricing page.** Add the 5 most common questions.
12. **Pricing hidden behind "Contact us"** for plans under $1,000/month.
13. **Same CTA repeated 6 times with no hierarchy.** Vary by stage.
14. **No case studies.** At least one named, specific, metric-backed case study.

## Code Example — The High-Conversion CTA Section

```tsx
function FinalCTA() {
  return (
    <section className="final-cta">
      <div className="container">
        <h2>Start shipping today</h2>
        <p>
          Free 14-day trial. No credit card required. Cancel anytime.
        </p>

        <div className="cta-row">
          <a href="/signup" className="btn btn-primary btn-lg">
            Start free trial
          </a>
          <a href="/demo" className="btn btn-secondary btn-lg">
            Book a demo
          </a>
        </div>

        <ul className="trust-signals">
          <li>
            <CheckIcon aria-hidden /> 14-day free trial
          </li>
          <li>
            <CheckIcon aria-hidden /> No credit card required
          </li>
          <li>
            <CheckIcon aria-hidden /> Cancel anytime
          </li>
          <li>
            <CheckIcon aria-hidden /> SOC 2 Type II certified
          </li>
        </ul>
      </div>
    </section>
  );
}
```

## Output

When you finish this guide, you should have:
- A landing page section order chosen via the decision tree, justified in `DESIGN-RATIONALE.md`
- CTAs at four mandatory locations (above fold, after value props, after social proof, footer)
- A primary CTA label that is verb + object, not "Get Started"
- Social proof at two levels: logo strip (weak) and testimonials/case studies (strong)
- A pricing page with anchor, decoy, "Most Popular" badge on the target tier, and monthly/annual toggle
- No dark patterns (no fake countdowns, no confirmshaming, no forced continuity)
- A signup form with the minimum possible fields (ideally just email)
- A multi-step form (if needed) with progress indicator
- A documented A/B test plan (headlines, CTA copy, social proof format — not button colors)
- An analytics tool installed with primary + micro-conversion tracking
