#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = argv.map(Number)
    .slice(2, argv.length)
    .sort((i, j) => i - j);
  const result = numbers[numbers.length - 2];
  console.log(result);
}
