const menuEl = document.getElementById('menu');
const hamburger = document.getElementById('hamburger');
let salary = document.querySelector('.salary')?.innerText

hamburger?.addEventListener('click', () => {
  menuEl.classList.toggle('hidden');
})

let salaryNum

if (salary) {
  salaryNum = parseInt(salary).toLocaleString('en', {useGrouping:true});
  document.querySelector('.salary').innerText = salaryNum;
}

