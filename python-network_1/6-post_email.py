#!/usr/bin/python3
"""Sends a POST request with an email parameter using requests."""

import requests
import sys


if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=values)
    print(response.text)
