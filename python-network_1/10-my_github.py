#!/usr/bin/python3
"""Uses GitHub API with basic auth to display the user id."""

import requests
import sys


if __name__ == "__main__":
    response = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    data = response.json()
    print(data.get("id"))
