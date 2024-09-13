const button = document.getElementById("button");
const input = document.getElementById("input");
const list = document.getElementById("textList");

button.addEventListener('click', addElement);

function addElement() {
    const li = document.createElement('li');
    li.textContent = input.value.trim();
    list.appendChild(li);
    input.value = '';
}