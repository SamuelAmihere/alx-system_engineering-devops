#!/usr/bin/python3
"""Querying subscribers on a Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """Finds the total number of subscribers.
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    head = {"User-Agent": "Client"}
    req = requests.get(url, headers=head)
    if req.status_code != 200:
        return 0
    return req.json().get("data").get("subscribers")
