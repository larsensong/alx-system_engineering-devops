#!/usr/bin/python3
'''
module that uses REST api to return info on user's TODO
'''

import requests
import sys


def todofunc():
    ''' function that gets todo tasks and prints the completed tasks '''
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(sys.argv[1]))
    new = r.json()
    name = new.get('name')
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(sys.argv[1]))
    new = r.json()
    size = len(new)
    titles = []
    count = 0
    for i in range(0, size):
        if new[i].get('completed'):
            count += 1
            titles.append(new[i].get('title'))

    print("Employee {} is done with tasks({}/{}):".format(name, count, size))
    for i in range(0, count):
                print("\t {}".format(titles[i]))


if __name__ == "__main__":
    todofunc()
