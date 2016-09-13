from flask import Flask
from flask import request
from collections import Counter
from html import *

app = Flask(__name__)

pageviews = Counter()

@app.route("/track.gif")
def track():
    # get the 'page' request argument (google it)
    page = request.url.split('=')
    if len(page)>1:
        pageviews[page[1]] += 1
        print "Visit to page " + page
    # return the result of calling app.send_static_file on 'images/shim.gif'
    return app.send_static_file('images/shim.gif')


@app.route("/dashboard")
def dashboard():
    ret = "<b>Count &emsp; Page Name</b> </br>"
    for e in pageviews:
        ret += str(pageviews[e]) + '&emsp;&emsp;&emsp;&emsp;' + e + '<br>'
    return ret

app.run()

