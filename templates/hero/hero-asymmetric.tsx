/**
 * HeroAsymmetric — Editorial-style hero with a massive headline that breaks the grid.
 *
 * References: pentagram.com, mucho.com, studio portfolios, awwwards editorial winners
 *
 * When to use:
 * - Portfolio sites
 * - Agency sites
 * - Creative / editorial brands
 * - When you have a striking single image
 *
 * When NOT to use:
 * - SaaS products (use HeroSplit with product UI instead)
 * - E-commerce (use HeroCentered with the product image)
 *
 * Design notes:
 * - Headline is HUGE (8-12rem on desktop). Use a real display face (Fraunces, Bricolage, Tiempos).
 * - Image extends past the column on purpose — breaks the grid.
 * - Subhead and CTA are bottom-aligned, not below the headline.
 * - Mix weights within the headline (regular + italic + bold).
 */

interface HeroAsymmetricProps {
  eyebrow?: string;
  /** Headline can include React nodes for weight/style variation */
  headline: React.ReactNode;
  subhead: string;
  cta: { label: string; href: string };
  image: {
    src: string;
    alt: string;
    width: number;
    height: number;
  };
  caption?: string;
}

export function HeroAsymmetric({
  eyebrow,
  headline,
  subhead,
  cta,
  image,
  caption,
}: HeroAsymmetricProps) {
  return (
    <section
      aria-labelledby="hero-heading"
      className="relative mx-auto max-w-[1400px] px-6 pt-20 pb-24 lg:pt-28 lg:pb-32"
    >
      {eyebrow && (
        <p className="mb-8 text-xs font-medium uppercase tracking-[0.22em] text-[var(--muted)]">
          {eyebrow}
        </p>
      )}

      <h1
        id="hero-heading"
        className="font-[var(--font-display)] text-[clamp(3rem,11vw,11rem)] font-medium leading-[0.92] tracking-[-0.04em] text-[var(--text)]"
      >
        {headline}
      </h1>

      <div className="mt-12 grid gap-8 lg:grid-cols-[1fr_1.2fr] lg:gap-16 lg:items-end">
        <div className="order-2 lg:order-1">
          <p className="max-w-md text-lg leading-relaxed text-[var(--muted)]">
            {subhead}
          </p>
          <a
            href={cta.href}
            className="mt-8 inline-flex items-center gap-3 text-base font-semibold text-[var(--text)] transition-colors hover:text-[var(--accent)] focus-visible:outline-none focus-visible:underline focus-visible:underline-offset-4 focus-visible:decoration-2"
          >
            {cta.label}
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden>
              <path d="M4 10h12M11 5l5 5-5 5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </a>
        </div>

        {/* Image extends past the column on purpose */}
        <figure className="order-1 lg:order-2 lg:-mr-12">
          <img
            src={image.src}
            alt={image.alt}
            width={image.width}
            height={image.height}
            className="w-full h-auto object-cover aspect-[4/5] lg:aspect-[5/6]"
            loading="eager"
            decoding="async"
          />
          {caption && (
            <figcaption className="mt-3 text-sm text-[var(--muted)] italic">
              {caption}
            </figcaption>
          )}
        </figure>
      </div>
    </section>
  );
}

export default HeroAsymmetric;
