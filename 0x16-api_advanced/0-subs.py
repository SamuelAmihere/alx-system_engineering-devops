#!/usr/bin/python3
"""Querying subscribers on a Reddit API ."""
import requests


def number_of_subscribers(subreddit):
    """Finds the total number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 404:
        return 0
    return res.json().get("data").get("subscribers")
