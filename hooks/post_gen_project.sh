#!/bin/sh


echo "Installing dependencies with poetry..."


# Install dependencies and package in .venv
poetry install

# Create lock file
poetry lock

# Build tarball and wheel in dist folder
# poetry build

# Build documentation
source .venv/bin/activate
cd ./docs
make html
cd ..
deactivate

echo "Project created succesfully!"


# Open fresh project in Vscode
if ! command -v code &> /dev/null
then
    echo "Trying to open Vscode..."
    code .
    exit
fi