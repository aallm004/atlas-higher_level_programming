#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  const total = a + b;
  return (total);
}

console.log(add(a, b));
