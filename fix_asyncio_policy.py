"""
Fix for asyncio ConnectionResetError on Windows.

This script changes the default event loop policy from WindowsProactorEventLoopPolicy
to WindowsSelectorEventLoopPolicy to avoid the ConnectionResetError that can occur
with the Proactor event loop.

Usage:
1. Place this file in your project directory
2. Import it at the beginning of your main script:
   import fix_asyncio_policy

Or run it directly before your application:
   python fix_asyncio_policy.py your_script.py
"""

import asyncio
import sys
import os

# Change the default event loop policy to use the Selector event loop
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print("Asyncio event loop policy set to WindowsSelectorEventLoopPolicy")

# If this script is run directly, it can be used to run another script
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Get the script to run
        script_path = sys.argv[1]
        sys.argv = sys.argv[1:]  # Remove this script from argv
        
        # Execute the script
        with open(script_path, 'rb') as script_file:
            script_code = script_file.read()
        
        # Use exec to run the script with the modified event loop policy
        exec(compile(script_code, script_path, 'exec'), globals(), globals())
