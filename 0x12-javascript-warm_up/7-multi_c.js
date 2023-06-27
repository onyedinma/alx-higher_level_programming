#!/usr/bin/node

const process = require('process');
const argv = process.argv;
let i;
if (argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (argv[2] < 0) {
  } else {
  for (i = 0; i < Number(argv[2]); i++) {
    console.log('C is fun');
  }
}
