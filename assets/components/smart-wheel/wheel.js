let currentMonth = 0; // Январь — это 0 (на 3 часах)
let locked = false;

// Текущий накопленный угол поворота колеса (не обнуляется, может расти/уменьшаться
// за пределы 0–360 — это нужно, чтобы колесо всегда крутилось кратчайшим путём,
// а не "отматывалось" назад на 330° вместо того, чтобы провернуться на 30°).
let currentRotation = 0;

// 12 месяцев: угол, на который нужно повернуть КОЛЕСО (по часовой стрелке),
// чтобы месяц с этим индексом оказался в положении 3 часа.
//
// ВАЖНО: на самой картинке wheel.svg месяцы расположены ПРОТИВ часовой стрелки
// (Jan на 3 часах, Dec чуть ниже него по часовой, Feb чуть выше него против часовой).
// Поэтому, чтобы подвинуть месяц №i к 3 часам, колесо нужно крутить ПО часовой
// на 30*i градусов (а не против, как было раньше).
const angles = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330];

// Ссылки на месяцы
const monthUrls = [
  'https://example.com/january', 'https://example.com/february', 'https://example.com/march',
  'https://example.com/april', 'https://example.com/may', 'https://example.com/june',
  'https://example.com/july', 'https://example.com/august', 'https://example.com/september',
  'https://example.com/october', 'https://example.com/november', 'https://example.com/december'
];

function go(targetMonthIndex) {
  if (locked) return;
  locked = true;

  const wheel = document.getElementById("wheelWrap");

  // Целевой угол (0–360), при котором targetMonthIndex окажется на 3 часах.
  const targetAngle = angles[targetMonthIndex];

  // Считаем кратчайшую дельту от текущего накопленного угла до целевого,
  // чтобы колесо не делало лишний почти-полный оборот.
  let delta = ((targetAngle - currentRotation) % 360 + 360) % 360;
  if (delta > 180) delta -= 360;

  currentRotation += delta;

  wheel.style.transform = `rotate(${currentRotation}deg)`;

  currentMonth = targetMonthIndex;

  // Запускаем анимацию лап — коты начинают крутить колесо вместе с вращением
  document.querySelector('.stage').classList.add('spinning');

  setTimeout(() => {
    window.open(monthUrls[targetMonthIndex], '_blank');
    window.location.reload();
  }, 2500);
}
