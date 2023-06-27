#!/usr/bin/node

const argv = process.argv;
// function to calculate the factorial of a number
function facto (n) {
  // check if n is negative, zero or positive or (not a number)
  if (n < 0) {
    // return null for negative numbers
    return null;
  } else if (n === 0 || isNaN(n)) {
    // return 1 for zero and when value is not a number
    return 1;
  } else {
    // return n times the factorial of n-1
    return n * facto(n - 1);
  }
}
console.log(facto(Number(argv[2])));
