const { argv } = require('process');

// Getting the second and third command-line arguments.
const firstArg = argv[2];
const secondArg = argv[3];

// printing the values of the second and third command-line arguments.
console.log(`${firstArg} is ${secondArg}`);
