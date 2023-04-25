#!/usr/bin/node
// script that computes the number of tasks completed by user id.
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error requesting ${apiUrl}: ${error}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code ${response.statusCode} for ${apiUrl}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedByUser = {};

  for (const todo of todos) {
    if (todo.completed) {
      if (!completedByUser[todo.userId]) {
        completedByUser[todo.userId] = 0;
      }
      completedByUser[todo.userId]++;
    }
  }

  for (const userId in completedByUser) {
    console.log(`User ${userId} completed ${completedByUser[userId]} tasks`);
  }
});
