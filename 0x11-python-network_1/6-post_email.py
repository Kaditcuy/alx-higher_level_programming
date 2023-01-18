#!/usr/bin/python3
"""
Module containing python script that posts a request to a server
"""
import requests
from sys import argv

if __name__ = "__main__":
    email = {'email': argv[2]}
    url = argv[1]
    res = requests.post(url, data=email)
    print(res.text)
