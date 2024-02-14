#!/usr/bin/python3
"""
A program that queries the Reddit API and returns
the number of subscribers.
"""
import requests
import re


def update_count(children, word_list, word_count):
    """
    update count
    """
    for child in children:
        title = child.get('data').get('title')
        title = title.lower()
        title = title.split()
        for word in title:
            word = re.sub(r'\W+', '', word)
            if word in word_list:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count

def count_words(subreddit, word_list):
    """
    main function
    """
    word_list = list(set(word_list))
    word_list.sort()
    word_list = [word.lower() for word in word_list]

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print()
        return
    response = response.json()
    data = response.get('data')
    children = data.get('children')
    word_count = update_count(children, word_list, {})

    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word in word_count:
        print('{}: {}'.format(word[0], word[1]))
    return