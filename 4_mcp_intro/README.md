# Session 4 MCP - macOS Paint Equivalent

This project demonstrates MCP (Model Context Protocol) server implementation with macOS automation capabilities, providing a macOS equivalent to Windows Paint automation.

## Features

### Calculator Tools
- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced mathematical functions (power, square root, cube root, factorial, log)
- Trigonometric functions (sin, cos, tan)
- List operations and Fibonacci sequence generation

### macOS Preview Automation (Paint Equivalent)
- `open_preview()`: Opens Preview application with a new blank document
- `draw_rectangle(x1, y1, x2, y2)`: Draws a rectangle in Preview using annotation tools
- `add_text_in_preview(text)`: Adds text annotations to Preview documents

### Gmail Integration
- `send_email(to_email, subject, body)`: Send emails via Gmail API

## Installation

1. Install dependencies:
```bash
uv sync
```

2. Set up Gmail API credentials:
```bash
python setup_gmail.py
# Follow the instructions to create credentials.json
```

## Usage

### Running the MCP Server
```bash
python example2.py dev
```

### Testing macOS Preview Automation
```bash
python test_macos_paint.py
```

### Testing Gmail Integration
```bash
# After setting up credentials.json, you can test email sending
python -c "
import asyncio
from example2 import send_email
asyncio.run(send_email('test@example.com', 'Test Subject', 'Test Body'))
"
```

## macOS vs Windows Implementation

The original Windows implementation used:
- `pywinauto` for application automation
- `win32gui` for window management
- Microsoft Paint as the target application

The macOS equivalent uses:
- `PyObjC` for native macOS application control
- `subprocess` and `osascript` for AppleScript automation
- Preview as the target application (macOS built-in image viewer/editor)

## Key Differences

1. **Application**: Preview instead of Paint
2. **Automation Method**: AppleScript + PyObjC instead of pywinauto
3. **Drawing Capabilities**: Preview's annotation tools instead of Paint's drawing tools
4. **Window Management**: macOS native APIs instead of Windows APIs

## Requirements

- macOS 10.14 or later
- Python 3.12+
- Preview application (built into macOS)
- Accessibility permissions for automation (may be required)
- Gmail API credentials for email functionality

## Gmail API Setup

1. **Create Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.developers.google.com/)
   - Create a new project or select existing one

2. **Enable Gmail API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Gmail API" and enable it

3. **Create OAuth 2.0 Credentials**:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client IDs"
   - Choose "Desktop application"
   - Download the JSON file and rename it to `credentials.json`

4. **Place credentials.json in project root**:
   ```bash
   # The file should be in the same directory as example2.py
   ls -la credentials.json
   ```

5. **First run will open browser for authentication**:
   - The first time you use `send_email`, it will open a browser window
   - Sign in to your Google account and authorize the application
   - A `token.json` file will be created for future use

## Notes

- Preview's drawing capabilities are more limited than Paint
- Some functions may require accessibility permissions
- AppleScript coordinates may need adjustment based on your display setup
- The automation relies on Preview's annotation toolbar for drawing operations
