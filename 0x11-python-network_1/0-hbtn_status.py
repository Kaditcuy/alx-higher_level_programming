#!/usr/bin/python3
"""Module that fetches alx, status url
using urlib"""

if __name__ == "__main__":
    from urllib.request import urlopen
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        output = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(output)))
        print('\t- content: {}'.format(output))
        print('\t- utf8 content: {}'.format(output.decode('utf-8')))
