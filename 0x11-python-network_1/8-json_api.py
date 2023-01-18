#!/usr/bin.python3
"""Module that takes in a letter and sends a POST request to a
url with the letter as parameter"""

from sys import argv
import requests

if __name__ == '__main__':
    q = argv[1] if len(argv) > 1 else ''
    letter = {'q': q}
    res = requests.post('http://0.0.0.0:5000/search_user', data=letter)
    try:
        output = res.json()
        if output == {}:
            print('No result')
        else:
            print('[{}] {}'.format(output.get('id'), output.get('name')))
    except ValueError:
        print('Not a valid JSON')
