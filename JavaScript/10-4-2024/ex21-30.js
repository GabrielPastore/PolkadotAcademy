//ex21
const checkMult = (a, b) => (a % b == 0 ? true: (b % a == 0 ? true: false));
console.log(`The numbers 20 and 5 ${checkMult(5, 20) ? 'are': 'are not'} multiples of each other`);

//ex22
const absoluteValue = (a) => (a >= 0 ? a:a*-1);
console.log(absoluteValue(-5));

//ex23
const sqrt = (a) => a ** 1/2;
console.log(sqrt(9));

//ex24
function checkDivisors(x) {
    let L = 1; let R = parseInt(x ** (1/2)); let divisors = [];
    while (L < R) {
        if (x % L == 0) {
            divisors.push(L);
            divisors.push(x/L);
        }
        if (x % R == 0) {
            divisors.push(R);
            divisors.push(x/R);
        }
        L ++; R --;
    }

    if (L == R && x % L == 0) {
        divisors.append(L);
    }
    return divisors
    }

console.log(checkDivisors(360));

//ex25
const removeVowels = str => str.replace(/[aeiou]/gi, '*');
console.log(removeVowels('i am very cool'));

//ex26
const haveSubStr = (str, substr) => (str.includes(substr) ? true:false);
console.log(haveSubStr("Good Morning", "Morning"));

//ex27
function sumOfPairs(list) {
    let L = 0; let R = list.length - 1; let sum = 0;
    while (L <= R) {
        sum += (list[L] % 2 == 0 ? list[L] : 0);
        sum += (list[R] % 2 == 0 ? list[R] : 0);
        L++; R--;
    } if (L == R && list[L] % 2 == 0) {
        sum += list[L];
    } return sum;
}

console.log(sumOfPairs([1,2,5,12,18,9,10,23,21,6,5,10]));

//ex28
function multNumsOnList(list) {
    let L = 0; let R = list.length-1; let mult = 1;
    while (L < R) {
        mult *= list[L] * list[R];
        L++; R--;
    }
    if (L == R) {
        mult *= list[L];
    } return mult
}

console.log(multNumsOnList([1,2,5,12,18,9,10,23,21,6,5,10]));

//ex29
function isSorted(list) {
    let L = 1; let R = list.length-1;
    while (L < R) {
        if (list[L] < list[L-1] || list[R] < list[R-1]) {
            return false
        } L++; R--;
    } if (L == R && list[L] < list[L-1]) {
        return false
    } return true
}

console.log(isSorted([1,2,3,4,5,7]));

//ex30
function evensCounter(list) {
    let L = 0; let R = list.length - 1; let sum = 0;
    while (L <= R) {
        sum += (list[L] % 2 == 1 ? 1 : 0);
        sum += (list[R] % 2 == 1 ? 1 : 0);
        L++; R--;
    } if (L == R && list[L] % 2 == 1) {
        sum += 1;
    } return sum;
}

console.log(evensCounter([1,2,5,12,18,9,10,23,21,6,5,10]));