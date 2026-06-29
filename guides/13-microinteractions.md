# 13 — Microinteractions

> A button that doesn't react when you press it is a dead thing. Microinteractions are the difference between a page that feels alive and one that feels like a screenshot. AI-coded sites ship five-state interactive elements only by accident — most ship two (rest, hover) and call it done. This guide forces you to design all five states for every interactive element, plus the loading, empty, error, and success states around them.

## Why AI fails at microinteractions

Four defaults ruin AI microinteractions:

1. **Only hover states.** LLMs ship `hover:bg-blue-600` and stop. No focus, no active, no disabled, no rest-vs-hover contrast strategy.
2. **No keyboard focus visible.** `focus:outline-none` everywhere, with no replacement. The site is unusable from the keyboard.
3. **Spinners for everything.** Loading state = a centered spinner. Skeletons are rarer, even though they reduce perceived wait time by 20–30%.
4. **No empty state.** A list with zero items renders an empty `<ul>`. No message, no illustration, no next action.

A senior designer treats every interactive element as having a lifecycle: rest → hover → focus → active → disabled. Every container has a data lifecycle: loading → empty → populated → error → success. AI skips both.

---

## Rule 1 — Every interactive element has 5 states

| State | When | Purpose | Visual change |
|-------|------|---------|---------------|
| **Rest** | Default | Baseline affordance | Base color, base elevation |
| **Hover** | Mouse over | "I'm clickable" | +10% bg saturation, cursor pointer |
| **Focus** | Keyboard focus, programmatic | "I'm selected" | Visible 2px outline ring (3:1 contrast) |
| **Active** | Mouse down / Enter key | "I'm being pressed" | -2% bg brightness, translateY(1px) |
| **Disabled** | `aria-disabled`, `disabled` | "I'm not available" | 50% opacity, `not-allowed` cursor |

```css
.btn {
  background: var(--accent);
  color: white;
  padding: var(--space-2) var(--space-4);
  border-radius: 8px;
  font-weight: 500;
  transition: background 120ms ease, transform 80ms ease;
  cursor: pointer;
}

/* Rest is the base above. */

.btn:hover {
  background: var(--accent-strong);  /* +10% darkness, not a glow */
}

.btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;  /* outside the button so it's always visible */
}

.btn:active {
  background: var(--accent-strong);
  transform: translateY(1px);  /* subtle "press" feedback */
}

.btn:disabled,
.btn[aria-disabled="true"] {
  background: var(--muted);
  color: var(--muted-foreground);
  cursor: not-allowed;
  opacity: 0.55;
  transform: none;
}
```

**`focus-visible`, not `focus`.** `:focus` triggers on mouse click too, leaving an ugly ring after every click. `:focus-visible` only shows the ring for keyboard users — modern browsers handle this for you.

**Never `outline: none` without a replacement.** If you remove the default outline, you must add a visible focus indicator. Otherwise the site is keyboard-unusable, which is an accessibility auto-fail (see guide 14).

## Rule 2 — Hover states do real work, not decoration

Bad hover: `hover:shadow-2xl hover:scale-105 hover:-translate-y-1` on every card. This is decoration — it doesn't tell the user anything.

Good hover: a card that's clickable gets `hover:border-accent` and `hover:shadow-lg`. The hover signals "this is interactive". A card that's not clickable gets no hover. Easy.

```css
/* Card that opens a detail view */
.card-link {
  border: 1px solid var(--border);
  transition: border-color 150ms ease, box-shadow 150ms ease, transform 150ms ease;
}

.card-link:hover {
  border-color: var(--accent);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
  /* No transform. Hover transforms cause layout shift and feel cheap. */
}

.card-link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.card-link:active {
  background: var(--surface-hover);
}
```

**Hover rules**:
- Hover signals interactivity, not personality.
- Hover never changes layout (no `scale-105`, no `translate-y`). Layout shifts cause performance jank and accessibility issues.
- Hover changes color, border, or shadow only.
- Hover has a 100–150ms transition. Faster feels twitchy; slower feels sluggish.

## Rule 3 — Active states confirm the press

Active state is the moment between mousedown and mouseup. It should feel like the element is being physically pressed.

```css
.btn:active {
  transform: translateY(1px);
  background: var(--accent-strong);
  transition: transform 0ms;  /* instant feedback, no delay */
}
```

For touch devices, `:active` triggers on tap. Keep it short — 100ms is the perceptual threshold for "instant".

## Rule 4 — Disabled states are not the same as hidden

Disabled elements stay visible to communicate "this exists, but you can't use it yet". Useful for showing users what they could do if they upgraded, completed a step, etc.

```tsx
<button disabled={!formValid} className="btn">
  Submit
</button>
```

Disabled requires:
- Visually distinct (opacity 0.4–0.6, no hover state, no shadow)
- Cursor `not-allowed`
- `aria-disabled="true"` or native `disabled`
- No tooltip on hover that says "disabled" — the visual is enough. If you need to explain why, use an adjacent helper text.

## Rule 5 — Loading states: skeletons, not spinners

A spinner says "wait". A skeleton says "here's what's coming". Skeletons reduce perceived wait time and eliminate layout shift when content loads.

```tsx
// ❌ Spinner
{loading ? <Spinner /> : <Content />}

// ✅ Skeleton
function ArticleSkeleton() {
  return (
    <div className="skeleton-stack">
      <div className="skeleton skeleton-line" style={{ width: '60%' }} />
      <div className="skeleton skeleton-line" />
      <div className="skeleton skeleton-line" />
      <div className="skeleton skeleton-line" style={{ width: '80%' }} />
      <div className="skeleton skeleton-block" style={{ height: 200 }} />
    </div>
  );
}

{loading ? <ArticleSkeleton /> : <Article data={data} />}
```

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--surface) 0%,
    var(--surface-hover) 50%,
    var(--surface) 100%
  );
  background-size: 200% 100%;
  animation: skeleton-shimmer 1.5s ease-in-out infinite;
  border-radius: 4px;
}

@keyframes skeleton-shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton-line  { height: 14px; margin-bottom: 8px; }
.skeleton-block { width: 100%; }

@media (prefers-reduced-motion: reduce) {
  .skeleton { animation: none; background: var(--surface-hover); }
}
```

**When to use a spinner instead of a skeleton**:
- The action takes <400ms (skeleton flash is worse than no skeleton).
- The action is a one-tap confirmation (submitting a form, copying to clipboard).
- The shape of the loading content is unknown.

**Spinner rules**:
- Size 16–20px for inline, 32–48px for full-page.
- One full rotation in 800–1200ms. Faster feels anxious.
- Always pair with a label: "Loading…" or "Saving…".

## Rule 6 — Empty states turn zero into a moment

A list with no items is a design opportunity, not a void. Every empty state has three parts:

1. **What's empty** (a short label: "No projects yet")
2. **Why** (a one-sentence explanation: "Projects you create will appear here")
3. **What to do next** (a CTA: "Create your first project")

```tsx
function EmptyProjects() {
  return (
    <div className="empty-state">
      <div className="empty-state-icon">
        {/* Custom illustration, not an emoji */}
        <FolderIcon size={48} />
      </div>
      <h3>No projects yet</h3>
      <p>Projects you create will appear here, ready to share with your team.</p>
      <button className="btn btn-primary">
        <PlusIcon size={16} /> New project
      </button>
    </div>
  );
}
```

**Forbidden**: rendering an empty container. If the list is empty, the user needs to know — and they need a path forward.

## Rule 7 — Error states explain and recover

An error state has four parts:

1. **What went wrong** (specific: "Email is required", not "Invalid input")
2. **Why it went wrong** (when not obvious: "The email must contain @")
3. **How to fix it** ("Please enter a valid email address")
4. **What happens next** ("Once you fix this, click Save again")

```tsx
<div className="field-error">
  <label htmlFor="email">Email</label>
  <input
    id="email"
    type="email"
    aria-invalid="true"
    aria-describedby="email-error"
    className={error ? 'input-error' : ''}
  />
  {error && (
    <p id="email-error" role="alert" className="error-message">
      <WarningIcon size={14} aria-hidden />
      Please enter a valid email address.
    </p>
  )}
</div>
```

```css
.input-error {
  border-color: var(--error);
  background: var(--error-bg, rgba(220, 38, 38, 0.04));
}

.error-message {
  color: var(--error);
  font-size: var(--step--1);
  margin-top: var(--space-2);
  display: flex;
  align-items: center;
  gap: var(--space-1);
}
```

Error states must:
- Be visible without color alone (include an icon, text, or both — colorblind users can't see "red border").
- Use `role="alert"` so screen readers announce them.
- Be associated with the input via `aria-describedby`.

## Rule 8 — Success states confirm what happened

A success state answers: "Did it work? What changed? What now?"

For micro-interactions (copy-to-clipboard, save), a 2-second toast is enough. For major actions (purchase, submission), a full-page or modal confirmation.

```tsx
// Copy-to-clipboard with optimistic confirmation
function CopyButton({ text }: { text: string }) {
  const [copied, setCopied] = useState(false);

  async function handleCopy() {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  return (
    <button onClick={handleCopy} className="btn btn-ghost">
      {copied ? (
        <>
          <CheckIcon size={16} aria-hidden /> Copied
        </>
      ) : (
        <>
          <CopyIcon size={16} aria-hidden /> Copy
        </>
      )}
    </button>
  );
}
```

**Toast rules**:
- Position: bottom-right on desktop, bottom-center on mobile.
- Auto-dismiss after 4 seconds for info, 6 seconds for success, never auto-dismiss for errors.
- One toast at a time. Queue subsequent ones.
- Includes a dismiss button (X).
- Animates in from the edge, 200ms.

## Rule 9 — Optimistic UI: show the result before the server confirms

For actions where the user is confident (liking, starring, marking read), update the UI immediately and reconcile in the background. If the server fails, roll back with a toast.

```tsx
function LikeButton({ postId }: { postId: string }) {
  const [liked, setLiked] = useState(false);
  const [pending, setPending] = useState(false);

  async function handleClick() {
    const previous = liked;
    setLiked(!previous);          // optimistic update
    setPending(true);
    try {
      await api.toggleLike(postId);
    } catch {
      setLiked(previous);         // rollback
      toast.error('Could not save your like. Try again.');
    } finally {
      setPending(false);
    }
  }

  return (
    <button onClick={handleClick} disabled={pending} aria-pressed={liked}>
      {liked ? <HeartFilledIcon /> : <HeartIcon />}
      {liked ? 'Liked' : 'Like'}
    </button>
  );
}
```

**Optimistic UI rules**:
- Use only for low-stakes actions (likes, bookmarks, read receipts).
- Never for purchases, deletes, or irreversible actions.
- Always have a rollback path.
- Disable the button during the pending state to prevent double-submits.

## Rule 10 — Tooltips vs Popovers vs Modals: the decision tree

```
Is the content essential to complete the task?
├── Yes → Modal (forces a decision)
└── No → Is the content >120 characters or interactive (form, list)?
         ├── Yes → Popover (rich content, dismissible by outside click)
         └── No → Is the content <120 characters and static?
                  ├── Yes → Tooltip (on hover/focus, non-interactive)
                  └── No → Inline help text next to the element
```

| Component | Trigger | Dismiss | Interactive | Use case |
|-----------|---------|---------|-------------|----------|
| Tooltip | Hover/focus | Mouse out / blur | No | Clarifying an icon, defining a term |
| Popover | Click | Outside click / Esc | Yes | Quick form, settings, filter |
| Modal | Click (button) | Esc / explicit close | Yes | Forced decision, multi-step flow |

```tsx
// Tooltip
<button
  aria-describedby="tip-copy"
  className="icon-button"
>
  <CopyIcon aria-hidden />
</button>
<span role="tooltip" id="tip-copy" className="tooltip">
  Copy to clipboard
</span>
```

```css
.tooltip {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  background: var(--text);
  color: var(--bg);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 12px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 150ms ease;
  z-index: 50;
}

.icon-button:hover + .tooltip,
.icon-button:focus-visible + .tooltip {
  opacity: 1;
}
```

**Tooltip rules**:
- Never essential information. If the tooltip is the only label, screen reader users miss it.
- Delay 500ms before showing (avoids flicker on mouse-traversal).
- Never on touch devices (no hover). Hide with `@media (hover: hover)`.
- Pair with `aria-describedby` for screen reader access.

## Rule 11 — Drag feedback: show what's happening

Drag-and-drop requires four visual states:

1. **Rest**: the draggable item at rest.
2. **Hovering over a drop zone**: the zone highlights.
3. **Dragging**: the dragged item gets opacity 0.5, a "ghost" follows the cursor.
4. **Dropped**: the item animates into its new position (200ms).

```tsx
<div
  draggable
  onDragStart={(e) => {
    e.dataTransfer.setData('text/plain', item.id);
    e.currentTarget.classList.add('dragging');
  }}
  onDragEnd={(e) => e.currentTarget.classList.remove('dragging')}
  className="draggable-item"
>
  {item.label}
</div>

<div
  onDragOver={(e) => {
    e.preventDefault();
    e.currentTarget.classList.add('drag-over');
  }}
  onDragLeave={(e) => e.currentTarget.classList.remove('drag-over')}
  onDrop={(e) => {
    e.currentTarget.classList.remove('drag-over');
    const id = e.dataTransfer.getData('text/plain');
    handleDrop(id);
  }}
  className="drop-zone"
/>
```

```css
.draggable-item.dragging {
  opacity: 0.4;
  cursor: grabbing;
}

.drop-zone.drag-over {
  background: var(--accent-soft);
  border: 2px dashed var(--accent);
}
```

**Drag-and-drop accessibility**: drag is a mouse-only interaction. Always provide a keyboard alternative (arrow keys + space to move, or a "move up / move down" button). Otherwise the feature is unusable for keyboard and screen reader users.

## Rule 12 — Reduced motion: respect the preference

Every microinteraction must respect `prefers-reduced-motion: reduce`.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

This isn't optional. About 3% of users have this preference enabled (vestibular disorders, motion sensitivity). See guide 14 for the full accessibility treatment.

## Anti-Patterns (Auto-Fail)

1. **Only `hover:` states.** Every interactive element needs all 5 states.
2. **`focus:outline-none`** without a replacement. Keyboard-unusable.
3. **Spinners for >1s loads.** Use skeletons.
4. **Empty `<ul>`** with no empty state.
5. **`scale-105` on hover.** Causes layout shift; feels cheap.
6. **Toasts that auto-dismiss errors.** Errors stay until dismissed.
7. **Tooltip as the only label.** Screen reader users get nothing.
8. **Drag-and-drop with no keyboard alternative.** Unusable for keyboard users.
9. **No active state.** The button looks identical at rest and during press.
10. **Disabled state at 100% opacity** ("ghost" disabled). Users can't tell it's disabled.
11. **Animations that ignore `prefers-reduced-motion`.** Vestibular harm.
12. **Color-only error states.** Colorblind users can't see them.
13. **`onMouseEnter` for tooltips without `onFocus`.** Keyboard users can't trigger them.

## Code Example — Full 5-State Button Component

```tsx
import { forwardRef } from 'react';

type ButtonProps = React.ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: 'primary' | 'secondary' | 'ghost';
  loading?: boolean;
};

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ variant = 'primary', loading, children, disabled, ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={`btn btn-${variant} ${loading ? 'is-loading' : ''}`}
        disabled={disabled || loading}
        aria-busy={loading}
        {...props}
      >
        {loading && <Spinner size={14} aria-hidden />}
        {children}
      </button>
    );
  }
);
Button.displayName = 'Button';
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  border-radius: 8px;
  font-weight: 500;
  font-size: var(--step-0);
  line-height: 1;
  cursor: pointer;
  transition: background 120ms ease, transform 80ms ease, box-shadow 120ms ease;
  border: 1px solid transparent;
}

.btn-primary { background: var(--accent); color: white; }
.btn-primary:hover { background: var(--accent-strong); }
.btn-primary:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.btn-primary:active { transform: translateY(1px); }
.btn-primary:disabled {
  background: var(--muted);
  cursor: not-allowed;
  opacity: 0.5;
  transform: none;
}
.btn-primary.is-loading {
  background: var(--accent-strong);
  cursor: progress;
}
```

## Output

When you finish this guide, you should have:
- A `Button` component with all 5 states (rest, hover, focus, active, disabled) + loading
- A `Skeleton` component matching the dimensions of every async-loaded component
- An `EmptyState` component used in every list-driven view
- A `Toast` system with auto-dismiss (info/success) and manual dismiss (error)
- A `Tooltip`, `Popover`, `Modal` set, each with the right trigger/dismiss behavior
- `:focus-visible` styles on every interactive element (no `outline: none` without replacement)
- `prefers-reduced-motion` handling globally
- A documented decision tree for tooltip-vs-popover-vs-modal in `DESIGN-RATIONALE.md`
