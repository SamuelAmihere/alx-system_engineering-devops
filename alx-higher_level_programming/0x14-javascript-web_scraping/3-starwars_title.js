#!/usr/bin/node

const episode = process.argv[2];
const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';

req(url + episode, function (error, res, body) {
  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    const JSONres = JSON.parse(body);
    console.log(JSONres.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
