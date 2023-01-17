#!/bin/bash
# Script that takes a url, sends a request to that url and displays response body size
curl -s "$1" | wc -c
