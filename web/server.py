from flask import Flask

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
	return

def htmltable(headers, data):
	"""Return an HTML table representing the headers and data."""
	return

app = Flask(__name__)

@app.route(...)
def history(ticker):
	"""
	In response to url /history/ticker, get data from Yahoo finance on
	ticker and return an HTML table representing that data.
	"""
	return

app.run() # kickstart your flask server
