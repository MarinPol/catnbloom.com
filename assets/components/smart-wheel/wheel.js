// SYSTEM LOG
// v1.0 — Initial standalone demo version (example.com URLs, window.open)
// v1.1 — 2026-06-23 — Fixed: real /smart/sc01/–sc12/ URLs, same-tab navigation,
//                      removed window.open + reload, removed locked reset on navigation.

let currentMonth = 0;
let locked = false;

// Accumulated rotation angle — never resets, so the wheel always spins the
// shortest path to the target rather than unwinding a full 330° the wrong way.
let currentRotation = 0;

// 12 sectors: clockwise angle needed to bring month index i to the 3 o'clock marker.
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

function go(targetMonthIndex) {
  if (locked) return;
  locked = true;

  const wheel = document.getElementById('wheelWrap');
  if (!wheel) return;

  // Shortest-path delta
  const targetAngle = angles[targetMonthIndex];
  let delta = ((targetAngle - currentRotation) % 360 + 360) % 360;
  if (delta > 180) delta -= 360;

  currentRotation += delta;
  wheel.style.transform = `rotate(${currentRotation}deg)`;
  currentMonth = targetMonthIndex;

  // Start paw animation
  const stage = document.querySelector('.stage');
  if (stage) stage.classList.add('spinning');

  // Navigate after animation completes (2.5s matches CSS transition)
  setTimeout(function () {
    window.location.href = monthUrls[targetMonthIndex];
  }, 2500);
}
