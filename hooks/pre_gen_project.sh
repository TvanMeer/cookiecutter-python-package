#!/bin/bash


# Upgrade pip
python3 -m pip install --upgrade pip

# Install virtualenv
pip3 install virtualenv

# Create python virtualenv .venv
python3 -m venv .venv

# Activate .venv
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Upgrade setuptools
pip install --upgrade setuptools

# Deactivate .venv
deactivate

exit 0