#!/usr/bin/python3
"""Module that takes in a url sends a request and displays 
its X-Request-Id variable found in the response header"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv
    url = argv[1]
    with urlopen(url) as response:
        output = response.info().__getitem__('X-Request-Id')
        print(output)
