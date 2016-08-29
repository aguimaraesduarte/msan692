import json
import csv

jsontxt = csv.getdata()

json_data = json.loads(jsontxt)

header = ""

for h in json_data["headers"]:
    header += h + ","
header = header[:-1] #remove trailing comma
header += "\n"

data = ""

headers = header.strip().split(",")

for entry in json_data["data"]:
    for key in headers:
        data += entry[key] + ","
    data = data[:-1] #remove trailing comma
    data = data + "\n"
data = data[:-1] #remove trailing new-line

csv = header + data

print csv