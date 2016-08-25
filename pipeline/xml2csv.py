import untangle
import csv

xmltxt = csv.getdata()

xml = untangle.parse(xmltxt)

headers = xml.children[0].children[0].cdata + "\n"
data = ""

for entry in xml.children[0].children[1].children:
    for i in range(len(headers.split(","))):
        data += entry.children[i].cdata + ","
    data = data[:-1] #remove trailing comma
    data += "\n"
data = data[:-1]

csv = headers + data

print csv