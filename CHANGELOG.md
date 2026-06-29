# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] — 2026-06-30

### 🎉 Added

**Initial public release.** A complete, framework-agnostic design skill for AI coding agents that forces the agent to think like a senior art director before writing frontend code.

#### Core skill
- `SKILL.md` — main orchestrator with mandatory 4-phase protocol (Research → Debate → Justify → Build)
- 15 auto-fail anti-patterns (centered hero, indigo/violet gradients, Inter-only, emoji icons, fade-in-up everywhere, and 10 more)
- Module loading table mapping design dimensions to specific guides
- Output contract specifying what every frontend deliverable must ship with

#### 21 deep guides (~54,000 words total)
- `01-thinking-redesign.md` — the 4-phase debate protocol (the soul of the skill)
- `02-color-palette-guide.md` — 5-role palette system, WCAG contrast rules, forbidden palettes
- `03-font-pairing-guide.md` — 4-role type system, loading strategy, modular scales
- `04-glassmorphism-guide.md` — 5-layer glass system with real recipes and fallbacks
- `05-hero-section-guide.md` — 7 rules + 6 layout patterns + choreography (longest guide, top-class required)
- `06-advanced-css-components.md` — @property, :has(), container queries, View Transitions API
- `07-seo-guide.md` — technical SEO + JSON-LD recipes + 30-point pre-launch checklist
- `08-llm-seo-guide.md` — GEO / AEO / llms.txt / AI Overviews / per-engine tactics
- `09-animation-guide.md` — timing curves, durations, Disney's 12 principles applied to UI
- `10-reference-research.md` — research methodology + worksheet template
- `11-about-info-email-contact.md` — complete sitemap (15-20 pages) + 12 transactional email templates
- `12-spacing-layout-grid.md` — 8pt system, grid, max-width strategy
- `13-microinteractions.md` — 5 mandatory states per interactive element
- `14-accessibility-guide.md` — WCAG 2.2 AA + 40-point checklist
- `15-performance-guide.md` — Core Web Vitals + Lighthouse 90+ recipe
- `16-dark-mode-guide.md` — designing dark (not inverting light)
- `17-responsive-design.md` — container queries + fluid type + thumb zones
- `18-content-typography.md` — copy length, reading level, voice
- `19-imagery-iconography.md` — real photos > stock, custom > unDraw
- `20-conversion-principles.md` — Cialdini + CTA placement + pricing psychology
- `21-checklist-launch.md` — 52-point pre-launch gate

#### 500 curated reference entries (5 JSON files, 100 entries each)
- `data/websites-100.json` — 100 reference sites across 10 categories with specific design notes
- `data/themes-100.json` — 100 named design themes with palette + type + texture + motion
- `data/palettes-100.json` — 100 palettes with 5 roles + 4 semantic colors + dark variants + WCAG AA verified contrast ratios
- `data/font-pairs-100.json` — 100 font pairings (display + body + numeric + mono) with rationale, fallbacks, and Google Fonts loading HTML
- `data/animations-100.json` — 100 animations with timing curves, durations, copy-pasteable CSS/JS code, reduced-motion handling, and references

#### Drop-in React + TypeScript + Tailwind templates
- 4 hero variants: `hero-split`, `hero-asymmetric`, `hero-product-first`, `hero-video-bg`
- 7 components: `glass-card`, `animated-nav`, `gradient-text`, `bento-grid`, `magnetic-button`, `counter`, `scroll-reveal`
- 3 CSS utility files: `tokens.css` (design tokens), `glassmorphism.css`, `animations.css`

#### Standalone HTML demo
- `examples/demo-saas-landing.html` — SaaS landing page demo showing split hero with real product UI, counter reveal, bento grid, glass sticky nav

#### Project scaffolding
- `README.md` with badges, tags, buttons, contributor welcome
- `LICENSE` (MIT)
- `CONTRIBUTING.md` with PR checklist
- `CODE_OF_CONDUCT.md`
- `CHANGELOG.md`
- `.github/` with issue templates (bug, feature, discussion), PR template, FUNDING.yml, RELEASE.md
- `.gitignore`
- `PUSH-TO-GITHUB.md` push instructions

### 🔄 Changed

N/A — initial release.

### ⛔ Deprecated

N/A — initial release.

### 🗑️ Removed

N/A — initial release.

### 🐛 Fixed

N/A — initial release.

### 🔒 Security

N/A — initial release.

---

## Versioning commitment

Going forward, this project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0): Incompatible changes to `SKILL.md` schema or required output contract
- **MINOR** (1.Y.0): Backward-compatible additions — new guides, new data entries, new templates
- **PATCH** (1.0.Z): Backward-compatible fixes — broken links, corrected contrast ratios, typos

---

[1.0.0]: https://github.com/huzaifaa-dev-vibe/anti-generic-ai-design/releases/tag/v1.0.0
