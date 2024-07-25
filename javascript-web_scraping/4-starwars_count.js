#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/people/18';
const request = require('request');

request(url, (error, response, body) => {
  if (error) console.log(error);

  const data = JSON.parse(body);
  console.log(data.films.length);
});
