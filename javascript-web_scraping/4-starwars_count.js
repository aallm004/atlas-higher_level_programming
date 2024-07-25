#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

  if (url !== undefined) {
request(url, (error, response, body) => {
  if (error) console.log(error);

  const data = JSON.parse(body).results;

  let movie = data.filter(x => x.characters.includes(
    'https://swapi-api.hbtn.io/api/people/18/'))
    console.log(movie)
  console.log(movie.length);
})
  }
