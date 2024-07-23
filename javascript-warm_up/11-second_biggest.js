#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
//  const numbers = args.map(Number);
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
