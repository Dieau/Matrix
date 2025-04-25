#!/bin/bash

if ! command -v python3 &>/dev/null; then
    echo "Python 3 could not be found. Please install Python 3.8 or higher."
    exit 1
fi

python3 -m venv .venv

source .venv/bin/activate

pip install --upgrade pip

pip install -e ".[dev]"

echo -e "\nSetup complete!\n"
echo -e "To activate the virtual environment, run:"
echo -e "source .venv/bin/activate\n"