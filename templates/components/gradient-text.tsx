/**
 * GradientText — Gradient text done right (not the AI default indigo→pink).
 *
 * The AI default is `bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 bg-clip-text text-transparent`.
 * BANNED.
 *
 * This component uses:
 * - Custom palette gradients (warm, cool, monochrome — never AI-default purple)
 * - Subtle motion (gradient shift, optional) — never decoration, always informational
 * - prefers-reduced-motion respected
 * - Accessible: still readable if gradient fails (fallback color set)
 *
 * See guides/02-color-palette-guide.md and guides/06-advanced-css-components.md
 */

import './gradient-text.css';

type GradientPreset =
  | 'sunset'      // warm: amber → orange → red
  | 'aurora'      // cool: teal → cyan → blue
  | 'ember'       // monochrome warm: brown → amber → cream
  | 'forest'      // green: deep teal → moss → sage
  | 'plum'        // editorial: deep purple → magenta (NOT the AI default)
  | 'steel'       // monochrome cool: graphite → silver → white
  | 'gold'        // luxury: deep gold → bright gold → cream
  | 'candy';      // playful: pink → coral → yellow (use sparingly)

interface GradientTextProps {
  children: React.ReactNode;
  preset?: GradientPreset;
  /** Animate the gradient slowly (use sparingly — once per page max) */
  animated?: boolean;
  className?: string;
}

export function GradientText({
  children,
  preset = 'sunset',
  animated = false,
  className = '',
}: GradientTextProps) {
  return (
    <span
      className={[
        'ag-gradient-text',
        `ag-gradient-text--${preset}`,
        animated && 'ag-gradient-text--animated',
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}

export default GradientText;

// Usage:
// <h1 className="text-7xl font-display font-medium tracking-tight">
//   Ship design reviews <GradientText preset="sunset">4× faster</GradientText>
// </h1>
//
// Forbidden:
// <h1 className="bg-gradient-to-r from-purple-500 to-pink-500 bg-clip-text text-transparent">
//   The Modern Way to Build Software  // banned: generic AI headline + banned gradient
// </h1>
