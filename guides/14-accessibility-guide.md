# 14 — Accessibility Guide

> Accessibility is not a feature. It is the baseline. A page that excludes 15% of users — the global average for people with disabilities — is a broken page. AI-coded sites ship `aria-label` on every div, `outline: none` on every focusable element, and headings that skip from H1 to H4 because "it looks bigger". This guide is the gate every page must pass.

## Why AI fails at accessibility

Five defaults ruin AI accessibility:

1. **`<div>` everywhere.** LLMs build buttons out of `<div onClick>`, navs out of nested `<div>`s, forms out of `<div>` with no `<label>`. The DOM has no semantics, so screen readers announce "group, group, group, group".
2. **`aria-label` as a substitute for proper content.** ARIA on a `<div>` does not make it a button. Use a `<button>`. ARIA is for when semantics can't be expressed in HTML — which is rarer than LLMs think.
3. **`outline: none` everywhere.** The default browser focus ring is removed for "aesthetics" and never replaced. Keyboard users cannot navigate.
4. **Headings used for size, not hierarchy.** H1, then H4, then H2, then H3 — chosen because of font size, not document structure. Screen reader users navigate by heading tree and get lost.
5. **Color as the only signal.** Error states that are only red. Required fields that are only a red asterisk. Links distinguished only by color. Colorblind users (8% of men) get nothing.

Accessibility is not hard. It is discipline. The rules below are the discipline.

---

## Rule 1 — Use semantic HTML, always

The element is the semantics. Don't build a button from a div. Don't build a list from divs. Don't build a form from divs.

| Wrong | Right | Why |
|-------|-------|-----|
| `<div onClick>` | `<button onClick>` | Button gets keyboard focus, Enter/Space activation, screen reader role for free |
| `<div role="heading">` | `<h1>` – `<h6>` | Native heading, navigable by screen readers |
| `<div class="list">` | `<ul>` / `<ol>` + `<li>` | Native list semantics |
| `<div class="input">` | `<input>` with `<label>` | Form semantics, label association, validation |
| `<div class="link">` | `<a href>` | Native link, middle-click, keyboard focus |
| `<div class="nav">` | `<nav>` | Landmark role for screen readers |

```tsx
// ❌ AI default
<div className="nav">
  <div className="nav-item" onClick={goHome}>Home</div>
  <div className="nav-item" onClick={goAbout}>About</div>
</div>

// ✅ Semantic
<nav aria-label="Main">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>
```

## Rule 2 — ARIA: when to use, when not to

The first rule of ARIA, from the W3C: **No ARIA is better than bad ARIA.**

ARIA is for cases where HTML can't express the semantics:
- A tablist (no native equivalent)
- A combobox / autocomplete (no native equivalent)
- A live region that announces updates (`aria-live`)
- A custom widget (accordion, tree, menu — though check if a native disclosure or `<details>` works first)

**Don't use ARIA when**:
- A native element exists (`<button>` not `<div role="button">`).
- You're "improving" an element that's already accessible (`aria-label` on a `<button>` with visible text — redundant and sometimes conflicts).
- You're adding `role="presentation"` to a meaningful element.

```tsx
// ❌ ARIA on top of native semantics (redundant, sometimes harmful)
<button role="button" aria-label="Save">Save</button>

// ✅ Native semantics, no ARIA needed
<button>Save</button>

// ✅ ARIA where HTML has no equivalent
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">Overview</button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2">Details</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">...</div>
```

## Rule 3 — Headings form a document outline

Headings are the table of contents for screen reader users. They must form a logical outline:

- Exactly **one `<h1>`** per page (the page title).
- Each subsequent heading is either the same level as the previous, or one level deeper.
- **Never skip levels**: H1 → H2 → H3, never H1 → H4.
- Use CSS to control visual size, not heading tags. An H3 that visually looks like an H2 is still an H3 semantically.

```tsx
// ❌ Skipping levels for visual reasons
<h1>Blog</h1>
<h4>Latest posts</h4>  {/* skipped H2, H3 */}
<h5>How to design</h5>

// ✅ Correct hierarchy
<h1>Blog</h1>
<h2>Latest posts</h2>
<h3>How to design accessible interfaces</h3>
```

## Rule 4 — Color contrast: the non-negotiable numbers

WCAG 2.2 AA contrast ratios:

| Element | Minimum | Ideal |
|---------|---------|-------|
| Body text (<24px regular, <18.66px bold) | 4.5:1 | 7:1 |
| Large text (≥24px regular, ≥18.66px bold) | 3:1 | 4.5:1 |
| UI components (button borders, icon strokes, focus rings) | 3:1 | 4.5:1 |
| Non-text contrast (form field borders, chart line vs bg) | 3:1 | 4.5:1 |

**Verify every pair.** Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) or the browser DevTools contrast inspector. The `contrast_ratios` field in `data/palettes-100.json` is pre-computed.

```css
/* These pass AA */
--text-on-bg: #18181B;       /* 16.4:1 on #FAFAFA */
--muted-on-bg: #52525B;      /* 7.2:1 on #FAFAFA */
--accent-on-white: #B45309;  /* 5.4:1 — passes AA, used for links */

/* These fail AA */
--muted-on-bg: #A1A1AA;      /* 2.8:1 on #FAFAFA — fails */
--accent-on-white: #FCD34D;  /* 1.5:1 — fails even for large text */
```

**The "muted text" trap**: gray-400 (`#9CA3AF`) on white is 2.6:1 — fails AA. Gray-500 (`#6B7280`) on white is 4.6:1 — passes. AI ships gray-400 for "secondary text" everywhere. Use gray-500 minimum.

## Rule 5 — Keyboard navigation: every interaction reachable

Every interactive element must be operable from the keyboard, in logical order, with no keyboard traps.

**Tab order**: follows the visual reading order (top-to-bottom, left-to-right in LTR). Don't fight this with `tabindex` hacks.

**`tabindex` rules**:
- `tabindex="0"` — element is focusable in DOM order (rarely needed; native elements already are).
- `tabindex="-1"` — element is focusable programmatically (for skip links, modal focus management).
- `tabindex="1"` or higher — **never**. It breaks natural tab order.

**Keyboard shortcuts for every widget**:
- Buttons: Enter + Space
- Links: Enter
- Checkboxes: Space
- Radio buttons: Arrow keys
- Tabs: Arrow keys (Left/Right), Home, End
- Modals: Esc to close, focus trapped inside
- Menus: Arrow keys, Esc to close

```tsx
// Focus trap in a modal
function Modal({ open, onClose, children }) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return;
    const dialog = ref.current;
    const focusable = dialog?.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const first = focusable?.[0] as HTMLElement;
    const last = focusable?.[focusable.length - 1] as HTMLElement;
    first?.focus();

    function handleKey(e: KeyboardEvent) {
      if (e.key === 'Escape') onClose();
      if (e.key === 'Tab') {
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last?.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first?.focus();
        }
      }
    }
    document.addEventListener('keydown', handleKey);
    return () => document.removeEventListener('keydown', handleKey);
  }, [open, onClose]);

  if (!open) return null;
  return (
    <div className="modal-overlay" onClick={onClose}>
      <div ref={ref} role="dialog" aria-modal="true" className="modal" onClick={e => e.stopPropagation()}>
        {children}
      </div>
    </div>
  );
}
```

## Rule 6 — Skip links: the first focusable element

A "Skip to content" link at the top of the page lets keyboard users bypass the nav.

```tsx
<a href="#main" className="skip-link">Skip to main content</a>
<nav>...</nav>
<main id="main">...</main>
```

```css
.skip-link {
  position: absolute;
  top: -100px;
  left: 0;
  background: var(--accent);
  color: white;
  padding: var(--space-3) var(--space-4);
  z-index: 1000;
  transition: top 150ms ease;
}

.skip-link:focus {
  top: 0;
}
```

## Rule 7 — Focus management: visible focus, programmatic focus

**Every focusable element has a visible focus indicator.** Minimum: 2px outline with 3:1 contrast against the adjacent background.

```css
/* Global focus style — never remove */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* If you must remove the default outline, replace it */
button:focus { outline: none; }
button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

**Programmatic focus**: when content changes (route change, modal open, toast appears), move focus to the new content. Otherwise keyboard users are stuck on the previous element.

```tsx
useEffect(() => {
  if (routeChanged) {
    mainRef.current?.focus();
  }
}, [routeChanged]);

<main ref={mainRef} tabIndex={-1}>...</main>
```

## Rule 8 — Forms: label everything, associate errors

Every form control has a `<label>` associated via `for`/`id`. Errors are associated via `aria-describedby` and announced via `role="alert"`.

```tsx
<div className="field">
  <label htmlFor="email" className="required">
    Email
  </label>
  <input
    id="email"
    type="email"
    name="email"
    required
    aria-required="true"
    aria-invalid={!!errors.email}
    aria-describedby={errors.email ? 'email-error' : 'email-hint'}
  />
  {!errors.email && (
    <p id="email-hint" className="hint">We'll never share your email.</p>
  )}
  {errors.email && (
    <p id="email-error" role="alert" className="error">
      Please enter a valid email address.
    </p>
  )}
</div>
```

**Required field indicators**: don't rely on a red asterisk alone. Use `aria-required="true"` and a visually-hidden "(required)" text.

## Rule 9 — Accessible names for icons and buttons

Every interactive element has an accessible name. For icon-only buttons, the name comes from `aria-label` (or visually-hidden text).

```tsx
// ❌ Icon-only button with no name
<button onClick={close}><XIcon /></button>

// ✅ With aria-label
<button onClick={close} aria-label="Close dialog">
  <XIcon aria-hidden="true" />
</button>

// ✅ With visually-hidden text (preferred — translates better)
<button onClick={close}>
  <XIcon aria-hidden="true" />
  <span className="sr-only">Close dialog</span>
</button>
```

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

**Decorative icons** (purely visual) get `aria-hidden="true"` so screen readers skip them. **Meaningful icons** (the only content) need an accessible name.

## Rule 10 — Live regions for dynamic content

When content updates dynamically (toasts, search results, live scores), use `aria-live` so screen readers announce the update.

| Region | Use case | Interruption |
|--------|----------|--------------|
| `aria-live="polite"` | Toasts, status updates | Announces when user is idle |
| `aria-live="assertive"` | Critical errors | Announces immediately, interrupts |
| `role="alert"` | Form errors | Same as assertive, but a stronger signal |

```tsx
<div aria-live="polite" aria-atomic="true" className="sr-only">
  {toastMessage}
</div>
```

## Rule 11 — Respect user preferences

```css
/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Color scheme */
@media (prefers-color-scheme: dark) {
  :root {
    /* dark theme tokens — see guide 16 */
  }
}

/* High contrast (Windows) */
@media (prefers-contrast: more) {
  :root {
    --border: rgba(0, 0, 0, 1);
    --text: #000000;
  }
}

/* Forced colors (Windows high-contrast mode) */
@media (forced-colors: active) {
  .icon {
    /* Use system colors */
    color: ButtonText;
  }
}
```

## Rule 12 — Screen reader testing: actually do it

Run a screen reader on your page. At minimum:

- **VoiceOver** (macOS, free): Cmd+F5 to toggle. Use Cmd+Option+Arrow keys to navigate.
- **NVDA** (Windows, free): Download from nvaccess.org. Use Caps Lock + Arrow keys.
- **TalkBack** (Android): Settings → Accessibility → TalkBack.

Test for:
- The page announces in logical order.
- Headings are navigable (Caps Lock + H in NVDA, Ctrl+Option+Cmd+H in VoiceOver).
- Every interactive element has a meaningful name.
- Form errors are announced.
- Live regions announce updates.
- No "group, group, group" dead-ends.

## Rule 13 — Touch targets: 44×44 minimum

WCAG 2.5.5 (AAA, but recommended for AA): touch targets at least 44×44 CSS pixels. iOS HIG and Material Design both require this.

```css
.icon-button {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

For inline links in dense text, allow smaller targets but ensure adequate spacing (24px between targets).

## The 40-Point Accessibility Checklist

| # | Category | Check |
|---|----------|-------|
| 1 | Semantics | Page has exactly one `<h1>` |
| 2 | Semantics | Headings form a logical outline (no skipped levels) |
| 3 | Semantics | All buttons are `<button>`, all links are `<a>`, all inputs are `<input>` |
| 4 | Semantics | Landmarks present: `<nav>`, `<main>`, `<footer>` |
| 5 | Semantics | Lists use `<ul>`/`<ol>` with `<li>` |
| 6 | Semantics | Tables use `<th>` with `scope` for headers |
| 7 | Contrast | Body text ≥ 4.5:1 against background |
| 8 | Contrast | Large text (≥24px) ≥ 3:1 |
| 9 | Contrast | UI components (borders, icons) ≥ 3:1 |
| 10 | Contrast | Focus indicator ≥ 3:1 against adjacent colors |
| 11 | Keyboard | All interactions reachable via keyboard |
| 12 | Keyboard | Logical tab order (matches visual order) |
| 13 | Keyboard | No keyboard traps |
| 14 | Keyboard | `:focus-visible` style on every focusable element |
| 15 | Keyboard | Skip link is the first focusable element |
| 16 | Keyboard | Modals trap focus, restore focus on close, Esc closes |
| 17 | Forms | Every input has a `<label>` with `for`/`id` association |
| 18 | Forms | Required fields marked with `aria-required` and visible text |
| 19 | Forms | Errors associated via `aria-describedby` and `role="alert"` |
| 20 | Forms | Errors don't rely on color alone (icon + text) |
| 21 | Forms | Autocomplete attributes set (`autocomplete="email"`, etc.) |
| 22 | Images | `<img>` has `alt` (descriptive for content, empty `alt=""` for decorative) |
| 23 | Images | Background images conveying info have a text equivalent |
| 24 | Icons | Decorative icons have `aria-hidden="true"` |
| 25 | Icons | Icon-only buttons have `aria-label` or visually-hidden text |
| 26 | Motion | `prefers-reduced-motion: reduce` respected globally |
| 27 | Motion | No autoplaying video or audio |
| 28 | Motion | No more than 3 flashes per second (seizure-safe) |
| 29 | Live regions | Toasts use `aria-live="polite"` |
| 30 | Live regions | Errors use `role="alert"` |
| 31 | Touch | Touch targets ≥ 44×44px (or 24×24 with spacing) |
| 32 | ARIA | No `aria-label` on elements with visible text |
| 33 | ARIA | No `role="button"` on a `<div>` when a `<button>` works |
| 34 | ARIA | `aria-hidden="true"` only on purely decorative elements |
| 35 | Language | `<html lang="en">` set |
| 36 | Language | Language changes within content marked with `lang` attribute |
| 37 | Page titles | `<title>` is unique and descriptive per page |
| 38 | Color scheme | `prefers-color-scheme: dark` supported (see guide 16) |
| 39 | Reading order | DOM order matches visual reading order |
| 40 | Tested | Page tested with VoiceOver or NVDA |

## Anti-Patterns (Auto-Fail)

1. **`outline: none` without a replacement focus style.**
2. **`<div onClick>` instead of `<button>`.**
3. **Heading levels chosen for size, not hierarchy.**
4. **Color-only error states.**
5. **`aria-label` repeating the visible button text.** Redundant, can conflict with translation.
6. **Icon-only buttons without accessible names.**
7. **`tabindex="1"`** (positive tabindex breaks DOM order).
8. **Autoplaying video or audio.**
9. **Forms with no `<label>` association.**
10. **Modals that don't trap focus.**
11. **No skip link on multi-section pages.**
12. **`alt` text that says "image" or "photo".** Describe the content.
13. **`prefers-reduced-motion` ignored.**
14. **Touch targets under 44px.**

## Output

When you finish this guide, you should have:
- All 40 checklist items passing
- A Lighthouse Accessibility score ≥ 95
- VoiceOver or NVDA test completed (page announces correctly, navigable by heading)
- Every interactive element with a visible focus indicator
- Every form field with a `<label>` and error association
- `prefers-reduced-motion` and `prefers-color-scheme` respected
- A skip link as the first focusable element
- Documented in `DESIGN-RATIONALE.md`: the assistive tech tested, the date, the tester
