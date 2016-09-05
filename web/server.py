from flask import Flask, request
from urllib import urlopen

def readcsv(data):
	"""
	Read CSV with header from data string and return a header list
	containing a list of names and also return the list of lists
	containing the data.
	"""
	info = data.split("\n")
	headers = info[0].split(",")
	data = []
	for i in range(len(info[1:])):
		data.append(info[i+1].split(","))
	return headers, data

def gethistory(ticker):
	"""
	Return header list, data (list of lists) for ticker,
	obtained from Yahoo finance.
	"""
	url = "http://ichart.finance.yahoo.com/table.csv?s=" + ticker
	response = urlopen(url)
	csvData = response.read()
	header, data = readcsv(csvData)
	return header, data

def htmltable(headers, data):

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

	return html

app = Flask(__name__)

@app.route("/")
def home():
	return app.send_static_file("index.html")

@app.route("/history/", methods=['POST'])
def post_history():
	ticker = request.form["ticker"]
	return history(ticker)

@app.route("/history/<ticker>")
def history(ticker):
	"""
	In response to url /history/ticker, get data from Yahoo finance on
	ticker and return an HTML table representing that data.
	"""
	html = "<html><body>%s</body></html>"
	hist = gethistory(ticker)
	headers = hist[0]
	data = hist[1]
	table = htmltable(headers, data)
	return html % table

@app.route("/data/<ticker>")
def data(ticker):
	"""
	In response to url /data/ticker, get data from Yahoo finance on
	ticker and return a JSON representing that data.
	"""
	url = "http://ichart.finance.yahoo.com/table.csv?s=" + ticker
	response = urlopen(url)
	csvData = response.read()
	jsonData = csv2json(csvData)
	return jsonData

def csv2json(csvdata):
	headers, data = readcsv(csvdata)

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

	return json

app.run() # kickstart your flask server
