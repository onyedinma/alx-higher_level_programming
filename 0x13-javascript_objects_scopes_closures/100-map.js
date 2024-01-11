#!/usr/bin/node

// Import the 'list' array from './100-data'
const array = require('./100-data').list;

// Print the 'arr' array to the console
console.log(array);

// Use the map() method on the 'arr' array to create a new array
// where each element is multiplied by its index
console.log(array.map((x, idx) => x * idx));
