import sys
import urllib
import urllib2
import json
import untangle


HistoryURL = "http://ichart.finance.yahoo.com/table.csv?s=%s"

ticker = sys.argv[1]  # E.g., AAPL
response = urllib2.urlopen(HistoryURL % ticker)
csvdata = response.read()
print csvdata

# csv Python lib prefers reading from files, and it's easy to handle ourselves.
for row in csvdata.strip().split("\n"):
	cols = row.split(',')
	print cols


"""
QuoteURL = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"

ticker = sys.argv[1]
field = sys.argv[2]
response = urllib2.urlopen(QuoteURL % (ticker, field))
quote = response.read()
print quote.strip().split(",")
"""

"""
URL = "http://openpayments.us/data?query=%s"

query = sys.argv[1]
query = urllib.quote(query)

response = urllib2.urlopen(URL % query)
data = response.read()

json_data = json.loads(data)
print json.dumps(json_data)
print json_data
print data
"""

"""
URL = "http://www.omdbapi.com/?"

query = {
    's' : sys.argv[1], # 'there will be blood'
    'y' : sys.argv[2], # 2007
    'r' : 'json'
}

# urlencode converts the dictionary to a list of x=y pairs
query_url = URL + urllib.urlencode(query)
print query_url

raw_input("OK?")

response = urllib2.urlopen(query_url)
data = response.read()

json_data = json.loads(data)
for result in json_data["Search"]:
	print json.dumps(result, indent=4)
"""
"""
URL = "http://www.omdbapi.com/?"

query = {
    's' : sys.argv[1],
    'r' : 'xml'
}

query_url = URL + urllib.urlencode(query)
print query_url

raw_input("OK?")

response = urllib2.urlopen(query_url)
data = response.read()

xml = untangle.parse(data)

for entry in xml.children[0].children:
	print entry["title"], entry["year"]
"""

