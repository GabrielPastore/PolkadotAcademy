const paragraph = document.getElementById("text");

const buttonText = document.getElementById("b1");
buttonText.addEventListener("click", function() {
    paragraph.style.color = "red"; 
});

const buttonBackground = document.getElementById("b2");
buttonBackground.addEventListener("click", function() {
    document.body.style.backgroundColor = "black";
});

const buttonFont = document.getElementById("b3");
buttonFont.addEventListener("click", function() {
    paragraph.style.fontFamily = 'Arial, sans-serif';
});