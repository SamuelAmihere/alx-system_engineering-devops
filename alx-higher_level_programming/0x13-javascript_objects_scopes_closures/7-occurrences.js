#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((c, n) => n === searchElement ? c + 1 : c, 0);
};
