#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    printChars(chars, 0);
  }
});

function printChars (chars, idx) {
  req(chars[idx], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) {
        printChars(chars, idx + 1);
      }
    }
  });
}
