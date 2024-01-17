#!/usr/bin/python3
"""Queries  Reddit API and prints hot postst."""
import requests


def top_ten(subreddit):
    """Prints 10 hottest posts' titles.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    UA = "My-User-Agent"
    headers = {
        "User-Agent": UA
    }
    params = {
        "limit": 10
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code >= 300:
        print("None")
    else:
        for child in res.json().get("data").get("children"):
            print(child.get("data").get("title"))
