/**
 * Counter — Animated number counter for stats.
 *
 * References: stripe.com pricing, linear.app hero, fathomanalytics.co
 *
 * When to use:
 * - Hero stats (1 per hero, max)
 * - Proof section
 * - Dashboard KPIs
 *
 * When NOT to use:
 * - When the number is small (e.g. "12") — animating makes it feel smaller
 * - On every stat on the page (lose impact)
 * - For currency you don't want to flash (use a fade instead)
 *
 * Accessibility:
 * - Respects prefers-reduced-motion (shows final value immediately)
 * - Uses tabular-nums to prevent layout shift
 * - aria-live="polite" so screen readers announce the final value
 */

import { useEffect, useRef, useState } from 'react';

interface CounterProps {
  to: number;
  from?: number;
  duration?: number; // ms
  format?: (n: number) => string;
  className?: string;
}

export function Counter({
  to,
  from = 0,
  duration = 2000,
  format = (n) => n.toLocaleString(),
  className = '',
}: CounterProps) {
  const ref = useRef<HTMLSpanElement>(null);
  const [display, setDisplay] = useState(format(from));
  const [done, setDone] = useState(false);

  useEffect(() => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) {
      setDisplay(format(to));
      setDone(true);
      return;
    }

    const el = ref.current;
    if (!el) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !done) {
            const start = performance.now();
            const tick = (now: number) => {
              const t = Math.min((now - start) / duration, 1);
              // easeOutQuart
              const eased = 1 - Math.pow(1 - t, 4);
              setDisplay(format(Math.floor(from + (to - from) * eased)));
              if (t < 1) {
                requestAnimationFrame(tick);
              } else {
                setDisplay(format(to));
                setDone(true);
              }
            };
            requestAnimationFrame(tick);
            observer.disconnect();
          }
        });
      },
      { threshold: 0.5 }
    );

    observer.observe(el);
    return () => observer.disconnect();
  }, [to, from, duration, format, done]);

  return (
    <span
      ref={ref}
      aria-live="polite"
      aria-atomic="true"
      className={['tabular-nums', className].join(' ')}
    >
      {display}
    </span>
  );
}

export default Counter;

// Usage:
// <p className="text-5xl font-display font-semibold">
//   <Counter to={1_247_893} duration={2000} />
//   <span className="text-muted text-2xl"> reviews shipped</span>
// </p>
// <p className="text-sm text-muted mt-2">Source: Stripe data, Q3 2025</p>
