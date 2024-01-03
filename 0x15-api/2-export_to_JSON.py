#!/usr/bin/python3
"""Exporting data to json format"""

from sys import argv
import csv
import json
import requests

if __name__ == "__main__":

    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    userTasks = {}
    tasks = []
    for task in todo.json():
        if task.get('userId') == int(user_id):
            tasks.append(
                    {"task": task.get('title'),
                     "username": user.json().get('username'),
                     "completed": task.get('completed')})

    userTasks[user_id] = tasks
    file = f"{}.json".format(user_id)
    with open(file, mode='w') as fd:
        json.dump(userTasks, fd)
