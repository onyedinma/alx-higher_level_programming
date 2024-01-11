#!/usr/bin/node
// Import the `process` module.
const { argv } = require('process');

// Get the second command-line argument.
const size = Number(argv[2]);

// Check if the size is NaN.
// If it is, print `Missing size`.
// Otherwise, print a square of X's with the specified size.
const message = 'Missing size';
if (isNaN(size)) {
  console.log(message);
} else {
  for (let r = 0; r < size; r++) {
    let row = '';
    for (let c = 0; c < size; c++) {
      row += 'X';
    }
    console.log(row);
  }
}
