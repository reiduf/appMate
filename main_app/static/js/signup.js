const signup = document.getElementById('signup');
const signupForm = document.getElementById('signup-form');
const signupX = document.getElementById('close-signup');

signup.addEventListener('click', () => {
  signupForm.classList.toggle('hidden')
})

signupX.addEventListener('click', () => {
  signupForm.classList.toggle('hidden')
})