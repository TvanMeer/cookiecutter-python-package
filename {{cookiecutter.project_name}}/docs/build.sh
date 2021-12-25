#!/bin/sh

# Builds the documentation and opens it in the browser.
# This will start a liveserver.
# 
# First make this script executable:
# $ chmod +x build.sh
#
# Then execute it:
# ./build.sh
#
../.venv/bin/python ../.venv/bin/sphinx-autobuild --port=0 --open-browser . ./_build/html