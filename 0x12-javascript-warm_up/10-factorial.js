#!/usr/bin/node

const argv = process.argv;
function facto (a) {
  let factorial = 1;
  if (argv[2] === undefined) {
    console.log(1);
  } else {
    for (let i = Number(a); i > 1; i--) {
      factorial = factorial * i;
    }
    console.log(factorial);
  }
}

facto(argv[2]);
