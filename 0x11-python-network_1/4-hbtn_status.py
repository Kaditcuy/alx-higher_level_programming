#!/usr/bin/python3
"""
Module that uses request package to fetch url's
"""
import requests

if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res.text))
