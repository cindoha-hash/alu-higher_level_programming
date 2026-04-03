#!/usr/bin/python3
"""Sends a letter to an API and prints the JSON response result."""

import requests
import sys


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data={"q": letter}
    )
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
