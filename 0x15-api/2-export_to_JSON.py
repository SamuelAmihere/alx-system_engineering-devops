#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
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
