# Chromebook Setup Guide

Chromebooks require a slightly different approach. Here are your options:

## Option 1: Enable Linux (Recommended)
1. Go to Settings → Advanced → Developers
2. Turn on "Linux development environment"  
3. Wait for Linux to install
4. Open Terminal from the app launcher
5. Navigate to the folder containing the org chart files
6. Run: `python3 run_server.py`
7. Browser opens automatically

## Option 2: Use Chrome Developer Mode
**Warning: This disables some security features**
1. Press Esc + Refresh + Power to enter Recovery Mode
2. Press Ctrl + D to enable Developer Mode
3. Wait for the reset (this wipes your device!)
4. After setup, press Ctrl + Alt + T to open terminal
5. Type `shell` and press Enter
6. Navigate to your files and run the Python server

## Option 3: Online Code Editor (Easiest)
1. Go to https://replit.com
2. Create new Python project
3. Upload all the org chart files
4. Click Run
5. View the result in the web preview

## Option 4: Chrome Extensions (Simple)
1. Install "Web Server for Chrome" extension
2. Choose the folder containing your org chart
3. Start the server
4. Click the web server URL

## Option 5: GitHub Pages (Share with Anyone)
1. Create GitHub account
2. Create new repository
3. Upload all org chart files
4. Go to Settings → Pages
5. Enable GitHub Pages
6. Share the generated URL with anyone

**Recommended:** Try Option 1 (Linux) first, then Option 3 (Replit) if that doesn't work.