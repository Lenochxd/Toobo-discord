@echo off

REM Check if .venv directory exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    python -m pip install -r requirements.txt
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
    call .venv\Scripts\activate.bat
)
