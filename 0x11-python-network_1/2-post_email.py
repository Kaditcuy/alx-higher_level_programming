#!/usr/bin/python3
"""Module that takes in a URl and an email and posts the email to
the server and displays a decoded body of the response(decoded in utf-8)"""

if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))
