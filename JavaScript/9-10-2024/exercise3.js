//Create a function with 3 arguments, 2 numbers and an arithmetic operation to subject the numbers and display their result
//All arguments of the function are given by the user's inputs through Node.js in the terminal

const sum = (a, b) => a + b;
const sub = (a, b) => a - b;
const mult = (a, b) => a * b;
const div = (a, b) => a / b;
const executeOperation = (x, y, op) => op(x, y);

const Selector = {
    1: sum,
    2: sub,
    3: mult,
    4: div
}

let nums = [];

function get_operation(message, deliver) {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question(message, input => {
        readline.close();
        deliver(input);
    });
}

function get_num_input(message, deliver, iterations) {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question(message, input => {
        const num = parseInt(input, 10);
        readline.close();
        if (isNaN(num)) {
            console.log("This is not a valid answer! Try again.");
            get_num_input(message, deliver, iterations);
        } else {
            deliver(num, iterations, message);
        }
    });
}

function save_input(input, iterations_left, message) {
    nums.push(input);
    iterations_left --;
    if (iterations_left > 0) {
        get_num_input(message, save_input, iterations_left);
    } else {
        get_operation("Choose an arithmetic operation.\n[1 for sum, 2 for subtraction, 3 for multiplication and 4 for division]\nA: ", input => {
            nums.push(input);
            if (nums[2] in Selector) {
                console.log(executeOperation(nums[0], nums[1], Selector[nums[2]]));
            } else {
                console.log("Not a valid operation.")
            }
        });
    }
}

function main() {
    get_num_input("Type an integer.\nA: ", save_input, 2);
}

main()
