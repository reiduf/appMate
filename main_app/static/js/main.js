const menuEl = document.getElementById('menu');
const hamburger = document.getElementById('hamburger');

hamburger.addEventListener('click', () => {
  menuEl.classList.toggle('hidden');
})