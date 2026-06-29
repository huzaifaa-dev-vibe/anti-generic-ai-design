# 16 — Dark Mode Guide

> Dark mode is not light mode inverted. It is a separate palette with its own rules, its own contrast math, its own emotional register. AI-coded sites take a light theme, swap `--bg` to `#000000`, leave `--text` at `#FFFFFF`, and call it done. The result is a page that burns the retina, has no depth, and looks like a terminal from 1995. This guide is how senior designers actually build dark mode.

## Why AI fails at dark mode

Six defaults ruin AI dark mode:

1. **Pure black background.** `#000000` against pure white text is 21:1 contrast — too harsh. Real dark mode uses `#0A0A0B` or `#0E0E10` — near-black with a hint of warmth or cool.
2. **Pure white text.** `#FFFFFF` glows on dark. Use `#E4E4E7` or `#F4F4F5` — off-white that reads as "white" but doesn't burn.
3. **Inverted surfaces.** Light mode: surface is white, bg is gray. Dark mode: surface should be **lighter** than bg (e.g. `#18181B` on `#0A0A0B`), not darker. AI inverts it the wrong way.
4. **Shadows that do nothing.** Drop shadows are invisible on dark backgrounds. Use 1px borders with low-opacity white instead.
5. **Same accent color.** The accent that works on white (saturated, mid-tone) doesn't work on black. Saturated colors glow aggressively on dark. Desaturate, brighten, or pick a different accent for dark mode.
6. **No toggle.** Hard-coded to one theme. Users who set `prefers-color-scheme: dark` get the wrong theme; users who want to switch can't.

Dark mode is a design problem, not a CSS inversion.

---

## Rule 1 — Dark mode has its own palette

Don't invert the light palette. Design a second palette from scratch, tuned for the physics of dark backgrounds.

```css
:root {
  /* Light theme */
  --bg: #FAFAFA;
  --surface: #FFFFFF;
  --surface-hover: #F4F4F5;
  --text: #18181B;
  --text-muted: #52525B;
  --border: rgba(24, 24, 27, 0.08);
  --accent: #B45309;          /* amber-700 */
  --accent-strong: #92400E;
  --accent-soft: #FDE68A;
}

:root[data-theme="dark"] {
  /* Dark theme — designed, not inverted */
  --bg: #0A0A0B;              /* near-black, slight cool */
  --surface: #18181B;         /* LIGHTER than bg, not darker */
  --surface-hover: #27272A;
  --text: #E4E4E7;            /* off-white, not pure white */
  --text-muted: #A1A1AA;
  --border: rgba(255, 255, 255, 0.08);
  --accent: #F59E0B;          /* brighter amber — was #B45309 */
  --accent-strong: #FBBF24;
  --accent-soft: rgba(245, 158, 11, 0.15);
}
```

Notice the moves:
- `--bg` went from `#FAFAFA` to `#0A0A0B` (not `#000000`).
- `--surface` is `#18181B` — **lighter** than `--bg`. Elevated surfaces get lighter, not darker. This mimics how light hits raised objects.
- `--text` went from `#18181B` to `#E4E4E7` (not `#FFFFFF`).
- `--accent` brightened from `#B45309` to `#F59E0B` — the same hue family, but the dark-mode version needs more luminance to read against the dark bg.

## Rule 2 — Surfaces get lighter, not darker

In light mode, a raised card is **white** on a **gray** bg — the card is lighter.

In dark mode, a raised card should be **lighter than the bg** — e.g. `#18181B` on `#0A0A0B`. This is counterintuitive but correct: light hits raised objects from above, so raised surfaces catch more light (appear lighter), even in dark mode.

```css
/* Surface elevation in dark mode */
--bg: #0A0A0B;          /* page background — darkest */
--surface: #18181B;     /* card — one step lighter */
--surface-2: #27272A;   /* card on card — two steps lighter */
--surface-3: #3F3F46;   /* modal, popover — three steps lighter */
```

**Apple's macOS dark mode** does exactly this: windows are `#1E1E1E`, sidebars are `#2A2A2C`, popovers are `#3A3A3C`. Each elevation step is one notch lighter.

## Rule 3 — Text colors: never pure white

Pure white (`#FFFFFF`) on dark backgrounds has a glow effect — the text appears to bleed outward. Use off-white instead.

| Element | Light mode | Dark mode |
|---------|-----------|-----------|
| Body text | `#18181B` (near-black) | `#E4E4E7` (near-white) |
| Muted text | `#52525B` | `#A1A1AA` |
| Disabled text | `#A1A1AA` | `#52525B` |
| Headings | `#000000` or `#18181B` | `#FAFAFA` or `#F4F4F5` |

Verify contrast: `#E4E4E7` on `#0A0A0B` is 14.5:1 — passes AAA. `#FFFFFF` on `#0A0A0B` is 19.3:1 — too much, harsh on the eyes.

## Rule 4 — Desaturate accents for dark mode

A saturated accent that looks great on white becomes radioactive on black. The same orange (`#F97316`) on white reads as "energetic"; on black, it reads as "warning". Two adjustments:

1. **Reduce saturation** by 10–20%.
2. **Increase luminance** so the color "lifts" off the dark bg.

```css
:root {
  --accent: #B45309;          /* light mode: amber-700 */
}

:root[data-theme="dark"] {
  --accent: #FBBF24;          /* dark mode: amber-400 — brighter, slightly less saturated */
}
```

| Light mode accent | Dark mode accent | Notes |
|-------------------|------------------|-------|
| `#B45309` (amber-700) | `#FBBF24` (amber-400) | +2 steps brighter |
| `#15803D` (green-700) | `#4ADE80` (green-400) | +2 steps brighter |
| `#1D4ED8` (blue-700) | `#60A5FA` (blue-400) | +2 steps brighter |
| `#BE185D` (pink-700) | `#F472B6` (pink-400) | +2 steps brighter |

The general rule: shift the accent 2–3 steps brighter in the same hue family. This keeps the brand recognizable while preventing the "glow" effect.

## Rule 5 — Shadows don't work. Use borders.

On light bg, a drop shadow (`0 4px 12px rgba(0,0,0,0.1)`) separates a card from the page. On dark bg, the same shadow is invisible — `rgba(0,0,0,0.1)` on `#0A0A0B` is imperceptible.

**Replace shadows with subtle borders** in dark mode:

```css
.card {
  /* Light mode */
  background: var(--surface);
  border: 1px solid var(--border);          /* subtle */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

:root[data-theme="dark"] .card {
  background: var(--surface);
  border: 1px solid var(--border);          /* rgba(255,255,255,0.08) — visible on dark */
  box-shadow: none;                          /* shadows don't work in dark mode */
}
```

For "elevated" surfaces (modals, popovers), combine a lighter bg with a stronger border:

```css
.modal {
  background: var(--surface-2);
  border: 1px solid rgba(255, 255, 255, 0.12);
}
```

If you must use a shadow in dark mode, use a **larger, darker** shadow that creates a "vignette" rather than a drop:

```css
.modal-dark {
  box-shadow:
    0 0 0 1px rgba(255, 255, 255, 0.06),
    0 24px 48px rgba(0, 0, 0, 0.6),
    0 8px 16px rgba(0, 0, 0, 0.4);
}
```

## Rule 6 — Glow effects: use sparingly, deliberately

A glow is the dark-mode equivalent of a soft shadow. Used on accent elements (active nav, focused buttons, primary CTAs), it creates depth. Used everywhere, it looks like a 2018 crypto site.

```css
.btn-primary-dark {
  background: var(--accent);
  color: var(--bg);
  box-shadow:
    0 0 0 1px rgba(245, 158, 11, 0.4),
    0 4px 16px rgba(245, 158, 11, 0.2);
}

.btn-primary-dark:hover {
  box-shadow:
    0 0 0 1px rgba(245, 158, 11, 0.6),
    0 6px 24px rgba(245, 158, 11, 0.35);
}
```

**Glow rules**:
- One glow per element. Not three.
- Glows only on accent-colored elements. A neutral button should never glow.
- Glow opacity ≤ 0.35. Higher = "neon sign".
- Never glow text. It causes haloing.

## Rule 7 — Semantic colors need dark-mode variants

The success/warning/error/info colors need their own dark-mode versions, following the same rules as accents: brighter, slightly less saturated.

```css
:root {
  --success: #15803D;
  --warning: #B45309;
  --error: #B91C1C;
  --info: #1D4ED8;
}

:root[data-theme="dark"] {
  --success: #4ADE80;     /* green-400 */
  --warning: #FBBF24;     /* amber-400 */
  --error: #F87171;       /* red-400 */
  --info: #60A5FA;        /* blue-400 */
}
```

## Rule 8 — Images and illustrations need dark-mode variants

A screenshot of a light-themed product UI, on a dark page, is a jarring white rectangle. Two options:

1. **Provide a dark-mode version** of the image (a screenshot of the dark-themed product UI).
2. **Wrap the image in a "browser chrome" frame** so the white rectangle looks intentional.

```tsx
<div className="screenshot-frame">
  <img
    src={isDark ? '/dashboard-dark.png' : '/dashboard-light.png'}
    alt="Product dashboard"
  />
</div>
```

For illustrations (custom SVG), use `currentColor` for strokes so they adapt:

```svg
<svg viewBox="0 0 24 24" stroke="currentColor" fill="none">
  <path d="..." />
</svg>
```

## Rule 9 — Implement `prefers-color-scheme` + manual toggle

Three states: system, light, dark. The toggle cycles between them.

```tsx
type Theme = 'system' | 'light' | 'dark';

function useTheme() {
  const [theme, setTheme] = useState<Theme>(
    () => (localStorage.getItem('theme') as Theme) || 'system'
  );

  useEffect(() => {
    const root = document.documentElement;
    const systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const resolved = theme === 'system' ? (systemDark ? 'dark' : 'light') : theme;

    root.setAttribute('data-theme', resolved);
    root.style.colorScheme = resolved;
    localStorage.setItem('theme', theme);
  }, [theme]);

  return { theme, setTheme };
}
```

### Prevent FOUC (flash of unstyled content)

The theme must be set before React hydrates, or users see the wrong theme flash. Inline script in `<head>`:

```html
<script>
  (function() {
    const stored = localStorage.getItem('theme');
    const system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    const resolved = stored === 'system' || !stored ? system : stored;
    document.documentElement.setAttribute('data-theme', resolved);
    document.documentElement.style.colorScheme = resolved;
  })();
</script>
```

## Rule 10 — Toggle UX: 3-position, not 2

The toggle cycles `system → light → dark → system`. Three positions, not two, because users want:
- "Follow my OS preference" (system)
- "Always light"
- "Always dark"

```tsx
function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  return (
    <button
      onClick={() => {
        const next = theme === 'system' ? 'light' : theme === 'light' ? 'dark' : 'system';
        setTheme(next);
      }}
      aria-label={`Theme: ${theme}. Click to change.`}
      className="theme-toggle"
    >
      {theme === 'system' && <MonitorIcon aria-hidden />}
      {theme === 'light'  && <SunIcon aria-hidden />}
      {theme === 'dark'   && <MoonIcon aria-hidden />}
    </button>
  );
}
```

### Toggle placement

- Top-right of the nav (most common, expected).
- In a settings page (for apps).
- In the footer (for content sites — less prominent).

## Rule 11 — Test in both themes, every time

A design that works in light mode and breaks in dark mode is not done. Test every component, every state, every page in both themes.

Common dark-mode bugs:
- White images in dark sections (provide dark variants).
- Low-contrast text (e.g. gray-400 muted text that's fine on white but invisible on `#0A0A0B`).
- Box shadows that disappear.
- Borders that disappear (use `rgba(255,255,255,0.08)`, not `rgba(0,0,0,0.08)`).
- Form autofill that turns inputs bright yellow (override with `-webkit-autofill`).
- SVGs with hardcoded fills (use `currentColor`).
- Code blocks with light syntax highlighting (use a dark theme like Night Owl or Dracula).

```css
/* Form autofill fix for dark mode */
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  -webkit-text-fill-color: var(--text);
  -webkit-box-shadow: 0 0 0 1000px var(--surface) inset;
  caret-color: var(--text);
}
```

## Rule 12 — The dark-mode token system

```css
:root {
  /* Color roles (semantic — same name in both themes) */
  --bg: ...;
  --surface: ...;
  --surface-hover: ...;
  --surface-2: ...;
  --text: ...;
  --text-muted: ...;
  --text-disabled: ...;
  --border: ...;
  --border-strong: ...;
  --accent: ...;
  --accent-strong: ...;
  --accent-soft: ...;
  --success: ...;
  --warning: ...;
  --error: ...;
  --info: ...;

  /* Effects */
  --shadow-card: ...;
  --shadow-modal: ...;
  --glow-accent: ...;
}

/* Light theme values */
:root,
:root[data-theme="light"] {
  --bg: #FAFAFA;
  --surface: #FFFFFF;
  --surface-hover: #F4F4F5;
  --surface-2: #FAFAFA;
  --text: #18181B;
  --text-muted: #52525B;
  --text-disabled: #A1A1AA;
  --border: rgba(24, 24, 27, 0.08);
  --border-strong: rgba(24, 24, 27, 0.16);
  --accent: #B45309;
  --accent-strong: #92400E;
  --accent-soft: #FDE68A;
  --success: #15803D;
  --warning: #B45309;
  --error: #B91C1C;
  --info: #1D4ED8;
  --shadow-card: 0 1px 2px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.06);
  --shadow-modal: 0 24px 48px rgba(0,0,0,0.12), 0 8px 16px rgba(0,0,0,0.08);
  --glow-accent: none;
}

/* Dark theme values */
:root[data-theme="dark"] {
  --bg: #0A0A0B;
  --surface: #18181B;
  --surface-hover: #27272A;
  --surface-2: #27272A;
  --text: #E4E4E7;
  --text-muted: #A1A1AA;
  --text-disabled: #52525B;
  --border: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(255, 255, 255, 0.16);
  --accent: #FBBF24;
  --accent-strong: #FCD34D;
  --accent-soft: rgba(251, 191, 36, 0.15);
  --success: #4ADE80;
  --warning: #FBBF24;
  --error: #F87171;
  --info: #60A5FA;
  --shadow-card: 0 0 0 1px rgba(255,255,255,0.06);
  --shadow-modal: 0 0 0 1px rgba(255,255,255,0.1), 0 24px 48px rgba(0,0,0,0.5);
  --glow-accent: 0 0 24px rgba(251, 191, 36, 0.2);
}

/* System preference (when no manual override) */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    /* dark theme values */
  }
}
```

## Anti-Patterns (Auto-Fail)

1. **Pure black `#000000` background.** Use near-black.
2. **Pure white `#FFFFFF` text.** Use off-white.
3. **Surfaces darker than bg.** They should be lighter.
4. **Same accent in both themes.** Tune for dark.
5. **Drop shadows as the only depth cue.** They're invisible. Use borders.
6. **Hardcoded `#fff` or `#000` in components.** Use tokens.
7. **No `prefers-color-scheme` support.** Users who set it get the wrong theme.
8. **No toggle.** Users can't override.
9. **FOUC on load** — the wrong theme flashes before JS runs. Inline script in `<head>`.
10. **SVG icons with hardcoded fill colors.** Use `currentColor`.
11. **White screenshots on dark pages.** Provide dark variants or frame them.
12. **Glow on every accent.** One glow, used sparingly.
13. **Color-scheme not set** — `color-scheme: dark` on the root so native form controls render dark.

## Code Example — Theme Toggle with No FOUC

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <script>
    (function() {
      try {
        const stored = localStorage.getItem('theme') || 'system';
        const system = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        const resolved = stored === 'system' ? system : stored;
        document.documentElement.setAttribute('data-theme', resolved);
        document.documentElement.style.colorScheme = resolved;
      } catch (e) {
        document.documentElement.style.colorScheme = 'light';
      }
    })();
  </script>
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
  <button class="theme-toggle" aria-label="Toggle theme">
    <svg class="icon-sun" aria-hidden="true"><!-- ... --></svg>
    <svg class="icon-moon" aria-hidden="true"><!-- ... --></svg>
  </button>
</body>
</html>
```

## Output

When you finish this guide, you should have:
- Two complete theme palettes (light + dark) as CSS variables with the same token names
- `data-theme` attribute on `<html>` switched by inline script before hydration (no FOUC)
- A 3-position theme toggle (system / light / dark) with the choice persisted in `localStorage`
- `prefers-color-scheme: dark` honored when no manual choice is set
- All surfaces lighter than the bg in dark mode (not darker)
- All text in off-white (`#E4E4E7` family), not pure white
- All accents brightened 2–3 steps for dark mode
- Shadows replaced with 1px borders in dark mode
- One glow effect on the primary CTA in dark mode (maximum)
- All SVG icons using `currentColor`
- All images with dark-mode variants or wrapped in a "browser frame"
- Lighthouse test passed in both themes
