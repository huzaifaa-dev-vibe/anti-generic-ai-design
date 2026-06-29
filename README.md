# Anti-Generic AI Design Skill

> **Stop shipping AI-coded pages that *look* AI-coded.**

A complete, framework-agnostic design skill for AI coding agents (Claude Code, Manus, Super Z, Cursor, Cline, etc.) that forces the agent to **think like a senior art director** before writing a single line of JSX.

Born from one observation: in the vibe-coding era, the bottleneck is no longer *can the AI build it* — it's *does the output look like every other LLM-generated site*. Bland indigo gradients. Default Inter. Centered hero with one H1, one subhead, two buttons. Glass cards with no depth. No reference research. No debate. No soul.

This skill fixes that.

---

## What's inside

```
ai-design-skill/
├── SKILL.md                  ← Main orchestrator (the AI loads this first)
├── guides/                   ← 21 deep guides, one per design dimension
│   ├── 01-thinking-redesign.md      (debate protocol — the soul of this skill)
│   ├── 02-color-palette-guide.md
│   ├── 03-font-pairing-guide.md
│   ├── 04-glassmorphism-guide.md
│   ├── 05-hero-section-guide.md     (top-class hero patterns)
│   ├── 06-advanced-css-components.md
│   ├── 07-seo-guide.md
│   ├── 08-llm-seo-guide.md          (AI Overviews / llms.txt / GEO)
│   ├── 09-animation-guide.md
│   ├── 10-reference-research.md
│   ├── 11-about-info-email-contact.md
│   ├── 12-spacing-layout-grid.md
│   ├── 13-microinteractions.md
│   ├── 14-accessibility-guide.md
│   ├── 15-performance-guide.md
│   ├── 16-dark-mode-guide.md
│   ├── 17-responsive-design.md
│   ├── 18-content-typography.md
│   ├── 19-imagery-iconography.md
│   ├── 20-conversion-principles.md
│   └── 21-checklist-launch.md
├── data/                     ← Curated reference datasets (100 entries each)
│   ├── websites-100.json            (100 reference sites by category)
│   ├── themes-100.json              (100 design themes)
│   ├── palettes-100.json            (100 color palettes + contrast)
│   ├── font-pairs-100.json          (100 font pairings + rationale)
│   └── animations-100.json          (100 animations + timing curves)
├── templates/                ← Drop-in React + TS + Tailwind components
│   ├── hero/                        (4 hero variants)
│   ├── components/                  (glass card, animated nav, gradient text, ...)
│   └── styles/                      (glassmorphism.css, animations.css)
└── examples/                 ← Standalone HTML demos
```

---

## How to use it

### Option A — Drop into your agent's project

Copy this entire folder into your repo (or symlink `SKILL.md` from your agent's skill loader). When the agent starts a frontend task, it reads `SKILL.md`, which orchestrates the rest.

### Option B — Paste as system prompt

Paste the contents of `SKILL.md` (plus the relevant `guides/*.md`) into your agent's system prompt or `CLAUDE.md` / `.cursorrules` / `manus.toml`.

### Option C — Use the data files directly

The `data/*.json` files are framework-agnostic. Import them in any design tool, Figma plugin, or code generator.

---

## The core idea

Most AI design fails because the agent **skips the thinking step**. It jumps from "build a landing page" straight to `<div className="max-w-7xl mx-auto text-center">`.

This skill inserts a **mandatory debate + research phase** before any code is written:

1. **Research** — pull 3+ reference sites from `data/websites-100.json` matching the project category.
2. **Debate** — for every design decision (palette, font, hero layout, animation), the agent must argue *for* and *against* its choice, then defend or revise.
3. **Justify** — every shipped element must trace back to a cited reference or a stated principle.
4. **Build** — only then does code start. And the code uses templates from `templates/`, not generic divs.

---

## What makes a hero "top-class"

See `guides/05-hero-section-guide.md` for the full treatment. Short version: a top-class hero has

- **One unmistakable focal point** (headline or product visual, never both competing)
- **A clear visual hierarchy** — H1, subhead, primary CTA, secondary CTA in that order
- **Motion with intent** — every animation reveals information, never decorates
- **A real product moment** — show the actual product, not a stock illustration
- **Proof within the fold** — logo strip, single stat, or one testimonial
- **No more than 7 elements** above the fold

---

## Contributing

PRs welcome. The data files are the easiest place to contribute — add a palette, a font pair, a reference site. See `CONTRIBUTING.md`.

## License

MIT — see `LICENSE`.

---

**Built to kill the "AI look". One debate at a time.**
