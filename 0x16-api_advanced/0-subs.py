#!/usr/bin/python3
"""Querying subscribers on a Reddit API ."""
import requests


def number_of_subscribers(subreddit):
    """Finds the total number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    UA = "Client"
    headers = {
        "User-Agent": UA
    }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 404:
        return 0
    data = res.json().get("data")
    return data.get("subscribers")
