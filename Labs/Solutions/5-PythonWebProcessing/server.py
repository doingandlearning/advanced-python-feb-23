from http.server import BaseHTTPRequestHandler, HTTPServer
from fib import fib

fib_closure = fib()

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
            if self.path == "/hello":   
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                result = "<b>Hello World!</b>"
                self.wfile.write(result.encode('utf-8'))
            elif self.path.startswith("/hello/"):
                _, name = self.path.split("/hello/")
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                result = f"<b>Hello {name}!</b>"
                self.wfile.write(result.encode('utf-8'))
            elif self.path == "/fib":
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                result = f"<b>{fib_closure()}</b>"
                self.wfile.write(result.encode('utf-8'))

            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                result = "<b>We don't have a page here yet, check back soon!</b>"
                self.wfile.write(result.encode('utf-8'))	
            

def main():
    try:
        server = HTTPServer(('', 8001), MyHandler)
        print('Started HTTP server...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Ctrl+C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()

