/**
 * AnimatedNav — Sticky glass nav that shrinks on scroll.
 *
 * References: linear.app, vercel.com, framer.com nav patterns
 *
 * Features:
 * - Transparent at top, glass background after scrolling
 * - Shrinks padding on scroll
 * - Mobile menu (off-canvas)
 * - Active link indicator
 * - Focus-visible states
 * - Keyboard accessible (ESC closes mobile menu)
 */

import { useEffect, useState } from 'react';

interface NavItem {
  label: string;
  href: string;
}

interface AnimatedNavProps {
  logo: React.ReactNode;
  items: NavItem[];
  cta?: { label: string; href: string };
  activeHref?: string;
}

export function AnimatedNav({ logo, items, cta, activeHref }: AnimatedNavProps) {
  const [scrolled, setScrolled] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setMobileOpen(false);
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  return (
    <header
      className={[
        'fixed inset-x-0 top-0 z-50 transition-all duration-300',
        scrolled
          ? 'bg-[var(--bg)]/80 backdrop-blur-md border-b border-[var(--border)]'
          : 'bg-transparent border-b border-transparent',
      ].join(' ')}
    >
      <nav
        aria-label="Primary"
        className={[
          'mx-auto flex max-w-6xl items-center justify-between px-6 transition-all duration-300',
          scrolled ? 'h-14' : 'h-20',
        ].join(' ')}
      >
        <a
          href="/"
          className="flex items-center gap-2 font-[var(--font-display)] text-lg font-semibold tracking-tight text-[var(--text)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)] rounded"
        >
          {logo}
        </a>

        {/* Desktop nav */}
        <ul className="hidden md:flex items-center gap-1">
          {items.map((item) => (
            <li key={item.href}>
              <a
                href={item.href}
                aria-current={activeHref === item.href ? 'page' : undefined}
                className={[
                  'relative px-4 py-2 text-sm font-medium rounded-full transition-colors',
                  activeHref === item.href
                    ? 'text-[var(--text)]'
                    : 'text-[var(--muted)] hover:text-[var(--text)]',
                  'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)]',
                ].join(' ')}
              >
                {item.label}
                {activeHref === item.href && (
                  <span
                    className="absolute inset-x-3 -bottom-px h-px bg-[var(--accent)]"
                    aria-hidden
                  />
                )}
              </a>
            </li>
          ))}
        </ul>

        <div className="flex items-center gap-3">
          {cta && (
            <a
              href={cta.href}
              className="hidden sm:inline-flex items-center gap-2 rounded-full bg-[var(--accent)] px-4 py-2 text-sm font-semibold text-white transition-all hover:scale-[1.03] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)] active:scale-[0.98]"
            >
              {cta.label}
            </a>
          )}

          {/* Mobile menu toggle */}
          <button
            type="button"
            aria-label={mobileOpen ? 'Close menu' : 'Open menu'}
            aria-expanded={mobileOpen}
            aria-controls="mobile-menu"
            onClick={() => setMobileOpen((v) => !v)}
            className="md:hidden inline-flex h-9 w-9 items-center justify-center rounded-full text-[var(--text)] hover:bg-[var(--surface)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)]"
          >
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden>
              {mobileOpen ? (
                <path d="M5 5l10 10M15 5L5 15" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" />
              ) : (
                <path d="M3 6h14M3 10h14M3 14h14" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" />
              )}
            </svg>
          </button>
        </div>
      </nav>

      {/* Mobile off-canvas menu */}
      {mobileOpen && (
        <div
          id="mobile-menu"
          className="md:hidden fixed inset-0 top-[calc(var(--nav-height,5rem)-1px)] z-40 bg-[var(--bg)]"
          role="dialog"
          aria-modal="true"
          aria-label="Mobile navigation"
        >
          <ul className="flex flex-col gap-1 p-6">
            {items.map((item) => (
              <li key={item.href}>
                <a
                  href={item.href}
                  aria-current={activeHref === item.href ? 'page' : undefined}
                  onClick={() => setMobileOpen(false)}
                  className="block px-4 py-3 text-lg font-medium text-[var(--text)] rounded-lg hover:bg-[var(--surface)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)]"
                >
                  {item.label}
                </a>
              </li>
            ))}
            {cta && (
              <li className="mt-4">
                <a
                  href={cta.href}
                  onClick={() => setMobileOpen(false)}
                  className="block rounded-full bg-[var(--accent)] px-6 py-3 text-center text-sm font-semibold text-white"
                >
                  {cta.label}
                </a>
              </li>
            )}
          </ul>
        </div>
      )}
    </header>
  );
}

export default AnimatedNav;
