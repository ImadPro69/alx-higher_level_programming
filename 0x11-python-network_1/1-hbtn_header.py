#!/usr/bin/python3
"""Hi"""
import sys
from urllib import request


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.headers['X-Request-Id'])
