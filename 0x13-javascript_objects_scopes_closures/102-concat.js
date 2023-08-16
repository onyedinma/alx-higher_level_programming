#!/usr/bin/node
const { argv } = require('process');
const file = require('file');
let content = '';

// Read the content of the first file specified as a command-line argument
content = content.concat(file.readFileSync(argv[2]));

// Read the content of the second file specified as a command-line argument
content = content.concat(file.readFileSync(argv[3]));

// Write the concatenated content to a new file specified as a command-line argument
file.writeFileSync(argv[4], content);
