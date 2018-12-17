from pyautogui import press, typewrite, hotkey

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import urllib.parse as urlparse

PORT_NUMBER = 9000

class S(BaseHTTPRequestHandler):
  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

  def do_GET(self):
    self._set_headers()
    self.wfile.write("test-success".encode())
      
  def do_POST(self):
    post_data = str(self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8"))
    print ("Received: ",post_data)
    typewrite(post_data)
    hotkey('enter') 
    self._set_headers()
    self.wfile.write("scan-success".encode())
        
def run(server_class=HTTPServer, handler_class=S, port=PORT_NUMBER):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print ('Starting httpd...')
  httpd.serve_forever()

if __name__ == "__main__":
  from sys import argv

  if len(argv) == 2:
    run(port=int(argv[1]))
  else:
    run()