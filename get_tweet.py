# Python 3

import subprocess
import requests

def main():
	# Get query to search
    query = get_query()
    string = get_html("https://twitter.com/" + query).split()
    for n in range(0, len(string)):
        if string[n] == 'dir="ltr"':
            if 'data-aria-label-part="0"' in string[n + 1]:
                temp = string[n + 1].split(">")
                print(temp[1] + " ", end="")
                tempVar = n + 2
                while "</p>" not in string[tempVar]:
                    print(string[tempVar] + " ", end="")
                    tempVar += 1
                temp = string[tempVar].split("<")
                print(temp[0])
                print("\n----------\n")
                n = tempVar


def get_query():
	""" Gets the page of tweets from user. """
	query = input("Whose page would you like to get? ")
	return query

def get_html(url):

    url.replace(" ", "-")

    print("Attempting to grab html...\n")

    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    main()
