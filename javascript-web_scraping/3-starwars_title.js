#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');

if (id !== undefined) {
  request(url, (error, response, body) => {
    if (error) console.log(error);

    const data = JSON.parse(body);
    console.log(data.title);
  });
}
