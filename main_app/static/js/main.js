const menuEl = document.getElementById('menu');
const hamburger = document.getElementById('hamburger');
const signup = document.getElementById('signup');

hamburger.addEventListener('click', () => {
  menuEl.classList.toggle('hidden');
})

signup.addEventListener('click', () => {
  console.log('clicked')
})