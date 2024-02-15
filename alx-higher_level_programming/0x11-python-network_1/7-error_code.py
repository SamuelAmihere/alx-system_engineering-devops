#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
"""
from requests import get
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    resp = get(url)
    if (resp.status_code < 400):
        print(resp.text)
    else:
        print("Error code: {}".format(resp.status_code))
