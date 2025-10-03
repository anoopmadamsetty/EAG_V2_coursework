# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
import subprocess
import time

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# Global variables to store Preview app reference and canvas state
preview_app = None
current_canvas = None
temp_file_path = None

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle on the existing canvas in Preview"""
    global preview_app, current_canvas, temp_file_path
    try:
        if not preview_app or current_canvas is None:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Preview is not open. Please call open_preview first."
                    )
                ]
            }

        # Draw rectangle on the existing canvas
        from PIL import ImageDraw
        
        draw = ImageDraw.Draw(current_canvas)
        draw.rectangle([x1, y1, x2, y2], outline='black', width=2)
        
        # Save the updated canvas to the same file
        current_canvas.save(temp_file_path)
        
        # Refresh Preview to show the updated image
        subprocess.run(['osascript', '-e', f'tell application "Preview" to close front window'], check=False)
        subprocess.run(['open', '-a', 'Preview', temp_file_path], check=True)
        time.sleep(1)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2}) on the canvas"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def add_text_in_preview(text: str) -> dict:
    """Add text to the existing canvas in Preview or inside rectangle."""
    global preview_app, current_canvas, temp_file_path
    try:
        if not preview_app or current_canvas is None:
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Preview is not open. Please call open_preview first."
                    )
                ]
            }
        
        # Add text to the existing canvas
        from PIL import ImageDraw, ImageFont
        
        draw = ImageDraw.Draw(current_canvas)
        
        # Try to use a default font, fallback to basic if not available
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 12)
        except:
            font = ImageFont.load_default()
        
        # Add text to the canvas (positioned inside the rectangle)
        # Rectangle is at (250, 200) to (550, 300), so center text at (400, 250)
        draw.text((400, 250), text, fill='black', font=font, anchor='mm')
        
        # Save the updated canvas to the same file
        current_canvas.save(temp_file_path)
        
        # Refresh Preview to show the updated image
        subprocess.run(['osascript', '-e', f'tell application "Preview" to close front window'], check=False)
        subprocess.run(['open', '-a', 'Preview', temp_file_path], check=True)
        time.sleep(1)
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text:'{text}' added successfully to the canvas"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error adding text: {str(e)}"
                )
            ]
        }

@mcp.tool()
async def open_preview() -> dict:
    """Open Preview (macOS equivalent of Paint) with a new blank document"""
    global preview_app, current_canvas, temp_file_path
    try:
        # Create a simple blank image file first
        from PIL import Image
        import tempfile
        import os
        
        # Create a blank white image
        current_canvas = Image.new('RGB', (800, 600), color='white')
        
        # Save to a temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        current_canvas.save(temp_file.name)
        temp_file_path = temp_file.name
        temp_file.close()
        
        # Open the blank image in Preview
        subprocess.run(['open', '-a', 'Preview', temp_file_path], check=True)
        time.sleep(2)
        
        # Set preview_app to True to indicate Preview is running
        preview_app = True
        
        return {
            "content": [
                TextContent(
                    type="text",
                    text="Preview opened successfully with a blank white canvas"
                )
            ]
        }
            
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error opening Preview: {str(e)}"
                )
            ]
        }
# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING THE SERVER AT AMAZING LOCATION")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
