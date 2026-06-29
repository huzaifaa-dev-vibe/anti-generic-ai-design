/**
 * ScrollReveal — Triggered fade/slide-in when element enters viewport.
 *
 * References: linear.app, framer.com, vercel.com scroll sections
 *
 * IMPORTANT: Use SPARINGLY. The AI default is to put this on every section.
 * That's an anti-pattern. See guides/09-animation-guide.md.
 *
 * Rule: scroll-triggered animation should reveal information, not decorate.
 * Use it for:
 * - Charts that draw in when scrolled into view
 * - Product UI that unrolls a flow
 * - Step-by-step diagrams that build progressively
 *
 * Do NOT use it for:
 * - Plain text blocks
 * - Every card in a grid (use a single stagger instead)
 * - Headings (just show them)
 */

import { useEffect, useRef, useState, ReactNode } from 'react';

interface ScrollRevealProps {
  children: ReactNode;
  /** Direction to slide in from */
  direction?: 'up' | 'down' | 'left' | 'right' | 'none';
  distance?: number; // px
  duration?: number; // ms
  delay?: number; // ms
  /** Only animate first time (default) — set false to replay on every enter */
  once?: boolean;
  threshold?: number; // 0-1
  className?: string;
  as?: keyof JSX.IntrinsicElements;
}

export function ScrollReveal({
  children,
  direction = 'up',
  distance = 24,
  duration = 600,
  delay = 0,
  once = true,
  threshold = 0.2,
  className = '',
  as: Tag = 'div',
}: ScrollRevealProps) {
  const ref = useRef<HTMLElement>(null);
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) {
      setVisible(true);
      return;
    }

    const el = ref.current;
    if (!el) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setVisible(true);
            if (once) observer.disconnect();
          } else if (!once) {
            setVisible(false);
          }
        });
      },
      { threshold }
    );

    observer.observe(el);
    return () => observer.disconnect();
  }, [once, threshold]);

  const hiddenTransform = {
    up: `translateY(${distance}px)`,
    down: `translateY(-${distance}px)`,
    left: `translateX(${distance}px)`,
    right: `translateX(-${distance}px)`,
    none: 'translate(0, 0)',
  }[direction];

  return (
    <Tag
      // @ts-expect-error — ref typing across intrinsic elements is loose
      ref={ref}
      className={className}
      style={{
        transform: visible ? 'translate(0, 0)' : hiddenTransform,
        opacity: visible ? 1 : 0,
        transition: `opacity ${duration}ms cubic-bezier(0.16, 1, 0.3, 1) ${delay}ms, transform ${duration}ms cubic-bezier(0.16, 1, 0.3, 1) ${delay}ms`,
        willChange: 'opacity, transform',
      }}
    >
      {children}
    </Tag>
  );
}

export default ScrollReveal;

// Usage (sparingly!):
// <ScrollReveal direction="up" duration={600}>
//   <ProductFlow />  // ← this animates in when scrolled into view
// </ScrollReveal>
