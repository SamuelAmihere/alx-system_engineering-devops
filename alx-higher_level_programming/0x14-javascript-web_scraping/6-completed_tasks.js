#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req(url, function (err, res, body) {
  if (!err) {
    const todoAll = JSON.parse(body);

    const completed = {};
    todoAll.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else if (todo.completed) {
        completed[todo.userId] += 1;
      }
    });

    console.log(completed);
  }
});
