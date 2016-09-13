import csv

headers, data = csv.readcsv(csv.getdata())

json_template = """{
%s
%s
}"""

json_headers = '"headers":['
for header in headers:
	json_headers += '"'+ header + '",'
json_headers = json_headers[:-1]
json_headers += '''],'''

json_data = '''"data":['''
for line in data:
	s = '''
{
'''
	i = 0
	for entry in line:
		s += '"' + headers[i] + '":"' + entry + '", '
		i += 1
	s = s[:-2] #remove trailing comma and space
	s += '''
},'''
	json_data += s
json_data = json_data[:-1]
json_data += '''
]'''

json = json_template % (json_headers, json_data)

print json
