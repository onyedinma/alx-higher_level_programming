#!/usr/bin/node

// Import the 'dict' object from './101-data'
const { dict } = require('./101-data');

// Use the reduce() method on Object.entries(dict) to transform the 'dict' object
const myValue = Object.entries(dict).reduce((acc, [key, value]) => {
  // Check if the 'value' already exists as a key in the 'acc' object
  if (acc[value]) {
    // If it exists, append the 'key' to the existing array value
    acc[value] = [...acc[value], key];
  } else {
    // If it doesn't exist, create a new array value with the 'key'
    acc[value] = [key];
  }
  return acc;
}, {});

// Print the resulting 'myValue' object to the console
console.log(myValue);
