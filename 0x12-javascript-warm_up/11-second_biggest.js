#!/usr/bin/node

// This script prints the second largest number passed as a command line argument.

// Check if there are fewer than 3 command line arguments
if (process.argv.length <= 3) {
  // If there are, print 0
  console.log(0);
} else {
  // Otherwise, create an array of the command line arguments, converted to numbers and sorted in ascending order
  const numbers = process.argv.slice(2).map(Number).sort((a, b) => a - b);

  // Get the second largest number from the array
  const secondLargestNumber = numbers[numbers.length - 2];

  // Print the second largest number
  console.log(secondLargestNumber);
}
