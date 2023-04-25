#!/usr/bin/node
// script that prints the number of movies
const request = require('request');

// Get the URL to request from the command-line arguments
const url = process.argv[2];

// Make an HTTP request to the URL using 'request'
request(url, (err, res, body) => {
  if (err) {
    // If there was an error, log it to the console and return
    console.error(err);
    return;
  }

  // Parse the response body as JSON
  const data = JSON.parse(body);

  // Count the number of characters whose URLs include the string '18'
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const chars = data.results[i].characters;
    for (let k = 0; k < chars.length; k++) {
      if (chars[k].includes('18')) {
        count = count + 1;
      }
    }
  }

  // Log the count to the console
  console.log(count);
});
