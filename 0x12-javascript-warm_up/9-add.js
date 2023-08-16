#!/usr/bin/node

const {argv} = require('process');

// This script adds two numbers passed as command line arguments and prints the result.

function add(a, b) {
  return a + b;
}

const firstNumber = Number(argv[2]);
const secondNumber = Number(argv[3]);
const sum = add(firstNumber, secondNumber);
console.log(sum);

