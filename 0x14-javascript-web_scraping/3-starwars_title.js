#!/usr/bin/node
// script that prints the title of a Star Wars movi
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
