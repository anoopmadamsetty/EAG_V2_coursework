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

## Installation

1. Install dependencies:
```bash
uv sync
```

2. Install macOS-specific dependencies:
```bash
pip install pyobjc-framework-Cocoa pyobjc-framework-Quartz pyobjc-framework-ApplicationServices
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

## Notes

- Preview's drawing capabilities are more limited than Paint
- Some functions may require accessibility permissions
- AppleScript coordinates may need adjustment based on your display setup
- The automation relies on Preview's annotation toolbar for drawing operations
