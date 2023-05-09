#!/usr/bin/python3
'''
module for the Reddit API
'''

import requests


def number_of_subscribers(subscribers):
    '''function that queries and returns the number of subscribers '''
    headers = {'User-agent': 'test'}
    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subscribers), headers=headers)
    try:
        subs = res.json()['data']['subscribers']
    except Exception:
        return 0
    return subs
