from http import server
import ssl
import urllib.parse

class CustomHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

        print("Received POST data:", parsed_data)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"POST request received.")

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='./server.pem')

httpd = server.HTTPServer(('0.0.0.0', 4443), CustomHTTPRequestHandler)

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://0.0.0.0:4443")
httpd.serve_forever()