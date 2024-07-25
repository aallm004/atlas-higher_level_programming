#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const out = {};
let results;

if (url !== undefined) {
  request(url, (error, response, body) => {
    if (error) console.log(error);
    const data = JSON.parse(body);
    results = data.filter(x => x.completed);
    results.forEach(element => {
      if (out[element.userId]) { out[element.userId] += 1; } else { out[element.userId] = 1; }
    });
    console.log(out);
  });
}
