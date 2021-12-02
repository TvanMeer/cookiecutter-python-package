#!/bin/sh


# Upgrade pip
python3.10 -m pip install --upgrade pip

# Install virtualenv
pip3.10 install virtualenv

# Create python virtualenv .venv
python3.10 -m venv .venv

# Upgrade pip
.venv/bin/python -m pip install --upgrade pip

# Upgrade setuptools
.venv/bin/python -m pip install --upgrade setuptools


exit 0