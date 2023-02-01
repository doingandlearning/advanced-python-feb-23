from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    pass

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

