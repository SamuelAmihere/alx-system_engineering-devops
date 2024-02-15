#!/usr/bin/node

const { dict } = require('./101-data');

const obj = Object.entries(dict);

const newDict = {};

obj.forEach(item => {
  newDict[item[1]] ? newDict[item[1]].push(item[0]) : newDict[item[1]] = [item[0]];
});

console.log(newDict);
