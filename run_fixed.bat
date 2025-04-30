@echo off

call environment.bat

cd %~dp0webui

REM Run with the fixed asyncio policy
"%DIR%\python\python.exe" %~dp0fix_asyncio_policy.py demo_gradio.py --server 127.0.0.1 --inbrowser

:done
pause
