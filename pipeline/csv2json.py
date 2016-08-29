import csv

headers, data = csv.readcsv(csv.getdata())

json_template = """{
%s
%s
}"""

json_headers = '"headers":['
for i in range(len(headers)):
	json_headers += '"'+ headers[i] + '",'
json_headers = json_headers[:-1]
json_headers += '''],'''

json_data = '''"data":['''
for i in range(len(data)):
	s = '''
{
'''
	for j in range(len(data[i])):
		s += '"' + headers[j] + '":"' + data[i][j] + '", '
	s = s[:-2] #remove trailing comma and space
	s += '''
},'''
	json_data += s
json_data = json_data[:-1]
json_data += '''
]'''

json = json_template % (json_headers, json_data)

print json
