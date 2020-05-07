from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
#from BaseHTTPServer
class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send.header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World'.encode())
        #self.wfile.write(self.path[1:].encode())

def main():
        PORT = 8000
        server = HTTPServer(('', PORT), echoHandler)
        print('Server Running on port %s' % PORT)
        server.serve_forever()

if __name__ == '__main__':
    main()

#In Python 2.7 run command line:
#python -m SimpleHTTPServer 8000

#http.server only exists in Python 3
#In python 2, You should use he BaseHTTPServer module:
#   from BaseHTTPServer import BaseHTTPRequestHandler
#link: https://stackoverflow.com/questions/24444343/no-module-named-http-server

#then type python server.py