from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080

server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)

print(f"Greeter app running on port {PORT}...")

server.serve_forever()