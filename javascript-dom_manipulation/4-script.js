const parent = document.querySelector('ul.my_list');
const addChild = document.querySelector('#add_item');

addChild.addEventListener('click', () => {
	const child = document.createElement('li');
	child.textContent = 'Item';
  parent.appendChild(child);
});
