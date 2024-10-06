//ex1
console.log("Hello World!");

//ex2
let sum = (a, b) => a + b;
console.log(sum(2,3));

//ex3
let num = 3;
console.log(`The number ${num} is ${num % 2 === 0 ? 'even':'odd'}`)

//ex4
function intComparison(a, b) {
    let higher = (a > b ? a : b);
    return higher
}
console.log(`The biggest number between 7 and 4 is ${intComparison(4, 7)} `)

//ex5
for (let i = 1; i < 11; i++) {
    console.log(i);
}

//ex6
function sumInterval() {
    let L = 1; let R = 101; let sums = 0;
    while (L < R) {
        sums += L + R;
        L ++; R--;
    } if (L == R) {
        sums += L;
    }
    return sums
}
console.log(sumInterval());

//ex7
function checkDivisors(x) {
    let L = 2; let R = parseInt(x ** (1/2)); let divisors = [];
    while (L < R) {
        if (x % L == 0) {
            divisors.push(L);
            break
        }
        if (x % R == 0) {
            divisors.push(R);
            break
        }
        L ++; R --;
    }

    if (L == R && x % L == 0) {
        divisors.append(L)
    }
    return divisors
    }

console.log(`The number 19 ${checkDivisors(19).length > 0 ? 'is not a prime number.' : 'is a prime number.' }`);

//ex8
function arithmeticMean(list) {
    let L = 0; let R = list.length-1; let intSum = 0;
    while (L < R) {
        intSum += list[L] + list[R];
        L ++; R --;
    } if (L == R) {
        intSum += list[L];
    }
    return intSum / list.length
}

console.log(`The arithmetic mean of the numbers 8,6,9,5 and 12 is ${arithmeticMean([8,6,9,5,12])}`);

//ex9
function stringInverter(str) {
    return str.split('').reverse().join('');
}

console.log(`The inverse of the word 'hello' is ${stringInverter('hello')}!`);

//ex10
function vowelsCount(str) {
    str = str.toLowerCase().replace(/\s/g, "");
    let L = 0; let R = str.length-1; counter = 0;
    while (L < R) {
        if ('aeiou'.match(str[L])) {
            counter ++;
        }
        if ('aeiou'.match(str[R])) {
            counter ++;
        }
        L ++; R --;
    } if (L == R && 'aeiou'.match(str[L])) {
        counter ++;
    } return counter
}

console.log(`The text 'I am clEver' has a total of ${vowelsCount('I am clEver')} vowels.`);