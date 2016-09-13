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
for header in headers:
	s += header + ","
s = s[:-1] #remove trailing comma
xml += xml_headers_template % s

s = ""
for line in data:
	s_entry = ""
	i = 0
	for entry in line:
		s_entry += xml_record_entry_template % (headers[i].replace(" ", "_"), entry, headers[i].replace(" ", "_"))
		i += 1
	s += xml_record_template % s_entry

xml += xml_data_template % s

xml = xml_head + xml_template % xml

print xml


