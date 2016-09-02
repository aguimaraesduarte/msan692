import urllib2
import sys
from bs4 import BeautifulSoup
import re

page = sys.argv[1]

response = urllib2.urlopen(page)
html = response.read()
html = html.replace('&nbsp;', ' ') # replace html space specifier with space char
soup = BeautifulSoup(html, 'html.parser')
html = soup.get_text(' ', strip=False)  # space between tags, don't strip newlines

print html