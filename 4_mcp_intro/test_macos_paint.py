#!/usr/bin/env python3
"""
Test script for macOS Preview automation functions
This demonstrates the macOS equivalent of the Windows Paint automation
"""

import asyncio
import sys
import os

# Add the current directory to the path so we can import from example2
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from example2 import open_preview, draw_rectangle, add_text_in_preview

async def test_macos_paint_equivalent():
    """Test the macOS Preview automation functions"""
    print("Testing macOS Preview automation (equivalent to Windows Paint)...")
    
    # Step 1: Open Preview
    print("\n1. Opening Preview...")
    result = await open_preview()
    print(f"Result: {result['content'][0].text}")
    
    # Wait a bit for Preview to fully load
    await asyncio.sleep(2)
    
    # Step 2: Draw a rectangle
    print("\n2. Drawing a rectangle...")
    result = await draw_rectangle(100, 100, 300, 200)
    print(f"Result: {result['content'][0].text}")
    
    # Wait a bit
    await asyncio.sleep(1)
    
    # Step 3: Add text
    print("\n3. Adding text...")
    result = await add_text_in_preview("Hello from macOS!")
    print(f"Result: {result['content'][0].text}")
    
    print("\nTest completed! Check Preview to see the results.")

if __name__ == "__main__":
    asyncio.run(test_macos_paint_equivalent())
