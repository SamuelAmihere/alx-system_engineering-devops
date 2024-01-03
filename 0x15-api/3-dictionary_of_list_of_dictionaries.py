#!/usr/bin/python3
"""using this REST API, for a given employee ID"""

from sys import argv
import json
import requests

if __name__ == "__main__":

    all_users = requests.get("https://jsonplaceholder.typicode.com/users")\
            .json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    all_todos = {}
    for user in all_users:
        tasks = []
        for task in todo:
            if task.get('userId') == user.get('id'):
                tasks.append({"task": task.get('title'),
                              "completed": task.get('completed'),
                              "username": user.get('username')})

        all_todos[user.get('id')] = tasks

    file = 'todo_all_employees.json'
    with open(file, mode='w') as f:
        json.dump(all_todos, f)
