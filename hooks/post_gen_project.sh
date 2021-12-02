#!/bin/sh


echo "Installing dependencies with poetry..."


# Install dependencies and package in .venv
poetry install

# Create lock file
poetry lock

# Build tarball and wheel in dist folder
# poetry build


echo "Project created succesfully!"


# Open fresh project in Vscode
if ! command -v code &> /dev/null
then
    echo "Trying to open Vscode..."
    code .
    exit
fi