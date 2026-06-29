# 01 — Thinking & Redesign: The Debate Protocol

> This is the soul of the skill. If you skip this, you ship generic work. Period.

## Why this guide exists

Every senior designer you've ever worked with does something AI coding agents don't: they **argue with themselves** before committing to a design. They sketch three directions, hate two of them, defend the third to a colleague, lose the argument, and emerge with a fourth direction that's actually right.

AI agents skip this. They go from "build a landing page" to `<div className="max-w-7xl mx-auto">` in 200ms. That's why every AI site looks the same.

This guide inserts the missing argument.

---

## The 4-Phase Protocol

### Phase 1 — Research (5–10 minutes of agent time)

**Do not write code yet.** Open these data files and read them:

1. `data/websites-100.json` — filter by `category` matching the project. Pick **3 references**. For each, read the `design_notes` field. Write down one thing you'll borrow (layout, palette, motion, copy structure) and one thing you'll explicitly **not** borrow (so you don't copy blindly).

2. `data/themes-100.json` — pick **3 themes** whose `voice` field matches the project. Don't commit yet; you'll debate in Phase 2.

3. `data/palettes-100.json` — pick **3 palettes**. For each, check `contrast_ratios.body_on_bg`. Reject any below 4.5:1. Reject any whose `vibe` is "AI default" (indigo→violet→pink).

4. `data/font-pairs-100.json` — pick **3 pairings**. Verify the fonts are loadable (Google Fonts / Fontsource). Note the `best_for` field — does it match your project type?

5. `data/animations-100.json` — bookmark **5–8 animations** matching the project's energy. Note which are "ambient" (always running) vs "triggered" (on scroll / hover / interaction).

**Output of Phase 1**: a shortlist document. Nothing is committed yet.

### Phase 2 — Debate (the critical phase)

For each of the 7 decisions below, write a 3-block argument:

```
DECISION: [topic]
CHOICE:   [what you picked]
FOR:      [why it's right — cite a reference, a principle, or a data point]
AGAINST:  [the strongest counter-argument an actual senior designer would make]
REBUTTAL: [why the counter doesn't kill your choice, OR admit defeat and pick again]
```

#### The 7 mandatory debates

1. **Hero layout** — Split / Centered / Asymmetric / Video-bg / 3D / Product-first / Editorial
   - Default AI choice: Centered. **Banned unless you can defend it.**
   - Strong defaults: Split (text left, product right) for SaaS; Asymmetric for portfolios; Product-first for dev tools.

2. **Primary color**
   - Default AI choice: indigo/violet/pink gradient. **Banned.**
   - Pick a real brand color with a reason. "We chose deep teal (#0E5C5A) because the audience is healthcare-adjacent and teal reads clinical without being sterile."

3. **Type pairing**
   - Default AI choice: Inter for everything. **Banned.**
   - Pick a display face for headings + a body face. Numeric + mono only if the project needs them (dashboards, data-heavy sites).

4. **Visual texture**
   - Default AI choice: flat + subtle Tailwind shadow. **Banned as default.**
   - Choose: flat / glass / grain / gradient mesh / brutalist / paper / duotone photography. Commit to one texture language across the site.

5. **Motion energy**
   - Default AI choice: fade-in-up on every section. **Banned.**
   - Pick a budget: calm (1–2 animations, page-load only) / measured (3–5, including scroll-triggered) / energetic (6–10, with hover micro-interactions) / cinematic (10+, with hero choreography).

6. **Content density**
   - Default AI choice: balanced. **Not always right.**
   - Editorial sites need sparse. Dashboards need dense. Marketing pages need balanced with one dense proof section. Don't default — match the audience.

7. **Dark or light default**
   - Default AI choice: light. **Banned as default.**
   - Pick based on audience and content type: dev tools → dark; reading-heavy → light; luxury → dark; data-dense → light or toggle; creative portfolio → either, but commit.

### Phase 3 — Justify (the design rationale document)

Write `DESIGN-RATIONALE.md` containing:

```markdown
# Design Rationale — [Project Name]

## Brief
- Category: [SaaS / portfolio / ...]
- Audience: [who they are, what they care about]
- Primary goal: [sign up / contact / read / buy]

## References (3 minimum)
1. [Site name] — [URL]
   - Borrow: [specific element]
   - Avoid: [specific element]
2. ...

## Final palette
| Role | Hex | Use |
|------|-----|-----|
| bg | #... | page background |
| surface | #... | cards, panels |
| text | #... | body copy |
| accent | #... | CTAs, links |
| muted | #... | secondary text |

Contrast: body-on-bg = X:1 (passes WCAG AA)

## Final type
- Headings: [Family] [Weights] — load via [Google/Fontsource]
- Body: [Family] [Weights]
- Numeric: [Family] (if applicable)
- Mono: [Family] (if applicable)

## Final hero
- Layout: [split / asymmetric / ...]
- Focal point: [headline / product / video / ...]
- Motion: [what animates, why]
- Proof element: [stat / logo / testimonial]

## Motion budget
- Ambient: [list]
- Triggered: [list]
- Total: N animations (matches "measured" budget)

## Debate log
[The 7 debate blocks from Phase 2]
```

### Phase 4 — Build

Only now do you write code. Use `templates/` as the starting point.

---

## The "Steel-Man" Rule

When writing the **AGAINST** block, you must argue against yourself **as strongly as a hostile senior designer would**. Vague objections like "it might look generic" don't count. Specific objections like "split-hero with a product screenshot on the right is overused in B2B SaaS — Linear, Vercel, and Resend all do it, and a 4th copy makes you invisible" count.

If your AGAINST block makes you uncomfortable, it's strong enough.

## The "Three-Option" Rule

For each of the 7 decisions, you must have considered **at least 3 options** before picking one. If you only considered one (the default), you didn't decide — you defaulted. Defaults are what make AI work look like AI work.

## The "Reference-Or-Principle" Rule

Every FOR block must contain **either**:
- A cited reference (a site in `data/websites-100.json` that does this and works), OR
- A named design principle (Fitts's Law, Hicks Law, visual hierarchy, proximity, contrast, etc.)

"I think it looks nice" is not a justification.

## When the User Pushes Back

If the user says "I don't like it" but can't articulate why, **do not just try another palette**. Ask:

1. "Which of the 3 reference sites feels closest to what you want? What about it works?"
2. "Is the objection to color, layout, density, or motion? Pick one."
3. "Show me one website you love. I'll reverse-engineer why it works and apply that."

Vague feedback means the user can't see your design rationale. Show them `DESIGN-RATIONALE.md` and ask them to debate specific blocks.

## Anti-Pattern: "Trust Me" Design

Never say "trust me, this works" without a rationale. If you can't explain it in `DESIGN-RATIONALE.md`, you don't understand it. Ship nothing you can't defend.

## Anti-Pattern: Decision Fatigue

If you find yourself debating the 8th, 9th, 10th decision, stop. The 7 mandatory debates are enough. Other decisions (button radius, icon set, copy tone) follow from those 7. Don't re-debate everything.

## Output

At the end of Phase 3, you should have:
- `DESIGN-RATIONALE.md` (the document)
- A shortlist of palette + fonts + hero pattern + motion budget, committed

At the end of Phase 4, you should have:
- Code that uses `templates/` as scaffolding
- Every design decision traceable to a block in `DESIGN-RATIONALE.md`
- No anti-patterns from `SKILL.md` present in the output
