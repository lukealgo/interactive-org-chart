import http.server
import socketserver
import os

# Change to current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

print(f"🚀 Starting Interactive Org Chart server on port {PORT}")
print("📂 Files ready to serve!")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🌍 Server running! Click the 'Webview' tab to see the org chart")
    httpd.serve_forever()