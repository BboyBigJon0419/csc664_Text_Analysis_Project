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

#then type python server.py