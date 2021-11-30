#!/bin/bash


echo "Installing dependencies with poetry..."


# Install dependencies
poetry install

# Create lock file
poetry lock

# Build tarball and wheel in dist folder
poetry build


echo "Project created succesfully!"