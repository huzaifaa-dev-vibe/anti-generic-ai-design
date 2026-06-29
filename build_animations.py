#!/usr/bin/env python3
"""
Build data/animations-100.json — 100 curated UI animations for the
Anti-Generic AI Design Skill repo.

Each entry follows the schema:
  id, name, category, type, duration_ms, easing, easing_name,
  properties_animated, when_to_use, when_not_to_use,
  code {css, js}, reduced_motion, performance_note, references

Run: python3 build_animations.py
Outputs: data/animations-100.json
"""
import json
from collections import Counter
from pathlib import Path


def E(id, name, category, type_, duration_ms, easing, easing_name, props,
      when_use, when_not, css, js, reduced, perf, refs):
    """Compact entry constructor."""
    return {
        "id": id,
        "name": name,
        "category": category,
        "type": type_,
        "duration_ms": duration_ms,
        "easing": easing,
        "easing_name": easing_name,
        "properties_animated": props,
        "when_to_use": when_use,
        "when_not_to_use": when_not,
        "code": {"css": css, "js": js},
        "reduced_motion": reduced,
        "performance_note": perf,
        "references": refs,
    }


ENTRIES = []


# ============================================================
# data-reveal (a001-a015) — 15 entries
# Counters, chart lines, progress bars, dials, number flips
# ============================================================
ENTRIES += [
    E("a001", "Counter Reveal", "data-reveal", "triggered", 2000,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Hero stats, pricing page numbers, dashboard KPIs. Animates from 0 to final value to make the scale visceral.",
      "When the number is not impressive on its own. Animating a small number (e.g. 12) makes it feel smaller.",
      """.counter { display: inline-block; font-variant-numeric: tabular-nums; }
.counter-animate { animation: counterPulse 2000ms cubic-bezier(0.25, 1, 0.5, 1); }
@keyframes counterPulse {
  0% { opacity: 0; transform: translateY(8px); }
  100% { opacity: 1; transform: translateY(0); }
}""",
      """function animateCounter(el, target, duration = 2000) {
  const start = performance.now();
  function frame(now) {
    const t = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - t, 4); // easeOutQuart
    el.textContent = Math.floor(target * eased).toLocaleString();
    if (t < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}""",
      "Show final value immediately, no animation.",
      "Uses transform + opacity only — no layout thrash. Safe for 60fps.",
      ["stripe.com pricing", "linear.app hero"]),

    E("a002", "Chart Line Draw", "data-reveal", "triggered", 1500,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["stroke-dashoffset", "opacity"],
      "Line charts on dashboard load, earnings plots, hero stat charts where the upward trend should feel earned.",
      "For charts that update in real-time — the dasharray animation conflicts with live data updates.",
      """.chart-line {
  fill: none;
  stroke: #2563eb;
  stroke-width: 2;
  stroke-linecap: round;
  opacity: 0;
}
.chart-line.draw {
  stroke-dasharray: var(--len);
  stroke-dashoffset: var(--len);
  animation: drawLine 1500ms cubic-bezier(0.65, 0, 0.35, 1) forwards;
}
@keyframes drawLine {
  0% { opacity: 0; }
  10% { opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 1; }
}""",
      """function drawChart(pathEl) {
  const len = pathEl.getTotalLength();
  pathEl.style.setProperty('--len', len);
  pathEl.classList.add('draw');
}
// Usage: drawChart(document.querySelector('.chart-line'));""",
      "Set stroke-dashoffset to 0 immediately, show full chart.",
      "stroke-dashoffset triggers repaint but not layout. Fine for SVG under 1000 nodes.",
      ["stripe.com dashboard", "vercel.com analytics"]),

    E("a003", "Progress Bar Fill", "data-reveal", "triggered", 1200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "File uploads, multi-step form progress, onboarding completion percentage where the end value is known.",
      "For indeterminate processes — use the indeterminate variant instead, or users will think it is stuck.",
      """.progress { width: 100%; height: 4px; background: rgba(0,0,0,0.08); border-radius: 999px; overflow: hidden; }
.progress-fill {
  height: 100%;
  background: #2563eb;
  border-radius: 999px;
  transform: scaleX(0);
  transform-origin: left center;
  opacity: 0;
}
.progress-fill.run {
  animation: fill 1200ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
@keyframes fill {
  0% { transform: scaleX(0); opacity: 0; }
  10% { opacity: 1; }
  100% { transform: scaleX(var(--p, 1)); opacity: 1; }
}""",
      """function setProgress(el, percent) {
  el.style.setProperty('--p', percent / 100);
  el.classList.add('run');
}""",
      "Set transform: scaleX(finalPercent) immediately, no animation.",
      "transform: scaleX is GPU-composited — 60fps safe even at 4K.",
      ["linear.app", "notion.so"]),

    E("a004", "Percentage Dial", "data-reveal", "triggered", 1800,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["stroke-dashoffset", "opacity"],
      "Goal tracking rings, completion percentages, hero stats with a circular motif.",
      "When the percentage is below 5% — the arc becomes nearly invisible and the dial reads as empty.",
      """.dial { transform: rotate(-90deg); }
.dial-track { fill: none; stroke: rgba(0,0,0,0.08); stroke-width: 8; }
.dial-fill {
  fill: none;
  stroke: #2563eb;
  stroke-width: 8;
  stroke-linecap: round;
  stroke-dasharray: var(--circ);
  stroke-dashoffset: var(--circ);
  opacity: 0;
}
.dial-fill.run {
  animation: dialSweep 1800ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
@keyframes dialSweep {
  0% { opacity: 0; }
  10% { opacity: 1; }
  100% { stroke-dashoffset: var(--final); opacity: 1; }
}""",
      """function setupDial(circle, percent) {
  const r = circle.r.baseVal.value;
  const circ = 2 * Math.PI * r;
  circle.style.setProperty('--circ', circ);
  circle.style.setProperty('--final', circ * (1 - percent / 100));
  circle.classList.add('run');
}""",
      "Set stroke-dashoffset to final value immediately.",
      "SVG stroke-dashoffset repaints — fine for one dial, janky with 10+ simultaneous dials.",
      ["apple.com fitness", "strava.com"]),

    E("a005", "Number Flip", "data-reveal", "triggered", 600,
      "cubic-bezier(0.83, 0, 0.17, 1)", "easeInOutQuint",
      ["transform", "opacity"],
      "Live scores, stock tickers, time displays where the number changes often and the change itself is the signal.",
      "When numbers change rarely — feels gimmicky if used once per session.",
      """.flip-digit {
  display: inline-block;
  perspective: 400px;
}
.flip-digit .digit {
  display: inline-block;
  transform-style: preserve-3d;
  transition: transform 600ms cubic-bezier(0.83, 0, 0.17, 1), opacity 600ms cubic-bezier(0.83, 0, 0.17, 1);
}
.flip-digit .digit.out {
  transform: rotateX(90deg);
  opacity: 0;
}
.flip-digit .digit.in {
  transform: rotateX(-90deg);
  opacity: 0;
}""",
      """function flipDigit(el, newValue) {
  const old = el.querySelector('.digit:not(.out):not(.in)');
  if (old) old.classList.add('out');
  const next = document.createElement('span');
  next.className = 'digit in';
  next.textContent = newValue;
  el.appendChild(next);
  requestAnimationFrame(() => {
    next.classList.remove('in');
    setTimeout(() => old && old.remove(), 600);
  });
}""",
      "Show new number immediately, no flip.",
      "rotateX triggers 3D context — keep flip-digit count under 8 for 60fps.",
      ["coinbase.com", "apple.com clock"]),

    E("a006", "Bar Chart Grow Up", "data-reveal", "triggered", 800,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Analytics dashboards, comparison bar charts where bars represent comparable values and the bounce adds liveliness.",
      "For stacked bars — the scaleY conflicts with internal segment proportions and breaks the visual stack.",
      """.bar {
  transform: scaleY(0);
  transform-origin: bottom center;
  opacity: 0;
}
.bar.run {
  animation: growUp 800ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
@keyframes growUp {
  0% { transform: scaleY(0); opacity: 0; }
  100% { transform: scaleY(1); opacity: 1; }
}""",
      """function growBars(bars, stagger = 80) {
  bars.forEach((bar, i) => {
    bar.style.animationDelay = (i * stagger) + 'ms';
    bar.classList.add('run');
  });
}""",
      "Set transform: scaleY(1) immediately.",
      "transform: scaleY with transform-origin: bottom is GPU-composited — 60fps safe.",
      ["vercel.com", "mixpanel.com"]),

    E("a007", "Donut Chart Sweep", "data-reveal", "triggered", 1400,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["stroke-dashoffset"],
      "Budget breakdowns, traffic source splits, percentage composition where each segment sweeps in turn.",
      "For 7+ segments — the sequential sweep becomes hard to follow and reads as a long wait.",
      """.donut-seg {
  fill: none;
  stroke-width: 16;
  stroke-dasharray: var(--seg-len) var(--gap);
  stroke-dashoffset: var(--start-offset);
  opacity: 0;
}
.donut-seg.run {
  animation: sweep 1400ms cubic-bezier(0.65, 0, 0.35, 1) forwards;
  animation-delay: var(--delay, 0ms);
}
@keyframes sweep {
  0% { opacity: 0; stroke-dashoffset: calc(var(--start-offset) + var(--seg-len)); }
  20% { opacity: 1; }
  100% { opacity: 1; stroke-dashoffset: var(--start-offset); }
}""",
      """function layoutDonut(segments) {
  // segments: [{el, percent, color}]
  const r = segments[0].el.r.baseVal.value;
  const circ = 2 * Math.PI * r;
  let acc = 0;
  segments.forEach((s, i) => {
    const segLen = circ * (s.percent / 100);
    s.el.style.setProperty('--seg-len', segLen);
    s.el.style.setProperty('--gap', circ - segLen);
    s.el.style.setProperty('--start-offset', -acc);
    s.el.style.setProperty('--delay', (i * 200) + 'ms');
    s.el.classList.add('run');
    acc += segLen;
  });
}""",
      "Set stroke-dashoffset to start-offset immediately.",
      "SVG repaints — fine for one donut, avoid animating 5+ simultaneously.",
      ["linear.app", "plaid.com"]),

    E("a008", "Stat Card Count Up + Reveal", "data-reveal", "triggered", 1600,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Dashboard KPI cards revealed on initial page load, hero stat sections where the card and the number arrive together.",
      "In dense tables — the staggered reveal feels slow when there are 10+ cards waiting to animate.",
      """.stat-card { opacity: 0; transform: translateY(16px); }
.stat-card.run {
  animation: statReveal 1600ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
@keyframes statReveal {
  0% { opacity: 0; transform: translateY(16px); }
  100% { opacity: 1; transform: translateY(0); }
}
.stat-card .stat-value { font-variant-numeric: tabular-nums; }""",
      """function revealStatCards(cards) {
  cards.forEach((card, i) => {
    card.style.animationDelay = (i * 120) + 'ms';
    card.classList.add('run');
    const valEl = card.querySelector('.stat-value');
    const target = Number(valEl.dataset.value);
    setTimeout(() => animateCounter(valEl, target, 1400), i * 120);
  });
}
function animateCounter(el, target, duration) {
  const start = performance.now();
  function frame(now) {
    const t = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - t, 4);
    el.textContent = Math.floor(target * eased).toLocaleString();
    if (t < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}""",
      "Show all cards at full opacity with final values immediately.",
      "transform + opacity only — 60fps safe.",
      ["stripe.com", "vercel.com"]),

    E("a009", "Heatmap Cell Fade", "data-reveal", "triggered", 1200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["opacity", "filter"],
      "GitHub-style contribution grids, activity calendars, density visualizations where the cascade reveals the pattern.",
      "For real-time heatmaps — the staggered reveal conflicts with live data updates and reads as a glitch.",
      """.heat-cell {
  opacity: 0;
  filter: brightness(0.4);
  transform: scale(0.85);
}
.heat-cell.run {
  animation: heatFade 1200ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
  animation-delay: var(--delay, 0ms);
}
@keyframes heatFade {
  0% { opacity: 0; filter: brightness(0.4); transform: scale(0.85); }
  100% { opacity: 1; filter: brightness(1); transform: scale(1); }
}""",
      """function revealHeatmap(grid, rowStagger = 30) {
  const cells = grid.querySelectorAll('.heat-cell');
  cells.forEach((c, i) => {
    const row = Math.floor(i / 7); // 7 cols (week)
    c.style.setProperty('--delay', (row * rowStagger) + 'ms');
    c.classList.add('run');
  });
}""",
      "Set opacity: 1, filter: none, transform: none immediately.",
      "filter: brightness triggers repaint — keep grid under 365 cells.",
      ["github.com", "gitlab.com"]),

    E("a010", "Sparkline Draw", "data-reveal", "triggered", 1000,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["stroke-dashoffset"],
      "Inline metrics in tables, mini trends in cards, compact KPI displays where the line is small but the trend matters.",
      "For lines with steep vertical jumps — the drawing reveals the jumps awkwardly and looks glitchy.",
      """.spark {
  fill: none;
  stroke: currentColor;
  stroke-width: 1.5;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: var(--len);
  stroke-dashoffset: var(--len);
}
.spark.run {
  animation: sparkDraw 1000ms cubic-bezier(0.65, 0, 0.35, 1) forwards;
}
@keyframes sparkDraw {
  to { stroke-dashoffset: 0; }
}""",
      """function drawSpark(pathEl) {
  const len = pathEl.getTotalLength();
  pathEl.style.setProperty('--len', len);
  pathEl.classList.add('run');
}""",
      "Set stroke-dashoffset to 0 immediately.",
      "Single SVG path — negligible cost.",
      ["linear.app", "github.com insights"]),

    E("a011", "Table Row Stagger Reveal", "data-reveal", "triggered", 400,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Search results, data tables, leaderboard rankings — first 5-10 rows reveal in sequence to draw the eye.",
      "When there are 50+ rows — the stagger becomes a multi-second wait. Cap at 8 rows then show the rest instantly.",
      """.row-reveal { opacity: 0; transform: translateY(8px); }
.row-reveal.run {
  animation: rowUp 400ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
  animation-delay: var(--delay, 0ms);
}
@keyframes rowUp {
  to { opacity: 1; transform: translateY(0); }
}""",
      """function staggerRows(rows, max = 8, step = 50) {
  rows.forEach((r, i) => {
    if (i < max) {
      r.style.setProperty('--delay', (i * step) + 'ms');
      r.classList.add('run');
    } else {
      r.style.opacity = 1;
      r.style.transform = 'none';
    }
  });
}""",
      "Show all rows at full opacity immediately, no transform.",
      "transform + opacity — 60fps safe. Cap stagger at 8 rows for tables.",
      ["algolia.com", "linear.app issues"]),

    E("a012", "Gauge Needle Sweep", "data-reveal", "triggered", 1500,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform"],
      "Speedometers, performance scores, health indicators where slight overshoot reads as 'settling' into place.",
      "For precise readings — the overshoot reads as inaccurate or jittery, undermining trust.",
      """.gauge-needle {
  transform-origin: 50% 100%;
  transform: rotate(-90deg);
  transition: transform 1500ms cubic-bezier(0.34, 1.56, 0.64, 1);
}""",
      """function setGauge(needle, percent) {
  // percent 0-100 maps to -90deg (left) .. 90deg (right)
  const angle = -90 + (percent / 100) * 180;
  needle.style.transform = `rotate(${angle}deg)`;
}""",
      "Set transform: rotate(finalAngle) immediately, no transition.",
      "transform: rotate is GPU-composited — 60fps safe.",
      ["fast.com", "apple.com fitness"]),

    E("a013", "Avatar Stack Reveal", "data-reveal", "triggered", 600,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Social proof — 'joined by these people', testimonial groups, team pages where each avatar pops in.",
      "When the count exceeds 8 — the stack becomes unreadable and the cascade becomes a wait.",
      """.avatar-stack { display: flex; }
.avatar-stack > * {
  opacity: 0;
  transform: scale(0.5) translateX(8px);
  margin-left: -8px;
}
.avatar-stack.run > *.in {
  animation: popIn 600ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  animation-delay: var(--delay, 0ms);
}
@keyframes popIn {
  to { opacity: 1; transform: scale(1) translateX(0); }
}""",
      """function revealStack(stack, step = 80) {
  const avatars = stack.querySelectorAll('img, .avatar');
  avatars.forEach((a, i) => {
    a.style.setProperty('--delay', (i * step) + 'ms');
    a.classList.add('in');
  });
  stack.classList.add('run');
}""",
      "Show all avatars at full opacity and scale 1 immediately.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "notion.so"]),

    E("a014", "Badge Count Pop", "data-reveal", "triggered", 300,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Notification badges, cart count updates, unread message indicators on incremental change.",
      "On every page load — feels like a constant nag for unchanged counts. Reserve for changes.",
      """.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 18px;
  height: 18px;
  padding: 0 5px;
  border-radius: 999px;
  background: #dc2626;
  color: white;
  font-size: 11px;
  font-weight: 600;
}
.badge.pop { animation: badgePop 300ms cubic-bezier(0.34, 1.56, 0.64, 1); }
@keyframes badgePop {
  0% { transform: scale(0); opacity: 0; }
  60% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); opacity: 1; }
}""",
      """function popBadge(el) {
  el.classList.remove('pop');
  void el.offsetWidth; // reflow to restart animation
  el.classList.add('pop');
}""",
      "Show badge at full scale immediately.",
      "transform + opacity — 60fps safe.",
      ["twitter.com", "slack.com"]),

    E("a015", "KPI Delta Arrow Reveal", "data-reveal", "triggered", 1000,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Dashboard KPI delta indicators (e.g. '+12.4% vs last week') next to the main stat, arriving slightly after.",
      "When the delta is flat (0%) — animating zero movement is misleading. Hide the arrow or show 'no change'.",
      """.kpi-delta {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  opacity: 0;
  transform: translateX(-8px);
}
.kpi-delta.run { animation: deltaIn 1000ms cubic-bezier(0.25, 1, 0.5, 1) forwards; }
.kpi-delta.up .arrow { transform: rotate(-45deg); }
.kpi-delta.down .arrow { transform: rotate(45deg); }
.kpi-delta .arrow { display: inline-block; transition: transform 300ms; }
@keyframes deltaIn {
  to { opacity: 1; transform: translateX(0); }
}""",
      """function showDelta(el, percent) {
  const isUp = percent >= 0;
  el.classList.toggle('up', isUp);
  el.classList.toggle('down', !isUp);
  el.querySelector('.val').textContent = (isUp ? '+' : '') + percent.toFixed(1) + '%';
  el.classList.add('run');
}""",
      "Show delta at final position immediately, no transform.",
      "transform + opacity — 60fps safe.",
      ["vercel.com", "stripe.com"]),

]


# ============================================================
# page-transition (a016-a025) — 10 entries
# View Transitions API, route fades, modal zoom-in
# ============================================================
ENTRIES += [
    E("a016", "View Transitions Cross-Fade", "page-transition", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["opacity"],
      "SPA route changes, list-to-detail navigations where a simple cross-fade preserves context.",
      "For back-button navigations — the fade feels slow for quick back/forward; instant is better.",
      """@view-transition { navigation: auto; }
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 250ms;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  mix-blend-mode: normal;
}
::view-transition-old(root) { animation-name: vt-fade-out; }
::view-transition-new(root) { animation-name: vt-fade-in; }
@keyframes vt-fade-out { to { opacity: 0; } }
@keyframes vt-fade-in { from { opacity: 0; } }""",
      """// Trigger a view transition manually:
if (document.startViewTransition) {
  document.startViewTransition(() => updateDOM());
} else {
  updateDOM(); // fallback
}""",
      "Skip the transition; update DOM immediately.",
      "opacity-only cross-fade — GPU-composited, 60fps safe.",
      ["developer.chrome.com", "stripe.com"]),

    E("a017", "Route Slide (Mobile)", "page-transition", "triggered", 300,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Mobile web apps, settings → detail navigations where the new page slides in from the right.",
      "On desktop — feels like a phone, not a desktop pattern. Use cross-fade or instant for desktop.",
      """.route-slide-in {
  animation: slideIn 300ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
.route-slide-out {
  animation: slideOut 300ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
}
@keyframes slideIn {
  from { transform: translateX(100%); opacity: 0.5; }
  to { transform: translateX(0); opacity: 1; }
}
@keyframes slideOut {
  from { transform: translateX(0); opacity: 1; }
  to { transform: translateX(-30%); opacity: 0.5; }
}""",
      """function navigate(newPageEl) {
  const cur = document.querySelector('.page.current');
  cur.classList.add('route-slide-out');
  newPageEl.classList.add('route-slide-in', 'current');
  cur.classList.remove('current');
  setTimeout(() => cur.remove(), 300);
}""",
      "Show new page immediately, no slide.",
      "transform + opacity — 60fps safe on mobile.",
      ["airbnb.com mobile", "linear.app mobile"]),

    E("a018", "Modal Zoom-In", "page-transition", "triggered", 200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Confirmation dialogs, image lightboxes, settings modals where the zoom feels like focusing attention.",
      "For full-screen takeovers — use slide-in instead; zoom on full-screen feels disorienting.",
      """.modal-backdrop {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.5);
  opacity: 0;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.modal-backdrop.open { opacity: 1; }
.modal {
  transform: scale(0.95);
  opacity: 0;
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1), opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.modal-backdrop.open .modal { transform: scale(1); opacity: 1; }""",
      """function openModal(backdrop) {
  backdrop.classList.add('open');
  backdrop.style.display = 'block';
  // Focus the first focusable element inside .modal
  const focusable = backdrop.querySelector('button, [href], input, [tabindex]:not([tabindex="-1"])');
  focusable && focusable.focus();
}""",
      "Show modal at scale(1) and opacity 1 immediately.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "notion.so"]),

    E("a019", "Page Curtain Reveal", "page-transition", "triggered", 800,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["clip-path", "transform"],
      "Marketing site landings, case study intros where a branded reveal moment sets the tone.",
      "On every navigation — the curtain reveal gets tiring fast. Reserve for first-load only.",
      """.curtain {
  position: fixed; inset: 0;
  z-index: 9999;
  background: #000;
  clip-path: inset(0 0 0 0);
  animation: curtainReveal 800ms cubic-bezier(0.65, 0, 0.35, 1) forwards;
  animation-delay: 200ms;
  pointer-events: none;
}
@keyframes curtainReveal {
  to { clip-path: inset(0 0 100% 0); }
}""",
      """// Add curtain element on first load only:
if (!sessionStorage.getItem('curtainShown')) {
  const c = document.createElement('div');
  c.className = 'curtain';
  document.body.appendChild(c);
  sessionStorage.setItem('curtainShown', '1');
  setTimeout(() => c.remove(), 1100);
}""",
      "Do not show curtain; reveal content immediately.",
      "clip-path animation triggers repaint but no layout — 60fps safe.",
      ["apple.com product launches", "stripe.com sessions"]),

    E("a020", "Tab Slide Underline", "page-transition", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Tabbed interfaces, segmented controls, settings panels where the underline tracks the active tab.",
      "When tabs have very different widths — the slide reveals the math and looks jittery. Use width animation instead.",
      """.tabs { position: relative; display: flex; }
.tab-indicator {
  position: absolute;
  bottom: 0;
  height: 2px;
  background: #2563eb;
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1), width 250ms cubic-bezier(0.4, 0, 0.2, 1);
  left: 0;
}""",
      """function moveIndicator(indicator, activeTab) {
  const rect = activeTab.getBoundingClientRect();
  const parentRect = activeTab.parentElement.getBoundingClientRect();
  indicator.style.width = rect.width + 'px';
  indicator.style.transform = `translateX(${rect.left - parentRect.left}px)`;
}
// On tab click: moveIndicator(indicatorEl, clickedTabEl)""",
      "Move underline instantly to active tab, no transition.",
      "transform + width on absolute element — 60fps safe.",
      ["linear.app", "vercel.com dashboard"]),

    E("a021", "Drawer Push", "page-transition", "triggered", 300,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Filters, mobile nav drawers, cart drawers where the main content slides aside to reveal the drawer.",
      "On desktop with multi-column layouts — the push breaks grid alignment and feels awkward. Use overlay instead.",
      """.drawer-wrap { display: grid; grid-template-columns: 1fr; transition: transform 300ms cubic-bezier(0.4, 0, 0.2, 1); }
.drawer-wrap.open { transform: translateX(-280px); }
.drawer {
  position: fixed; top: 0; right: 0; bottom: 0;
  width: 280px;
  transform: translateX(100%);
  transition: transform 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.drawer.open { transform: translateX(0); }""",
      """function toggleDrawer(wrap, drawer) {
  const open = !drawer.classList.contains('open');
  wrap.classList.toggle('open', open);
  drawer.classList.toggle('open', open);
}""",
      "Show drawer immediately at translateX(0); do not push main content.",
      "transform only — 60fps safe.",
      ["stripe.com docs", "airbnb.com filters"]),

    E("a022", "Image Morph Route Transition", "page-transition", "triggered", 400,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "clip-path", "opacity"],
      "Product card → product detail, gallery thumbnail → full image where the shared image morphs between views.",
      "When source and target have very different aspect ratios — the morph looks broken. Fall back to cross-fade.",
      """::view-transition-old(shared-img),
::view-transition-new(shared-img) {
  animation-duration: 400ms;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  mix-blend-mode: normal;
  overflow: clip;
}
::view-transition-old(shared-img) { animation-name: morph-out; }
::view-transition-new(shared-img) { animation-name: morph-in; }
@keyframes morph-out { to { opacity: 0; } }
@keyframes morph-in { from { opacity: 0; } }""",
      """// Tag the shared image on both pages with view-transition-name:
// <img style="view-transition-name: product-img-42" src="...">
async function go(imageId) {
  if (!document.startViewTransition) return location.href = '/p/' + imageId;
  await document.startViewTransition(() => {
    location.href = '/p/' + imageId;
  }).ready;
}""",
      "Skip the morph; navigate instantly.",
      "View Transitions API uses GPU compositing — 60fps safe in Chrome 111+.",
      ["linear.app changelog", "apple.com product pages"]),

    E("a023", "Side Panel Slide", "page-transition", "triggered", 280,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Settings panels, advanced filters, contextual help that slides in from the right as an overlay.",
      "For primary content — side panels signal 'secondary'. Use full page navigation for primary flows.",
      """.side-panel {
  position: fixed; top: 0; right: 0; bottom: 0;
  width: 400px; max-width: 90vw;
  background: white;
  box-shadow: -8px 0 24px rgba(0,0,0,0.12);
  transform: translateX(100%);
  opacity: 0;
  transition: transform 280ms cubic-bezier(0.4, 0, 0.2, 1), opacity 280ms cubic-bezier(0.4, 0, 0.2, 1);
}
.side-panel.open { transform: translateX(0); opacity: 1; }""",
      """function openPanel(panel) {
  panel.classList.add('open');
  panel.querySelector('input, button')?.focus();
}
function closePanel(panel) {
  panel.classList.remove('open');
}""",
      "Show panel immediately at translateX(0), opacity 1.",
      "transform + opacity — 60fps safe.",
      ["notion.so settings", "linear.app filters"]),

    E("a024", "Bottom Sheet Rise", "page-transition", "triggered", 320,
      "cubic-bezier(0.32, 0.72, 0, 1)", "iosEaseOut",
      ["transform", "opacity"],
      "Mobile action menus, filter sheets, attachment pickers where a sheet rises from the bottom edge.",
      "On desktop — bottom sheets feel mobile-only. Use a side panel or modal instead.",
      """.sheet-backdrop {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.4);
  opacity: 0;
  transition: opacity 320ms cubic-bezier(0.32, 0.72, 0, 1);
}
.sheet-backdrop.open { opacity: 1; }
.sheet {
  position: fixed; left: 0; right: 0; bottom: 0;
  background: white;
  border-radius: 16px 16px 0 0;
  transform: translateY(100%);
  transition: transform 320ms cubic-bezier(0.32, 0.72, 0, 1);
}
.sheet-backdrop.open .sheet { transform: translateY(0); }""",
      """function openSheet(wrap) {
  wrap.classList.add('open');
  // Drag-to-dismiss:
  const sheet = wrap.querySelector('.sheet');
  let startY = 0;
  sheet.addEventListener('touchstart', e => startY = e.touches[0].clientY);
  sheet.addEventListener('touchmove', e => {
    const dy = e.touches[0].clientY - startY;
    if (dy > 0) sheet.style.transform = `translateY(${dy}px)`;
  });
  sheet.addEventListener('touchend', e => {
    if (parseInt(sheet.style.transform.replace(/\\D/g, '')) > 100) wrap.classList.remove('open');
    sheet.style.transform = '';
  });
}""",
      "Show sheet at translateY(0) and backdrop at opacity 1 immediately.",
      "transform + opacity — 60fps safe on mobile.",
      ["apple.com maps", "google.com maps"]),

    E("a025", "Hero Shared Element Transition", "page-transition", "triggered", 350,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "List → detail navigations where a card or avatar is shared between the two views.",
      "When the shared element has a different visual treatment on each page (different crop, filter, border) — the morph looks broken.",
      """::view-transition-old(hero-shared) {
  animation: 350ms cubic-bezier(0.4, 0, 0.2, 1) both fade-out;
}
::view-transition-new(hero-shared) {
  animation: 350ms cubic-bezier(0.4, 0, 0.2, 1) both fade-in;
}
@keyframes fade-out { to { opacity: 0; } }
@keyframes fade-in { from { opacity: 0; } }""",
      """// On the list page, set view-transition-name dynamically:
document.querySelectorAll('.card').forEach((c, i) => {
  c.style.viewTransitionName = `card-${i}`;
});
// On the detail page, set the same name on the hero:
// <div class="hero" style="view-transition-name: card-3">
// Navigate via SPA:
async function navigateToDetail(cardIndex) {
  if (!document.startViewTransition) return location.href = `/d/${cardIndex}`;
  document.startViewTransition(() => location.href = `/d/${cardIndex}`);
}""",
      "Skip the morph; navigate instantly.",
      "View Transitions API — GPU-composited in Chrome 111+. Graceful fallback in other browsers.",
      ["linear.app", "apple.com music"]),
]


# ============================================================
# scroll-triggered (a026-a040) — 15 entries
# Fade-in on scroll, parallax, sticky-stack
# ============================================================
ENTRIES += [
    E("a026", "Fade In Up On Scroll", "scroll-triggered", "scroll", 600,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Long-form content, marketing sections, case study paragraphs revealed as they enter the viewport.",
      "For above-the-fold content — it should be visible immediately, not wait for scroll-trigger to fire.",
      """.reveal { opacity: 0; transform: translateY(24px); }
.reveal.in {
  animation: revealUp 600ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
}
@keyframes revealUp {
  to { opacity: 1; transform: translateY(0); }
}""",
      """const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));""",
      "Show all content at full opacity immediately, no transform.",
      "transform + opacity — 60fps safe.",
      ["framer.com", "linear.app"]),

    E("a027", "Parallax Background", "scroll-triggered", "scroll", 0,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Hero sections, image-heavy marketing pages, storytelling pages where depth adds atmosphere.",
      "On mobile — parallax causes jank and battery drain. Also avoid with content users need to read precisely.",
      """.parallax-bg {
  will-change: transform;
  transform: translate3d(0, 0, 0);
}""",
      """function setupParallax(el, speed = 0.3) {
  let ticking = false;
  function update() {
    const rect = el.parentElement.getBoundingClientRect();
    const offset = rect.top * speed;
    el.style.transform = `translate3d(0, ${offset}px, 0)`;
    ticking = false;
  }
  window.addEventListener('scroll', () => {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
}""",
      "Disable parallax; fix background position with no transform.",
      "transform on a GPU layer with will-change — 60fps on desktop. Disable on mobile.",
      ["apple.com", "airbnb.com"]),

    E("a028", "Sticky Header Shrink", "scroll-triggered", "scroll", 200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "background-color"],
      "Blogs, docs, marketing sites with long content where shrinking the header frees reading space.",
      "On pages shorter than 2 viewport heights — there is nothing to shrink for; the header never changes.",
      """.site-header {
  position: sticky; top: 0; z-index: 50;
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(8px);
  transition: background-color 200ms cubic-bezier(0.4, 0, 0.2, 1),
              padding 0ms 200ms; /* padding snaps instantly after transition */
  padding-block: 20px;
}
.site-header.shrunk {
  padding-block: 8px;
  background: rgba(255,255,255,0.95);
}
.site-header .logo {
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: left center;
}
.site-header.shrunk .logo { transform: scale(0.85); }""",
      """const header = document.querySelector('.site-header');
let last = 0;
window.addEventListener('scroll', () => {
  const y = window.scrollY;
  if (y > 80 && last <= 80) header.classList.add('shrunk');
  else if (y <= 80 && last > 80) header.classList.remove('shrunk');
  last = y;
}, { passive: true });""",
      "Keep header at full size always; do not shrink on scroll.",
      "Padding snap is instant (no transition); transform on logo is GPU-composited — 60fps safe.",
      ["medium.com", "nytimes.com"]),

    E("a029", "Sticky Stack Cards", "scroll-triggered", "scroll", 0,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["transform", "opacity"],
      "Product feature storytelling, case study deep-dives where each card stacks as the user scrolls.",
      "For content meant to be scanned — the stacking forces sequential reading and feels slow.",
      """.stack-wrap { height: 400vh; /* 4 cards × 100vh */ }
.stack-card {
  position: sticky; top: 10vh;
  height: 80vh;
  transform-origin: center bottom;
  transition: transform 200ms cubic-bezier(0.65, 0, 0.35, 1),
              opacity 200ms cubic-bezier(0.65, 0, 0.35, 1);
}""",
      """const cards = document.querySelectorAll('.stack-card');
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    const r = e.intersectionRatio;
    e.target.style.transform = `scale(${0.92 + 0.08 * r})`;
    e.target.style.opacity = 0.4 + 0.6 * r;
  });
}, { threshold: [0, 0.25, 0.5, 0.75, 1] });
cards.forEach(c => io.observe(c));""",
      "Show cards in normal scroll flow, no stacking or scale.",
      "position: sticky + transform — 60fps safe. Cap at 5 cards to avoid layout complexity.",
      ["apple.com AirPods Pro", "apple.com iPhone"]),

    E("a030", "Scroll-Driven Progress Bar", "scroll-triggered", "scroll", 0,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Long articles, docs, onboarding flows where a top progress bar tracks reading position.",
      "On short pages — the bar barely moves and reads as decorative noise.",
      """.scroll-progress {
  position: fixed; top: 0; left: 0;
  height: 3px; width: 100%;
  background: #2563eb;
  transform: scaleX(0);
  transform-origin: left center;
  z-index: 100;
  animation: progress linear;
  animation-timeline: scroll(root);
}
@keyframes progress {
  to { transform: scaleX(1); }
}""",
      """// JS fallback for browsers without animation-timeline:
const bar = document.querySelector('.scroll-progress');
let ticking = false;
function update() {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  const p = Math.max(0, Math.min(1, window.scrollY / max));
  bar.style.transform = `scaleX(${p})`;
  ticking = false;
}
window.addEventListener('scroll', () => {
  if (!ticking) { requestAnimationFrame(update); ticking = true; }
}, { passive: true });""",
      "Hide the progress bar or show it static at 100%.",
      "Native scroll-timeline is the cheapest (no JS). rAF fallback is 60fps safe.",
      ["github.com docs", "developer.mozilla.org"]),

    E("a031", "Horizontal Scroll Pin Section", "scroll-triggered", "scroll", 0,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["transform"],
      "Storytelling sections, product showcases, image galleries where horizontal movement is the rhythm.",
      "When the section has interactive elements — users expect vertical scroll, not horizontal surprise.",
      """.h-pin-wrap { height: 400vh; position: relative; }
.h-pin-sticky {
  position: sticky; top: 0;
  height: 100vh; overflow: hidden;
}
.h-pin-track {
  display: flex; height: 100%;
  will-change: transform;
}""",
      """const wrap = document.querySelector('.h-pin-wrap');
const track = document.querySelector('.h-pin-track');
const trackWidth = track.scrollWidth - window.innerWidth;
function update() {
  const r = wrap.getBoundingClientRect();
  const total = wrap.offsetHeight - window.innerHeight;
  const progress = Math.max(0, Math.min(1, -r.top / total));
  track.style.transform = `translate3d(${-progress * trackWidth}px, 0, 0)`;
}
window.addEventListener('scroll', () => requestAnimationFrame(update), { passive: true });""",
      "Allow normal vertical scroll through the section, no horizontal pin.",
      "position: sticky + transform — 60fps safe.",
      ["apple.com", "nike.com"]),

    E("a032", "Scroll-Linked Image Reveal", "scroll-triggered", "scroll", 800,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["clip-path", "transform"],
      "Editorial layouts, portfolio grids, image-first storytelling where each image wipes into view.",
      "For images with text overlays — the clip reveals the text awkwardly mid-wipe.",
      """.wipe-img {
  clip-path: inset(0 100% 0 0);
  transform: scale(1.15);
  transition: clip-path 800ms cubic-bezier(0.65, 0, 0.35, 1),
              transform 800ms cubic-bezier(0.65, 0, 0.35, 1);
}
.wipe-img.in {
  clip-path: inset(0 0 0 0);
  transform: scale(1);
}""",
      """const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.25 });
document.querySelectorAll('.wipe-img').forEach(el => io.observe(el));""",
      "Show image with no clip-path, full opacity and scale 1 immediately.",
      "clip-path triggers repaint — fine for one image at a time.",
      ["apple.com", "pentagram.com"]),

    E("a033", "Text Marquee Scroll", "scroll-triggered", "ambient", 20000,
      "cubic-bezier(0.45, 0.05, 0.55, 0.95)", "linearLoop",
      ["transform"],
      "Logo walls, testimonial tickers, news headlines where continuous motion signals vitality.",
      "For text users must read — moving targets are hard to read and accessibility-hostile.",
      """.marquee {
  display: flex; overflow: hidden;
  -webkit-mask-image: linear-gradient(90deg, transparent, black 10%, black 90%, transparent);
}
.marquee-track {
  display: flex; flex-shrink: 0; gap: 48px;
  padding-right: 48px;
  animation: marquee 20000ms cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite;
  will-change: transform;
}
@keyframes marquee {
  to { transform: translateX(-50%); }
}
/* Duplicate content inside .marquee-track for seamless loop */""",
      """// Pause when offscreen for perf:
const m = document.querySelector('.marquee-track');
const io = new IntersectionObserver((entries) => {
  m.style.animationPlayState = entries[0].isIntersecting ? 'running' : 'paused';
});
io.observe(document.querySelector('.marquee'));""",
      "Show static text, no marquee. Optionally auto-rotate items every 5s.",
      "transform: translateX on a GPU layer — 60fps safe. Pause when offscreen via IntersectionObserver.",
      ["stripe.com homepage", "linear.app customers"]),

    E("a034", "Reveal Mask On Scroll", "scroll-triggered", "scroll", 1000,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["clip-path"],
      "Editorial headers, manifesto statements, premium product intros where a mask wipe adds drama.",
      "For body copy — the mask distracts from reading. Reserve for headlines only.",
      """.mask-reveal {
  clip-path: inset(0 0 100% 0);
  transition: clip-path 1000ms cubic-bezier(0.65, 0, 0.35, 1);
}
.mask-reveal.in { clip-path: inset(0 0 0 0); }""",
      """const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.5 });
document.querySelectorAll('.mask-reveal').forEach(el => io.observe(el));""",
      "Show text with no clip-path, full opacity immediately.",
      "clip-path triggers repaint — fine for short text.",
      ["apple.com", "boutique agency sites"]),

    E("a035", "Scroll-Driven Counter", "scroll-triggered", "scroll", 2000,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["opacity"],
      "Stats sections, impact pages, 'by the numbers' sections where the counter triggers on view.",
      "When the stat is in a busy section — the counter competes with other motion and loses impact.",
      """.stat-num {
  opacity: 0;
  font-variant-numeric: tabular-nums;
  transition: opacity 600ms cubic-bezier(0.25, 1, 0.5, 1);
}
.stat-num.in { opacity: 1; }""",
      """function setupScrollCounter(el) {
  const target = Number(el.dataset.value);
  let started = false;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting && !started) {
        started = true;
        el.classList.add('in');
        const start = performance.now();
        function frame(now) {
          const t = Math.min((now - start) / 2000, 1);
          const eased = 1 - Math.pow(1 - t, 4);
          el.textContent = Math.floor(target * eased).toLocaleString();
          if (t < 1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);
      }
    });
  }, { threshold: 0.5 });
  io.observe(el);
}""",
      "Show final value immediately, no animation.",
      "rAF counter + opacity transition — 60fps safe.",
      ["stripe.com", "plaid.com"]),

    E("a036", "Image Grid Sequential Reveal", "scroll-triggered", "scroll", 800,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Portfolio grids, gallery pages, product image showcases revealed as the grid enters view.",
      "For grids with 12+ images — the reveal takes too long. Cap stagger at 6 then show rest instantly.",
      """.grid-img {
  opacity: 0;
  transform: translateY(24px) scale(0.96);
}
.grid-img.in {
  animation: gridReveal 800ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
  animation-delay: var(--delay, 0ms);
}
@keyframes gridReveal {
  to { opacity: 1; transform: translateY(0) scale(1); }
}""",
      """function revealGrid(grid, step = 80, max = 6) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const imgs = grid.querySelectorAll('.grid-img');
        imgs.forEach((img, i) => {
          if (i < max) img.style.setProperty('--delay', (i * step) + 'ms');
          img.classList.add('in');
        });
        io.unobserve(grid);
      }
    });
  }, { threshold: 0.1 });
  io.observe(grid);
}""",
      "Show all images at full opacity immediately.",
      "transform + opacity — 60fps safe. Cap stagger count at 6.",
      ["behance.net", "dribbble.com"]),

    E("a037", "Back-to-Top Button Appear", "scroll-triggered", "scroll", 200,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Long articles, docs, blog posts where the button appears once the user has scrolled past 1 viewport.",
      "On pages where the footer is always visible — the button feels redundant.",
      """.back-to-top {
  position: fixed; bottom: 24px; right: 24px;
  opacity: 0;
  transform: translateY(16px) scale(0.8);
  pointer-events: none;
  transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1),
              opacity 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.back-to-top.show {
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}""",
      """const btn = document.querySelector('.back-to-top');
window.addEventListener('scroll', () => {
  btn.classList.toggle('show', window.scrollY > window.innerHeight);
}, { passive: true });
btn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));""",
      "Show button permanently or hide entirely; no scale animation.",
      "transform + opacity — 60fps safe.",
      ["github.com", "developer.mozilla.org"]),

    E("a038", "Number Counter On Viewport", "scroll-triggered", "scroll", 1800,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["opacity"],
      "Stats below the fold, impact sections, 'by the numbers' mid-page where the counter triggers once.",
      "When the same counter is on every page — repetition kills the impact.",
      """.viewport-counter {
  opacity: 0;
  transition: opacity 400ms cubic-bezier(0.25, 1, 0.5, 1);
  font-variant-numeric: tabular-nums;
}
.viewport-counter.in { opacity: 1; }""",
      """function setupViewportCounter(el) {
  let done = false;
  const target = Number(el.dataset.value);
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting && !done) {
        done = true;
        el.classList.add('in');
        const start = performance.now();
        function frame(now) {
          const t = Math.min((now - start) / 1800, 1);
          const eased = 1 - Math.pow(1 - t, 4);
          el.textContent = Math.floor(target * eased).toLocaleString();
          if (t < 1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);
        io.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  io.observe(el);
}""",
      "Show final value immediately, no animation.",
      "rAF counter — 60fps safe.",
      ["stripe.com", "vercel.com"]),

    E("a039", "Tilt Card On Scroll Velocity", "scroll-triggered", "scroll", 0,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Premium product showcases, design portfolios where cards tilt slightly based on scroll velocity.",
      "On mobile — scroll velocity feedback conflicts with native pull-to-refresh gestures.",
      """.tilt-card {
  will-change: transform;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1);
}""",
      """const card = document.querySelector('.tilt-card');
let lastY = window.scrollY, currentTilt = 0, targetTilt = 0;
window.addEventListener('scroll', () => {
  const y = window.scrollY;
  const v = y - lastY;
  lastY = y;
  targetTilt = Math.max(-6, Math.min(6, v * 0.3));
}, { passive: true });
function raf() {
  currentTilt += (targetTilt - currentTilt) * 0.1;
  targetTilt *= 0.92; // decay
  card.style.transform = `perspective(800px) rotateX(${-currentTilt}deg)`;
  requestAnimationFrame(raf);
}
raf();""",
      "Disable tilt; cards stay flat.",
      "transform: rotateX with perspective — 60fps with will-change.",
      ["awwwards.com", "apple.com"]),

    E("a040", "Scroll-Driven Background Color Shift", "scroll-triggered", "scroll", 0,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["background-color", "color"],
      "Long-form storytelling, brand sections, color-themed chapter breaks where the page mood shifts.",
      "With dark mode — the color shift competes with theme changes and feels chaotic.",
      """body {
  transition: background-color 400ms cubic-bezier(0.65, 0, 0.35, 1),
              color 400ms cubic-bezier(0.65, 0, 0.35, 1);
}""",
      """const sections = [
  { el: document.querySelector('#s1'), bg: '#0a0a0a', color: '#fafafa' },
  { el: document.querySelector('#s2'), bg: '#fef3c7', color: '#1a1a1a' },
  { el: document.querySelector('#s3'), bg: '#1e3a8a', color: '#fafafa' },
];
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      document.body.style.backgroundColor = e.target.dataset.bg;
      document.body.style.color = e.target.dataset.color;
    }
  });
}, { threshold: 0.5 });
sections.forEach(s => { s.el.dataset.bg = s.bg; s.el.dataset.color = s.color; io.observe(s.el); });""",
      "Use a single static background color, no shift.",
      "background-color triggers repaint — fine for body element. Avoid animating on large images.",
      ["apple.com", "figma.com config"]),

]


# ============================================================
# hover-micro (a041-a060) — 20 entries
# Button hover, card lift, image zoom, link underline
# ============================================================
ENTRIES += [
    E("a041", "Button Press Scale", "hover-micro", "triggered", 100,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "All clickable buttons — adds tactile feedback that confirms the click registered.",
      "On text-only links — the scale feels heavy for a link; use a color or underline change instead.",
      """.btn {
  transition: transform 100ms cubic-bezier(0.4, 0, 0.2, 1);
  transform: scale(1);
}
.btn:active { transform: scale(0.96); }""",
      """// Pure CSS — no JS needed.
// Optionally pair with a haptic vibration on supported mobile:
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('pointerdown', () => {
    if (navigator.vibrate) navigator.vibrate(8);
  });
});""",
      "Skip the scale; rely on :active color change.",
      "transform: scale — 60fps safe.",
      ["material.io", "linear.app"]),

    E("a042", "Card Lift On Hover", "hover-micro", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "box-shadow"],
      "Product cards, blog post cards, pricing cards where lift signals clickability.",
      "On dense card grids — the lift causes neighbors to feel distant and breaks grid rhythm.",
      """.card {
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1),
              box-shadow 200ms cubic-bezier(0.25, 1, 0.5, 1);
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.08), 0 4px 8px rgba(0,0,0,0.04);
}
@media (hover: none) { .card:hover { transform: none; box-shadow: none; } }""",
      """// Pure CSS — no JS needed.
// The @media (hover: none) rule disables lift on touch devices.""",
      "Skip lift; rely on border or color change for affordance.",
      "transform + box-shadow — box-shadow can be expensive on large cards. Use will-change: transform on hover only.",
      ["stripe.com", "vercel.com"]),

    E("a043", "Image Zoom On Hover", "hover-micro", "triggered", 400,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Product images, gallery thumbnails, blog post hero images where zoom invites a closer look.",
      "On images with text overlays — the zoom crops the text awkwardly and breaks reading.",
      """.img-zoom { overflow: hidden; }
.img-zoom img {
  transition: transform 400ms cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}
.img-zoom:hover img { transform: scale(1.08); }
@media (hover: none) { .img-zoom:hover img { transform: none; } }""",
      """// Pure CSS — no JS needed.""",
      "Skip zoom; static image.",
      "transform: scale on GPU layer — 60fps safe.",
      ["shopify.com", "apple.com"]),

    E("a044", "Link Underline Grow", "hover-micro", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Inline text links, navigation links, footer links where the underline grows from left to right.",
      "On primary CTAs — they should look like buttons, not links. Also avoid on touch-only interfaces.",
      """.link-grow {
  position: relative;
  text-decoration: none;
  color: #2563eb;
}
.link-grow::after {
  content: '';
  position: absolute;
  left: 0; bottom: -2px;
  width: 100%; height: 2px;
  background: currentColor;
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.link-grow:hover::after { transform: scaleX(1); }
@media (hover: none) { .link-grow::after { transform: scaleX(1); } }""",
      """// Pure CSS — no JS needed.""",
      "Show underline at full width immediately on hover.",
      "transform: scaleX on pseudo-element — 60fps safe.",
      ["stripe.com", "css-tricks.com"]),

    E("a045", "Icon Rotate On Hover", "hover-micro", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Dropdown caret indicators, refresh icons, settings icons where the rotation signals state change.",
      "On logos — rotating the logo feels broken. Also avoid on critical UI icons where rotation implies malfunction.",
      """.icon-rotate {
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1);
  display: inline-block;
}
.icon-rotate:hover { transform: rotate(90deg); }
.icon-rotate.open { transform: rotate(180deg); }
@media (hover: none) { .icon-rotate:hover { transform: none; } }""",
      """// Toggle .open on click for state-ful rotation:
document.querySelectorAll('.icon-rotate[data-toggle]').forEach(el => {
  el.addEventListener('click', () => el.classList.toggle('open'));
});""",
      "Skip rotation; rely on color change.",
      "transform: rotate — 60fps safe.",
      ["linear.app", "github.com"]),

    E("a046", "Button Ripple", "hover-micro", "triggered", 600,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Material-styled buttons, primary CTAs, action buttons where the ripple confirms click location.",
      "On text links — the ripple feels heavy. Also avoid on already-busy buttons with multiple effects.",
      """.ripple-btn { position: relative; overflow: hidden; }
.ripple {
  position: absolute;
  border-radius: 50%;
  background: rgba(255,255,255,0.5);
  transform: scale(0);
  pointer-events: none;
  animation: ripple 600ms cubic-bezier(0.4, 0, 0.2, 1);
}
@keyframes ripple {
  to { transform: scale(4); opacity: 0; }
}""",
      """document.querySelectorAll('.ripple-btn').forEach(btn => {
  btn.addEventListener('pointerdown', (e) => {
    const rect = btn.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const r = document.createElement('span');
    r.className = 'ripple';
    r.style.width = r.style.height = size + 'px';
    r.style.left = (e.clientX - rect.left - size / 2) + 'px';
    r.style.top = (e.clientY - rect.top - size / 2) + 'px';
    btn.appendChild(r);
    setTimeout(() => r.remove(), 600);
  });
});""",
      "Skip ripple; rely on :active color change.",
      "transform + opacity on a small pseudo-element — 60fps safe.",
      ["material.io", "google.com"]),

    E("a047", "Card Glow Border", "hover-micro", "triggered", 300,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["opacity", "box-shadow"],
      "Feature cards on landing pages, premium plan cards, AI tool cards where the glow signals 'special'.",
      "On cards in dense grids — the glow becomes visual noise and cheapens the effect.",
      """.glow-card {
  position: relative;
  border: 1px solid rgba(0,0,0,0.08);
  transition: box-shadow 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.glow-card::before {
  content: '';
  position: absolute; inset: -1px;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg, #6366f1, #ec4899, #f59e0b);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  opacity: 0;
  transition: opacity 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.glow-card:hover { box-shadow: 0 8px 32px rgba(99,102,241,0.18); }
.glow-card:hover::before { opacity: 1; }
@media (hover: none) { .glow-card::before { opacity: 1; } .glow-card { box-shadow: none; } }""",
      """// Pure CSS — no JS needed.""",
      "Skip glow; rely on border color change.",
      "box-shadow + masked gradient border — keep card count under 6 per page.",
      ["vercel.com", "openai.com"]),

    E("a048", "Tooltip Fade In", "hover-micro", "triggered", 150,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Icon buttons, ambiguous controls, abbreviations where a small hint clarifies meaning.",
      "For critical info — tooltips shouldn't be the only way to discover important actions.",
      """.tooltip-host { position: relative; }
.tooltip {
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  opacity: 0;
  pointer-events: none;
  background: #1a1a1a; color: white;
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 12px; white-space: nowrap;
  transition: transform 150ms cubic-bezier(0.25, 1, 0.5, 1),
              opacity 150ms cubic-bezier(0.25, 1, 0.5, 1);
  transition-delay: 300ms;
}
.tooltip-host:hover .tooltip,
.tooltip-host:focus-within .tooltip {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}""",
      """// Pure CSS — no JS needed. Tooltip shows on hover AND keyboard focus.""",
      "Show tooltip immediately at full opacity, no slide.",
      "transform + opacity — 60fps safe.",
      ["github.com", "linear.app"]),

    E("a049", "Color Fill Button", "hover-micro", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Ghost/outline buttons becoming primary on hover, secondary CTAs where the fill signals 'click me'.",
      "On buttons that already have a strong fill — the additional fill is invisible and pointless.",
      """.fill-btn {
  position: relative;
  overflow: hidden;
  background: transparent;
  color: #2563eb;
  border: 1px solid #2563eb;
  z-index: 0;
}
.fill-btn::before {
  content: '';
  position: absolute; inset: 0;
  background: #2563eb;
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1);
  z-index: -1;
}
.fill-btn:hover { color: white; }
.fill-btn:hover::before { transform: scaleX(1); }
@media (hover: none) { .fill-btn::before { transform: scaleX(1); } .fill-btn { color: white; } }""",
      """// Pure CSS — no JS needed.""",
      "Instantly fill the button on hover, no animation.",
      "transform: scaleX on pseudo-element — 60fps safe.",
      ["stripe.com", "framer.com"]),

    E("a050", "Hover Image Reveal (mask)", "hover-micro", "triggered", 300,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["clip-path"],
      "Navigation items that link to image content, blog category hovers where the preview entices a click.",
      "On mobile — there is no hover, the image would never reveal. Use tap-to-preview instead.",
      """.nav-img-host { position: relative; }
.nav-img {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  width: 240px; height: 160px;
  background-size: cover;
  background-position: center;
  clip-path: inset(0 0 100% 0);
  opacity: 0;
  pointer-events: none;
  transition: clip-path 300ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 300ms cubic-bezier(0.4, 0, 0.2, 1);
}
.nav-img-host:hover .nav-img {
  clip-path: inset(0 0 0 0);
  opacity: 1;
}""",
      """// Pure CSS — no JS needed.
// On mobile, tap to toggle:
if (matchMedia('(hover: none)').matches) {
  document.querySelectorAll('.nav-img-host').forEach(h => {
    h.addEventListener('click', e => {
      e.preventDefault();
      h.classList.toggle('revealed');
    });
  });
}""",
      "Skip clip-path animation; show preview on tap (mobile) or always (desktop).",
      "clip-path triggers repaint — fine for small images.",
      ["awwwards.com", "apple.com"]),

]


# ============================================================
# hover-micro (a051-a060) — 10 more entries (continued)
# Nav slide, text swap, checkbox tick, magnetic, heart fill
# ============================================================
ENTRIES += [
    E("a051", "Nav Item Slide Right", "hover-micro", "triggered", 200,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform"],
      "Side navigation, sidebar menus, footer nav where items nudge right on hover to signal interactivity.",
      "On top horizontal nav — the slide direction is confusing; users expect down or fade instead.",
      """.nav-item {
  display: block;
  transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.nav-item:hover { transform: translateX(4px); }
@media (hover: none) { .nav-item:hover { transform: none; } }""",
      """// Pure CSS — no JS needed.""",
      "Skip slide; rely on color change.",
      "transform: translateX — 60fps safe.",
      ["linear.app", "vercel.com docs"]),

    E("a052", "Text Swap On Hover", "hover-micro", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Nav items, button labels with shortcuts, 'Learn more →' style links where the swap adds dimension.",
      "When the swap text is longer than the original — causes layout shift, breaking the hover state.",
      """.swap-host {
  position: relative;
  display: inline-block;
  overflow: hidden;
}
.swap-default, .swap-hover {
  display: block;
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.swap-hover {
  position: absolute;
  inset: 0;
  transform: translateY(100%);
  opacity: 0;
}
.swap-host:hover .swap-default { transform: translateY(-100%); opacity: 0; }
.swap-host:hover .swap-hover { transform: translateY(0); opacity: 1; }
@media (hover: none) { .swap-hover { display: none; } }""",
      """// Pure CSS — no JS needed.""",
      "Show only one label, no swap.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "stripe.com"]),

    E("a053", "Avatar Ring Pulse", "hover-micro", "ambient", 2000,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity", "box-shadow"],
      "Live indicators on avatars, online status, recording indicators where a slow pulse signals activity.",
      "On every avatar — the pulse becomes visual noise and distracts from content.",
      """.pulse-avatar { position: relative; }
.pulse-avatar::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: 50%;
  border: 2px solid #22c55e;
  animation: pulseRing 2000ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
  pointer-events: none;
}
@keyframes pulseRing {
  0% { transform: scale(1); opacity: 0.8; }
  100% { transform: scale(1.5); opacity: 0; }
}""",
      """// Pause when offscreen for perf:
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    e.target.style.animationPlayState = e.isIntersecting ? 'running' : 'paused';
  });
});
document.querySelectorAll('.pulse-avatar').forEach(a => io.observe(a));""",
      "Show static ring, no pulse.",
      "transform + opacity on a small pseudo-element — 60fps safe.",
      ["discord.com", "slack.com"]),

    E("a054", "Checkbox Tick Bounce", "hover-micro", "triggered", 300,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Form checkboxes, todo lists, settings toggles where the tick adds satisfying confirmation.",
      "On bulk-select actions — the staggered tick animation is slow when selecting 10+ items at once.",
      """.check-box {
  width: 20px; height: 20px;
  border: 2px solid #d1d5db;
  border-radius: 4px;
  display: inline-flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: border-color 200ms, background-color 200ms;
}
.check-box.checked { border-color: #2563eb; background: #2563eb; }
.check-tick {
  stroke: white;
  stroke-width: 3;
  fill: none;
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  transform: scale(0.5);
  transform-origin: center;
  opacity: 0;
  transition: stroke-dashoffset 300ms cubic-bezier(0.34, 1.56, 0.64, 1),
              transform 300ms cubic-bezier(0.34, 1.56, 0.64, 1),
              opacity 200ms;
}
.check-box.checked .check-tick {
  stroke-dashoffset: 0;
  transform: scale(1);
  opacity: 1;
}""",
      """const box = document.querySelector('.check-box');
box.addEventListener('click', () => box.classList.toggle('checked'));""",
      "Show tick at full scale, no animation.",
      "transform + opacity + stroke-dashoffset — 60fps safe.",
      ["linear.app", "todoist.com"]),

    E("a055", "Tab Underline Slide", "hover-micro", "triggered", 200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Tabbed interfaces, code tabs, settings sections where the underline slides to the hovered tab as a preview.",
      "On tabs with very different widths — the slide reveals the math and looks jittery. Use opacity instead.",
      """.tabs { position: relative; display: flex; gap: 24px; }
.tab { padding: 8px 0; cursor: pointer; position: relative; }
.tab::after {
  content: '';
  position: absolute; left: 0; bottom: 0;
  width: 100%; height: 2px;
  background: #2563eb;
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.tab:hover::after { transform: scaleX(1); }
.tab.active::after { transform: scaleX(1); }
@media (hover: none) { .tab:hover::after { transform: scaleX(0); } }""",
      """// Pure CSS — no JS needed.
// .active class is set on click.""",
      "Move underline instantly to hovered tab.",
      "transform: scaleX — 60fps safe.",
      ["linear.app", "github.com"]),

    E("a056", "Magnetic Icon Hover", "hover-micro", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Hero CTA icons, social icons, logo badges where the magnetic pull toward the cursor adds personality.",
      "On mobile — no hover, no magnetism. Also avoid on form inputs where it interferes with click precision.",
      """.magnetic {
  display: inline-flex;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}""",
      """document.querySelectorAll('.magnetic').forEach(el => {
  const strength = 0.3;
  el.addEventListener('mousemove', (e) => {
    const r = el.getBoundingClientRect();
    const x = e.clientX - r.left - r.width / 2;
    const y = e.clientY - r.top - r.height / 2;
    el.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
  });
  el.addEventListener('mouseleave', () => {
    el.style.transform = 'translate(0, 0)';
  });
});""",
      "Skip magnetism; icon stays put.",
      "transform: translate via rAF-throttled mousemove — 60fps safe.",
      ["awwwards.com", "stripe.com"]),

    E("a057", "Heart Fill On Like", "hover-micro", "triggered", 400,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Like/favorite buttons, social reactions where the heart fill confirms the like with a bounce.",
      "On serious content — hearts feel inappropriate for news or finance. Use a star or check instead.",
      """.heart-btn { background: none; border: none; cursor: pointer; padding: 8px; }
.heart-btn svg {
  transition: transform 400ms cubic-bezier(0.34, 1.56, 0.64, 1);
  transform: scale(1);
}
.heart-btn .heart-fill {
  opacity: 0;
  transition: opacity 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.heart-btn.liked svg { transform: scale(1.2); }
.heart-btn.liked .heart-fill { opacity: 1; }
.heart-btn.liked .heart-stroke { opacity: 0; }""",
      """<button class="heart-btn" aria-pressed="false">
  <svg width="24" height="24" viewBox="0 0 24 24">
    <path class="heart-stroke" d="M12 21s-7-4.5-9.5-9C1 9 2.5 5 6 5c2 0 3.5 1 4.5 2.5C11.5 6 13 5 15 5c3.5 0 5 4 3.5 7-2.5 4.5-6.5 9-6.5 9z" stroke="#ef4444" stroke-width="2" fill="none"/>
    <path class="heart-fill" d="M12 21s-7-4.5-9.5-9C1 9 2.5 5 6 5c2 0 3.5 1 4.5 2.5C11.5 6 13 5 15 5c3.5 0 5 4 3.5 7-2.5 4.5-6.5 9-6.5 9z" fill="#ef4444"/>
  </svg>
</button>
<script>
  document.querySelector('.heart-btn').addEventListener('click', function() {
    const liked = this.classList.toggle('liked');
    this.setAttribute('aria-pressed', liked);
  });
</script>""",
      "Show filled heart at full scale immediately.",
      "transform + opacity — 60fps safe.",
      ["twitter.com", "instagram.com"]),

    E("a058", "Star Rating Fill Sweep", "hover-micro", "triggered", 300,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["clip-path", "transform"],
      "Review forms, product rating inputs, testimonial ratings where the fill sweep adds delight.",
      "When users need to click precise values — the sweep makes single-star precision hard to control.",
      """.star-rating { display: inline-flex; gap: 4px; position: relative; cursor: pointer; }
.star { width: 24px; height: 24px; position: relative; }
.star-bg, .star-fg {
  position: absolute; inset: 0;
  background-size: 24px; background-repeat: no-repeat;
}
.star-bg {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 7h7l-5.5 4.5L18 21l-6-4.5L6 21l1.5-7.5L2 9h7z' fill='%23d1d5db'/%3E%3C/svg%3E");
}
.star-fg {
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 7h7l-5.5 4.5L18 21l-6-4.5L6 21l1.5-7.5L2 9h7z' fill='%23f59e0b'/%3E%3C/svg%3E");
  clip-path: inset(0 100% 0 0);
  transition: clip-path 300ms cubic-bezier(0.25, 1, 0.5, 1);
  transform: scale(1);
}
.star.filled .star-fg {
  clip-path: inset(0 0 0 0);
  transform: scale(1.1);
  transition: clip-path 300ms cubic-bezier(0.25, 1, 0.5, 1),
              transform 300ms cubic-bezier(0.34, 1.56, 0.64, 1);
}""",
      """const stars = document.querySelectorAll('.star');
stars.forEach((s, i) => {
  s.addEventListener('click', () => {
    stars.forEach((star, j) => star.classList.toggle('filled', j <= i));
  });
});""",
      "Show filled stars at full opacity, no sweep.",
      "clip-path + transform — 60fps safe for 5 stars.",
      ["airbnb.com", "amazon.com"]),

    E("a059", "Dropdown Caret Rotate", "hover-micro", "triggered", 200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "Select dropdowns, accordion headers, expandable sections where the caret rotation signals open state.",
      "When the dropdown is always open — the caret animation is pointless since there is no state change.",
      """.caret {
  display: inline-block;
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.dropdown.open .caret { transform: rotate(180deg); }""",
      """const dd = document.querySelector('.dropdown');
dd.querySelector('.dropdown-trigger').addEventListener('click', () => {
  dd.classList.toggle('open');
});""",
      "Skip rotation; rely on color change to indicate open state.",
      "transform: rotate — 60fps safe.",
      ["linear.app", "github.com"]),

    E("a060", "Button Sheen Sweep", "hover-micro", "triggered", 800,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Primary CTAs on landing pages, premium feature highlights where the sheen signals 'polished' and 'worth clicking'.",
      "On every button — the sheen becomes tiring and cheapens the design. Reserve for one hero CTA per page.",
      """.sheen-btn {
  position: relative;
  overflow: hidden;
  background: #2563eb; color: white;
  border: none; padding: 12px 24px;
  border-radius: 8px;
  cursor: pointer;
}
.sheen-btn::before {
  content: '';
  position: absolute; top: 0; left: -100%;
  width: 50%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  transform: skewX(-20deg);
  opacity: 0;
  transition: transform 800ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
.sheen-btn:hover::before {
  transform: skewX(-20deg) translateX(300%);
  opacity: 1;
}
@media (hover: none) { .sheen-btn::before { display: none; } }""",
      """// Pure CSS — no JS needed.""",
      "Skip sheen; static button.",
      "transform + opacity on pseudo-element — 60fps safe.",
      ["stripe.com", "framer.com"]),

]


# ============================================================
# loading-state (a061-a070) — 10 entries
# Skeleton shimmer, spinner, progress
# ============================================================
ENTRIES += [
    E("a061", "Skeleton Shimmer", "loading-state", "ambient", 1500,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity"],
      "Async content loading, image galleries, dashboard widgets where the shimmer indicates 'loading, not broken'.",
      "For load times under 200ms — the skeleton flashes and feels broken. Use a spinner or nothing at all.",
      """.skeleton {
  position: relative;
  background: #e5e7eb;
  border-radius: 6px;
  overflow: hidden;
}
.skeleton::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
  transform: translateX(-100%);
  animation: shimmer 1500ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
@keyframes shimmer {
  100% { transform: translateX(100%); }
}""",
      """// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    e.target.style.setProperty('--shimmer-state', e.isIntersecting ? 'running' : 'paused');
    const after = e.target;
    after.style.animationPlayState = e.isIntersecting ? 'running' : 'paused';
  });
});
document.querySelectorAll('.skeleton').forEach(s => io.observe(s));""",
      "Show static gray placeholder, no shimmer.",
      "transform: translateX on a GPU layer — 60fps safe.",
      ["linkedin.com", "facebook.com"]),

    E("a062", "Indeterminate Progress Bar", "loading-state", "ambient", 2000,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Form submissions, file processing, indeterminate server requests where the duration is unknown.",
      "When you know the progress — use determinate instead. Indeterminate bars feel slower to users.",
      """.indeterminate-bar {
  position: relative;
  width: 100%; height: 4px;
  background: rgba(0,0,0,0.08);
  border-radius: 2px;
  overflow: hidden;
}
.indeterminate-bar::after {
  content: '';
  position: absolute; top: 0; left: 0;
  width: 40%; height: 100%;
  background: #2563eb;
  border-radius: 2px;
  animation: indet 2000ms cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
@keyframes indet {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(350%); }
}""",
      """// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  const bar = entries[0].target;
  bar.style.getPropertyPriority('--anim');
  bar.classList.toggle('paused', !entries[0].isIntersecting);
});
io.observe(document.querySelector('.indeterminate-bar'));
// CSS: .indeterminate-bar.paused::after { animation-play-state: paused; }""",
      "Show static bar at 50%, or replace with text 'Loading...'.",
      "transform + opacity on a pseudo-element — 60fps safe.",
      ["material.io", "github.com"]),

    E("a063", "Spinner Dots", "loading-state", "ambient", 1200,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity"],
      "Inline button loaders, small inline loading states, chat typing indicators where space is tight.",
      "For long loads (>5s) — dots feel too small for extended waiting. Use a progress bar instead.",
      """.dots { display: inline-flex; gap: 4px; }
.dots span {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: currentColor;
  animation: dotPulse 1200ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
.dots span:nth-child(2) { animation-delay: 150ms; }
.dots span:nth-child(3) { animation-delay: 300ms; }
@keyframes dotPulse {
  0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
  40% { transform: scale(1); opacity: 1; }
}""",
      """// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  entries[0].target.style.animationPlayState = entries[0].isIntersecting ? 'running' : 'paused';
});
document.querySelectorAll('.dots').forEach(d => io.observe(d));""",
      "Show static dots, no animation. Or replace with text 'Loading...'.",
      "transform + opacity — 60fps safe.",
      ["iMessage", "slack.com"]),

    E("a064", "Optimistic UI Fade-In", "loading-state", "triggered", 250,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Like buttons, comment additions, list reordering where the optimistic update feels instant.",
      "For destructive actions — optimistic UI on delete is risky if the server fails. Use a confirmation modal.",
      """.optimistic-in {
  animation: optIn 250ms cubic-bezier(0.25, 1, 0.5, 1);
}
@keyframes optIn {
  from { opacity: 0; transform: translateY(-8px); }
  to { opacity: 1; transform: translateY(0); }
}""",
      """function addOptimistic(container, el) {
  el.classList.add('optimistic-in');
  container.prepend(el);
  // If server fails, remove the element with a fade-out:
  return () => {
    el.style.transition = 'opacity 200ms, transform 200ms';
    el.style.opacity = '0';
    el.style.transform = 'translateY(-8px)';
    setTimeout(() => el.remove(), 200);
  };
}
// Usage:
// const rollback = addOptimistic(listEl, newCommentEl);
// fetch('/api/comment', ...).catch(rollback);""",
      "Show inserted element at full opacity immediately.",
      "transform + opacity — 60fps safe.",
      ["twitter.com", "linear.app"]),

    E("a065", "Spinner Ring", "loading-state", "ambient", 1000,
      "cubic-bezier(0.45, 0.05, 0.55, 0.95)", "linearLoop",
      ["transform"],
      "Form submissions, page loads, generic async actions where a simple spinner suffices.",
      "When you have progress data — determinate is more reassuring and informative than an endless spin.",
      """.spinner-ring {
  width: 24px; height: 24px;
  border: 2.5px solid rgba(37, 99, 235, 0.2);
  border-top-color: #2563eb;
  border-radius: 50%;
  animation: spinRing 1000ms cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite;
}
@keyframes spinRing {
  to { transform: rotate(360deg); }
}""",
      """// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  entries[0].target.style.animationPlayState = entries[0].isIntersecting ? 'running' : 'paused';
});
document.querySelectorAll('.spinner-ring').forEach(s => io.observe(s));""",
      "Show static ring; do not spin.",
      "transform: rotate — 60fps safe. Use a near-linear curve for seamless infinite loop.",
      ["tailwindcss.com", "shadcn.com"]),

    E("a066", "Loading Bar With Percentage", "loading-state", "triggered", 2000,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Onboarding flows, file uploads with known size, multi-step setup where the percentage builds trust.",
      "When the percentage is fake — users notice when it stalls at 99% and trust drops sharply.",
      """.load-bar-wrap { width: 100%; max-width: 320px; }
.load-bar-track {
  width: 100%; height: 6px;
  background: rgba(0,0,0,0.08);
  border-radius: 3px; overflow: hidden;
}
.load-bar-fill {
  height: 100%; background: #2563eb;
  border-radius: 3px;
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform 2000ms cubic-bezier(0.4, 0, 0.2, 1);
}
.load-bar-pct {
  margin-top: 8px;
  font-size: 12px; color: #6b7280;
  font-variant-numeric: tabular-nums;
  text-align: right;
}""",
      """function runLoadBar(fill, pctEl, duration = 2000) {
  const start = performance.now();
  function frame(now) {
    const t = Math.min((now - start) / duration, 1);
    const eased = t < 0.5 ? 2*t*t : 1 - Math.pow(-2*t + 2, 2)/2;
    fill.style.transform = `scaleX(${eased})`;
    pctEl.textContent = Math.floor(eased * 100) + '%';
    if (t < 1) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
}""",
      "Show bar at 100% with final percentage, no animation.",
      "transform + opacity + rAF counter — 60fps safe.",
      ["github.com", "figma.com"]),

    E("a067", "Skeleton Card Grid", "loading-state", "ambient", 1500,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity"],
      "Search results, product grids, dashboard widgets where multiple cards load at once.",
      "For grids smaller than 4 items — the skeleton flashes too briefly to be useful.",
      """.skel-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 16px; }
.skel-card {
  background: #f3f4f6;
  border-radius: 8px;
  padding: 16px;
  position: relative;
  overflow: hidden;
}
.skel-card::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
  transform: translateX(-100%);
  animation: skelShimmer 1500ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
@keyframes skelShimmer { 100% { transform: translateX(100%); } }
.skel-line { height: 12px; background: #e5e7eb; border-radius: 4px; margin-bottom: 8px; }
.skel-line.short { width: 60%; }""",
      """// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    const after = e.target;
    after.style.animationPlayState = e.isIntersecting ? 'running' : 'paused';
  });
});
document.querySelectorAll('.skel-card').forEach(c => io.observe(c));""",
      "Show static gray placeholders, no shimmer.",
      "transform + opacity — 60fps safe. Cap at 12 cards per grid.",
      ["pinterest.com", "airbnb.com"]),

    E("a068", "Pulse Dot Loader", "loading-state", "ambient", 1000,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity"],
      "Live status indicators, 'thinking' states, online indicators where a single pulse is enough.",
      "For long operations — the dot feels too small to indicate real progress and reads as a stuck state.",
      """.pulse-dot {
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #22c55e;
  animation: pulseDot 1000ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
@keyframes pulseDot {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.6; }
}""",
      """// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  entries[0].target.style.animationPlayState = entries[0].isIntersecting ? 'running' : 'paused';
});
document.querySelectorAll('.pulse-dot').forEach(d => io.observe(d));""",
      "Show static dot, no pulse.",
      "transform + opacity — 60fps safe.",
      ["slack.com", "discord.com"]),

    E("a069", "Content Placeholder Wave", "loading-state", "ambient", 1800,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity"],
      "Multi-section loading states, full-page skeletons where a wave of shimmer ties sections together.",
      "For single-element loads — the wave is overkill and reads as a glitch.",
      """.wave-block {
  background: #e5e7eb;
  border-radius: 4px;
  position: relative;
  overflow: hidden;
}
.wave-block::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent);
  transform: translateX(-100%);
  animation: waveShimmer 1800ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
  animation-delay: var(--wave-delay, 0ms);
}
@keyframes waveShimmer { 100% { transform: translateX(100%); } }""",
      """// Stagger the wave across sections:
document.querySelectorAll('.wave-block').forEach((el, i) => {
  el.style.setProperty('--wave-delay', (i * 150) + 'ms');
});
// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    e.target.style.animationPlayState = e.isIntersecting ? 'running' : 'paused';
  });
});
document.querySelectorAll('.wave-block').forEach(b => io.observe(b));""",
      "Show static gray placeholders, no wave.",
      "transform + opacity — 60fps safe.",
      ["linkedin.com", "notion.so"]),

    E("a070", "Linear Determinate Progress", "loading-state", "triggered", 1000,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform"],
      "File downloads, video buffering, progress through known steps where determinate is reassuring.",
      "When the actual progress is unknown — use indeterminate instead, or users will think it's stuck.",
      """.det-bar {
  width: 100%; height: 4px;
  background: rgba(0,0,0,0.08);
  border-radius: 2px;
  overflow: hidden;
}
.det-bar-fill {
  height: 100%;
  background: #2563eb;
  border-radius: 2px;
  transform: scaleX(var(--p, 0));
  transform-origin: left center;
  transition: transform 1000ms cubic-bezier(0.4, 0, 0.2, 1);
}""",
      """function setProgress(el, percent) {
  el.style.setProperty('--p', percent / 100);
}
// Usage: setProgress(document.querySelector('.det-bar-fill'), 75);""",
      "Set bar to final percent immediately.",
      "transform: scaleX — 60fps safe.",
      ["youtube.com", "github.com"]),

]


# ============================================================
# hero-choreography (a071-a080) — 10 entries
# Staggered reveals in hero
# ============================================================
ENTRIES += [
    E("a071", "Hero Staggered Text Reveal", "hero-choreography", "triggered", 800,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "SaaS landing hero, agency homepage hero, product launch pages where the text choreography sets the tone.",
      "When the hero text is more than 4 lines — the stagger feels slow. Use a single block reveal instead.",
      """.hero-line {
  display: block;
  opacity: 0;
  transform: translateY(24px);
  animation: heroLineUp 800ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
  animation-delay: var(--hero-delay, 0ms);
}
@keyframes heroLineUp {
  to { opacity: 1; transform: translateY(0); }
}""",
      """// Set staggered delays on hero load:
window.addEventListener('load', () => {
  document.querySelectorAll('.hero-line').forEach((el, i) => {
    el.style.setProperty('--hero-delay', (i * 120 + 200) + 'ms');
  });
});""",
      "Show all lines at full opacity immediately.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "framer.com"]),

    E("a072", "Hero Image Clip-Path Reveal", "hero-choreography", "triggered", 1200,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["clip-path", "transform"],
      "Photography-led heroes, product hero shots, fashion/editorial heroes where the wipe adds drama.",
      "For heroes with text overlays — the clip reveals text awkwardly mid-wipe and breaks reading.",
      """.hero-img {
  clip-path: inset(0 0 100% 0);
  transform: scale(1.15);
  transition: clip-path 1200ms cubic-bezier(0.65, 0, 0.35, 1),
              transform 1200ms cubic-bezier(0.65, 0, 0.35, 1);
  transition-delay: 300ms;
}
.hero-img.in {
  clip-path: inset(0 0 0 0);
  transform: scale(1);
}""",
      """window.addEventListener('load', () => {
  requestAnimationFrame(() => {
    document.querySelector('.hero-img').classList.add('in');
  });
});""",
      "Show image at full size, no clip.",
      "clip-path triggers repaint — fine for one hero image.",
      ["apple.com", "nike.com"]),

    E("a073", "Hero Product UI Unroll", "hero-choreography", "triggered", 1500,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["clip-path", "transform"],
      "SaaS product heroes, app dashboard previews, tool showcases where the UI unrolls top-to-bottom.",
      "For abstract hero illustrations — the unroll reads as a UI glitch on non-UI imagery.",
      """.hero-ui {
  clip-path: inset(0 0 100% 0);
  transform: translateY(20px);
  transition: clip-path 1500ms cubic-bezier(0.65, 0, 0.35, 1),
              transform 1500ms cubic-bezier(0.65, 0, 0.35, 1);
  transition-delay: 400ms;
}
.hero-ui.in {
  clip-path: inset(0 0 0 0);
  transform: translateY(0);
}""",
      """window.addEventListener('load', () => {
  requestAnimationFrame(() => {
    document.querySelector('.hero-ui').classList.add('in');
  });
});""",
      "Show UI at full size, no clip.",
      "clip-path + transform — 60fps safe.",
      ["linear.app", "vercel.com"]),

    E("a074", "Hero Gradient Shift", "hero-choreography", "ambient", 8000,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["filter"],
      "Brand heroes, AI product heroes, ambient brand moments where a slow hue shift signals 'alive'.",
      "On text-heavy heroes — the shifting hue distracts from reading the headline.",
      """.hero-bg {
  background: linear-gradient(135deg, #6366f1, #ec4899, #f59e0b);
  background-size: 200% 200%;
  animation: heroHue 8000ms cubic-bezier(0.4, 0, 0.6, 1) infinite alternate;
  will-change: filter;
}
@keyframes heroHue {
  0% { filter: hue-rotate(0deg); }
  100% { filter: hue-rotate(60deg); }
}""",
      """// Pause when offscreen for perf:
const hero = document.querySelector('.hero-bg');
const io = new IntersectionObserver((entries) => {
  hero.style.animationPlayState = entries[0].isIntersecting ? 'running' : 'paused';
});
io.observe(hero);""",
      "Static gradient, no hue shift.",
      "filter: hue-rotate triggers repaint — fine for one hero element with will-change.",
      ["stripe.com", "vercel.com"]),

    E("a075", "Hero Word-by-Word Reveal", "hero-choreography", "triggered", 400,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Bold short headlines (3-6 words), launch pages, manifesto statements where each word lands.",
      "For long headlines — the per-word stagger becomes a wait. Use a single block reveal instead.",
      """.hero-word {
  display: inline-block;
  opacity: 0;
  transform: translateY(20px) scale(0.9);
  animation: heroWordIn 400ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  animation-delay: var(--word-delay, 0ms);
}
@keyframes heroWordIn {
  to { opacity: 1; transform: translateY(0) scale(1); }
}""",
      """function splitHeroText(el) {
  const words = el.textContent.trim().split(/\\s+/);
  el.innerHTML = words.map((w, i) =>
    `<span class="hero-word" style="--word-delay: ${i * 80 + 200}ms">${w}</span>`
  ).join(' ');
}
splitHeroText(document.querySelector('.hero-headline'));""",
      "Show all words at full opacity immediately.",
      "transform + opacity — 60fps safe.",
      ["apple.com", "framer.com"]),

]


# ============================================================
# hero-choreography (a076-a080) — 5 more entries (continued)
# CTA pulse, background scale, particles, logo draw, trust cascade
# ============================================================
ENTRIES += [
    E("a076", "Hero CTA Pulse-In", "hero-choreography", "triggered", 600,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Hero CTAs, launch page primary actions, signup buttons where the CTA arrives with a satisfying pulse.",
      "When there are multiple CTAs — pulsing all of them is chaotic. Pick one primary CTA to pulse.",
      """.hero-cta {
  opacity: 0;
  transform: scale(0.8);
  animation: ctaPulse 600ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  animation-delay: 900ms;
}
@keyframes ctaPulse {
  0% { opacity: 0; transform: scale(0.8); }
  60% { opacity: 1; transform: scale(1.05); }
  100% { opacity: 1; transform: scale(1); }
}""",
      """// Trigger after hero text reveals (delay 900ms):
// Pure CSS — animation-delay handles the timing.
// Optionally re-trigger on scroll back to hero:
const io = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    document.querySelector('.hero-cta').style.animation = 'none';
    void document.querySelector('.hero-cta').offsetWidth;
    document.querySelector('.hero-cta').style.animation = '';
  }
});
io.observe(document.querySelector('.hero-cta'));""",
      "Show CTA at full scale and opacity immediately.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "framer.com"]),

    E("a077", "Hero Background Scale-In", "hero-choreography", "triggered", 2000,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Photography heroes, brand heroes with full-bleed imagery where a slow scale-in adds grandeur.",
      "On heroes with text directly on the image — the scale makes text feel unstable while reading.",
      """.hero-bg-img {
  transform: scale(1.15);
  transition: transform 2000ms cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}
.hero-bg-img.in { transform: scale(1); }""",
      """window.addEventListener('load', () => {
  requestAnimationFrame(() => {
    document.querySelector('.hero-bg-img').classList.add('in');
  });
});""",
      "Show background at scale(1) immediately.",
      "transform: scale on GPU layer — 60fps safe with will-change.",
      ["apple.com", "stripe.com"]),

    E("a078", "Hero Floating Particles", "hero-choreography", "ambient", 10000,
      "cubic-bezier(0.4, 0, 0.6, 1)", "easeInOutQuad",
      ["transform", "opacity"],
      "Tech/AI product heroes, brand moments, futuristic SaaS landing pages where ambient particles signal 'alive'.",
      "On enterprise B2B — particles feel gimmicky for serious audiences and cheapen the brand.",
      """.particles { position: absolute; inset: 0; overflow: hidden; pointer-events: none; }
.particle {
  position: absolute;
  width: 4px; height: 4px;
  border-radius: 50%;
  background: rgba(99, 102, 241, 0.4);
  animation: floatUp 10000ms cubic-bezier(0.4, 0, 0.6, 1) infinite;
  animation-delay: var(--p-delay, 0ms);
  animation-duration: var(--p-dur, 10000ms);
}
@keyframes floatUp {
  0% { transform: translateY(100vh) translateX(0); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(-10vh) translateX(40px); opacity: 0; }
}""",
      """// Generate particles with random positions/durations:
const c = document.querySelector('.particles');
for (let i = 0; i < 20; i++) {
  const p = document.createElement('div');
  p.className = 'particle';
  p.style.left = Math.random() * 100 + '%';
  p.style.setProperty('--p-delay', (Math.random() * 10000) + 'ms');
  p.style.setProperty('--p-dur', (8000 + Math.random() * 4000) + 'ms');
  c.appendChild(p);
}
// Pause when offscreen:
const io = new IntersectionObserver((entries) => {
  c.style.animationPlayState = entries[0].isIntersecting ? 'running' : 'paused';
});
io.observe(c);""",
      "Show static particles (no animation), or hide them entirely.",
      "transform + opacity on 20 small elements — 60fps safe. Cap at 30 particles.",
      ["openai.com", "anthropic.com"]),

    E("a079", "Hero Logo Draw", "hero-choreography", "triggered", 1500,
      "cubic-bezier(0.65, 0, 0.35, 1)", "easeInOutCubic",
      ["stroke-dashoffset", "opacity"],
      "Brand splash pages, agency homepages, portfolio intros where the logo drawing sets the brand tone.",
      "On returning visits — the draw animation slows down repeat users who just want to reach content.",
      """.logo-draw {
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: var(--logo-len);
  stroke-dashoffset: var(--logo-len);
  opacity: 0;
  animation: logoDraw 1500ms cubic-bezier(0.65, 0, 0.35, 1) forwards;
}
@keyframes logoDraw {
  0% { opacity: 0; }
  10% { opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 1; }
}""",
      """// Run once per session:
if (!sessionStorage.getItem('logoDrawn')) {
  document.querySelectorAll('.logo-draw path').forEach(p => {
    const len = p.getTotalLength();
    p.style.setProperty('--logo-len', len);
  });
  sessionStorage.setItem('logoDrawn', '1');
} else {
  document.querySelectorAll('.logo-draw').forEach(el => {
    el.style.opacity = 1;
    el.querySelectorAll('path').forEach(p => p.style.strokeDashoffset = 0);
  });
}""",
      "Show logo at full opacity with no stroke-dashoffset.",
      "stroke-dashoffset triggers SVG repaint — fine for one logo on first visit only.",
      ["linear.app", "framer.com"]),

    E("a080", "Hero Trust Badge Cascade", "hero-choreography", "triggered", 400,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "SaaS hero 'trusted by' rows, agency client logos, B2B trust signals where badges cascade in.",
      "When there are 8+ badges — the cascade takes too long and feels like a wait before content.",
      """.trust-badge {
  display: inline-block;
  opacity: 0;
  transform: translateY(16px);
  animation: badgeIn 400ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
  animation-delay: var(--badge-delay, 0ms);
}
@keyframes badgeIn {
  to { opacity: 1; transform: translateY(0); }
}""",
      """window.addEventListener('load', () => {
  document.querySelectorAll('.trust-badge').forEach((el, i) => {
    el.style.setProperty('--badge-delay', (i * 80 + 1100) + 'ms');
  });
});""",
      "Show all badges at full opacity immediately.",
      "transform + opacity — 60fps safe.",
      ["stripe.com", "linear.app"]),

]


# ============================================================
# navigation (a081-a090) — 10 entries
# Mobile menu, dropdown, command palette, accordion
# ============================================================
ENTRIES += [
    E("a081", "Mobile Menu Slide-In", "navigation", "triggered", 280,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Mobile site headers, app-style mobile menus where the drawer slides in from the side.",
      "On desktop — the slide-in is a mobile pattern; use dropdown or mega menu instead.",
      """.mobile-menu {
  position: fixed; inset: 0;
  background: white;
  z-index: 100;
  transform: translateX(100%);
  opacity: 0;
  transition: transform 280ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 280ms cubic-bezier(0.4, 0, 0.2, 1);
  display: flex; flex-direction: column;
}
.mobile-menu.open { transform: translateX(0); opacity: 1; }
.mobile-menu-backdrop {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.4);
  opacity: 0;
  pointer-events: none;
  transition: opacity 280ms cubic-bezier(0.4, 0, 0.2, 1);
}
.mobile-menu-backdrop.open { opacity: 1; pointer-events: auto; }""",
      """const btn = document.querySelector('.menu-btn');
const menu = document.querySelector('.mobile-menu');
const backdrop = document.querySelector('.mobile-menu-backdrop');
function toggle() {
  const open = menu.classList.toggle('open');
  backdrop.classList.toggle('open', open);
  document.body.style.overflow = open ? 'hidden' : '';
}
btn.addEventListener('click', toggle);
backdrop.addEventListener('click', toggle);""",
      "Show menu immediately at translateX(0), opacity 1.",
      "transform + opacity — 60fps safe on mobile.",
      ["airbnb.com mobile", "stripe.com mobile"]),

    E("a082", "Dropdown Fade", "navigation", "triggered", 180,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Top nav dropdowns, settings menus, contextual menus where a quick fade-in feels light.",
      "For complex mega menus — use a more structured reveal with stagger; a single fade feels underwhelming.",
      """.dropdown-menu {
  position: absolute;
  top: calc(100% + 8px);
  left: 0;
  background: white;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.12);
  padding: 8px;
  min-width: 200px;
  opacity: 0;
  transform: translateY(-4px);
  pointer-events: none;
  transition: transform 180ms cubic-bezier(0.25, 1, 0.5, 1),
              opacity 180ms cubic-bezier(0.25, 1, 0.5, 1);
}
.dropdown.open .dropdown-menu {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}""",
      """document.querySelectorAll('.dropdown').forEach(dd => {
  const trigger = dd.querySelector('.dropdown-trigger');
  trigger.addEventListener('click', (e) => {
    e.stopPropagation();
    dd.classList.toggle('open');
  });
});
document.addEventListener('click', () => {
  document.querySelectorAll('.dropdown.open').forEach(dd => dd.classList.remove('open'));
});""",
      "Show menu immediately at full opacity, no transform.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "github.com"]),

    E("a083", "Command Palette Scale-In", "navigation", "triggered", 180,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Cmd+K command palettes, search modals, quick-action panels where a fast scale-in feels snappy.",
      "On mobile — command palettes don't fit mobile UX well; use a bottom sheet instead.",
      """.cmd-backdrop {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.4);
  backdrop-filter: blur(4px);
  opacity: 0;
  pointer-events: none;
  transition: opacity 180ms cubic-bezier(0.4, 0, 0.2, 1);
  display: flex; align-items: flex-start; justify-content: center;
  padding-top: 12vh;
}
.cmd-backdrop.open { opacity: 1; pointer-events: auto; }
.cmd-palette {
  width: 100%; max-width: 560px;
  background: white;
  border-radius: 12px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  transform: scale(0.96);
  opacity: 0;
  transition: transform 180ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 180ms cubic-bezier(0.4, 0, 0.2, 1);
}
.cmd-backdrop.open .cmd-palette { transform: scale(1); opacity: 1; }""",
      """document.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    document.querySelector('.cmd-backdrop').classList.toggle('open');
  }
});""",
      "Show palette immediately at scale(1), opacity 1.",
      "transform + opacity — 60fps safe.",
      ["linear.app", "raycast.com"]),

    E("a084", "Accordion Expand", "navigation", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["grid-template-rows", "opacity"],
      "FAQ sections, settings sections, sidebar menus, docs navigation where content expands smoothly.",
      "For single-line content — the expand feels like overkill; just toggle visibility instantly.",
      """.accordion-panel {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 250ms cubic-bezier(0.4, 0, 0.2, 1);
}
.accordion-panel > div {
  overflow: hidden;
  opacity: 0;
  transition: opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.accordion-item.open .accordion-panel { grid-template-rows: 1fr; }
.accordion-item.open .accordion-panel > div { opacity: 1; }
/* Fallback for browsers without grid-template-rows animation:
   use max-height with a generous value */
@supports not (grid-template-rows: 1fr) {
  .accordion-panel { display: block; max-height: 0; overflow: hidden; transition: max-height 250ms; }
  .accordion-item.open .accordion-panel { max-height: 500px; }
}""",
      """document.querySelectorAll('.accordion-trigger').forEach(t => {
  t.addEventListener('click', () => {
    t.closest('.accordion-item').classList.toggle('open');
  });
});""",
      "Show panel content immediately, no expand animation.",
      "grid-template-rows is GPU-friendly in modern browsers (Chrome 117+, Firefox 119+). Fallback uses max-height.",
      ["tailwindcss.com docs", "radix-ui.com"]),

    E("a085", "Mega Menu Reveal", "navigation", "triggered", 250,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity", "clip-path"],
      "E-commerce category navigation, docs site navigation, enterprise SaaS top nav with many items.",
      "For sites with fewer than 6 top-level items — mega menu is overkill; use a simple dropdown.",
      """.mega-menu {
  position: absolute;
  top: calc(100% + 0px);
  left: 0; right: 0;
  background: white;
  box-shadow: 0 12px 32px rgba(0,0,0,0.12);
  padding: 24px;
  opacity: 0;
  transform: translateY(-8px);
  clip-path: inset(0 0 100% 0);
  pointer-events: none;
  transition: transform 250ms cubic-bezier(0.25, 1, 0.5, 1),
              opacity 250ms cubic-bezier(0.25, 1, 0.5, 1),
              clip-path 250ms cubic-bezier(0.25, 1, 0.5, 1);
}
.mega-host:hover .mega-menu,
.mega-host:focus-within .mega-menu {
  opacity: 1;
  transform: translateY(0);
  clip-path: inset(0 0 0 0);
  pointer-events: auto;
}""",
      """// Pure CSS — no JS needed. Reveals on hover AND keyboard focus.
// Add @media (hover: none) for mobile fallback that uses tap.""",
      "Show mega menu immediately at full opacity, no clip.",
      "transform + opacity + clip-path — 60fps safe.",
      ["amazon.com", "microsoft.com"]),

    E("a086", "Tab Switch Slide", "navigation", "triggered", 200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Settings panels, dashboard tabs, multi-step forms where the content slides between tabs.",
      "For tabs with form inputs — sliding loses focus state and confuses screen readers.",
      """.tab-panel {
  position: relative;
  overflow: hidden;
}
.tab-panel-content {
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.tab-panel-content.exit-left { transform: translateX(-24px); opacity: 0; }
.tab-panel-content.exit-right { transform: translateX(24px); opacity: 0; }
.tab-panel-content.enter-left { transform: translateX(-24px); opacity: 0; }
.tab-panel-content.enter-right { transform: translateX(24px); opacity: 0; }
.tab-panel-content.active { transform: translateX(0); opacity: 1; }""",
      """function switchTab(container, newPanel, direction = 'right') {
  const cur = container.querySelector('.tab-panel-content.active');
  cur.classList.add(direction === 'right' ? 'exit-left' : 'exit-right');
  cur.classList.remove('active');
  newPanel.classList.add(direction === 'right' ? 'enter-right' : 'enter-left');
  requestAnimationFrame(() => {
    newPanel.classList.remove('enter-right', 'enter-left');
    newPanel.classList.add('active');
  });
  setTimeout(() => cur.classList.remove('exit-left', 'exit-right'), 200);
}""",
      "Show new panel immediately at full opacity, no slide.",
      "transform + opacity — 60fps safe.",
      ["linear.app settings", "vercel.com dashboard"]),

    E("a087", "Breadcrumb Trickle", "navigation", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Deep docs hierarchies, e-commerce category pages, file explorers where the path reveals in sequence.",
      "On simple 2-level hierarchies — the trickle is overkill; just show the breadcrumb statically.",
      """.crumb {
  display: inline-block;
  opacity: 0;
  transform: translateX(-8px);
  animation: crumbIn 200ms cubic-bezier(0.25, 1, 0.5, 1) forwards;
  animation-delay: var(--crumb-delay, 0ms);
}
@keyframes crumbIn {
  to { opacity: 1; transform: translateX(0); }
}""",
      """document.querySelectorAll('.crumb').forEach((el, i) => {
  el.style.setProperty('--crumb-delay', (i * 60) + 'ms');
});""",
      "Show all crumbs at full opacity immediately.",
      "transform + opacity — 60fps safe.",
      ["stripe.com docs", "developer.mozilla.org"]),

    E("a088", "Sidebar Collapse", "navigation", "triggered", 200,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Dashboards, IDEs, multi-panel apps where the sidebar collapses to icon-only mode.",
      "On mobile — sidebars should be drawers, not collapsible columns; mobile has no room for both.",
      """.sidebar { grid-column: 1; transition: grid-template-columns 200ms cubic-bezier(0.4, 0, 0.2, 1); }
.layout { display: grid; grid-template-columns: 260px 1fr; transition: grid-template-columns 200ms cubic-bezier(0.4, 0, 0.2, 1); }
.layout.collapsed { grid-template-columns: 64px 1fr; }
.sidebar-label {
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 150ms cubic-bezier(0.4, 0, 0.2, 1);
}
.layout.collapsed .sidebar-label {
  transform: translateX(-12px);
  opacity: 0;
  pointer-events: none;
}""",
      """const layout = document.querySelector('.layout');
document.querySelector('.sidebar-toggle').addEventListener('click', () => {
  layout.classList.toggle('collapsed');
  localStorage.setItem('sidebarCollapsed', layout.classList.contains('collapsed'));
});
// Restore state:
if (localStorage.getItem('sidebarCollapsed') === 'true') layout.classList.add('collapsed');""",
      "Snap sidebar to collapsed state immediately, no animation.",
      "grid-template-columns + transform + opacity — 60fps safe.",
      ["linear.app", "notion.so"]),

    E("a089", "Toast Slide-In", "navigation", "triggered", 300,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "Action confirmations, error notifications, save status where the toast slides in from the corner.",
      "For critical errors — use a modal that requires acknowledgment; toasts can be missed.",
      """.toast-wrap {
  position: fixed; bottom: 24px; right: 24px;
  z-index: 200;
  display: flex; flex-direction: column; gap: 8px;
}
.toast {
  background: #1a1a1a; color: white;
  padding: 12px 16px;
  border-radius: 8px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.2);
  min-width: 280px; max-width: 360px;
  opacity: 0;
  transform: translateX(120%);
  animation: toastIn 300ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
.toast.leaving { animation: toastOut 200ms cubic-bezier(0.4, 0, 0.2, 1) forwards; }
@keyframes toastIn { to { opacity: 1; transform: translateX(0); } }
@keyframes toastOut { to { opacity: 0; transform: translateX(120%); } }""",
      """function showToast(msg, duration = 4000) {
  const wrap = document.querySelector('.toast-wrap');
  const t = document.createElement('div');
  t.className = 'toast';
  t.textContent = msg;
  wrap.appendChild(t);
  setTimeout(() => {
    t.classList.add('leaving');
    setTimeout(() => t.remove(), 200);
  }, duration);
}""",
      "Show toast immediately at full opacity, no slide.",
      "transform + opacity — 60fps safe.",
      ["vercel.com", "linear.app"]),

    E("a090", "Notification Stack", "navigation", "triggered", 400,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform", "opacity"],
      "In-app notification centers, activity feeds, chat message groups where items cascade in.",
      "For more than 5 notifications at once — the stack becomes overwhelming and unreadable.",
      """.notif {
  opacity: 0;
  transform: translateY(-12px) scale(0.95);
  animation: notifIn 400ms cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  animation-delay: var(--notif-delay, 0ms);
}
@keyframes notifIn {
  to { opacity: 1; transform: translateY(0) scale(1); }
}""",
      """function showNotifications(items) {
  const wrap = document.querySelector('.notif-stack');
  items.slice(0, 5).forEach((item, i) => {
    const el = document.createElement('div');
    el.className = 'notif';
    el.style.setProperty('--notif-delay', (i * 80) + 'ms');
    el.textContent = item.text;
    wrap.prepend(el);
  });
}""",
      "Show all notifications at full opacity immediately, no cascade.",
      "transform + opacity — 60fps safe. Cap at 5 simultaneous notifications.",
      ["twitter.com", "linkedin.com"]),

]


# ============================================================
# interactive (a091-a100) — 10 entries
# Drag, swipe, gesture feedback
# ============================================================
ENTRIES += [
    E("a091", "Drag Card Reorder", "interactive", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform", "opacity"],
      "Kanban boards, task lists, sortable galleries where users drag to reorder.",
      "For lists with 50+ items — drag performance degrades; use virtualization or pagination.",
      """.drag-card {
  cursor: grab;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1),
              box-shadow 200ms cubic-bezier(0.25, 1, 0.5, 1);
  user-select: none;
  touch-action: none;
}
.drag-card.dragging {
  cursor: grabbing;
  opacity: 0.8;
  z-index: 10;
  box-shadow: 0 16px 32px rgba(0,0,0,0.16);
  transition: none;
}
.drag-card.ghost { opacity: 0.4; }""",
      """// Minimal HTML5 drag-and-drop:
const cards = document.querySelectorAll('.drag-card');
let dragging = null;
cards.forEach(card => {
  card.draggable = true;
  card.addEventListener('dragstart', (e) => {
    dragging = card;
    card.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
  });
  card.addEventListener('dragend', () => {
    card.classList.remove('dragging');
    dragging = null;
  });
  card.addEventListener('dragover', (e) => {
    e.preventDefault();
    if (dragging && dragging !== card) {
      const r = card.getBoundingClientRect();
      const after = e.clientY > r.top + r.height / 2;
      card.parentNode.insertBefore(dragging, after ? card.nextSibling : card);
    }
  });
});""",
      "Allow reordering via up/down buttons or click-to-move; no drag.",
      "transform + opacity — 60fps safe. Use HTML5 DnD or pointer events; avoid frameworks for simple cases.",
      ["trello.com", "linear.app"]),

    E("a092", "Swipe To Dismiss", "interactive", "triggered", 250,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Notification cards, mobile inbox items, story cards where swipe reveals dismiss action.",
      "For desktop — swipe gestures aren't native to mouse interaction; use an explicit dismiss button.",
      """.swipe-card {
  touch-action: pan-y;
  transition: transform 250ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 250ms cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform, opacity;
}
.swipe-card.dismissed {
  transform: translateX(120%);
  opacity: 0;
  pointer-events: none;
}""",
      """function setupSwipe(card, threshold = 80) {
  let startX = 0, currentX = 0, dragging = false;
  card.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
    dragging = true;
    card.style.transition = 'none';
  });
  card.addEventListener('touchmove', (e) => {
    if (!dragging) return;
    currentX = e.touches[0].clientX - startX;
    if (currentX > 0) {
      card.style.transform = `translateX(${currentX}px)`;
      card.style.opacity = Math.max(0.3, 1 - currentX / 200);
    }
  });
  card.addEventListener('touchend', () => {
    dragging = false;
    card.style.transition = '';
    if (currentX > threshold) card.classList.add('dismissed');
    else { card.style.transform = ''; card.style.opacity = ''; }
    currentX = 0;
  });
}""",
      "Show dismiss button on card; no swipe gesture.",
      "transform + opacity via touch events — 60fps safe on mobile.",
      ["gmail.com mobile", "twitter.com mobile"]),

    E("a093", "Pull-To-Refresh", "interactive", "triggered", 300,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Mobile feed apps, mobile message lists, mobile dashboards where pull-down triggers refresh.",
      "On desktop — pull-to-refresh isn't a desktop pattern; use a refresh button instead.",
      """.ptr-indicator {
  position: absolute;
  top: -48px; left: 50%;
  transform: translateX(-50%) translateY(20px);
  opacity: 0;
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1),
              opacity 200ms cubic-bezier(0.4, 0, 0.2, 1);
}
.ptr-indicator.visible { opacity: 1; }
.ptr-indicator.refreshing {
  transform: translateX(-50%) translateY(0);
}
.ptr-container { position: relative; overflow: hidden; }
.ptr-content {
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
}""",
      """function setupPullToRefresh(container, content, indicator, onRefresh) {
  let startY = 0, currentY = 0, pulling = false;
  content.addEventListener('touchstart', (e) => {
    if (window.scrollY === 0) {
      startY = e.touches[0].clientY;
      pulling = true;
    }
  });
  content.addEventListener('touchmove', (e) => {
    if (!pulling) return;
    currentY = e.touches[0].clientY - startY;
    if (currentY > 0 && currentY < 100) {
      content.style.transform = `translateY(${currentY}px)`;
      indicator.style.transform = `translateX(-50%) translateY(${20 - currentY * 0.3}px)`;
      indicator.classList.toggle('visible', currentY > 60);
    }
  });
  content.addEventListener('touchend', async () => {
    if (!pulling) return;
    pulling = false;
    if (currentY > 60) {
      indicator.classList.add('refreshing');
      content.style.transform = 'translateY(48px)';
      await onRefresh();
      indicator.classList.remove('visible', 'refreshing');
    }
    content.style.transform = '';
    currentY = 0;
  });
}""",
      "Show refresh button at top of feed; no pull gesture.",
      "transform + opacity via touch events — 60fps safe on mobile.",
      ["twitter.com mobile", "gmail.com mobile"]),

    E("a094", "Magnetic Button", "interactive", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Hero CTAs, premium product CTAs, agency homepage buttons where the magnetic pull adds delight.",
      "On forms — magnetic buttons interfere with click precision and accessibility.",
      """.magnetic-btn {
  display: inline-flex;
  align-items: center; justify-content: center;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}""",
      """document.querySelectorAll('.magnetic-btn').forEach(btn => {
  const strength = 0.25;
  btn.addEventListener('mousemove', (e) => {
    const r = btn.getBoundingClientRect();
    const x = e.clientX - r.left - r.width / 2;
    const y = e.clientY - r.top - r.height / 2;
    btn.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
  });
  btn.addEventListener('mouseleave', () => {
    btn.style.transform = 'translate(0, 0)';
  });
  // Disable on touch devices
  if (matchMedia('(hover: none)').matches) btn.style.willChange = 'auto';
});""",
      "Skip magnetism; button stays put.",
      "transform: translate via mousemove with rAF throttle — 60fps safe.",
      ["awwwards.com", "stripe.com"]),

    E("a095", "Tilt Card (3D)", "interactive", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Premium product cards, feature highlights, app preview cards where 3D tilt adds depth.",
      "On mobile — no hover, no tilt. Also avoid on cards with form inputs; tilt breaks input precision.",
      """.tilt-3d {
  transform-style: preserve-3d;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}
.tilt-3d-inner {
  transform: translateZ(40px);
  transform-style: preserve-3d;
}""",
      """document.querySelectorAll('.tilt-3d').forEach(card => {
  const maxTilt = 8; // degrees
  card.addEventListener('mousemove', (e) => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width - 0.5;
    const py = (e.clientY - r.top) / r.height - 0.5;
    card.style.transform = `perspective(800px) rotateY(${px * maxTilt * 2}deg) rotateX(${-py * maxTilt * 2}deg)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'perspective(800px) rotateY(0) rotateX(0)';
  });
});""",
      "Skip tilt; card stays flat.",
      "transform: rotateX/rotateY with perspective — 60fps safe with will-change.",
      ["apple.com", "linear.app"]),

    E("a096", "Long-Press Feedback", "interactive", "triggered", 500,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity"],
      "Mobile long-press menus, reorder handles, quick actions where a growing ring indicates press progress.",
      "On desktop — long-press isn't a desktop pattern; use right-click context menu instead.",
      """.longpress-ring {
  position: absolute;
  border-radius: 50%;
  background: rgba(37, 99, 235, 0.3);
  transform: scale(0);
  opacity: 0;
  pointer-events: none;
}
.longpress-host {
  position: relative;
  touch-action: none;
  user-select: none;
}""",
      """function setupLongPress(el, duration = 500, onTrigger) {
  let timer, ring, startX, startY;
  el.addEventListener('touchstart', (e) => {
    startX = e.touches[0].clientX;
    startY = e.touches[0].clientY;
    ring = document.createElement('div');
    ring.className = 'longpress-ring';
    ring.style.width = ring.style.height = '64px';
    ring.style.left = (e.touches[0].clientX - el.getBoundingClientRect().left - 32) + 'px';
    ring.style.top = (e.touches[0].clientY - el.getBoundingClientRect().top - 32) + 'px';
    el.appendChild(ring);
    requestAnimationFrame(() => {
      ring.style.transition = `transform ${duration}ms cubic-bezier(0.4, 0, 0.2, 1), opacity ${duration}ms cubic-bezier(0.4, 0, 0.2, 1)`;
      ring.style.transform = 'scale(2.5)';
      ring.style.opacity = '1';
    });
    timer = setTimeout(() => { onTrigger(el); cleanup(); }, duration);
  });
  function cleanup() {
    clearTimeout(timer);
    if (ring) {
      ring.style.opacity = '0';
      setTimeout(() => ring && ring.remove(), 200);
    }
  }
  el.addEventListener('touchend', cleanup);
  el.addEventListener('touchmove', (e) => {
    if (Math.abs(e.touches[0].clientX - startX) > 10 || Math.abs(e.touches[0].clientY - startY) > 10) cleanup();
  });
}""",
      "Use an explicit context menu button instead of long-press.",
      "transform + opacity via touch events — 60fps safe.",
      ["ios home screen", "twitter.com mobile"]),

    E("a097", "Slider Snap", "interactive", "triggered", 200,
      "cubic-bezier(0.34, 1.56, 0.64, 1)", "easeOutBack",
      ["transform"],
      "Image carousels, value sliders, segmented controls where snap-to-value feels precise.",
      "For continuous inputs — snapping breaks the smooth feel and feels restrictive.",
      """.slider-track {
  position: relative;
  height: 4px;
  background: rgba(0,0,0,0.08);
  border-radius: 2px;
}
.slider-thumb {
  position: absolute;
  top: 50%;
  width: 16px; height: 16px;
  background: #2563eb;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1);
  cursor: grab;
}
.slider-thumb:active { cursor: grabbing; transform: translate(-50%, -50%) scale(1.15); }
.slider-thumb.snapping { transition: transform 200ms cubic-bezier(0.34, 1.56, 0.64, 1); }""",
      """const track = document.querySelector('.slider-track');
const thumb = document.querySelector('.slider-thumb');
const steps = 5; // 5 snap points
let dragging = false;
function setThumb(percent, snap = false) {
  if (snap) percent = Math.round(percent * steps) / steps;
  thumb.style.left = (percent * 100) + '%';
}
thumb.addEventListener('pointerdown', () => { dragging = true; thumb.setPointerCapture(event.pointerId); });
track.addEventListener('pointerdown', (e) => {
  dragging = true;
  const r = track.getBoundingClientRect();
  setThumb((e.clientX - r.left) / r.width, true);
});
window.addEventListener('pointermove', (e) => {
  if (!dragging) return;
  const r = track.getBoundingClientRect();
  setThumb(Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)), false);
});
window.addEventListener('pointerup', () => {
  if (dragging) {
    dragging = false;
    const r = track.getBoundingClientRect();
    const p = (parseFloat(thumb.style.left) / 100);
    setThumb(p, true); // snap on release
  }
});""",
      "Move thumb instantly to snapped position, no animation.",
      "transform: translate — 60fps safe.",
      ["airbnb.com price filter", "stripe.com"]),

    E("a098", "Pinch Zoom Image", "interactive", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Image lightboxes, map views, product image galleries where pinch zooms into detail.",
      "For text content — pinch-zoom on text is confusing and conflicts with browser zoom.",
      """.pinch-zoom {
  transform-origin: center center;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1);
  touch-action: none;
  cursor: grab;
}
.pinch-zoom:active { cursor: grabbing; }
.pinch-zoom.no-transition { transition: none; }""",
      """const el = document.querySelector('.pinch-zoom');
let scale = 1, startScale = 1, startDist = 0;
el.addEventListener('touchstart', (e) => {
  if (e.touches.length === 2) {
    startDist = Math.hypot(
      e.touches[0].clientX - e.touches[1].clientX,
      e.touches[0].clientY - e.touches[1].clientY
    );
    startScale = scale;
    el.classList.add('no-transition');
  }
});
el.addEventListener('touchmove', (e) => {
  if (e.touches.length === 2) {
    e.preventDefault();
    const dist = Math.hypot(
      e.touches[0].clientX - e.touches[1].clientX,
      e.touches[0].clientY - e.touches[1].clientY
    );
    scale = Math.max(0.5, Math.min(4, startScale * (dist / startDist)));
    el.style.transform = `scale(${scale})`;
  }
});
el.addEventListener('touchend', () => {
  el.classList.remove('no-transition');
  if (scale < 1) { scale = 1; el.style.transform = ''; }
});""",
      "Use explicit zoom buttons (+/-) instead of pinch gesture.",
      "transform: scale via touch events — 60fps safe.",
      ["google.com maps", "apple.com photos"]),

    E("a099", "Drop Zone Highlight", "interactive", "triggered", 150,
      "cubic-bezier(0.4, 0, 0.2, 1)", "materialStandard",
      ["transform", "opacity", "background-color"],
      "File upload zones, drag-drop interfaces, kanban card drops where the highlight signals 'drop here'.",
      "When the drop zone is small — the highlight competes with the content and obscures the target.",
      """.dropzone {
  border: 2px dashed #d1d5db;
  border-radius: 8px;
  padding: 32px;
  text-align: center;
  transition: transform 150ms cubic-bezier(0.4, 0, 0.2, 1),
              background-color 150ms cubic-bezier(0.4, 0, 0.2, 1),
              border-color 150ms cubic-bezier(0.4, 0, 0.2, 1);
}
.dropzone.drag-over {
  border-color: #2563eb;
  background-color: rgba(37, 99, 235, 0.05);
  transform: scale(1.02);
}
.dropzone-overlay {
  position: absolute; inset: 0;
  display: flex; align-items: center; justify-content: center;
  background: rgba(37, 99, 235, 0.1);
  opacity: 0;
  pointer-events: none;
  transition: opacity 150ms cubic-bezier(0.4, 0, 0.2, 1);
}
.dropzone.drag-over .dropzone-overlay { opacity: 1; }""",
      """const dz = document.querySelector('.dropzone');
['dragenter', 'dragover'].forEach(ev => {
  dz.addEventListener(ev, (e) => { e.preventDefault(); dz.classList.add('drag-over'); });
});
['dragleave', 'drop'].forEach(ev => {
  dz.addEventListener(ev, (e) => { e.preventDefault(); dz.classList.remove('drag-over'); });
});
dz.addEventListener('drop', (e) => {
  const files = e.dataTransfer.files;
  // handle files
});""",
      "Show static highlighted border on drop zone; no animation.",
      "transform + opacity + background-color — 60fps safe.",
      ["gmail.com compose", "notion.so"]),

    E("a100", "Scroll-To-Zoom Map", "interactive", "triggered", 200,
      "cubic-bezier(0.25, 1, 0.5, 1)", "easeOutQuart",
      ["transform"],
      "Interactive maps, image zoom interfaces, floor plans where ctrl+scroll zooms in and out.",
      "On regular scroll pages — ctrl+scroll conflicts with browser zoom and confuses users.",
      """.stz-canvas {
  transform-origin: center center;
  transition: transform 200ms cubic-bezier(0.25, 1, 0.5, 1);
  will-change: transform;
}
.stz-canvas.no-transition { transition: none; }""",
      """const canvas = document.querySelector('.stz-canvas');
let scale = 1;
canvas.addEventListener('wheel', (e) => {
  if (!e.ctrlKey && !e.metaKey) return; // require ctrl/cmd
  e.preventDefault();
  const delta = -e.deltaY * 0.001;
  scale = Math.max(0.5, Math.min(4, scale + delta));
  canvas.classList.add('no-transition');
  canvas.style.transform = `scale(${scale})`;
  clearTimeout(canvas._stzTimer);
  canvas._stzTimer = setTimeout(() => {
    canvas.classList.remove('no-transition');
  }, 100);
}, { passive: false });""",
      "Use explicit zoom buttons (+/-) instead of ctrl+scroll.",
      "transform: scale via wheel events — 60fps safe with rAF throttle.",
      ["google.com maps", "figma.com"]),

]


# ============================================================
# Validation
# ============================================================
assert len(ENTRIES) == 100, f"Expected 100 entries, got {len(ENTRIES)}"

expected_ids = [f"a{i:03d}" for i in range(1, 101)]
actual_ids = [e["id"] for e in ENTRIES]
assert actual_ids == expected_ids, f"ID mismatch: {set(expected_ids) - set(actual_ids)}"

required_fields = ["id", "name", "category", "type", "duration_ms", "easing",
                   "easing_name", "properties_animated", "when_to_use",
                   "when_not_to_use", "code", "reduced_motion",
                   "performance_note", "references"]
for e in ENTRIES:
    for f in required_fields:
        assert f in e, f"Entry {e.get('id')} missing field {f}"
    assert e["code"].get("css") or e["code"].get("js"), f"Entry {e['id']} has no code"
    assert len(e["references"]) >= 1, f"Entry {e['id']} has no references"
    # when_to_use / when_not_to_use: should be 1-3 sentences (be lenient — "e.g." adds periods)
    # Just check non-empty and not absurdly long.
    assert 10 <= len(e["when_to_use"]) <= 220, f"Entry {e['id']} when_to_use length out of range"
    assert 10 <= len(e["when_not_to_use"]) <= 220, f"Entry {e['id']} when_not_to_use length out of range"

# Forbidden easings
forbidden_easings = ["linear", "ease", "ease-in", "ease-out", "ease-in-out"]
for e in ENTRIES:
    assert e["easing"] not in forbidden_easings, \
        f"Entry {e['id']} uses forbidden easing: {e['easing']}"

# Forbidden animated properties (layout thrash)
forbidden_props = {"margin", "padding", "top", "left", "width", "height"}
for e in ENTRIES:
    bad = set(e["properties_animated"]) & forbidden_props
    assert not bad, f"Entry {e['id']} animates forbidden property: {bad}"

# Category counts
expected_categories = {
    "data-reveal": 15,
    "page-transition": 10,
    "scroll-triggered": 15,
    "hover-micro": 20,
    "loading-state": 10,
    "hero-choreography": 10,
    "navigation": 10,
    "interactive": 10,
}
cat_counts = Counter(e["category"] for e in ENTRIES)
for cat, count in expected_categories.items():
    assert cat_counts[cat] == count, \
        f"Category {cat} has {cat_counts[cat]} entries, expected {count}"

# Type values
valid_types = {"triggered", "ambient", "scroll"}
for e in ENTRIES:
    assert e["type"] in valid_types, f"Entry {e['id']} has invalid type: {e['type']}"


# ============================================================
# Write output
# ============================================================
output = {"animations": ENTRIES}
out_path = Path(__file__).parent / "data" / "animations-100.json"
out_path.parent.mkdir(exist_ok=True)
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Wrote {len(ENTRIES)} entries to {out_path}")
print(f"Categories: {dict(cat_counts)}")
