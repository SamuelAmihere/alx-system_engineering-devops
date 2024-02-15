#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (arr, n) {
    arr.push(n);
    return arr;
  }, []);
};
