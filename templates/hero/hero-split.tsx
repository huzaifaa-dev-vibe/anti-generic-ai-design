/**
 * HeroSplit — Split hero with text left, real product UI right.
 *
 * References: linear.app, vercel.com, resend.com, cal.com
 *
 * When to use:
 * - SaaS landing pages
 * - Dev tools
 * - Any product where you can show real UI in the hero
 *
 * When NOT to use:
 * - Editorial / publication sites (use HeroAsymmetric instead)
 * - Cinematic / video brands (use HeroVideoBg instead)
 *
 * Customization:
 * - Replace <ProductMockup /> with a real screenshot or live component
 * - Replace <Proof /> with a real stat / testimonial / logo+case-study-link
 * - Update copy to be specific (see guides/05-hero-section-guide.md Rule 6)
 */

import { useEffect, useRef, useState } from 'react';

interface HeroSplitProps {
  eyebrow?: string;
  headline: string;
  subhead: string;
  primaryCta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
  proof?: {
    stat: string;
    label: string;
    source?: string;
  };
  productMockup: React.ReactNode;
}

export function HeroSplit({
  eyebrow,
  headline,
  subhead,
  primaryCta,
  secondaryCta,
  proof,
  productMockup,
}: HeroSplitProps) {
  return (
    <section
      aria-labelledby="hero-heading"
      className="relative mx-auto max-w-6xl px-6 pt-24 pb-20 lg:pt-32 lg:pb-28"
    >
      <div className="grid gap-12 lg:grid-cols-[1.1fr_1fr] lg:gap-16 lg:items-center">
        {/* Left: copy */}
        <div className="hero-copy">
          {eyebrow && (
            <p className="mb-5 flex items-center gap-2 text-xs font-medium uppercase tracking-[0.18em] text-[var(--muted)]">
              <span className="inline-block h-1.5 w-1.5 rounded-full bg-[var(--accent)]" aria-hidden />
              {eyebrow}
            </p>
          )}

          <h1
            id="hero-heading"
            className="font-[var(--font-display)] text-4xl font-medium leading-[1.05] tracking-[-0.025em] text-[var(--text)] sm:text-5xl lg:text-[3.5rem]"
          >
            {headline}
          </h1>

          <p className="mt-6 max-w-xl text-lg leading-relaxed text-[var(--muted)] sm:text-xl">
            {subhead}
          </p>

          <div className="mt-8 flex flex-wrap items-center gap-3">
            <a
              href={primaryCta.href}
              className="inline-flex items-center gap-2 rounded-full bg-[var(--accent)] px-6 py-3 text-sm font-semibold text-white shadow-[0_1px_2px_rgba(0,0,0,0.05),0_8px_24px_rgba(0,0,0,0.08)] transition-all hover:scale-[1.02] hover:shadow-[0_1px_2px_rgba(0,0,0,0.05),0_12px_32px_rgba(0,0,0,0.12)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)] active:scale-[0.98]"
            >
              {primaryCta.label}
              <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden>
                <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round" />
              </svg>
            </a>
            {secondaryCta && (
              <a
                href={secondaryCta.href}
                className="inline-flex items-center gap-2 rounded-full border border-[var(--border)] px-6 py-3 text-sm font-semibold text-[var(--text)] transition-colors hover:bg-[var(--surface)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)]"
              >
                {secondaryCta.label}
              </a>
            )}
          </div>

          {proof && (
            <div className="mt-10 flex items-baseline gap-3 border-t border-[var(--border)] pt-6">
              <span className="font-[var(--font-display)] text-3xl font-semibold tabular-nums text-[var(--text)]">
                {proof.stat}
              </span>
              <span className="text-sm text-[var(--muted)]">
                {proof.label}
                {proof.source && (
                  <>
                    {' '}
                    <span className="text-[var(--muted)]/70">· {proof.source}</span>
                  </>
                )}
              </span>
            </div>
          )}
        </div>

        {/* Right: product */}
        <div className="hero-product relative">
          <div
            className="absolute -inset-4 -z-10 rounded-3xl bg-[radial-gradient(circle_at_50%_50%,var(--accent-glow,rgba(99,102,241,0.12)),transparent_70%)]"
            aria-hidden
          />
          <div className="overflow-hidden rounded-xl border border-[var(--border)] bg-[var(--surface)] shadow-[0_1px_2px_rgba(0,0,0,0.04),0_8px_24px_rgba(0,0,0,0.06)]">
            {productMockup}
          </div>
        </div>
      </div>

      <HeroChoreography />
    </section>
  );
}

/**
 * Choreographed hero reveal — under 3 seconds total.
 * Respects prefers-reduced-motion.
 * See guides/09-animation-guide.md.
 */
function HeroChoreography() {
  const reducedMotion = usePrefersReducedMotion();

  useEffect(() => {
    if (reducedMotion) return;
    const els = document.querySelectorAll<HTMLElement>('[data-hero-step]');
    els.forEach((el) => {
      const step = Number(el.dataset.heroStep);
      el.style.opacity = '0';
      el.style.transform = 'translateY(12px)';
      el.style.transition = 'opacity 600ms cubic-bezier(0.16,1,0.3,1), transform 600ms cubic-bezier(0.16,1,0.3,1)';
      el.style.transitionDelay = `${step * 150}ms`;
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          el.style.opacity = '1';
          el.style.transform = 'translateY(0)';
        });
      });
    });
  }, [reducedMotion]);

  return null;
}

function usePrefersReducedMotion() {
  const [reduced, setReduced] = useState(false);
  useEffect(() => {
    const mq = window.matchMedia('(prefers-reduced-motion: reduce)');
    setReduced(mq.matches);
    const handler = (e: MediaQueryListEvent) => setReduced(e.matches);
    mq.addEventListener('change', handler);
    return () => mq.removeEventListener('change', handler);
  }, []);
  return reduced;
}

export default HeroSplit;
