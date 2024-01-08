const menuEl = document.getElementById('menu');
const hamburger = document.getElementById('hamburger');
const salary = document.getElementById('salary')

hamburger?.addEventListener('click', () => {
  menuEl.classList.toggle('hidden');
})



salary?.toLocaleString('en', {useGrouping:true});
