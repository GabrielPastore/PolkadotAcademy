const button = document.getElementById("b1");
const text = document.getElementById("text");

const rotation = ['Vasco', 'da', 'Gama'];
let textIndex = 0;

function changeText() {
    text.textContent = rotation[textIndex];
    textIndex = (textIndex+1) % rotation.length;
}

document.addEventListener('DOMContentLoaded', changeText);
button.addEventListener('click', changeText);