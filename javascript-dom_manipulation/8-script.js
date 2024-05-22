document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then((data) => {
      const hello = document.querySelector('#hello');
      hello.textContent = data.hello;
    })
.catch((error) => {
  console.error('Error fetching data', error);
  });
});
