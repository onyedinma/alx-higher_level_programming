#!/usr/bin/node

const argv = process.argv;

function factorial (a) {
  let factorial = 1;
  if (argv[2] === undefined) {
    return 1;
  } else {
    for (let i = Number(a); i > 1; i--) {
      factorial *= i;
    }
    return factorial;
  }
}

console.log(factorial(argv[2]));
