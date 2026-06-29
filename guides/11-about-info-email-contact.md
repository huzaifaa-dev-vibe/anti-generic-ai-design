# 11 — About, Info Architecture, Email, Contact (The Pages AI Forgets)

> The AI agent ships a hero, three feature cards, a pricing page, and a footer. That's 4 pages. A real website has 15–20. The missing 12 are the "info architecture" — About, Contact, Press, Privacy, Terms, Status, Changelog, Help, Brand Assets, Email templates, the footer itself. AI agents forget these exist because they're not in the "make it pretty" prompt. They're the difference between a demo and a real product.

## Why AI agents skip info architecture

Four reasons:

1. **The user didn't ask for it.** "Build me a landing page" doesn't include "and a Privacy Policy and a Changelog and an abandoned-cart email." So the agent doesn't build them.
2. **The agent doesn't know they exist.** AI training data skews toward marketing-page templates, not the full sitemap of a real product.
3. **They're "boring."** Privacy policies and Terms of Service aren't visually exciting. But shipping without them is a legal liability.
4. **Email architecture is invisible to the user until it's broken.** The welcome email is the first impression after signup. AI agents ship a hero and forget the email.

This guide is the fix: every page a complete website needs, the structure of each, and a sitemap template so you stop shipping 4-page demos.

---

## The Complete Sitemap (15–20 pages minimum)

A real SaaS / product website ships this:

```text
/                          Home
/about                     About page (story, team, values, timeline, press)
/contact                   Contact page (form, email, phone, address, hours)
/pricing                   Pricing
/features                  Features overview
/features/{feature}        One page per major feature (3–8 pages)
/case-studies              Customer stories index
/case-studies/{slug}       Individual case study (5–10 pages)
/blog                      Blog index
/blog/{slug}               Individual posts
/docs                      Documentation home (often a subdomain)
/help                      Help center / FAQ
/changelog                 Versioned release notes
/status                    Uptime / incident report (often status.example.com)
/press                     Press kit / media assets
/brand                     Brand assets download (logos, colors, fonts)
/privacy                   Privacy policy
/terms                     Terms of service
/cookies                   Cookie policy (or section in Privacy)
/security                  Security overview (for B2B / SaaS)
/careers                   Open roles (if hiring)
/login                     Login
/signup                    Signup

Email (transactional):
- Welcome email
- Onboarding sequence (3–5 emails)
- Receipt / invoice
- Password reset
- Email verification
- Abandoned cart (e-commerce)
- Abandoned signup (SaaS)
- Re-engagement (dormant users)
- Trial expiring / expired
- Subscription canceled
- Team member invite
- Notification digests
```

Most AI sites ship 4 pages (home, features, pricing, contact) and miss 12+. The user notices the gaps when they look for "Privacy Policy" in the footer and it doesn't exist.

---

## Page-by-Page Templates

### About page (`/about`)

The About page is the second-most-visited page on most sites (after home). It's where users go to decide if they trust you. Ship a generic one and you lose them.

**Structure:**

```text
1. Hero
   - One-sentence company description (not the marketing tagline)
   - Photo of the team or the product in use
   - Optional: founded date, location

2. Story (the founding narrative)
   - Why does this company exist?
   - What problem did the founders hit?
   - What's the origin story?
   - 3–5 paragraphs, narrative voice

3. Values (3–5 principles)
   - Each value: a short title + 2-sentence explanation
   - Real values, not "we are customer-obsessed" platitudes

4. Team
   - Photos (real, not stock)
   - Names, roles
   - One-line bio each
   - Link to LinkedIn / Twitter
   - Optional: a "we're hiring" CTA

5. Timeline / milestones
   - Founded, first product, funding rounds, key hires, major releases
   - Visual: vertical timeline or year-by-year cards

6. Press / mentions
   - Logos of publications that covered you
   - Links to the actual articles
   - Link to /press for full press kit

7. CTA
   - "Join us" (careers), "Get started" (signup), or "Read the docs"
```

**Example structure (TSX):**

```tsx
export default function AboutPage() {
  return (
    <>
      <AboutHero
        tagline="We help product teams ship design reviews faster."
        image="/team/2025-offsite.jpg"
        founded="2023"
        location="San Francisco, CA"
      />

      <Story
        title="Why we started Frameable"
        paragraphs={[
          "In 2022, our founder Maya was leading design at a Series B startup...",
          "Design reviews took 5 days. Reviewers were scattered across time zones...",
          "She built the first prototype in a weekend. The team's cycle time dropped to 4 hours...",
        ]}
      />

      <Values values={[
        { title: 'Async by default', body: 'Synchronous should be the exception, not the rule.' },
        { title: 'Respect the reviewer', body: 'Reviewers donate their time. Make it frictionless.' },
        { title: 'Evidence over opinion', body: 'Every claim ships with a source.' },
      ]} />

      <Team members={[...]} />

      <Timeline milestones={[
        { date: '2023-03', event: 'Founded in San Francisco' },
        { date: '2023-08', event: 'Y Combinator W24 batch' },
        { date: '2024-01', event: 'Public beta launch' },
        { date: '2024-06', event: 'Series A — $8M led by Accel' },
        { date: '2025-02', event: '10,000 paying teams' },
      ]} />

      <PressMentions mentions={[
        { outlet: 'TechCrunch', headline: 'Frameable raises $8M to kill sync design reviews', url: '...' },
        { outlet: 'The Verge', headline: 'The async design revolution', url: '...' },
      ]} />

      <CTASection
        heading="Want to work with us?"
        primaryCta={{ label: 'See open roles', href: '/careers' }}
        secondaryCta={{ label: 'Try Frameable free', href: '/signup' }}
      />
    </>
  );
}
```

**About anti-patterns:**
- "We are a team of passionate designers and engineers" — generic
- No team photos — users don't trust a faceless company
- No founding date or location — feels evasive
- Marketing-speak instead of story

### Contact page (`/contact`)

The Contact page is where users go when something is wrong, when they want to buy, or when they want to talk to a human. Make it useful.

**Structure:**

```text
1. Form (with clear fields)
   - Name, email, message minimum
   - Optional: company, role, topic (sales / support / press / other)
   - Honeypot field for spam (not CAPTCHA — degrades UX)

2. Direct email addresses (don't make people use the form)
   - sales@ — for prospects
   - support@ — for customers
   - press@ — for media
   - security@ — for vulnerability reports
   - legal@ — for legal inquiries
   - hello@ — catch-all

3. Phone number (if you have one)
   - With country code
   - Hours of availability

4. Mailing address (real, not a PO box if possible)
   - For legal / contracts

5. Office hours
   - When do humans read the form?
   - When can people expect a response?

6. Response time SLA
   - "We respond to sales inquiries within 1 business day."
   - "We respond to support tickets within 4 business hours."

7. Map (if physical location matters)
   - Embedded Google Maps or static map image
   - Don't make it interactive if it's not needed

8. Social links
   - Twitter, LinkedIn, GitHub, etc.
```

**Form code:**

```tsx
function ContactForm() {
  return (
    <form action="/api/contact" method="POST" className="contact-form">
      {/* Honeypot — hidden from users, bots fill it */}
      <input type="text" name="website" tabIndex={-1} autoComplete="off"
             style={{ position: 'absolute', left: '-9999px' }} aria-hidden="true" />

      <label htmlFor="name">Name <span aria-hidden="true">*</span></label>
      <input id="name" name="name" type="text" required autoComplete="name" />

      <label htmlFor="email">Email <span aria-hidden="true">*</span></label>
      <input id="email" name="email" type="email" required autoComplete="email" />

      <label htmlFor="company">Company (optional)</label>
      <input id="company" name="company" type="text" autoComplete="organization" />

      <label htmlFor="topic">What's this about?</label>
      <select id="topic" name="topic">
        <option value="sales">I'm evaluating Frameable for my team</option>
        <option value="support">I need help with my account</option>
        <option value="press">Press / media inquiry</option>
        <option value="security">Security vulnerability report</option>
        <option value="other">Something else</option>
      </select>

      <label htmlFor="message">Message <span aria-hidden="true">*</span></label>
      <textarea id="message" name="message" rows={6} required />

      <button type="submit" className="btn-primary">Send message</button>

      <p className="form-sla">We respond within 1 business day. For urgent issues, email <a href="mailto:support@frameable.app">support@frameable.app</a>.</p>
    </form>
  );
}
```

**Contact anti-patterns:**
- Only a form, no email addresses — users can't escalate
- CAPTCHA — degrades UX, blocks some real users
- No response-time SLA — users don't know what to expect
- "We'll get back to you soon" — vague, useless
- No topic selector — every email goes to one inbox and gets misrouted

### Email Architecture (transactional emails)

Email is part of the product. AI agents ship the website and forget the emails. Each transactional email needs design, copy, and code as deliberate as any page on the site.

**The 12 transactional emails every SaaS needs:**

#### 1. Welcome email

Sent immediately after signup. The user's inbox is the second screen they see after your hero.

```text
Subject: Welcome to Frameable, {{first_name}} 👋
Preheader: Here's how to ship your first review in 5 minutes.

Hi {{first_name}},

You're in. Here's how to ship your first design review in 5 minutes:

1. Connect your Figma account → /onboarding/connect-figma
2. Upload a design → /onboarding/upload
3. Invite 3 reviewers → /onboarding/invite
4. Get your first video annotation back

Most teams ship their first review in 4 hours. Get started:
[ → Open Frameable ]

If you get stuck, hit reply. A human reads every email.

— Maya Patel, Founder

P.S. Reply with "feedback" and tell us what brought you here. We read every response.
```

**Welcome email rules:**
- Send within 30 seconds of signup
- One CTA — get them back into the product
- Personal signature (not "The Frameable Team")
- Reply-able — a human reads replies
- No images that block text — many email clients block images by default
- Plain text often outperforms HTML for welcome emails

#### 2. Onboarding sequence (3–5 emails)

Day 0 (welcome, above), Day 1, Day 3, Day 7, Day 14.

```text
Day 1 subject: "Did you connect Figma yet?"
Day 3 subject: "Here's how Stripe uses Frameable"
Day 7 subject: "You haven't shipped a review yet — here's why that's fine"
Day 14 subject: "Your trial ends in 3 days. Here's what to check."
```

Each email: one CTA, one piece of value, one piece of social proof. Don't sell — help.

#### 3. Receipt / invoice

```text
Subject: Your Frameable receipt — {{date}}

Thanks for your payment. Here's your receipt:

Plan: Frameable Team
Billing period: {{start_date}} – {{end_date}}
Amount: ${{amount}}
Payment method: •••• {{last4}}

[ Download invoice (PDF) ]

This charge will appear on your statement as "FRAMEABLE".

Need a different format for your accounting team? Reply to this email.

— Frameable Billing
```

**Receipt rules:**
- Send immediately after charge
- PDF invoice attached or linked
- Clear statement descriptor (what shows on the credit card statement)
- Tax breakdown if applicable
- Reply-able for billing questions

#### 4. Password reset

```text
Subject: Reset your Frameable password

Hi {{first_name}},

We received a request to reset your Frameable password. Click below to choose a new one:

[ Reset password → ]

This link expires in 30 minutes.

If you didn't request this, you can safely ignore this email — your password hasn't been changed.

— Frameable
```

**Rules:**
- Link expires in 30 min (not 24 hours — too long, security risk)
- Tell the user what to do if they didn't request it
- Don't reveal whether the email exists in the system (security)
- Send from a recognizable domain (not no-reply@)

#### 5. Email verification

```text
Subject: Verify your email

Tap below to verify {{email}}:

[ Verify email → ]

This link expires in 24 hours.
```

#### 6. Abandoned signup (SaaS)

User started signup, didn't finish. Send 24 hours later.

```text
Subject: You're 2 minutes from your first design review

Hey — you started setting up Frameable yesterday but didn't finish.

Usually that means you got pulled into a meeting. Here's a 60-second path to done:

1. Pick a plan → /signup/continue
2. Add your team (you can skip and add later)
3. Connect Figma → you're ready

[ Continue signup → ]

Reply if you got stuck on something specific.

— Maya
```

#### 7. Abandoned cart (e-commerce)

User added to cart, didn't check out. Send 1 hour, 24 hours, and 72 hours later.

```text
Subject: You left {{product_name}} in your cart

Your cart is waiting. {{product_name}} is still in stock.

[ Complete checkout → ]

Use code COMEBACK10 for 10% off — valid for 48 hours.
```

#### 8. Re-engagement (dormant users)

User hasn't logged in for 30 days.

```text
Subject: We miss you (and we have data to prove it)

Hi {{first_name}},

You haven't logged into Frameable in 30 days. That's fine — async means you use it when you need it.

But we noticed something: when you were active, your team shipped reviews 4× faster than the industry average. We'd love to know what changed.

[ Reply with what's up ]

Or jump back in: [ Open Frameable → ]

— Maya
```

#### 9. Trial expiring / expired

Day 11 of a 14-day trial:

```text
Subject: 3 days left in your Frameable trial

You've shipped {{review_count}} reviews. Your team has saved an estimated {{hours_saved}} hours.

Don't lose momentum — add a payment method before your trial ends Friday:

[ Add payment method → ]

— Frameable
```

Day 14 (trial ended):

```text
Subject: Your trial ended. Here's what you lose.

Your team can no longer:
- Receive new video annotations
- Access reviews from the last 14 days

Your data is preserved for 30 days. Pick a plan to keep things running:

[ Choose a plan → ]
```

#### 10. Subscription canceled

```text
Subject: Your Frameable subscription is canceled

We're sorry to see you go. Your subscription is canceled effective {{date}}.

Your data will be preserved for 30 days. After that, it's permanently deleted.

[ Reactivate subscription → ]

Mind replying with what didn't work? We read every response.

— Maya
```

#### 11. Team member invite

```text
Subject: {{inviter_name}} invited you to {{team_name}} on Frameable

{{inviter_name}} invited you to join {{team_name}} on Frameable.

[ Accept invite → ]

This invitation expires in 7 days.
```

#### 12. Notification digests (daily / weekly)

```text
Subject: Your Frameable digest — {{date}}

3 new reviews · 12 annotations · 2 reviewers haven't responded

- {{review_title}} — {{status}}
- {{review_title}} — {{status}}
- {{review_title}} — {{status}}

[ Open Frameable → ]

Settings: daily | weekly | off → /settings/notifications
```

**Email design rules:**
- All emails must work in plain text (many clients block HTML)
- Max width 600px for HTML emails
- Use a system font stack — custom fonts don't load in most email clients
- Test in Gmail, Outlook, Apple Mail — they render differently
- Always include an unsubscribe link (CAN-SPAM, GDPR)
- Send from a real domain (not gmail.com), with SPF/DKIM/DMARC configured
- Don't send from `no-reply@` — replies are gold

### Footer

The footer is the most-overlooked UI on AI sites. It's where users look for: legal pages, social links, status, sitemap, careers. Ship a thin footer with just copyright and you fail.

**Footer structure:**

```text
┌─────────────────────────────────────────────────────────────┐
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│  │ Product  │  │ Company  │  │ Resources│  │ Legal    │     │
│  │ Features │  │ About    │  │ Docs     │  │ Privacy  │     │
│  │ Pricing  │  │ Blog     │  │ Help     │  │ Terms    │     │
│  │ Changelog│  │ Careers  │  │ API      │  │ Cookies  │     │
│  │ Status   │  │ Press    │  │ Community│  │ Security │     │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘     │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │ Subscribe to our newsletter                          │    │
│  │ [email input] [Subscribe]                            │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌─ Social ─────────────────────────────────────────────┐    │
│  │ Twitter · LinkedIn · GitHub · YouTube · RSS          │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
│  © 2025 Frameable, Inc. · 143 Bell St, Seattle, WA 98121     │
│  All systems operational ● · Status →                        │
└─────────────────────────────────────────────────────────────┘
```

```tsx
function Footer() {
  return (
    <footer className="site-footer">
      <div className="footer-grid">
        <FooterColumn title="Product" links={[
          { label: 'Features', href: '/features' },
          { label: 'Pricing', href: '/pricing' },
          { label: 'Changelog', href: '/changelog' },
          { label: 'Status', href: 'https://status.frameable.app' },
        ]} />
        <FooterColumn title="Company" links={[
          { label: 'About', href: '/about' },
          { label: 'Blog', href: '/blog' },
          { label: 'Careers', href: '/careers' },
          { label: 'Press', href: '/press' },
          { label: 'Contact', href: '/contact' },
        ]} />
        <FooterColumn title="Resources" links={[
          { label: 'Docs', href: 'https://docs.frameable.app' },
          { label: 'Help', href: '/help' },
          { label: 'API', href: 'https://docs.frameable.app/api' },
          { label: 'Community', href: '/community' },
        ]} />
        <FooterColumn title="Legal" links={[
          { label: 'Privacy', href: '/privacy' },
          { label: 'Terms', href: '/terms' },
          { label: 'Cookies', href: '/cookies' },
          { label: 'Security', href: '/security' },
        ]} />
      </div>

      <NewsletterSignup />

      <SocialLinks />

      <div className="footer-meta">
        <p>© 2025 Frameable, Inc. · 143 Bell St, Seattle, WA 98121</p>
        <p>
          <span className="status-dot status-dot--ok" aria-hidden="true">●</span>
          {' '}
          <a href="https://status.frameable.app">All systems operational</a>
        </p>
      </div>
    </footer>
  );
}
```

### Privacy Policy (`/privacy`)

Don't generate this from scratch — use a lawyer or a service like Termsfeed / iubenda. But you must have one.

**Structure:**
1. Last updated date
2. What data we collect
3. Why we collect it (legal basis for EU users — GDPR)
4. Who we share it with (subprocessors list)
5. How long we keep it
6. Your rights (access, deletion, portability)
7. Cookies (or link to separate cookie policy)
8. International transfers
9. Children's privacy
10. Changes to this policy
11. Contact for privacy questions (DPO email if applicable)

### Terms of Service (`/terms`)

Same: use a lawyer or service. Must include:
1. Acceptance of terms
2. Description of service
3. Account registration and responsibilities
4. Acceptable use policy
5. Payment terms
6. Cancellation and refunds
7. Intellectual property
8. Disclaimers and limitations of liability
9. Indemnification
10. Termination
11. Governing law and dispute resolution
12. Changes to terms

### Cookie Policy (`/cookies`)

Required if you serve EU / UK users. List:
1. What cookies you set
2. Why (essential / analytics / marketing)
3. How long they persist
4. Third-party cookies (analytics, chat, video)
5. How to opt out

If you use a cookie banner (recommended), it must:
- Be dismissable without accepting non-essential cookies
- Save the user's preference
- Not block the page (the user must be able to read the page before choosing)

### Security page (`/security`)

For B2B / SaaS. Required for enterprise sales.

**Structure:**
1. Security overview (one paragraph)
2. Compliance badges (SOC 2, ISO 27001, GDPR)
3. Data encryption (at rest, in transit)
4. Subprocessors list
5. Vulnerability disclosure policy (link to security.txt)
6. Security contact (security@)
7. Audit logs and access controls
8. Backup and disaster recovery

Also ship a `/.well-known/security.txt` file:

```text
Contact: mailto:security@frameable.app
Expires: 2026-12-31T00:00:00.000Z
Preferred-Languages: en
Canonical: https://frameable.app/.well-known/security.txt
Policy: https://frameable.app/security/vulnerability-disclosure
```

### Status page (`status.example.com` or `/status`)

Use a hosted service (Statuspage.io, BetterUptime, Instatus) — don't build your own.

**Must show:**
1. Overall status (all systems operational / partial outage / major outage)
2. Per-component status (API, web app, background jobs, etc.)
3. Uptime history (90 days minimum)
4. Incident history with post-mortems
5. Subscribe to updates (email, Slack, RSS)
6. Scheduled maintenance windows

Link to it from the footer. The status dot should reflect real-time state — green for operational, yellow for degraded, red for outage.

### Changelog (`/changelog`)

A versioned list of changes. AI agents ship a "What's New" modal that no one reads. Ship a real changelog.

**Structure per entry:**

```markdown
## v2.4.0 — 2025-03-14

### Added
- New: Video annotations now support timestamped comments
- New: Slack integration with custom notification routing

### Changed
- Improved: Reviewer invite flow — 3 steps instead of 5
- Changed: Default annotation color from blue to brand accent

### Fixed
- Fixed: Long review titles truncated in the dashboard
- Fixed: Safari 17 video playback issue

### Deprecated
- Deprecated: v1 API endpoints — removal scheduled for 2025-09-01

### Removed
- Removed: Legacy "comments" feature (replaced by annotations)
```

Use a tool like [Mintlify](https://mintlify.com), [Headway](https://headwayapp.co), or [Fathym](https://fathym.com) — or build your own from Markdown.

### Help / docs (`/help` or `docs.example.com`)

For self-serve support. Structure:

```text
/docs                       Home
/docs/quickstart            5-minute quickstart
/docs/guides                How-to guides
/docs/guides/{slug}         Individual guide
/docs/api                   API reference
/docs/api/{endpoint}        Endpoint docs
/docs/troubleshooting       Common issues
/docs/faq                   FAQ
```

Use a docs framework: Mintlify, Docusaurus, GitBook, Nextra. Don't build your own.

### Press / Media kit (`/press`)

For journalists. Include:

1. **Company description** (3 lengths: 1 sentence, 1 paragraph, 1 page)
2. **Logos** — PNG and SVG, horizontal and stacked, full-color and white-only, in 3 sizes
3. **Product screenshots** — high-res, current
4. **Team photos** — headshots, full team photo
5. **Boilerplate** — for journalists to copy-paste
6. **Press releases** — dated, full text
7. **Press contact** — name, email, phone
8. **Mentioned in** — links to existing coverage
9. **Brand guidelines** — color palette, type, voice

```text
/press
/press/logos/frameable-logo-horizontal-color.svg
/press/logos/frameable-logo-horizontal-color.png
/press/logos/frameable-logo-stacked-color.svg
/press/logos/frameable-logo-horizontal-white.svg
/press/screenshots/dashboard-2025-q1.png
/press/team-headshots/maya-patel.jpg
/press/boilerplate.md
/press/contact.md
```

### Brand assets (`/brand`)

Similar to /press but for customers / partners who want to use your brand.

```text
/brand
/brand/logos/             — all logo variants
/brand/colors/            — palette with hex codes
/brand/typography/        — type families and pairings
/brand/voice/             — tone and voice guide
/brand/icons/             — icon set
/brand/illustrations/     — illustration style
/brand/examples/          — do's and don'ts
```

This page is rare on AI-built sites. Shipping it signals "we take our brand seriously."

### Careers (`/careers`)

If you're hiring, this page matters. Most AI-built sites skip it.

**Structure:**
1. Why work here (culture, mission, perks)
2. Open roles (filtered by team / location)
3. Application process (what to expect)
4. Benefits (salary range transparency, equity, health, PTO)
5. Interview process (steps, timeline)
6. Team photos / video

### Login / Signup

Don't over-design. Standard pattern:
- Email + password, or
- OAuth (Google, GitHub), or
- Magic link

Always offer passwordless (magic link) — highest conversion.

---

## The Complete Sitemap Template

Copy this. Add to `DESIGN-RATIONALE.md`. Mark each page as ✅ (will ship), ⚠️ (defer), or ❌ (not applicable).

```markdown
## Sitemap

### Marketing pages
- [ ] / (Home)
- [ ] /features (Features overview)
- [ ] /features/{feature} (3–8 sub-pages)
- [ ] /pricing
- [ ] /case-studies (Index)
- [ ] /case-studies/{slug} (5–10 stories)
- [ ] /blog (Index)
- [ ] /blog/{slug}
- [ ] /changelog
- [ ] /about
- [ ] /contact
- [ ] /press
- [ ] /brand
- [ ] /careers

### Product pages
- [ ] /login
- [ ] /signup
- [ ] /onboarding/{step} (3–5 steps)
- [ ] /dashboard (auth required)
- [ ] /settings (auth required)
- [ ] /billing (auth required)

### Support pages
- [ ] /docs (or docs.example.com)
- [ ] /help (FAQ / help center)
- [ ] /status (or status.example.com)

### Legal pages
- [ ] /privacy
- [ ] /terms
- [ ] /cookies
- [ ] /security
- [ ] /acceptable-use (if applicable)
- [ ] /dpa (Data Processing Agreement, for B2B)
- [ ] /subprocessors (list of subprocessors)

### Hidden / utility
- [ ] /404
- [ ] /500
- [ ] /sitemap.xml
- [ ] /robots.txt
- [ ] /llms.txt
- [ ] /llms-full.txt
- [ ] /.well-known/security.txt
- [ ] /manifest.json (PWA manifest)
- [ ] /favicon.ico, /apple-touch-icon.png

### Email (transactional)
- [ ] Welcome
- [ ] Email verification
- [ ] Password reset
- [ ] Onboarding sequence (3–5 emails)
- [ ] Receipt / invoice
- [ ] Trial expiring (day 11, day 14)
- [ ] Trial expired (day 15)
- [ ] Subscription canceled
- [ ] Team member invite
- [ ] Notification digest (daily / weekly)
- [ ] Abandoned signup (day 1)
- [ ] Re-engagement (day 30 dormant)

### Email (marketing)
- [ ] Newsletter (weekly / monthly)
- [ ] Product announcement
- [ ] Drip campaigns (3–5 per campaign)

### Footer must include
- [ ] Sitemap links (4-column structure)
- [ ] Newsletter signup
- [ ] Social links (Twitter, LinkedIn, GitHub, etc.)
- [ ] Legal links (Privacy, Terms, Cookies, Security)
- [ ] Status link with live indicator
- [ ] Mailing address
- [ ] Copyright with current year
```

A real SaaS ships all of the above. If you're shipping less, you're shipping a demo, not a product.

---

## Anti-Patterns (Auto-Fail)

1. **3-page site** (home, features, pricing). Missing 12+ pages users expect.
2. **No Privacy Policy / Terms** — legal liability, can't sign B2B deals.
3. **No Status page** — users assume the worst during outages.
4. **No Changelog** — users don't know what's new, can't tell if the product is alive.
5. **No Help / docs** — users submit support tickets for things they could self-serve.
6. **No Press / Brand assets** — journalists give up, partners use the wrong logo.
7. **Contact page is only a form** — users can't escalate, can't find the right person.
8. **No transactional emails** — users sign up and never come back.
9. **`no-reply@` sender** — kills the most valuable signal (user replies).
10. **No response-time SLA on the contact page** — users don't know what to expect.
11. **CAPTCHA on the contact form** — degrades UX, blocks some users, doesn't stop all bots.
12. **Footer is just copyright** — wasted opportunity for sitemap, social, newsletter, legal.
13. **About page is generic** ("we are a passionate team of...") — users don't trust a faceless company.
14. **No team photos** — users assume you're a one-person shop or a scam.
15. **Missing `/.well-known/security.txt`** — security researchers can't report vulnerabilities responsibly.
16. **No cookie banner** (if serving EU users) — GDPR violation.
17. **Cookie banner blocks the page** — accessibility / UX failure.
18. **Login / signup are over-designed** — conversion killer. Keep them simple.
19. **No abandoned-signup / abandoned-cart emails** — leaking revenue.
20. **Same template for all transactional emails** — welcome email should feel personal; receipt should feel mechanical. Don't make them look the same.

## Output

When you finish this guide, you should have:
- A sitemap in `DESIGN-RATIONALE.md` with every required page marked
- An About page with story, values, team, timeline, press mentions
- A Contact page with form + direct emails + phone + address + SLA
- A Footer with 4-column sitemap + newsletter + social + legal + status
- Privacy Policy, Terms, Cookies, Security pages (or scheduled with legal)
- Status page (hosted on Statuspage.io / BetterUptime / Instatus)
- Changelog page with versioned entries
- Help / docs site (on Mintlify / Docusaurus / GitBook / Nextra)
- Press kit page with logos, screenshots, boilerplate, contact
- Brand assets page (logos, colors, type, voice, icons)
- `/.well-known/security.txt` file
- 12 transactional email templates designed and coded
- Cookie banner (if applicable to your audience)
- 404 and 500 error pages with helpful links
- No anti-patterns from the list above
