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
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print("None")
        return
    if 'data' in res:
        for top in res.get("data").get("children"):
            print(top.get("data").get("title"))
    else:
        print(None)
