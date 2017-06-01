import sys
import os
import requests

from bs4 import BeautifulSoup
from optparse import OptionParser


## Using benford's law to detect fraud or misinformation in articles.

def main():

    parser = OptionParser()
    parser.add_option("-l", "--link", help="Select a link to scrap.")

    options, arguments = parser.parse_args()

    if options.link:
        link = options.link
        resp = requests.get(link)
        soup = BeautifulSoup(resp.text, 'lxml')

        f = open('webfile.txt', 'w')
        f.write(soup.txt)

        f.close()
        print(link, "[Completed]")



    else:
        print("No link given using -l.")


if __name__ == "__main__":
    main()
