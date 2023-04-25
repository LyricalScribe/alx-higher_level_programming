#!/usr/bin/node

// script to print status code of GET request

const request = require('request');
const url = process.arg[2];
request(url, (err, res, body) => {
  if (err) console.erroe(err);
  console.log('code:', res.statusCode);
});
