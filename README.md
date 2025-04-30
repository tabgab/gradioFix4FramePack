# Asyncio ConnectionResetError Fix for Windows

This directory contains files to fix the following error that occurs on Windows when using asyncio:

```
Exception in callback _ProactorBasePipeTransport._call_connection_lost(None)
handle: <Handle _ProactorBasePipeTransport._call_connection_lost(None)>
Traceback (most recent call last):
  File "asyncio\events.py", line 80, in _run
  File "asyncio\proactor_events.py", line 162, in _call_connection_lost
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
```

## The Issue

This error occurs because the default event loop policy on Windows is `WindowsProactorEventLoopPolicy`, which can sometimes cause connection reset errors. The solution is to change the default event loop policy to `WindowsSelectorEventLoopPolicy`.

## Solutions

This repository provides three different ways to fix the issue:

### 1. Using fix_asyncio_policy.py

This is a standalone script that changes the event loop policy and can be used to run any Python script with the fixed policy.

Usage:
```
python fix_asyncio_policy.py your_script.py
```

Or import it at the beginning of your script:
```python
import fix_asyncio_policy
```

### 2. Using run_fixed.bat

This batch file uses the fix_asyncio_policy.py script to run the original demo_gradio.py with the fixed event loop policy.

Usage:
```
run_fixed.bat
```

### 3. Using run_fixed2.bat with demo_gradio_fixed.py

This solution uses a modified version of demo_gradio.py (demo_gradio_fixed.py) that includes the event loop policy fix directly in the script.

Usage:
```
run_fixed2.bat
```

## Which Solution to Choose?

- **Solution 1** is the most flexible and can be used with any Python script.
- **Solution 2** is good if you don't want to modify the original script.
- **Solution 3** is the most direct and doesn't require an additional script.

Choose the solution that best fits your needs.

## Technical Details

The fix works by changing the default event loop policy from `WindowsProactorEventLoopPolicy` to `WindowsSelectorEventLoopPolicy` using the following code:

```python
import asyncio
import sys
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

This change must be made before any asyncio operations are performed.
