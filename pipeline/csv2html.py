import csv

headers, data = csv.readcsv(csv.getdata())

html_template = """<html>
<body>
<table>
%s
%s
</table>
</body>
</html>"""

html_header_template = "<tr>%s</tr>"
html_header_entry_template = "<th>%s</th>"

html_entries_template = """<tr>%s</tr>
"""
html_entries_entry_template = "<td>%s</td>"

s_header = ""
for header in headers:
	s_header += html_header_entry_template % header

s_entries = ""
for line in data:
	s_entry = ""
	for entry in line:
		s_entry += html_entries_entry_template % entry
	s_entries += html_entries_template % s_entry

html_header = html_header_template % s_header
html_entries = s_entries
html = html_template % (html_header, html_entries)

print html