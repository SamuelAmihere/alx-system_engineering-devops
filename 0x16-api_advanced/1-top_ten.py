#!/usr/bin/python3
"""Queries  Reddit API and prints hot postst."""
import requests


def top_ten(subreddit):
    """Prints 10 hottest posts' titles.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    UA = "CustomClient/1.0"
    headers = {
        "User-Agent": UA
    }
    request = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if request.status_code != 200:
        print(None)
        return
    jsonreq = request.json()

    if 'data' in jsonreq:
        for top in jsonreq.get("data").get("children"):
            print(top.get("data").get("title"))
    else:
        print(None)
