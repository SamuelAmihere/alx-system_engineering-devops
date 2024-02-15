#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  number = ++number;
  theFunction(number);
};
