// SYSTEM LOG
// v1.0 — Initial standalone demo version (example.com URLs, window.open)
// v1.1 — 2026-06-23 — Fixed: real /smart/sc01/–sc12/ URLs, same-tab navigation
// v1.2 — 2026-06-23 — BUGFIX: corrected month lookup to account for current wheel rotation
//                      Sectors are static; wheel image rotates — go() now maps sectorIndex
//                      to actualMonth via: (sectorIndex + rotationOffset) % 12

let currentMonth = 0;
let locked = false;

// Accumulated rotation angle — never resets, so the wheel always spins the
// shortest path to the target rather than unwinding the wrong way.
let currentRotation = 0;

// 12 sectors: clockwise angle to rotate the wheel so month i reaches the marker.
// January = 0° (already at 3 o'clock on the SVG), each step = 30°.
const angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330];

// Month destination URLs — match _smart/ permalink structure
const monthUrls = [
  '/smart/sc01/',
  '/smart/sc02/',
  '/smart/sc03/',
  '/smart/sc04/',
  '/smart/sc05/',
  '/smart/sc06/',
  '/smart/sc07/',
  '/smart/sc08/',
  '/smart/sc09/',
  '/smart/sc10/',
  '/smart/sc11/',
  '/smart/sc12/'
];

function go(sectorIndex) {
  if (locked) return;
  locked = true;

  const wheel = document.getElementById('wheelWrap');
  if (!wheel) return;

  // ── FIX v1.2 ──────────────────────────────────────────────────────────────
  // The SVG overlay sectors are STATIC. The wheel IMAGE rotates.
  // When the wheel is rotated by R degrees, the user clicking on visual month j
  // actually triggers sector i = (j - R/30) mod 12.
  // Inverse: the actual month the user intended = (sectorIndex + R/30) mod 12.
  const rotationOffset = Math.round(((currentRotation % 360) + 360) % 360 / 30);
  const actualMonth = (sectorIndex + rotationOffset) % 12;
  // ──────────────────────────────────────────────────────────────────────────

  // Shortest-path delta to bring actualMonth to the marker
  const targetAngle = angles[actualMonth];
  let delta = ((targetAngle - currentRotation) % 360 + 360) % 360;
  if (delta > 180) delta -= 360;

  currentRotation += delta;
  wheel.style.transform = `rotate(${currentRotation}deg)`;
  currentMonth = actualMonth;

  // Start paw animation
  const stage = document.querySelector('.stage');
  if (stage) stage.classList.add('spinning');

  // Navigate after animation completes (2.5s matches CSS transition)
  setTimeout(function () {
    window.location.href = monthUrls[actualMonth];
  }, 2500);
}
