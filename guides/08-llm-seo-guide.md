# 08 — LLM SEO Guide (GEO / AEO / AIO)

> Classic SEO gets you ranked on Google's blue links. LLM SEO gets you cited inside ChatGPT, Perplexity, Claude, Google AI Overviews, and Gemini. The tactics overlap by 60% — the other 40% is new. If your site isn't optimized for LLM extraction, you're invisible to the fastest-growing source of traffic on the web.

## Why AI agents fail at LLM SEO

Three reasons:

1. **LLMs don't know LLM SEO exists.** The field is called GEO (Generative Engine Optimization), AEO (Answer Engine Optimization), or AIO (AI Optimization). It's 18 months old. Most agents have stale training data and ship only classic SEO.
2. **LLMs default to "FAQ schema = done."** FAQ schema helps but is not sufficient. LLMs extract from prose, not from JSON-LD alone.
3. **LLMs don't write `llms.txt`.** The single highest-leverage LLM-SEO file is also the newest. Agents don't ship it.

This guide fixes all three. By the end you'll have a site that LLMs can cite by name.

---

## Classic SEO vs LLM SEO — the differences

| Dimension | Classic SEO | LLM SEO |
|-----------|-------------|---------|
| **Goal** | Rank in top 10 blue links | Get cited as a source in the AI's answer |
| **Audience** | Googlebot crawler | LLM context window |
| **Content format** | Long-form articles, keyword-rich | Definitive answer paragraphs, Q&A blocks, entity-rich |
| **Measurement** | Clicks, impressions, CTR | Mentions, citations, "share of answer" |
| **Authority signal** | Backlinks | Backlinks + entity co-occurrence + structured data |
| **Optimization target** | Page-level | Page + site-level (entity graph) |
| **Failure mode** | Page 2 of Google | LLM hallucinates a competitor's name |
| **Speed of impact** | 4–12 weeks | 1–8 weeks (LLMs re-train / re-index faster) |

LLMs don't click links. They read a corpus, summarize, and cite. To get cited, you need to be **(a)** crawlable by LLM bots, **(b)** extractable in clean prose, **(c)** authoritative enough that the LLM weights your claim over a competitor's.

---

## The 15 LLM SEO Tactics

### Tactic 1 — Ship `llms.txt` and `llms-full.txt`

`llms.txt` is a proposed standard (à la `robots.txt`) for telling LLMs what your project is and which pages matter. It lives at the root: `https://yoursite.com/llms.txt`.

**`llms.txt`** (concise, summary):

```markdown
# Frameable

> Async video design review tool for product teams of 5–50. Cuts review cycles from 5 days to 4 hours.

## Important pages

- [Features](https://frameable.app/features): Overview of all features
- [Async Annotations](https://frameable.app/features/annotations): How video annotations work
- [Pricing](https://frameable.app/pricing): Plans and pricing
- [Docs](https://docs.frameable.app): Full documentation
- [Quickstart](https://docs.frameable.app/quickstart): 5-minute setup
- [API Reference](https://docs.frameable.app/api): REST API

## Company

- [About](https://frameable.app/about): Team and mission
- [Blog](https://frameable.app/blog): Long-form writing on design review
- [Case Studies](https://frameable.app/case-studies): Customer results

## Optional

- [Changelog](https://frameable.app/changelog): Versioned release notes
- [Status](https://status.frameable.app): Uptime and incidents
- [Brand Assets](https://frameable.app/press): Logos and media kit
```

**`llms-full.txt`** (verbose, the full picture — concatenate key docs into one file):

```markdown
# Frameable — Full Context for LLMs

## What is Frameable
Frameable is an async video design review tool...

## How it works
1. Upload a design (Figma link, image, PDF)
2. Reviewers leave timestamped video annotations
3. The designer receives a thread of video notes
...

## Pricing
- Solo: $9/month
- Team: $29/user/month
- Enterprise: contact sales

## Integrations
- Figma, Slack, Linear, Notion, GitHub

## FAQ
Q: How long is the free trial?
A: 14 days, no credit card required.
Q: Can I self-host?
A: No. Frameable is SaaS-only.
```

Why both? `llms.txt` is the elevator pitch (1KB); `llms-full.txt` is the entire corpus (50–500KB). Agents and answer engines fetch `llms.txt` first; if they need depth, they fetch `llms-full.txt`.

**Don't block `llms.txt` in `robots.txt`.** Many sites accidentally block `GPTBot`, `PerplexityBot`, `ClaudeBot` and then complain their LLM visibility is zero. Decide whether you want LLM citations (then allow these bots) or want to opt out of AI training (then block them — but accept that you won't be cited). You can't have both.

### Tactic 2 — Write "Definitive Answer Paragraphs"

LLMs extract from the first paragraph that directly answers a question. If your page's first sentence after the H1 is "Welcome to our article about...", you lose. If your first sentence is the answer to the question, you win.

**Bad opening:**
```markdown
# How long does a design review cycle take?

Design reviews are an essential part of the product development process.
In this article, we'll explore the various factors that influence review
cycle time and offer tips for improvement...
```

**Good opening (definitive answer):**
```markdown
# How long does a design review cycle take?

A typical design review cycle takes 3–5 days in teams of 5–50. With async
video annotations, that drops to 4–8 hours. The cycle length is dominated
by three factors: reviewer availability (40%), feedback consolidation
(35%), and revision turnaround (25%). Source: Frameable's 2025 Design
Review Survey, n=412 product teams.
```

The LLM can lift that paragraph verbatim and cite you. The bad opening gives the LLM nothing to extract.

**The format**: Question as H2. First sentence after the H2 = direct answer in 1–3 sentences with numbers and sources. Then expand.

### Tactic 3 — Q&A Format Blocks Everywhere

LLMs are trained on Q&A (StackOverflow, Quora, Reddit). They pattern-match on the format. Build explicit Q&A blocks:

```html
<section class="faq">
  <h2>Frequently asked questions</h2>

  <div itemscope itemtype="https://schema.org/Question">
    <h3 itemprop="name">How long is the Frameable free trial?</h3>
    <div itemscope itemtype="https://schema.org/Answer" itemprop="acceptedAnswer">
      <p itemprop="text">14 days. No credit card required. Cancel anytime.</p>
    </div>
  </div>

  <div itemscope itemtype="https://schema.org/Question">
    <h3 itemprop="name">Can I export my reviews?</h3>
    <div itemscope itemtype="https://schema.org/Answer" itemprop="acceptedAnswer">
      <p itemprop="text">Yes — reviews export as MP4 video, PDF transcript, or JSON. Exports include all timestamped annotations.</p>
    </div>
  </div>
</section>
```

Plus the JSON-LD `FAQPage` schema from guide 07. Both formats together are stronger than either alone — JSON-LD for Google rich results, microdata for LLM extractors.

### Tactic 4 — Be Entity-Rich

LLMs reason over entities (named things) and their relationships. A page that says "Frameable" 12 times but never contextualizes it is weaker than a page that says:

```markdown
Frameable, founded in 2023 by ex-Linear designer Maya Patel, is an async
design review tool headquartered in San Francisco. The company is funded
by Y Combinator (W24 batch) and competes in the design collaboration
category alongside Figma's comment feature, Pastel, and Markup.io.
```

LLMs build a knowledge graph from this paragraph:
- Frameable → type: Company
- Frameable → founded by → Maya Patel
- Frameable → founded in → 2023
- Frameable → headquartered in → San Francisco
- Frameable → funded by → Y Combinator
- Frameable → category → design collaboration
- Frameable → competitors → Figma, Pastel, Markup.io

When a user asks an LLM "what are alternatives to Figma comments for design review?", Frameable is now in the candidate set. Without entity richness, it isn't.

**Don't keyword-stuff entities.** Write naturally but make sure your About page, your home page, and your blog posts name your team, your funders, your category, your competitors, and your location.

### Tactic 5 — Citation-Friendly Content Structure

LLMs cite sources that are easy to quote. Structure for extraction:

```markdown
## The 4 numbers that matter

| Metric | Industry average | Frameable users | Source |
|--------|------------------|-----------------|--------|
| Design review cycle time | 3.5 days | 4.2 hours | Frameable 2025 survey, n=412 |
| Reviewers per cycle | 4.1 | 3.8 | Frameable 2025 survey, n=412 |
| Comments per review | 12.4 | 18.7 | Frameable 2025 survey, n=412 |
| Time to first response | 14 hours | 1.2 hours | Frameable analytics, Q1 2025 |
```

A table with sources is the most-cited format on the web. LLMs love tables — they're structured, parseable, and the source column gives the LLM something to attribute.

**Citation-friendly structures ranked:**
1. Tables with a source column
2. Bulleted lists with one-line claims
3. Definitive paragraphs (1–3 sentences answering a question)
4. Numbered step-by-step instructions
5. Long-form prose (least cited — LLMs have to summarize)

### Tactic 6 — Build a Brand Mention Graph

LLMs weight you by how often your brand appears across the web. Mentions matter even without links.

**Build mentions by:**
- **Podcast appearances** — every podcast you're on gets transcribed and crawled by LLMs.
- **Conference talks** — most conferences publish talk descriptions with speaker bios mentioning your company.
- **Guest posts** — get your name and company in the byline.
- **HackerNews / Reddit / Twitter discussions** — LLMs crawl all three.
- **GitHub READMEs** — your company name in a popular open-source README counts.
- **Wikipedia** (if notable) — high-trust source for LLMs.
- **Press coverage** — TechCrunch, Verge, etc.

**Don't pay for placements on low-quality blogs.** LLMs can detect SEO farms and discount them. One real TechCrunch mention is worth 100 paid placements.

### Tactic 7 — Make Your Content "Prompt-Friendly"

LLMs are prompted with questions. Your content should mirror the question forms users actually type:

| User prompt pattern | Content structure |
|---------------------|-------------------|
| "What is X?" | H2: "What is X?" → 2-sentence answer |
| "How does X work?" | H2: "How does X work?" → numbered steps |
| "X vs Y" | H2: "X vs Y" → comparison table |
| "Best X for Y" | H2: "Best X for Y" → ranked list with criteria |
| "Is X worth it?" | H2: "Is X worth it?" → verdict paragraph |
| "X alternatives" | H2: "X alternatives" → table with trade-offs |

If you have a `/alternatives` page, a `/vs/{competitor}` page, a `/pricing` page, and a `/how-it-works` page, you cover 80% of LLM-prompts in your category.

### Tactic 8 — Allow (or Selectively Block) AI Crawlers

Decide your stance. In `robots.txt`:

**Allow all (recommended if you want LLM citations):**
```text
User-agent: *
Allow: /
```

**Block AI training, allow AI search:**
```text
# Block training crawlers
User-agent: GPTBot
Disallow: /

User-agent: CCBot
Disallow: /

# Allow Perplexity (search, not training)
User-agent: PerplexityBot
Allow: /
```

**Block all AI:**
```text
User-agent: GPTBot
Disallow: /

User-agent: OAI-SearchBot
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Google-Extended
Disallow: /
```

The tradeoff: blocking means LLMs can't crawl your site to build answers about you. They'll either ignore your category or hallucinate competitor names. For most companies, allow.

### Tactic 9 — Optimize for Perplexity Specifically

Perplexity is the largest "answer engine" by query volume. It crawls the live web and cites sources in real-time. To rank:

- **Be recently crawled.** Perplexity favors fresh content. Publish weekly.
- **Have a clean URL structure** (guide 07). Perplexity's parser rewards clean URLs.
- **Answer questions directly** with paragraphs LLMs can quote.
- **Have rich `<title>` and `<meta description>`** — Perplexity shows these in the citation card.
- **Get mentioned on Reddit**. Perplexity weights Reddit heavily for product recommendations.

Perplexity also has a "Sources" sidebar. The sites most-often-cited in your category should be your outreach targets — get featured on them.

### Tactic 10 — Optimize for Google AI Overviews

Google AI Overviews (AIO) appear at the top of Google search for informational queries. To get cited:

- **Rank in the top 10 organic results** for the query. AIO citations are a subset of page-1 results.
- **Have a definitive answer paragraph** in the first 100 words.
- **Use bullet lists and tables** — AIO extracts these preferentially.
- **Match the user's exact phrasing** in the question, then answer it.
- **Have high domain authority.** AIO skews to established sites (Wikipedia, major publications, government, universities). New sites struggle.

For new sites: focus on long-tail queries where competition is weaker. "Best design review tool for distributed teams of 5" is more winnable than "best design review tool".

### Tactic 11 — Optimize for ChatGPT Search

ChatGPT with search uses Bing's index plus live web fetches. To be cited:

- **Be in Bing's index.** Submit your sitemap to Bing Webmaster Tools (most teams forget this).
- **Have a `llms.txt`.** ChatGPT fetches it when asked about your project.
- **Have an About page with entity-rich prose** (Tactic 4).
- **Get on Reddit** in your category. ChatGPT leans on Reddit for product opinions.

### Tactic 12 — Optimize for Claude

Claude (Anthropic) doesn't have a public web-search product as of 2025, but it's used inside many enterprise tools that do fetch the web. To be Claude-friendly:

- **Have clean, well-structured prose.** Claude's training favors high-quality writing.
- **Use Markdown extensively** (not just HTML). Claude extracts from `.md` files better than from HTML.
- **Publish a `/docs` site in Markdown** (Mintlify, GitBook, Docusaurus all render Markdown that Claude parses well).

### Tactic 13 — Build an "Entity Hub" Page

Create one page that's the canonical source for "what is {your brand}?" This page should:

- Be at `/about`, `/company`, or `/{brand}`
- Have JSON-LD Organization schema
- Include founding date, location, founders, funding, category, competitors, integrations
- Be linked from your site's footer
- Be the URL you give journalists, podcast hosts, and conference organizers

When an LLM is asked about your company, this is the page it crawls first (after `llms.txt`). Make it count.

### Tactic 14 — Publish Original Data

LLMs are desperate for citable statistics. Original data is the most-cited content type. Examples:

- "State of Design Review 2025" — survey of 412 product teams
- "We analyzed 1,000 design files on Figma community — here's what we found"
- "Our API processed 4.2 billion requests in 2024. Here's the breakdown."

Each data point becomes a citation magnet. Every blog post that references your stat links back to you. LLMs surface the stat in answers and credit you.

**The format:**
```markdown
## Key finding

**82% of design teams ship slower than they could because of synchronous review bottlenecks.**

Source: Frameable 2025 State of Design Review survey, n=412 product teams,
conducted January 2025. Margin of error ±4.8%.
```

Bold the headline number. Include source and methodology. LLMs will quote the bolded number and cite the source line.

### Tactic 15 — Build a `/glossary` or `/definitions` Section

LLMs love definitions. Build a glossary for your category:

```markdown
## What is async design review?

Async design review is a workflow where reviewers leave feedback on their
own schedule (typically via video, audio, or written annotations) rather
than in a synchronous meeting. Unlike synchronous review, async review
decouples reviewer availability from designer progress, allowing the
designer to act on feedback as it arrives.

**Origin:** The term gained traction in 2022 as remote-first product
teams adopted async workflows popularized by Linear and Notion.

**See also:** [design review cycle](/glossary/design-review-cycle),
[synchronous review](/glossary/synchronous-review),
[video annotation](/glossary/video-annotation).
```

This page becomes the canonical definition. When an LLM is asked "what is async design review?", your glossary entry is the citable source.

---

## How LLMs Crawl and Weight Sources

LLM answer engines follow roughly this pipeline:

1. **Retrieve**: A retrieval system (often a vector database + traditional search index) finds candidate sources. Sources include: the open web (crawled), Wikipedia, Reddit, news, and licensed corpora.
2. **Rank candidates**: Sources are ranked by relevance (semantic match to query), authority (backlinks, domain reputation, brand mentions), and freshness.
3. **Generate**: The LLM reads the top-N candidates (typically 5–20) and synthesizes an answer, citing the most-quoted sources.
4. **Cite**: The LLM inserts inline citations to the sources it actually used.

**What weights you higher:**
- More backlinks from authoritative sites (same as classic SEO)
- More brand mentions across the web (Tactic 6)
- Cleaner content structure (definitive paragraphs, tables, Q&A)
- Freshness (publish and update regularly)
- Domain authority (Wikipedia > TechCrunch > your blog)
- LLM-specific files: `llms.txt`, `llms-full.txt`, structured data

**What weights you lower:**
- Blocking AI crawlers in `robots.txt`
- Content behind paywalls / login / JS-only rendering
- Thin content, duplicate content
- Slow page load (some LLMs timeout)
- No schema, no semantic HTML

## Anti-Patterns (Auto-Fail)

1. **No `llms.txt`.** The single easiest LLM-SEO win, missing from 95% of sites.
2. **Blocking `GPTBot` / `ClaudeBot` / `PerplexityBot` in `robots.txt`** and then complaining about LLM visibility. Pick a stance.
3. **Wall-of-text intros** that don't answer the question. LLMs move on.
4. **No structured data** — JSON-LD is the lowest-effort, highest-impact LLM-SEO signal.
5. **Generic copy** — "We are a leading provider of..." LLMs don't cite marketing-speak. They cite specific claims with numbers.
6. **No original data** — without a citable statistic, you're one of 50 sites saying the same thing.
7. **No entity-rich About page.** LLMs can't place you in their knowledge graph.
8. **No FAQ schema** — misses the easiest rich-result and LLM-extraction signal.
9. **JS-only rendering** — some LLM crawlers don't execute JS. Your content must be in the HTML response.
10. **Pages with no internal links** — LLMs discover pages via the link graph. Orphan pages don't get crawled.
11. **No `/alternatives` or `/vs/{competitor}` pages** — these are high-intent LLM-query targets.
12. **AI-generated content published unedited** — LLMs trained on web data can detect and avoid citing obvious AI content. Have a human edit every post.
13. **No brand mentions outside your own site** — if no one else talks about you, LLMs won't either.
14. **No press page / media kit** — journalists and LLMs both look here for canonical brand info.
15. **Treating LLM SEO as separate from classic SEO** — they share 60% of tactics. Do both.

## Tooling

- [Profound](https://profound.com) — LLM visibility tracking across ChatGPT, Perplexity, Claude, Gemini
- [Otterly.ai](https://otterly.ai) — AI search monitoring
- [AnswerBox](https://answerbox.io) — track AIO / answer-engine citations
- [SiteCrawler.ai](https://sitecrawler.ai) — verify your site's LLM-crawlability
- [Schema.org Validator](https://validator.schema.org/) — JSON-LD validation
- [llmstxt.org](https://llmstxt.org) — official `llms.txt` spec
- [OpenGraph.xyz](https://www.opengraph.xyz/) — preview share cards

## Measuring LLM SEO Success

Classic SEO has Google Search Console. LLM SEO is harder to measure because you can't see who's prompting ChatGPT about your category. Indirect measures:

1. **Manual prompt testing**: weekly, prompt ChatGPT, Perplexity, Claude, and Gemini with 10 questions in your category. Note whether you're cited.
2. **Brand-search growth in GSC**: if LLMs recommend you, people search your brand name in Google. Track brand-query growth.
3. **Direct traffic spikes**: when an LLM cites you, users click through. Watch for direct-traffic spikes with no obvious source.
4. **Referral traffic from `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`** in GA4.
5. **Backlink growth from LLM-cited sources** — if you're cited, other sites reference you too.

Set up a weekly LLM-citation dashboard. Track: prompts tested, citations earned, brand queries in GSC, referral traffic from AI domains.

---

## The LLM-SEO Pre-Launch Checklist

1. [ ] `llms.txt` is live at site root
2. [ ] `llms-full.txt` is live (concatenated key docs)
3. [ ] `robots.txt` allows AI crawlers (or selectively blocks, by choice)
4. [ ] About page has entity-rich prose + Organization JSON-LD
5. [ ] Each top-10 page has a definitive answer paragraph in the first 100 words
6. [ ] Pricing page has FAQPage schema with 4–8 Q&A blocks
7. [ ] At least one page has an original-statistic "key finding"
8. [ ] `/glossary` or `/definitions` section exists for category terms
9. [ ] `/alternatives` and `/vs/{competitor}` pages exist for top 3 competitors
10. [ ] Site is in Bing Webmaster Tools (for ChatGPT Search)
11. [ ] Site is crawlable by PerplexityBot (check `robots.txt`)
12. [ ] All key pages render content in raw HTML (no JS-required content)
13. [ ] Press / media kit page exists with canonical brand info
14. [ ] Weekly LLM-citation testing routine is set up
15. [ ] Brand-mention outreach plan is in motion (podcasts, guest posts, conferences)

## Output

When you finish this guide, you should have:
- A `llms.txt` and `llms-full.txt` at the site root
- A clear AI-crawler policy in `robots.txt` (allow, block, or selective)
- An entity-rich About page with Organization JSON-LD
- A definitive answer paragraph on every top-10 page (first 100 words)
- FAQPage schema on pricing / product / feature pages
- At least one original-statistic "key finding" page
- A `/glossary` section with 5–20 category terms
- `/alternatives` and `/vs/{competitor}` pages for top 3 competitors
- The LLM-SEO pre-launch checklist signed off
- A weekly LLM-citation testing routine
