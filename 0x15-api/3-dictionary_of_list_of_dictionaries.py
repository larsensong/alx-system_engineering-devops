#!/usr/bin/python3
'''
module that uses REST api to return info on user's TODO and write to file
'''

import json
import requests


def todojson():
    ''' function that gets todo tasks and exports data to json file '''
    ur = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tr = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users_data = {}
    for i in ur:
        userid = i.get('id')
        username = i.get('username')
        todos = list(filter(lambda x: x.get('userId') == userid, tr))
        user_data = list(map(
            lambda x: {
                'username': username,
                'task': x.get('title'),
                'completed': x.get('completed')
            }, todos))
        users_data['{}'.format(userid)] = user_data
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_data, f)


if __name__ == '__main__':
    todojson()
