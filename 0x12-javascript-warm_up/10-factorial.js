#!/usr/bin/node

// This script calculates the factorial of a number passed as a command line argument and prints the result.

// Define the factorial function
function factorial (n) {
  // Check if n is 0 or not a number
  if (n === 0 || isNaN(n)) {
    // If it is, return 1
    return 1;
  } else {
    // Otherwise, return n multiplied by the factorial of n-1
    return n * factorial(n - 1);
  }
}

// Get the first command line argument and convert it to a number
const number = Number(process.argv[2]);

// Calculate the factorial of the number
const result = factorial(number);

// Print the result
console.log(result);
