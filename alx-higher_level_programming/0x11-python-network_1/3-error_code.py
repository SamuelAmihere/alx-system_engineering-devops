#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
"""
import sys
from urllib.error import HTTPError
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
