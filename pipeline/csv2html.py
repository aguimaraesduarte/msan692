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
for i in range(len(headers)):
	s_header += html_header_entry_template % headers[i]

s_entries = ""
for i in range(len(data)):
	s_entry = ""
	for j in range(len(data[i])):
		s_entry += html_entries_entry_template % data[i][j]
	s_entries += html_entries_template % s_entry

html_header = html_header_template % s_header
html_entries = s_entries
html = html_template % (html_header, html_entries)

print html