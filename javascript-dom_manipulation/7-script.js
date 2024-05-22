fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then((data) => {
    const movie = document.querySelector('#list_movies');
    data.results.forEach(element => {
      const list = document.createElement('li');
      list.textContent = element.title;
      movie.appendChild(list);
    });
  })
  .catch((error) => {
    console.error('Error fetching data', error);
  });
