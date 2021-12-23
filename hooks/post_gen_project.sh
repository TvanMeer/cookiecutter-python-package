#!/bin/sh


echo "Installing dependencies with poetry..."


# Install dependencies and package in .venv
poetry install

# Create lock file
poetry lock

# Build tarball and wheel in dist folder
# poetry build

echo "Project created succesfully!"


# Open new project in Vscode
if ! command -v code &> /dev/null
then
    echo "Opening Vscode..."
    code .

    # Build documentation and start liveserver
    echo "Starting documentation liveserver..."
    .venv/bin/python .venv/bin/sphinx-autobuild docs docs/_build/html
    exit
fi