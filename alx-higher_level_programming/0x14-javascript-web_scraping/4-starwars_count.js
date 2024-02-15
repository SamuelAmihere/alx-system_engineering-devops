#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
req(id, function (err, res, body) {
  if (!err) {
    const results = JSON.parse(body).results;
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
