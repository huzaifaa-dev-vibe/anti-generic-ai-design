/**
 * HeroVideoBg — Cinematic hero with muted, autoplaying video background.
 *
 * References: apple.com, tesla.com, nike.com
 *
 * When to use:
 * - Cinematic / luxury brands
 * - Physical products with a "moment" (car driving, sneaker reveal)
 * - Brand films
 *
 * When NOT to use:
 * - SaaS / dev tools (irrelevant)
 * - Content-heavy sites (distracting)
 * - If you can't produce original video (stock video looks worse than a still image)
 *
 * Performance:
 * - Video must be ≤ 2MB total
 * - mp4 / h264 / AAC
 * - Poster image required (shown for the 200ms before video loads)
 * - Muted, autoplay, loop, playsinline (mobile-friendly)
 */

interface HeroVideoBgProps {
  videoSrc: string;
  posterSrc: string;
  eyebrow?: string;
  headline: string;
  subhead: string;
  cta: { label: string; href: string };
  secondaryCta?: { label: string; href: string };
}

export function HeroVideoBg({
  videoSrc,
  posterSrc,
  eyebrow,
  headline,
  subhead,
  cta,
  secondaryCta,
}: HeroVideoBgProps) {
  return (
    <section
      aria-labelledby="hero-heading"
      className="relative isolate overflow-hidden min-h-[88vh] flex items-center"
    >
      {/* Video background */}
      <video
        className="absolute inset-0 -z-10 h-full w-full object-cover"
        autoPlay
        muted
        loop
        playsInline
        poster={posterSrc}
        aria-hidden
      >
        <source src={videoSrc} type="video/mp4" />
      </video>

      {/* Dark overlay for text legibility */}
      <div
        className="absolute inset-0 -z-10 bg-black/45"
        aria-hidden
      />

      {/* Content */}
      <div className="mx-auto w-full max-w-5xl px-6 py-24 text-center text-white">
        {eyebrow && (
          <p className="mb-6 text-xs font-medium uppercase tracking-[0.22em] text-white/70">
            {eyebrow}
          </p>
        )}

        <h1
          id="hero-heading"
          className="font-[var(--font-display)] text-5xl font-medium leading-[1.02] tracking-[-0.03em] sm:text-6xl lg:text-7xl"
        >
          {headline}
        </h1>

        <p className="mx-auto mt-6 max-w-2xl text-lg leading-relaxed text-white/85 sm:text-xl">
          {subhead}
        </p>

        <div className="mt-10 flex flex-wrap items-center justify-center gap-3">
          <a
            href={cta.href}
            className="inline-flex items-center gap-2 rounded-full bg-white px-7 py-3.5 text-sm font-semibold text-black transition-all hover:scale-[1.02] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-black/40 active:scale-[0.98]"
          >
            {cta.label}
          </a>
          {secondaryCta && (
            <a
              href={secondaryCta.href}
              className="inline-flex items-center gap-2 rounded-full border border-white/30 bg-white/5 px-7 py-3.5 text-sm font-semibold text-white backdrop-blur-md transition-colors hover:bg-white/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-offset-2 focus-visible:ring-offset-black/40"
            >
              {secondaryCta.label}
            </a>
          )}
        </div>
      </div>

      {/* Scroll indicator */}
      <div
        className="absolute bottom-8 left-1/2 -translate-x-1/2 text-white/60"
        aria-hidden
      >
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M12 5v14M6 13l6 6 6-6" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      </div>
    </section>
  );
}

export default HeroVideoBg;
