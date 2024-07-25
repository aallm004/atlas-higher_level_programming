#!/usr/bin/node
const x = process.argv[2];
const fs = require('fs');

if (x != undefined) {
  fs.readFile(x, (err, data) => {
    if (err) throw err;
    console.log(data.toString());
  });
}
