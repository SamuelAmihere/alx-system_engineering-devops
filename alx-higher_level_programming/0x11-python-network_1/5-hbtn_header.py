#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
"""
from requests import get
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = get(url)
    print(req.headers.get("X-Request-Id"))
