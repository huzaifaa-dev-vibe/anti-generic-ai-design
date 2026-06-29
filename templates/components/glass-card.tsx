/**
 * GlassCard — Real glassmorphism, not the AI default.
 *
 * See guides/04-glassmorphism-guide.md for the full system.
 *
 * CRITICAL: This component only works if there is content behind it to blur.
 * Do not place over a flat background — the blur does nothing.
 */

import './glass-card.css';

interface GlassCardProps {
  children: React.ReactNode;
  variant?: 'light' | 'dark' | 'tinted' | 'smoked';
  className?: string;
  /** Adds a subtle SVG noise overlay — real frosted glass has grain */
  withNoise?: boolean;
  /** Premium gradient border */
  withGradientBorder?: boolean;
}

export function GlassCard({
  children,
  variant = 'light',
  className = '',
  withNoise = false,
  withGradientBorder = false,
}: GlassCardProps) {
  return (
    <div
      className={[
        'ag-glass',
        `ag-glass--${variant}`,
        withNoise && 'ag-glass--noise',
        withGradientBorder && 'ag-glass--premium-border',
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </div>
  );
}

export default GlassCard;

// Usage:
// <div className="relative">
//   {/* Background content: photo, gradient mesh, video */}
//   <img src="/hero-bg.jpg" alt="" className="absolute inset-0 w-full h-full object-cover" />
//
//   {/* Glass card floating over it — backdrop-blur works */}
//   <GlassCard variant="light" withNoise className="relative z-10 p-8 max-w-md">
//     <h3 className="text-2xl font-semibold">Sign up for early access</h3>
//     <p className="mt-2 text-sm text-muted">Get 3 months free when we launch.</p>
//   </GlassCard>
// </div>
