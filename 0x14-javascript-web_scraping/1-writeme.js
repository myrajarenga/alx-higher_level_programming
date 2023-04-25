#!/usr/bin/node
//script to write to file
const fs = require('fs');
const pathfile = process.argv[2];
const content = process.argv[3];
fs.writeFile(pathfile, content, err => {
  if (err) {
    console.error(err);
  }
});
