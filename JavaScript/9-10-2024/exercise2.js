//Create a function to calculate an area then recreate it using arrow function

class Rectangle { //Defining the class 
    constructor (length, width) {
        this.length = length;
        this.width = width;
    }

    area() { //Creating a method to show its area
        return this.length * this.width
    }
}

const shape = new Rectangle(10, 5); //Instantiating an object of the previously created class
console.log(shape.area()); //Exhibiting the area

const calc_area = (a, b) => a * b; //Creating the arrow function
console.log(calc_area(shape.length, shape.width)); //Showing the result