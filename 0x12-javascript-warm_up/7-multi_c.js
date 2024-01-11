#!/usr/bin/node

// This script prints the message 'C is fun' a specified number of times.

// Import the `process` module to access command line arguments
const { argv } = require('process');

// Get the second command line argument, which specifies the number of times to print the message
const numOccurrences = Number(argv[2]);

// Check if the number of occurrences is not a valid number
if (isNaN(numOccurrences)) {
  // If it is not a valid number, print an error message
  console.log('Missing number of occurrences');
} else {
  // Otherwise, print the message the specified number of times
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
