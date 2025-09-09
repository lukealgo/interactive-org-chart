# Interactive Org Chart - Standalone Version

This is a ready-to-run version of the interactive organizational chart viewer. No installation or setup required!

## 🚀 Quick Start (EASIEST - Recommended)

### Windows Users:
**Double-click `RUN_ME.bat`** - That's it! The server starts and opens your browser automatically.

### Mac/Linux Users:
**Double-click `run_server.py`** - The server starts and opens your browser automatically.

### Alternative for Any OS:
1. Open Terminal/Command Prompt in this folder
2. Run: `python run_server.py` (or `python3 run_server.py`)
3. Browser opens automatically to http://localhost:8000

## 📋 What Happens When You Run It

1. A simple web server starts on your computer
2. Your browser opens automatically to the org chart
3. The org chart loads perfectly (no file access errors!)
4. Press Ctrl+C (Cmd+C on Mac) in the terminal to stop when done

## Features

- Interactive organizational chart visualization
- Employee search functionality  
- Hierarchical display with levels and reporting structure
- Zoom and pan navigation
- Responsive design

## ⚠️ Why Not Just Double-Click index.html?

Modern browsers block local file access for security, causing CORS errors. The Python server solves this by serving files properly.

## 💻 Requirements

- Python (comes pre-installed on Mac/Linux, easy to install on Windows)
- Any modern web browser
- No npm, no Node.js, no complex setup!

## 📱 Chromebook Users

Chromebooks need special handling - see `chromebook_setup.md` for detailed instructions. Quick options:
- **Easiest:** Upload to https://netlify.com (drag & drop!)
- **Alternative:** Enable Linux in Settings → Advanced → Developers, then run normally
- **Browser:** Use "Web Server for Chrome" extension

## 🌐 Free Online Hosting (Works on ANY device!)

**NEW:** See `FREE_HOSTING_OPTIONS.md` for complete 2025 guide!

**Quick options:**
- **🥇 Netlify:** Just drag your folder to https://netlify.com - instant website!
- **🥈 GitHub Pages:** Enable in repo Settings → Pages
- **🥉 Vercel:** Import from GitHub at https://vercel.com

## 🛠️ Troubleshooting

**"Python not found" error?**
- Windows: Install Python from python.org
- Mac: Python should be pre-installed, try `python3` instead of `python`
- Linux: Install with `sudo apt install python3` or similar

**Port 8000 in use?**
- Close other applications or restart your computer
- The script will show a helpful error message

## 📁 What's Included

- `run_server.py` - Smart server script (Mac/Linux - double-click this!)
- `RUN_ME.bat` - Windows batch file (Windows - double-click this!)
- `index.html` - Main application file
- `static/` folder - Contains all necessary code and assets
- This README file

**Just double-click the right file for your OS and you're running!**