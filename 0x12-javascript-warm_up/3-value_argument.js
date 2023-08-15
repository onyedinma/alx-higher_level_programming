#!/usr/bin/env node

// This script prints the first command line argument, or 'No argument' if none is provided.

const firstArgument = process.argv[2];
if (typeof firstArgument === 'undefined') {
  console.log('No argument');
} else {
  console.log(firstArgument);
}
