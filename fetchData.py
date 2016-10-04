import urllib2
import sys
from bs4 import BeautifulSoup
import re
import time
import random
import os

#page = "https://news.ycombinator.com/newest"
#page = "https://www.reddit.com/r/all"
page = sys.argv[1]

outputdir = sys.argv[2]
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

def parse(URL):
	response = urllib2.urlopen(URL)
	html = response.read()
	html = html.replace('&nbsp;', ' ') # replace html space specifier with space char
	html = BeautifulSoup(html, 'html.parser')
	links = []
	#for link in html.find_all('a', {'class': 'storylink'}): #ycombinator
	for link in html.find_all('a', {'class': 'title may-blank outbound '}): #reddit
		if not link['href'].startswith("item"):
			links.append([link['href'], link.text])
	return (links, html)

def fetch(url,delay=(2,5)):
	"""
	Simulate human random clicking 2..5 seconds then fetch URL.
	Returns the actual page source fetched and the HTML object.
	"""
	time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
	
	try:
		req = urllib2.Request(url, headers={'User-Agent': "Resistance is futile"})
		response = urllib2.urlopen(req)
	except ValueError as e:
		print str(e)
		return '', BeautifulSoup('', "html.parser")
	except:
		return '', BeautifulSoup('', "html.parser")

	page = response.read().replace('&nbsp;', ' ') # replace html space specifier with space char
	html = BeautifulSoup(page, 'html.parser')
	return(page, html)

def parse_with_userAgent(URL):
	pagedata,html = fetch(URL)
	links = []
	#for link in html.find_all('a', {'class': 'storylink'}):
	for link in html.find_all('a', {'class': 'title may-blank outbound '}):
		if not link['href'].startswith("item"):
			links.append([link['href'], link.text])
	return (links, html)

def parse_with_userAgent_onlyLinks(URL):
	pagedata,html = fetch(URL)
	links = []
	for link in html.find_all('a', {'class': 'storylink'}):
	#for link in html.find_all('a', {'class': 'title may-blank outbound '}):
		if not link['href'].startswith("item"):
			links.append(link['href'])
	return links

def parse_3pages(URL):
	links = []
	current_URL = URL
	for i in range(3):
		pagedata,html = fetch(current_URL)
		print "Got links for page %s" % i
		curr_links = parse_with_userAgent_onlyLinks(current_URL)
		print "    Parsed links for page %s" % i
		for link in curr_links:
			links.append(link)
		current_URL = current_URL.split("?")[0]
		page_param = html.find_all('a', {'class': 'morelink'})[0]['href']
		current_URL += "?" + page_param.split("?")[1]
	print "Finished getting links!"
	print
	return links

def crawl(links, outputdir):
	i = 0
	for link in links:
		print "Fetching %s... " % link,
		page,html = fetch(link,delay=(0,0)) # no need to delay; pulling from random sites
		print "Done!"
		filename = "page%s" % i
		f = open(os.path.join(outputdir, filename), "w")
		print "    Writing to file %s... " % filename,
		f.write(page)
		print "Done!"
		f.close()
		i += 1

#links = parse_with_userAgent_onlyLinks(page)
links = parse_3pages(page)
#for link in links:
#	print link
crawl(links, outputdir)
