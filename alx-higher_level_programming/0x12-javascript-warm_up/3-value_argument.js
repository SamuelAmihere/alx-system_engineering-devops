#!/usr/bin/node
const argv = process.argv[2];
const msg = typeof argv === 'undefined' ? 'No argument' : argv;
console.log(msg);
