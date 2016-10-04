import urllib2
from bs4 import BeautifulSoup

def parse():
    response = urllib2.urlopen("http://data1.cde.ca.gov/dataquest/Acnt2013/2013GrthStAPI.aspx")
    html = BeautifulSoup(response, "html.parser")

    for table in html.find_all("table"):
        for tr in table.find_all("tr"):
            for td in tr.find_all("td"):
                if len(td.attrs)>0 and td.text.strip()!="":
                    if td.text.strip().find("\n") != -1:
                        print td.text.strip().split("\n")[0]
                    else:
                        print td.text.strip()

parse()
