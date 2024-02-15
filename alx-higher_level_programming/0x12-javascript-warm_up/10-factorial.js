#!/usr/bin/node
function factorial (n) {
  const fact = isNaN(n) || n === 0 ? 1 : n * factorial(n - 1);
  return fact;
}
const result = factorial(Number(process.argv[2]));
console.log(result);
