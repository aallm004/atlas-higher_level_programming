#!/usr/bin/node

const arg = 0;
const firstArg = arg[0];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
