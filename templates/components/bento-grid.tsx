/**
 * BentoGrid — Asymmetric bento layout for feature sections.
 *
 * References: apple.com (iPhone product pages), linear.app feature grids, vercel.com
 *
 * Replaces the "3 equal cards with emoji icons" AI default.
 *
 * Layout: 6-cell bento grid with varying sizes:
 * ┌────────────┬─────────┐
 * │  Cell 1    │ Cell 2  │
 * │  (large)   │         │
 * ├──────┬─────┴─────────┤
 * │Cell 3│   Cell 4      │
 * │      │   (wide)      │
 * ├──────┴────────┬──────┤
 * │   Cell 5       │Cell 6│
 * └────────────────┴──────┘
 *
 * Use 4-6 cells with varying importance. The largest cell = your hero feature.
 */

import { ReactNode } from 'react';

interface BentoCell {
  id: string;
  title: string;
  description: string;
  visual?: ReactNode;
  href?: string;
  /** Size class — controls grid placement */
  size: 'large' | 'wide' | 'tall' | 'square' | 'small';
}

interface BentoGridProps {
  cells: BentoCell[];
}

export function BentoGrid({ cells }: BentoGridProps) {
  return (
    <div
      className="grid gap-4 md:gap-5 grid-cols-2 md:grid-cols-4 auto-rows-[180px] md:auto-rows-[220px]"
      role="list"
    >
      {cells.map((cell) => (
        <BentoCellCard key={cell.id} cell={cell} />
      ))}
    </div>
  );
}

function BentoCellCard({ cell }: { cell: BentoCell }) {
  const sizeClasses: Record<BentoCell['size'], string> = {
    large: 'col-span-2 row-span-2',
    wide: 'col-span-2 row-span-1',
    tall: 'col-span-1 row-span-2',
    square: 'col-span-1 row-span-1',
    small: 'col-span-1 row-span-1',
  };

  const content = (
    <>
      <div className="relative z-10">
        <h3 className="font-[var(--font-display)] text-lg font-semibold tracking-tight text-[var(--text)] md:text-xl">
          {cell.title}
        </h3>
        <p className="mt-2 text-sm text-[var(--muted)] leading-relaxed">
          {cell.description}
        </p>
      </div>
      {cell.visual && (
        <div className="absolute inset-x-6 bottom-6 h-1/2 overflow-hidden">
          {cell.visual}
        </div>
      )}
    </>
  );

  const baseClass = [
    'group relative overflow-hidden rounded-2xl border border-[var(--border)] bg-[var(--surface)] p-6',
    'transition-all duration-300',
    'hover:border-[var(--accent)]/30 hover:shadow-[0_1px_2px_rgba(0,0,0,0.04),0_8px_24px_rgba(0,0,0,0.06)]',
    'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--accent)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--bg)]',
    sizeClasses[cell.size],
  ].join(' ');

  if (cell.href) {
    return (
      <a href={cell.href} role="listitem" className={baseClass}>
        {content}
      </a>
    );
  }
  return (
    <div role="listitem" className={baseClass}>
      {content}
    </div>
  );
}

export default BentoGrid;

// Example usage:
// <BentoGrid cells={[
//   {
//     id: '1',
//     title: 'Real-time collaboration',
//     description: 'See teammates\' cursors as they edit. No merge conflicts, ever.',
//     size: 'large',
//     visual: <CursorDemo />,
//     href: '/features/realtime'
//   },
//   {
//     id: '2',
//     title: 'Async video reviews',
//     description: 'Leave frame-perfect comments.',
//     size: 'wide',
//   },
//   // ... 2-4 more cells
// ]} />
