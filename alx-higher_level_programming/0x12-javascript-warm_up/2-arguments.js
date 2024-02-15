#!/usr/bin/node
const count = process.argv.length;
const msg = count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found';
console.log(msg);
