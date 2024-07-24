#!/bin/bash

# Activate the virtual environment
if [ ! -d ".venv" ]; then
    ./venv.sh
else
    source .venv/bin/activate
fi

# Run the bot
python3 bot.py
