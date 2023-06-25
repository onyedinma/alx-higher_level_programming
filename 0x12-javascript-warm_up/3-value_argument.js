#!/usr/bin/node

const process = require('process');
const argv = process.argv;
// print process.argv
if (argv[2]== null) {
  console.log('No argument');
} else{
  console.log(argv[2]);
}
