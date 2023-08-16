#!/usr/bin/node

// Import the `process` module.
const { argv } = require('process');

// Check if there are at least 3 command-line arguments.
// If there are not, print `0`.
// Otherwise, find the second largest number in the array of command-line arguments and print it.
const message = 'Missing command-line arguments';
if (argv.length <= 3) {
  console.log(message);
} else {
  // Get the array of command-line arguments without the first two arguments.
  const numbers = argv.slice(2);

  // Sort the array of numbers in descending order.
  numbers.sort((a, b) => b - a);

  // Get the second largest number in the array.
  const secondLargestNumber = numbers[numbers.length - 2];

  // Log the second largest number.
  console.log(secondLargestNumber);
}
