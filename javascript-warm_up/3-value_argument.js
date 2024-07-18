#!/usr/bin/node
const arg = process.argv.slice(2);
let count = 0;

for (const item of arg) {
  count++;
}

if (count === 0) {
  console.log('No argument');
} else {
    console.log(arg);
}
