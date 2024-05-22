const special = document.querySelector('#red_header');
special.addEventListener('click', function() {
  const header = document.querySelector('header');
  header.classList.add('red');
});
