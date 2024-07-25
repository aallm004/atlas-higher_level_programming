#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

if ((url !== undefined) && (path !== undefined)) {
  request(url, (error, response, body) => {
    if (error) console.log(error);
    fs.writeFile(path, body, (err) => {
      if (err) console.log(err);
    });
  });
}
