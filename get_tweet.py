# Python 3

import subprocess
import requests

def main():
	# Get query to search
    query = get_query()
    string = get_html("https://twitter.com/" + query).split()
    for word in string:
        print(word)

def get_query():
	""" Gets the page of tweets from user. """
	query = input("Whose page would you like to get? ")
	return query

def get_html(url):

    url.replace(" ", "-")

    print("Attempting to grab html...")

    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    main()
