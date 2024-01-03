#!/usr/bin/python3
"""Exports data in the CSV format"""

if __name__ == "__main__":

    import requests
    from sys import argv
    import csv


    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    user_name = user.json().get('name')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    fname = "{}.csv".format(user_id)

    with open(fname, mode="w"0) as fd:
        fwriter = csv.writer(fd, delimiter=',',
                             quotechar='"',
                             quoting=csv.QUOTE_ALL, lineterminator='\n')
        for tsk in todo.json():
            if tsk.get('userId') == int(user_id) and \
                    task.get('completed'):
                fwriter.writerow([user_id, name,
                                 str(tsk.get('completed')), tsk.get('title')])
