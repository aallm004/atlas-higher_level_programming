#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

if (url !== undefined) {
  request(url, (error, response, body) => {
    if (error) console.log(error);

    const data = JSON.parse(body).results;
    let count = 0;
    data.filter(x => x.characters.forEach(element => {
      if (element.indexOf('18') > 0) count++;
    }));
    console.log(count);
  });
}
