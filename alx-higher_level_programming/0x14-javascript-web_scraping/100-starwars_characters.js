#!/usr/bin/node

const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

req.get(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }

  const results = JSON.parse(body).characters;
  for (const i of results) {
    req.get(i, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
