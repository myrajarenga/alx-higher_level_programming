#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get({ url: url }, (error, response, body) => {
  if (error) {
    console.error(`Error requesting ${url}: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code ${response.statusCode} for ${url}`);
    return;
  }

  fs.writeFile(filePath, body, { encoding: 'utf8' }, (error) => {
    if (error) {
      console.error(`Error writing to file ${filePath}: ${error}`);
      return;
    }

    console.log(`Successfully wrote contents of ${url} to ${filePath}`);
  });
});
