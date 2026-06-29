# Contributing

Thanks for helping kill the "AI look". This repo accepts three kinds of contributions.

## 1. Data additions (easiest, highest impact)

Add entries to the JSON files in `data/`. Each file has a documented schema — read the first 30 lines before adding.

- `data/websites-100.json` — add a real, well-designed website with a one-paragraph design note
- `data/themes-100.json` — add a named theme (e.g. "Editorial dark") with palette + type + texture
- `data/palettes-100.json` — add a palette with 5 swatches, contrast ratios, and use-cases
- `data/font-pairs-100.json` — add a heading+body+numeric+mono pairing with rationale
- `data/animations-100.json` — add an animation with timing curve, duration, and when-to-use rule

**Rules:**
- No duplicates. Search before adding.
- Every entry must have a real `rationale` or `use_cases` field — no empty strings.
- Fonts must be freely loadable (Google Fonts / Fontsource / OFL-licensed self-host).
- Palettes must pass WCAG AA for body text (4.5:1 minimum).
- Websites must be live (no dead links) and genuinely well-designed (no Templatemonster defaults).

## 2. Guide improvements

The `guides/*.md` files are opinionated on purpose. If you disagree with a rule, open an issue first — don't just rewrite the guide. PRs that add new sub-sections, examples, or fallback patterns are welcome.

## 3. New templates

Templates live in `templates/` and must be:
- React + TypeScript + Tailwind (no styled-components, no CSS-in-JS)
- Self-contained (one file per component, no external imports beyond react + lucide-react)
- Accessible (semantic HTML, focus states, reduced-motion variant)
- Use the project's CSS variable conventions (see `templates/styles/`)

## PR checklist

- [ ] No duplicate entries
- [ ] All JSON validates (`npx json5 data/*.json` or `python -m json.tool`)
- [ ] No proprietary fonts, palettes, or images
- [ ] If adding a website, the link is live and the design note is specific
- [ ] If adding a palette, contrast ratios are accurate (use WebAIM or Stark)

## Code of conduct

Be excellent to each other. Design opinions are welcome; personal attacks are not.
