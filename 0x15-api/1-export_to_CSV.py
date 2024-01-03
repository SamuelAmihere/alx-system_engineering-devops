#!/usr/bin/python3
"""Exporting data to csv format"""

import requests
from sys import argv
import csv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    user_name = user.json().get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    fname = "{}.csv".format(user_id)
    for task in todo.json():
        if task.get('userId') == int(user_id):
            if task.get('completed'):
                completed_task += 1
        tasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed_task, tasks))
    for task in todo.json():
        if task.get('userId') == int(user_id) and \
                    task.get('completed'):
            print('\n'.join(["\t " + task.get('title')]))
