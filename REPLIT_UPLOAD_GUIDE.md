# 📤 How to Upload to Replit (Step-by-Step with Screenshots)

## Step 1: Go to Replit
1. Open your web browser
2. Go to https://replit.com
3. Sign up (free) or log in if you have an account

## Step 2: Create New Repl
1. Click the big **"+ Create Repl"** button
2. Choose **"Python"** from the template list
3. Give it a name like "interactive-org-chart"
4. Click **"Create Repl"**

## Step 3: Upload Your Files
**Method A: Drag & Drop (Easiest)**
1. Open your file manager/finder to the `interactive-org-chart-standalone` folder
2. Select ALL files in the folder (Ctrl+A or Cmd+A)
3. Drag them directly into the Replit file panel on the left
4. Wait for upload to complete

**Method B: Upload Button**
1. In Replit, look for the file panel on the left
2. Click the "Upload file" icon (looks like ⬆️ or 📤)
3. Select all files from your `interactive-org-chart-standalone` folder
4. Click "Open" to upload

## Step 4: Modify the Python Script
1. In Replit, click on `run_server.py` to open it
2. **Replace the entire file contents** with this simplified version:

```python
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
```

## Step 5: Run It!
1. Click the big green **"Run"** button at the top
2. Wait a few seconds for the server to start
3. Click the **"Webview"** tab that appears next to "Console"
4. **Your org chart is now live!** 🎉

## Step 6: Share It
1. Click the **"Share"** button in the top right
2. Copy the **"Cover page"** URL 
3. Send this URL to anyone - they can view your org chart instantly!

## Troubleshooting
- **Files not uploading?** Try Method B (upload button) instead of drag & drop
- **Server won't start?** Make sure you replaced the `run_server.py` content in Step 4
- **Webview not showing?** Try clicking the URL in the console output

**🎯 Result:** You'll get a permanent URL like `https://interactive-org-chart.username.repl.co` that works forever and on any device!

---

**Total time: 2-3 minutes** ⏱️