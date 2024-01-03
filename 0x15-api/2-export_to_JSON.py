#!/usr/bin/python3
"""Exporting data to json format"""

import requests
from sys import argv
import csv
import json
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todoUser = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get('username')}
            taskList.append(taskDict)
    todoUser[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)
