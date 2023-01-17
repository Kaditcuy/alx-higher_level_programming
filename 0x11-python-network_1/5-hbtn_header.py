#!/usr/bin/python3
"""Module that uses request package to send a request to a URL and
displays the value of the variable X-Request-Id in the header section"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)
    print('{}'.format(res.headers.get('x-request-id')))
