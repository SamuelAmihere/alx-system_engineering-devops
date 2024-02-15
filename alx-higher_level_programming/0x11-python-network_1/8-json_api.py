#!/usr/bin/python3
"""takes in a letter and sends a POST request
"""
import sys
from requests import post


if __name__ == "__main__":
    if len(sys.argv) < 2:
        let = ""
    else:
        let = sys.argv[1]

    q = {"q": letter}

    req = post('http://0.0.0.0:5000/search_user', {'q': q})
    try:
        resp = req.json()
        if resp:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
