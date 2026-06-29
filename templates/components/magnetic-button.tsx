/**
 * MagneticButton — Button that subtly attracts toward the cursor on hover.
 *
 * References: raycast.com, framer.com, premium agency sites
 *
 * When to use:
 * - Hero CTA (1 per page, max)
 * - Premium product CTAs
 * - When the button is the primary conversion target
 *
 * When NOT to use:
 * - Every button (becomes annoying)
 * - Mobile (no hover; touch doesn't benefit)
 * - Forms (distracting during input)
 *
 * Accessibility:
 * - Disables on touch devices
 * - Respects prefers-reduced-motion
 * - Full keyboard focus support
 */

import { useEffect, useRef, useState } from 'react';

interface MagneticButtonProps {
  children: React.ReactNode;
  href: string;
  variant?: 'primary' | 'secondary';
  /** Magnetic strength — 0 = off, 0.5 = default, 1 = strong */
  strength?: number;
  className?: string;
}

export function MagneticButton({
  children,
  href,
  variant = 'primary',
  strength = 0.4,
  className = '',
}: MagneticButtonProps) {
  const ref = useRef<HTMLAnchorElement>(null);
  const [offset, setOffset] = useState({ x: 0, y: 0 });
  const [enabled, setEnabled] = useState(false);

  useEffect(() => {
    const mqReduce = window.matchMedia('(prefers-reduced-motion: reduce)');
    const mqHover = window.matchMedia('(hover: hover) and (pointer: fine)');
    const update = () => setEnabled(!mqReduce.matches && mqHover.matches);
    update();
    mqReduce.addEventListener('change', update);
    mqHover.addEventListener('change', update);
    return () => {
      mqReduce.removeEventListener('change', update);
      mqHover.removeEventListener('change', update);
    };
  }, []);

  const handleMove = (e: React.MouseEvent) => {
    if (!enabled || !ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    setOffset({ x: x * strength, y: y * strength });
  };

  const handleLeave = () => setOffset({ x: 0, y: 0 });

  const base =
    'inline-flex items-center gap-2 rounded-full px-6 py-3 text-sm font-semibold transition-[transform,box-shadow,background-color] duration-200 ease-out focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)] active:scale-[0.97]';

  const variants = {
    primary:
      'bg-[var(--accent)] text-white shadow-[0_1px_2px_rgba(0,0,0,0.05),0_8px_24px_rgba(0,0,0,0.08)] hover:shadow-[0_1px_2px_rgba(0,0,0,0.05),0_12px_32px_rgba(0,0,0,0.12)]',
    secondary:
      'border border-[var(--border)] text-[var(--text)] hover:bg-[var(--surface)]',
  };

  return (
    <a
      ref={ref}
      href={href}
      onMouseMove={handleMove}
      onMouseLeave={handleLeave}
      style={{
        transform: `translate3d(${offset.x}px, ${offset.y}px, 0)`,
      }}
      className={[base, variants[variant], className].join(' ')}
    >
      {children}
    </a>
  );
}

export default MagneticButton;
