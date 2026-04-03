#!/usr/bin/python3
"""Sends a POST request with an email parameter using urllib."""

from urllib import parse
from urllib import request
import sys


if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    data = parse.urlencode(values).encode("ascii")
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
