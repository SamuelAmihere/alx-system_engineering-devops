#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
from requests import get


if __name__ == '__main__':
    resp = get('https://api.github.com/user', auth=(sys.argv[1],
               sys.argv[2]))
    data = resp.json()
    print(data.get('id'))
