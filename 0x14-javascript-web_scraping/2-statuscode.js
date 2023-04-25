#!/usr/bin/node
// script to priint status code of get request
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  console.log('code:', res.statusCode);
})
