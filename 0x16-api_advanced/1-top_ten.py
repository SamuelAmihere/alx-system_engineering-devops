#!/usr/bin/python3
"""Queries  Reddit API and prints hot postst."""
import requests


def top_ten(subreddit):
    """Prints 10 hottest posts' titles.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    UA = "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    headers = {
        "User-Agent": UA
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
