import sys
from bs4 import BeautifulSoup
import re
import collections

def html2text(html_text):
    html_text = html_text.replace('&nbsp;', ' ') # replace html space specifier with space char
    soup = BeautifulSoup(html_text, 'html.parser')
    html_text = soup.get_text(' ', strip=False)  # space between tags, don't strip newlines
    return html_text

filename = sys.argv[1]
f = open(filename, "r")
html = f.read()
text = html2text(html)
f.close()

text = text.encode('ascii', 'ignore')
text = re.sub("[\\n ]+", ' ', text)

words = text.strip().split(' ')
words = [word.lower() for word in words]
words_set = set(words)

print len(words_set)
raw_input()

#d = collections.defaultdict(int)
d = collections.Counter()
for word in words:
	d[word] += 1

print d


