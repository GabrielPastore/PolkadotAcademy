//ex11
let list = [1, 3, 2, 5, 8, 6, 12]; let num = 8;
console.log(`The number ${num} is${list.includes(num) ? '':' not'} on the list ${list}.`)

//ex12
function factorial(x) {
    if (x == 1) {
        return 1
    } return x * factorial(x-1)
}

console.log(factorial(8));

//ex13
function fibonacci(x) {
    let y = x--;
    if (x <= 1) {
        return 1
    } return fibonacci(y-1) + fibonacci(y-2)
}

console.log(fibonacci(10));

//ex 14
function strReplace(str) {
    return str.replace(/\s/g, "")
}

console.log(strReplace("   o   i    "));

//ex15 
function charCount(str, char) {
    str = str.toLowerCase().replace(/\s/g, "");
    let L = 0; let R = str.length-1; counter = 0;
    while (L < R) {
        if (str[L] == char) {
            counter ++;
        }
        if (str[R] == char) {
            counter ++;
        }
        L ++; R --;
    } if (L == R && str[L] == char) {
        counter ++;
    } return counter
}

console.log(charCount('arroz', 'r'));

//ex16
function checkPalindrome(str) {
    str = str.replace(/\s/g, '').toLowerCase();
    const strReversed = str.split('').reverse().join('');
    return str === strReversed;
}

console.log(checkPalindrome("socorram me subi no onibus em marrocos"))

//ex17
function sortNumbers(list) {
    return list.sort((a, b) => a - b);
}

console.log(sortNumbers([1, 7, 3, 12, 19, 2, 8, 15]));

//ex18
function randomNumberGenerator() {
    return Math.floor(Math.random() * 100 + 1);
}

console.log(randomNumberGenerator());

//ex19
function celsiusConvertion(x) {
    return (x * 9) /5 + 32
}

console.log(celsiusConvertion(20));

//ex20
function digitsSum(numStr) {
    let sum = 0;
    for (let i = 0; i < numStr.length; i++) {
        sum += parseInt(numStr[i]);
    }
    return sum
}

console.log(`The sum of all digits in the number 135 is ${digitsSum("135")}`);