import BaseHTTPServer
import urlparse

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        p = self.path.split('?')
        if len(p) > 1:
            params = urlparse.parse_qs(p[1], True, True)
            print params
        self.send_response(200)
        self.end_headers()
        return

url = 'http://localhost:8000?user=parrt&foo=bar'
server_address = ('localhost', 8000)
httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
print url
# Block until we get a single request to url
httpd.handle_request() # handle just one request