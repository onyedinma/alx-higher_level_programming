#!/usr/bin/node

const process = require('process');
const argv = process.argv;
let xNum = '';
if (!Number(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i <= argv[2] - 1; i++) {
    xNum = xNum + 'x';
  }
  for (let j = 0; j <= argv[2] - 1; j++) {
    console.log(xNum);
  }
}
