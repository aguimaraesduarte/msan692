"""
import socket
import sys

port = sys.argv[1]

# Create a serve socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print "server listening at "+ip+":"+port
serversocket.bind((ip, 8000)) # wait at port 8000
# Start listening for connections from client
serversocket.listen(5) # 5 is number of clients that can queue up before failure

# Wait for connection
(clientsocket, address) = serversocket.accept()

# Send a welcome
clientsocket.send("hello\n")

# Get up to 1000 bytes
data = clientsocket.recv(1000)
print data

# Echo it back to client
clientsocket.send(data)

clientsocket.close()
"""

from flask import Flask
from flask import request
from collections import Counter
from html import HTML

app = Flask(__name__)

pageviews = Counter()

@app.route("/dashboard")
def dashboard():
    page = HTML()
    t = page.table()
    r = t.tr
    r.th("Count")
    r.th("Page name")
    for name in pageviews:
        r = t.tr
        r.td(str(pageviews[name]))
        r.td(name)
    return str(page)

@app.route("/track.gif")
def track():
    page = request.args.get('page', default='')
    if len(page)>0:
        pageviews[page] += 1
        print "Visit to page "+page
    return app.send_static_file('images/shim.gif')

app.run()