#!/usr/bin/node
// script to read a file
const fs = require('fs');
const pathfile = process.argv[2];
fs.readFile(pathfile, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
