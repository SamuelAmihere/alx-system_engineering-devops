#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, fcontent) {
  console.log(err || fcontent);
});
