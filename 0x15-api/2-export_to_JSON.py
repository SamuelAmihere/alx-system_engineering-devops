#!/usr/bin/python3
"""Exports data in the JSON format"""

from sys import argv
import json
import requests

if __name__ == "__main__":

    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    userTasks = {}
    tasks = []

    for task in todo:
        if task.get('userId') == int(user_id):
            tasks.append(
                    {"task": task.get('title'),
                     "username": user.json().get('username'),
                     "completed": task.get('completed')})
    userTasks[user_id] = tasks

    file = '{}.json'.format(user_id)
    with open(file, mode='w') as f:
        json.dump(userTasks, f)
