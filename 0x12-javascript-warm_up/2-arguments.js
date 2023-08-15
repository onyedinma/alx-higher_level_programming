#!/usr/bin/node

// This script counts the number of command line arguments and prints a message accordingly.

const argument_count = process.argv.length - 2;
if (argument_count === 0) {
  console.log('No argument');
} else if (argument_count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
