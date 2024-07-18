#!/usr/bin/node

const arg = 0;
const firstArg = arg[0];

if (firstArg === 0) {
  console.log('No argument');
} else if (firstArg === 1) {
    console.log("Argument found");
} else {
  console.log("Arguments found");
}
