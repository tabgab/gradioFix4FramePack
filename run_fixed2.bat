@echo off

call environment.bat

cd %~dp0webui

REM Run with the fixed demo_gradio script that includes the asyncio policy fix
"%DIR%\python\python.exe" demo_gradio_fixed.py --server 127.0.0.1 --inbrowser

:done
pause
