
# Python 3

import subprocess
import requests
from html.parser import HTMLParser

def main():
	# Get query to search
    query = get_query()
    string = get_html("https://twitter.com/" + query).split()

    for n in range(0, len(string)):
        if string[n] == 'dir="ltr"':
            if 'data-aria-label-part="0"' in string[n + 1]:
                returnString = ""
                temp = string[n + 1].split(">")
                returnString = returnString + temp[1] + " "
                tempVar = n + 2
                while "</p>" not in string[tempVar]:
                    returnString = returnString + string[tempVar] + " "
                    tempVar += 1
                temp = string[tempVar].split("</p>")
                returnString = returnString + temp[0]
                print(strip_tags(returnString))
                print("\n----------\n")
                n = tempVar


def get_query():
	""" Gets the page of tweets from user. """
	query = input("Whose page would you like to get? ")
	return query

def strip_tags(html):
    # Need to find something that does this correctly. I will most likely
    # Have to write one myself.
    return html

def get_html(url):
    """ Gets the HTML for a page. """
    print("Attempting to grab html...\n")

    r = requests.get(url)

    return r.text

if __name__ == "__main__":
    main()
