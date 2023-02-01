from http.server import BaseHTTPRequestHandler, HTTPServer
import mimetypes
from os import curdir, sep
import time

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith('.zzz'):
				self.send_response(200)
				self.send_header("Content-Type", "text/html")
				self.end_headers()
				result = f"You requesed {self.path} on day {time.localtime()[7]} in {time.localtime()[0]}"
				self.wfile.write(result.encode('utf-8'))
			elif self.path == "/do-a-little-dance":
				self.send_response(200)
				self.send_header("Content-Type", "text/html")
				self.end_headers()
				result = f"<b>Dance!</b>"
				self.wfile.write(result.encode('utf-8'))
			else:
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-Type', mimetypes.guess_type(self.path)[0])
				self.end_headers()
				self.wfile.write(f.read().encode('utf-8'))
				f.close()
		except IOError:
				self.send_error(404, f"File not found: {self.path}")


def main():
	try:
		server = HTTPServer(("", 8080), MyHandler)
		print('Started HTTP server')
		server.serve_forever()
	except KeyboardInterrupt:
		print("Ctrl+C recieved, shutting down server")
		server.socket.close()

if __name__ == "__main__":
	main()