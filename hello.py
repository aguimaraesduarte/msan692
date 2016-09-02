from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<html><body>Hello MSAN692!</body></html>"

@app.route("/hello/<name>")
def hi(name):
    return "<html><body>Hi <i>%s</i>!</body></html>" % name

app.run()
