@echo off
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

pip install os
pip install sys
pip install ctypes
pip install shutil
