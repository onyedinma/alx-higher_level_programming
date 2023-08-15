#!/usr/bin/env node

// Import the `process` module.
const { argv } = require('process');

// Get the second command-line argument.
const num = Number(argv[2]);

// Check if the number is NaN.
// If it is, log `Not a number`.
// Otherwise, log the number.
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
