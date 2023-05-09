#!/usr/bin/python3
'''
module for the Reddit API
'''

import requests


def top_ten(subscribers):
    '''function that queries and returns the top 10 subscribers '''
    headers = {'User-agent': 'test'}
    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subscribers), headers=headers)
    try:
        data = res.json()['data']['children']
    except Exception:
        print(None)
        return
    for i in range(0, 10):
        print(data[i]['data']['title'])
