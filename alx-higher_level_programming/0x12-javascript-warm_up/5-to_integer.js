#!/usr/bin/node
const argv = Math.floor(Number(process.argv[2]));
const msg = isNaN(argv) ? 'Not a number' : `My number: ${argv}`;
console.log(msg);
