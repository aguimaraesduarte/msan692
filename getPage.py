import sys
import urllib2

page = sys.argv[1]

response = urllib2.urlopen(page)
html = response.read()
print html

