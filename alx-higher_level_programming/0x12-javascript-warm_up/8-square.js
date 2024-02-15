#!/usr/bin/node
const argv = Math.floor(Number(process.argv[2]));
if (!isNaN(argv)) {
  for (let i = 0; i < argv; i++) {
    let rw = '';
    for (let j = 0; j < argv; j++) {
      rw += 'X';
    }
    console.log(rw);
  }
} else {
  console.log('Missing size');
}
