# cookiecutter-python-package

A scaffolding tool that creates boilerplate code for a python package.

## Description

`cookiecutter-python-package` creates a project layout and builds a virtual environment within the projects root folder. It then installs and configures all development dependencies, generates a poetry.lock file, a test build in the dist folder, and installs your package within the virtualenv.


## Features

- A simple folder structure with some sample boilerplate code
- A pyproject.toml file that uses Poetry as dependency manager
- Pytest setup and configuration
- Black + iSort code formatters setup and configuration
- Pylint setup and configuration
- Vscode configuration

## Installation

Make sure [poetry](https://python-poetry.org/docs/#installation) is installed.
And of course also install [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html). They should be callable in the terminal as `poetry` and `cookiecutter`.


## Usage

Open a terminal and paste the following command:

```
$ cookiecutter gh:TvanMeer/cookiecutter-python-package
```
It will ask you to enter a bunch of variable names and then runs the installer.


## Portability

Requires the bash shell. Should run on all operating systems, but I have only tested it on Ubuntu Linux.
