<div align="center">

# 🎨 Anti-Generic AI Design Skill

### *Stop shipping AI-coded pages that **look** AI-coded.*

[![License: MIT](https://img.shields.io/badge/License-MIT-0E5C5A?style=for-the-badge&labelColor=1A1A1A)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-B45309?style=for-the-badge&labelColor=1A1A1A)](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/releases/tag/v1.0.0)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-15803D?style=for-the-badge&labelColor=1A1A1A)](CONTRIBUTING.md)
[![Made with ♥](https://img.shields.io/badge/made_with-%E2%9D%A4-DC2626?style=for-the-badge&labelColor=1A1A1A)](#contributing)
[![Status: Active](https://img.shields.io/badge/status-active-0E5C5A?style=for-the-badge&labelColor=1A1A1A)](#)

**A complete, framework-agnostic design skill for AI coding agents**
*(Claude Code · Manus · Cursor · Cline · Super Z · Aider)*

**Forces the agent to think like a senior art director before writing a single line of JSX.**

[📦 What's inside](#whats-inside) · [🚀 Quick start](#quick-start) · [📚 Guides](#guides) · [🎭 Live demo](#live-demo) · [🤝 Contributing](#contributing)

</div>

---

> ### ⚠️ The problem
>
> In the vibe-coding era, the bottleneck is no longer *can the AI build it* — it's *does the output look like every other LLM-generated site*. Bland indigo gradients. Default Inter. Centered hero with one H1, one subhead, two buttons. Glass cards with no depth. **No reference research. No debate. No soul.**
>
> ### ✅ The fix
>
> This skill inserts a **mandatory debate + research phase** before any code is written. The agent must research 3+ references, debate every design decision (palette, font, hero, motion), justify each choice with a cited reference or named principle, and only **then** write code — using battle-tested templates, not generic divs.

---

## 📦 What's inside

```
ai-design-skill/
├── SKILL.md                  ← Main orchestrator (the AI loads this first)
├── guides/                   ← 21 deep guides, one per design dimension
│   ├── 01-thinking-redesign.md      🧠 debate protocol — the soul of this skill
│   ├── 02-color-palette-guide.md    🎨 100 palettes + WCAG contrast rules
│   ├── 03-font-pairing-guide.md     🔤 100 font pairs + loading strategy
│   ├── 04-glassmorphism-guide.md    🪟 5-layer glass system (not the AI default)
│   ├── 05-hero-section-guide.md     🦸 TOP-CLASS hero patterns (longest guide)
│   ├── 06-advanced-css-components.md⚙️ @property, :has(), container queries, VTA
│   ├── 07-seo-guide.md              🔍 technical SEO + 30-point checklist
│   ├── 08-llm-seo-guide.md          🤖 GEO / AEO / llms.txt / AI Overviews
│   ├── 09-animation-guide.md        ✨ 100 animations + timing curves
│   ├── 10-reference-research.md     📚 research methodology + worksheet
│   ├── 11-about-info-email-contact.md📧 complete site sitemap + 12 email templates
│   ├── 12-spacing-layout-grid.md    📐 8pt system + grid + max-width strategy
│   ├── 13-microinteractions.md      🎯 5 mandatory states per interactive element
│   ├── 14-accessibility-guide.md    ♿ WCAG 2.2 AA + 40-point checklist
│   ├── 15-performance-guide.md      ⚡ Core Web Vitals + Lighthouse 90+ recipe
│   ├── 16-dark-mode-guide.md        🌙 designing dark (not inverting light)
│   ├── 17-responsive-design.md      📱 container queries + fluid type
│   ├── 18-content-typography.md     ✍️ copy length + reading level + voice
│   ├── 19-imagery-iconography.md    🖼️ real photos > stock, custom > unDraw
│   ├── 20-conversion-principles.md  💰 Cialdini + CTA placement + pricing psych
│   └── 21-checklist-launch.md       ✅ 52-point pre-launch gate
├── data/                     ← 500 curated reference entries
│   ├── websites-100.json            🌐 100 reference sites by category
│   ├── themes-100.json              🎭 100 named design themes
│   ├── palettes-100.json            🎨 100 palettes (WCAG AA verified)
│   ├── font-pairs-100.json          🔤 100 font pairings + rationale
│   └── animations-100.json          ✨ 100 animations + copy-paste code
├── templates/                ← Drop-in React + TS + Tailwind components
│   ├── hero/                        🦸 4 hero variants
│   ├── components/                  🧩 7 components (glass, nav, bento, ...)
│   └── styles/                      🎨 3 CSS utility files (tokens, glass, anim)
└── examples/                 ← Standalone HTML demos
    └── demo-saas-landing.html       🎬 live demo of all patterns
```

| | |
|:---:|:---:|
| **21 guides** | ~54,000 words of opinionated design wisdom |
| **500 references** | Curated websites, themes, palettes, fonts, animations |
| **11 templates** | React + TS + Tailwind, ready to drop in |
| **3 CSS systems** | Design tokens, glassmorphism, animation utilities |
| **1 demo** | Standalone HTML showing all patterns applied |

---

## 🚀 Quick start

### Option A — Drop into your agent's project

Copy this entire folder into your repo (or symlink `SKILL.md` from your agent's skill loader). When the agent starts a frontend task, it reads `SKILL.md`, which orchestrates the rest.

### Option B — Paste as system prompt

Paste the contents of `SKILL.md` (plus the relevant `guides/*.md`) into your agent's system prompt or `CLAUDE.md` / `.cursorrules` / `manus.toml`.

### Option C — Use the data files directly

The `data/*.json` files are framework-agnostic. Import them in any design tool, Figma plugin, or code generator.

```bash
git clone https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design.git
cd anti-generic-ai-design
```

---

## 🧠 The core idea

Most AI design fails because the agent **skips the thinking step**. It jumps from "build a landing page" straight to `<div className="max-w-7xl mx-auto text-center">`.

This skill inserts a **mandatory 4-phase protocol** before any code is written:

| Phase | What happens | Blocking? |
|-------|--------------|-----------|
| **1. Research** | Pull 3+ reference sites from `data/websites-100.json`. Shortlist palettes, fonts, themes, animations. | ✅ Yes |
| **2. Debate** | For every design decision (palette, font, hero, motion, density, dark/light), write a FOR / AGAINST / REBUTTAL block. | ✅ Yes |
| **3. Justify** | Output a `DESIGN-RATIONALE.md` document with all choices, references, and debate log. | ✅ Yes |
| **4. Build** | Only now does code start. Uses `templates/` as scaffolding. | — |

Skipping any phase = critical failure.

---

## 🦸 What makes a hero "top-class"

The hero is 80% of a landing page's first impression. **It must be top-class.** The 7 rules (full treatment in `guides/05-hero-section-guide.md`):

1. **One focal point** — never two competing elements
2. **Show the real product** — never a stock illustration
3. **Motion reveals information** — never decoration
4. **Proof within the fold** — one stat, one quote, or one case study
5. **Maximum 7 elements** above the fold
6. **Headline is specific** — "Ship design reviews 4× faster" not "The Modern Way to Build Software"
7. **CTA copy is action + outcome** — "Start free trial → ship today" not "Get Started"

---

## 🚫 Auto-fail anti-patterns

If the output contains ANY of these, the agent must redesign:

| # | Anti-pattern | Why it's banned |
|---|---|---|
| 1 | Centered hero with H1 + subhead + 2 stacked buttons | Most-shipped layout in web history. Invisible. |
| 2 | Indigo→violet→pink gradient | The #1 AI tell. Tailwind default. |
| 3 | Inter as the only font | Pair with a display face. Always. |
| 4 | Three equal glass cards with emoji icons | Replace with asymmetric bento or real product moment |
| 5 | "Trusted by" grayscale logo strip | Replace with 3 case-study cards |
| 6 | Generic Features / Pricing / Testimonials / FAQ stack | Restructure by conversion priority |
| 7 | Fade-in-up on every section | Motion must reveal, not decorate |
| 8 | `rounded-2xl` on everything | Vary radii intentionally |
| 9 | Default Tailwind shadow on every card | Use layered, colored, or no shadows |
| 10 | Stock illustration / unDraw vector | Use real product UI or real photography |
| 11 | `bg-gradient-to-r from-purple-500 to-pink-500` | Banned everywhere |
| 12 | Emoji as feature icons (🚀⚡🎯🔒) | Use Lucide / Phosphor / custom SVG |
| 13 | "Lorem ipsum" or "Your headline here" | All copy must be real and specific |
| 14 | H1 > 72px without editorial reason | Giant AI-hero text is a tell |
| 15 | No motion-reduce / no focus-visible / no skip-link | Accessibility is mandatory |

---

## 📚 Guides

| # | Guide | What it covers |
|---|-------|----------------|
| 01 | [Thinking & Redesign](guides/01-thinking-redesign.md) | The 4-phase debate protocol — the soul of the skill |
| 02 | [Color Palette](guides/02-color-palette-guide.md) | 5-role palette system, WCAG contrast, forbidden palettes |
| 03 | [Font Pairing](guides/03-font-pairing-guide.md) | 4-role type system, loading strategy, modular scales |
| 04 | [Glassmorphism](guides/04-glassmorphism-guide.md) | 5-layer glass system with real recipes |
| 05 | [Hero Section](guides/05-hero-section-guide.md) | 7 rules + 6 layout patterns + choreography |
| 06 | [Advanced CSS](guides/06-advanced-css-components.md) | @property, :has(), container queries, View Transitions |
| 07 | [SEO](guides/07-seo-guide.md) | Technical SEO + JSON-LD + 30-point checklist |
| 08 | [LLM SEO](guides/08-llm-seo-guide.md) | GEO / AEO / llms.txt / AI Overviews |
| 09 | [Animation](guides/09-animation-guide.md) | Timing curves, duration, 12 principles, reduced-motion |
| 10 | [Reference Research](guides/10-reference-research.md) | How to study references before designing |
| 11 | [About / Contact / Info](guides/11-about-info-email-contact.md) | Complete sitemap + 12 email templates |
| 12 | [Spacing & Layout](guides/12-spacing-layout-grid.md) | 8pt system, grid, max-width strategy |
| 13 | [Microinteractions](guides/13-microinteractions.md) | 5 mandatory states per interactive element |
| 14 | [Accessibility](guides/14-accessibility-guide.md) | WCAG 2.2 AA + 40-point checklist |
| 15 | [Performance](guides/15-performance-guide.md) | Core Web Vitals + Lighthouse 90+ recipe |
| 16 | [Dark Mode](guides/16-dark-mode-guide.md) | Designing dark, not inverting light |
| 17 | [Responsive](guides/17-responsive-design.md) | Container queries + fluid type + thumb zones |
| 18 | [Content Typography](guides/18-content-typography.md) | Copy length, reading level, voice |
| 19 | [Imagery & Iconography](guides/19-imagery-iconography.md) | Real photos > stock, custom > unDraw |
| 20 | [Conversion](guides/20-conversion-principles.md) | Cialdini + CTA placement + pricing psychology |
| 21 | [Launch Checklist](guides/21-checklist-launch.md) | 52-point pre-launch gate |

---

## 🎭 Live demo

Open `examples/demo-saas-landing.html` directly in a browser, or view it on GitHub Pages:

**👉 https://huzaifaa-dev-vibe.github.io/anti-generic-ai-design/**

The demo shows:
- Split hero with real product UI on the right
- Counter reveal animation (1,247,893 reviews shipped)
- Bento grid feature section (replaces 3-card layout)
- Glass sticky nav that shrinks on scroll
- Restrained motion (only the counter animates — everything else just appears)
- Real, specific copy (no "Your headline here")
- Custom amber palette (no indigo/violet/pink in sight)

---

## 🤝 Contributing

<div align="center">

### **Contributions are ALWAYS welcome. This is a living project.**

[![Contributors welcome](https://img.shields.io/badge/contributors-welcome-15803D?style=for-the-badge&labelColor=1A1A1A)](CONTRIBUTING.md)
[![Good first issue](https://img.shields.io/badge/good_first_issue-available-7B1E1E?style=for-the-badge&labelColor=1A1A1A)](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/labels/good%20first%20issue)
[![Help wanted](https://img.shields.io/badge/help_wanted-available-B45309?style=for-the-badge&labelColor=1A1A1A)](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/labels/help%20wanted)

</div>

This project is **always open for improvements**. Three ways to contribute:

### 1. 📊 Data additions (easiest, highest impact)

Add entries to the JSON files in `data/`. Each file has a documented schema — read the first 30 lines before adding.

- `data/websites-100.json` — add a real, well-designed website
- `data/themes-100.json` — add a named theme
- `data/palettes-100.json` — add a palette (must pass WCAG AA)
- `data/font-pairs-100.json` — add a font pairing (must be freely loadable)
- `data/animations-100.json` — add an animation with code

### 2. 📝 Guide improvements

The `guides/*.md` files are opinionated on purpose. If you disagree with a rule, open an issue first — don't just rewrite the guide. PRs that add new sub-sections, examples, or fallback patterns are welcome.

### 3. 🧩 New templates

Templates live in `templates/` and must be React + TypeScript + Tailwind, self-contained, accessible, and use the project's CSS variable conventions.

### PR checklist

- [ ] No duplicate entries
- [ ] All JSON validates
- [ ] No proprietary fonts/palettes/images
- [ ] If adding a website, the link is live and the design note is specific
- [ ] If adding a palette, contrast ratios are accurate

👉 See [`CONTRIBUTING.md`](CONTRIBUTING.md) for full guidelines.

---

## 🛠️ Tech stack

<div align="center">

| Layer | Choice | Why |
|-------|--------|-----|
| **Skill format** | Universal Markdown | Works with Claude Code, Manus, Cursor, Cline, Aider, Super Z |
| **Templates** | React 18+ · TypeScript 5+ · Tailwind 3+ | Industry standard, broad compatibility |
| **Data** | JSON | Framework-agnostic, importable anywhere |
| **CSS** | Custom properties + modern CSS | No build step needed for the styles |
| **Demo** | Vanilla HTML/CSS/JS | Zero dependencies, opens in any browser |
| **Motion** | Native CSS + Web APIs | No Framer Motion / GSAP dependency |

</div>

---

## 📈 Roadmap

- [ ] v1.1.0 — Add 50 more website references (target: 150 total)
- [ ] v1.2.0 — Add Vue + Svelte template variants
- [ ] v1.3.0 — Add Figma plugin that imports `data/palettes-100.json`
- [ ] v1.4.0 — Add CLI tool: `npx anti-generic-ai-design init`
- [ ] v2.0.0 — Auto-screenshot reference sites for visual comparison

Have an idea? [Open a discussion](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/discussions).

---

## 📄 License

[MIT](LICENSE) — use it, fork it, ship it. Just don't blame us when your AI stops producing generic work. 😉

---

## ⭐ Star history

If this skill saved your project from the "AI look", consider starring the repo. It helps others discover it.

<div align="center">

[![Star this repo](https://img.shields.io/badge/⭐_star-this_repo-0E5C5A?style=for-the-badge&labelColor=1A1A1A)](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/stargazers)

</div>

---

<div align="center">

**Built to kill the "AI look". One debate at a time.**

*Made with ♥ by [huzaifaa-dev-vibe](https://github.com/huzaifaa-dev-vibe) and contributors.*

*This project is and will always be **open for improvements**.*

[🐛 Report bug](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/issues/new?labels=bug) · [💡 Request feature](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/issues/new?labels=enhancement) · [💬 Discuss](https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/discussions) · [📖 Read the docs](SKILL.md)

</div>
