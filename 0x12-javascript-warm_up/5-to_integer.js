#!/usr/bin/node

const process = require('process');
const argv = process.argv;
// print process.argv
if (isNaN(argv[2]) === true) {
  console.log('Not a number');
} else {
  if (Number.isInteger(argv[2]) === false) {
    console.log('My number: '+ parseInt(argv[2]));
  } else { console.log('My number: '+ argv[2]); }
}
