import csv

headers, data = csv.readcsv(csv.getdata())

xml_head = """<?xml version="1.0"?>
"""

xml_template = """<file>
%s
</file>"""
xml_headers_template = """<headers>%s</headers>
"""
xml_data_template = """<data>
%s
</data>"""
xml_record_template = """<record>
%s
</record>"""
xml_record_entry_template = "<%s>%s</%s>"


xml = ""

s = ""
for i in range(len(headers)):
	s += headers[i] + ","
s = s[:-1] #remove trailing comma
xml += xml_headers_template % s

s = ""
for i in range(len(data)):
	s_entry = ""
	for j in range(len(data[i])):
		s_entry += xml_record_entry_template % (headers[j].replace(" ", "_"), data[i][j], headers[j].replace(" ", "_"))
	s += xml_record_template % s_entry

xml += xml_data_template % s

xml = xml_head + xml_template % xml

print xml


