#!/usr/bin/node

const argv = process.argv;

function add (a, b) {
  const c = Number(a) + Number(b);
  console.log(c);
}
add(argv[2], argv[3]);
