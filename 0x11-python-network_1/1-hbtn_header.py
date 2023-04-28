#!/usr/bin/python3
"""Script that takes in a URl
sends a request to the URL and
displays the value of the X-Request-Id
variable found in the header
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(dict(response.headers)("X-Request-Id"))
