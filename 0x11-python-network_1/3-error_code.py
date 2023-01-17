#!/usr/bin/python3
"""Module that takes a URL, sends a request to the url and displays the
body of the response (decode utf-8)"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
