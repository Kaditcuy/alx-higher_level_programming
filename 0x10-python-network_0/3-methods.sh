#!/bin/bash
# Script that takes in a url and dsiplays all http methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
