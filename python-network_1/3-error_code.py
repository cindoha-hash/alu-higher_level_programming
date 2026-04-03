#!/usr/bin/python3
"""Displays response body or HTTP error code using urllib."""

from urllib import error
from urllib import request
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
