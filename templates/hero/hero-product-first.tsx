/**
 * HeroProductFirst — Terminal/code hero with headline BELOW.
 *
 * References: vercel.com, supabase.com, railway.app, bun.sh
 *
 * When to use:
 * - Dev tools
 * - CLIs
 * - Open-source projects
 * - API-first products
 *
 * When NOT to use:
 * - Non-technical audiences
 * - Consumer products
 * - E-commerce
 *
 * Design notes:
 * - Terminal types itself out (real timing, real chars)
 * - Headline BELOW the terminal — uncommon, gets attention
 * - Mono font throughout the hero
 * - The "ship in 60 seconds" promise should be backed by the demo
 */

import { useEffect, useRef, useState } from 'react';

interface TerminalLine {
  text: string;
  type?: 'command' | 'output' | 'success' | 'link';
  delayBefore?: number; // ms
}

interface HeroProductFirstProps {
  lines: TerminalLine[];
  headline: string;
  subhead: string;
  primaryCta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
}

export function HeroProductFirst({
  lines,
  headline,
  subhead,
  primaryCta,
  secondaryCta,
}: HeroProductFirstProps) {
  const [visibleLines, setVisibleLines] = useState<number>(0);
  const [typingChar, setTypingChar] = useState<string>('');
  const terminalRef = useRef<HTMLDivElement>(null);
  const reducedMotion = usePrefersReducedMotion();

  useEffect(() => {
    if (reducedMotion) {
      setVisibleLines(lines.length);
      return;
    }

    let lineIdx = 0;
    let charIdx = 0;
    let timeoutId: number;

    function typeNext() {
      if (lineIdx >= lines.length) return;
      const line = lines[lineIdx];

      if (charIdx === 0 && line.delayBefore) {
        timeoutId = window.setTimeout(() => {
          charIdx = 0;
          typeNext();
        }, line.delayBefore);
        return;
      }

      if (charIdx <= line.text.length) {
        setTypingChar(line.text.slice(0, charIdx));
        charIdx++;
        timeoutId = window.setTimeout(typeNext, line.type === 'command' ? 32 : 8);
      } else {
        setVisibleLines((v) => v + 1);
        setTypingChar('');
        lineIdx++;
        charIdx = 0;
        timeoutId = window.setTimeout(typeNext, line.type === 'command' ? 200 : 120);
      }
    }

    timeoutId = window.setTimeout(typeNext, 400);
    return () => window.clearTimeout(timeoutId);
  }, [lines, reducedMotion]);

  return (
    <section
      aria-labelledby="hero-heading"
      className="relative mx-auto max-w-5xl px-6 pt-24 pb-20 lg:pt-32 lg:pb-28 text-center"
    >
      {/* Terminal */}
      <div
        ref={terminalRef}
        className="mx-auto max-w-3xl text-left overflow-hidden rounded-xl border border-[var(--border)] bg-[#0A0A0B] shadow-[0_1px_2px_rgba(0,0,0,0.04),0_24px_48px_-12px_rgba(0,0,0,0.25)]"
        role="region"
        aria-label="Product demo terminal"
      >
        <div className="flex items-center gap-2 border-b border-white/5 px-4 py-3">
          <span className="h-3 w-3 rounded-full bg-[#FF5F57]" aria-hidden />
          <span className="h-3 w-3 rounded-full bg-[#FEBC2E]" aria-hidden />
          <span className="h-3 w-3 rounded-full bg-[#28C840]" aria-hidden />
          <span className="ml-3 text-xs font-mono text-white/40">~/project</span>
        </div>
        <div className="px-5 py-6 font-mono text-sm leading-relaxed">
          {lines.slice(0, visibleLines).map((line, i) => (
            <Line key={i} line={line} />
          ))}
          {visibleLines < lines.length && (
            <Line line={{ ...lines[visibleLines], text: typingChar }} typing />
          )}
          {visibleLines >= lines.length && !reducedMotion && (
            <span className="inline-block w-2 h-4 bg-[var(--accent)] animate-pulse" aria-hidden />
          )}
        </div>
      </div>

      <h1
        id="hero-heading"
        className="mt-12 font-[var(--font-display)] text-4xl font-medium leading-[1.05] tracking-[-0.025em] text-[var(--text)] sm:text-5xl lg:text-6xl"
      >
        {headline}
      </h1>

      <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-[var(--muted)]">
        {subhead}
      </p>

      <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
        <a
          href={primaryCta.href}
          className="inline-flex items-center gap-2 rounded-full bg-[var(--accent)] px-6 py-3 text-sm font-semibold text-white shadow-[0_1px_2px_rgba(0,0,0,0.05),0_8px_24px_rgba(0,0,0,0.08)] transition-all hover:scale-[1.02] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)] active:scale-[0.98]"
        >
          {primaryCta.label}
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
    </section>
  );
}

function Line({ line, typing = false }: { line: TerminalLine; typing?: boolean }) {
  if (line.type === 'command') {
    return (
      <div className="text-white/90">
        <span className="text-[var(--accent)] mr-2">$</span>
        {line.text}
        {typing && <span className="inline-block w-2 h-4 ml-0.5 bg-white/80 animate-pulse" aria-hidden />}
      </div>
    );
  }
  if (line.type === 'success') {
    return <div className="text-[#28C840]">{line.text}</div>;
  }
  if (line.type === 'link') {
    return (
      <div className="text-[var(--accent)] underline underline-offset-2">{line.text}</div>
    );
  }
  return <div className="text-white/60">{line.text}</div>;
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

export default HeroProductFirst;

// Example usage:
// <HeroProductFirst
//   lines={[
//     { text: 'npm install @scope/pkg', type: 'command' },
//     { text: 'added 1 package in 1.2s', type: 'output' },
//     { text: 'scope init', type: 'command', delayBefore: 400 },
//     { text: '✓ Project created', type: 'success' },
//     { text: 'scope deploy', type: 'command', delayBefore: 400 },
//     { text: '→ https://my-app.scope.sh', type: 'link' },
//   ]}
//   headline="Ship in 60 seconds."
//   subhead="The database that scales with you, from prototype to production. Edge-deployed, serverless-friendly, zero-config."
//   primaryCta={{ label: 'Get Started', href: '/signup' }}
//   secondaryCta={{ label: 'Read the docs', href: '/docs' }}
// />
