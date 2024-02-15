#!/usr/bin/node
const argv = Math.floor(Number(process.argv[2]));
if (!isNaN(argv)) {
  for (let i = argv; i > 0; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
