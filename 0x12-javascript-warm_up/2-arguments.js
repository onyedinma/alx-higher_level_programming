#!/usr/bin/node

// This script counts the number of command line arguments and prints a message accordingly.

const argumentCount = process.argv.length - 2;
if (argumentCount === 0) {
  console.log('No argument');
} else if (argumentCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
