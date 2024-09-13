const title = document.getElementById('title');
const paragraph = document.getElementsByTagName('p');
const button = document.getElementById('button');

title.textContent = 'New Title';

for (let i = 0; i < paragraph.length; i++) {
    paragraph[i].textContent = `Modified text ${i+1}`;
}

button.addEventListener('click', function() {
    alert('Button clicked!');
});