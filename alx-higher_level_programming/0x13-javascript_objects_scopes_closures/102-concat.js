#!/usr/bin/node
const fs = require('fs');
const srca = fs.readFileSync(process.argv[2], 'utf8');
const srcb = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], srca + srcb);
