#!/usr/bin/python3
'''
prints the titles of the first 10 hot posts listed for a given subreddit
'''
import requests
from sys import argv


def top_ten(subreddit):
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)

