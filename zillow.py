import sys
import untangle
import urllib2
import urllib
import webbrowser

KEY = "X1-ZWz19kneru7ci3_anh8k"

"""
# Find out how much property 64969892 is worth
zpid = '64969892'
QuoteURL = "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s"
URL = QuoteURL % (KEY, zpid)
response = urllib2.urlopen(URL)
xmldata = response.read()  # read all data
#print xmldata

xml = untangle.parse(xmldata)
zestimate = xml.Zestimate_zestimate.response.zestimate.amount.cdata
propertyURL = xml.Zestimate_zestimate.response.links.homedetails.cdata

print zestimate
print propertyURL
"""

"""
Address = "190 7th St APT 4"
Address = urllib.quote(Address)
CityStateZip = "San Francisco, CA"
CityStateZip = urllib.quote(CityStateZip)
SearchURL = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=%s&address=%s&citystatezip=%s"
URL = SearchURL % (KEY, Address, CityStateZip)
response = urllib2.urlopen(URL)
xmldata = response.read()  # read all data
#print xmldata

xml = untangle.parse(xmldata)

code = xml.SearchResults_searchresults.message.code.cdata
if code == "0":
	zpid = xml.SearchResults_searchresults.response.results.result.zpid.cdata
	print zpid
else:
	print "No such address found"
"""

zpid = '64969892'
QuoteURL = "http://www.zillow.com/webservice/GetChart.htm?zws-id=%s&unit-type=percent&zpid=%s"
URL = QuoteURL % (KEY, zpid)
response = urllib2.urlopen(URL)
xmldata = response.read()  # read all data
#print xmldata

xml = untangle.parse(xmldata)
chartURL = xml.Chart_chart.response.url.cdata

print chartURL
