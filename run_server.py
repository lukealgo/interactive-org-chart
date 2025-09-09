#!/usr/bin/env python3
"""
Simple HTTP server for Interactive Org Chart
Double-click this file to start the server and open the org chart
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from threading import Timer

def open_browser():
    """Open the default web browser to the org chart"""
    webbrowser.open('http://localhost:8000')
    print("✅ Org chart should now be open in your browser!")
    print("🌐 If it didn't open automatically, visit: http://localhost:8000")
    print("\n⏹️  Press Ctrl+C (or Cmd+C on Mac) to stop the server")

def start_server():
    """Start the HTTP server"""
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    
    print("🚀 Starting Interactive Org Chart server...")
    print(f"📂 Serving files from: {os.getcwd()}")
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🌍 Server running at http://localhost:{PORT}")
            
            # Open browser after 1 second delay
            Timer(1.0, open_browser).start()
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Thanks for using Interactive Org Chart!")
        sys.exit(0)
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Port {PORT} is already in use.")
            print("💡 Try closing other applications or restart your computer.")
        else:
            print(f"❌ Error starting server: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    start_server()