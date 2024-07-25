#!/usr/bin/node
const x = process.argv[2];
const data = process.argv[3];
const fs = require('fs');

if ((x !== undefined) && (data !== undefined)) {
fs.writeFile(x, data, (err) => {
    if (err) console.log(err);
})}
