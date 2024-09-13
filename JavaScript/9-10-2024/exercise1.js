//Create 'car' object and iterate over it

function Car(brand, model, year, color) { //Defining the object throught constructor function
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.color = color;
}

car = new Car("Toyota", "Corolla GLi", "2024", "white"); //Instantiating the new object

Object.entries(car).forEach(([k, v]) => console.log(`This car ${k} is ${v}`)); //Exhibiting the entries of car object through loops

car.color = "black"; //Changing its 'color' value
console.log(car.color); //Exhibiting its altered value

const {brand, model} = car; //Destructuring assignment

console.log(`The brand is ${brand} and the model is ${model}`);