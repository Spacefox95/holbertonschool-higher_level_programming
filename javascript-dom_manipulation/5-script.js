const newHeader = document.querySelector('#update_header');

newHeader.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.textContent = 'New Header';
});
