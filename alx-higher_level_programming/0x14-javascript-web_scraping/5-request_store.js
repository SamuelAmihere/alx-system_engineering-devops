#!/usr/bin/node
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const dest = process.argv[3];
req(url).pipe(fs.createWriteStream(dest));
