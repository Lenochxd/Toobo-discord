@echo off

REM Activate the virtual environment
if not exist .venv\ (
    call venv.bat
) else (
    call .venv\Scripts\activate.bat
)

REM Run the bot
python bot.py
