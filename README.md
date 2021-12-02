# cookiecutter-python-package

A kickstarter tool for python package development projects.

## Description

`cookiecutter-python-package` is a tool that kickstarts the process of creating a new python package project, a.k.a. library that can be installed with pip.  

It creates a sensible project layout and builds a virtual environment within the projects root folder (.venv directory). It then installs and configures development dependencies such as linters and formatters in the virtualenv, generates a poetry.lock file, and installs the new package in the virtualenv.
Vscode then opens up completely configured. 

`cookiecutter-python-package` saves you from having to do a lot of installation and configuration tasks when starting a new project. Instead, it provides a
full development environment setup with a base project layout so you can get started right away.


## Features

- A clean folder structure with some sample boilerplate code
- A [pyproject.toml](https://www.python.org/dev/peps/pep-0518/) project configuration that uses [Poetry](https://python-poetry.org/) as dependency manager
- [Pytest](https://docs.pytest.org/en/6.2.x/) setup and configuration
- [Black](https://black.readthedocs.io/en/stable/) + [iSort](https://pycqa.github.io/isort/) code formatters setup and configuration
- [Pylint](https://pylint.pycqa.org/en/latest/intro.html#what-is-pylint) setup and configuration
- [Vscode](https://code.visualstudio.com/docs/python/settings-reference) configuration

## Installation



Make sure [poetry](https://python-poetry.org/docs/#installation) is installed.
Also install [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).   
Both should be callable in the terminal as `poetry` and `cookiecutter`.  
[vscode](https://code.visualstudio.com/) is optional but will get the most out of `cookiecutter-python-package`.


## Usage

Open a terminal and paste the following command:

```
$ cookiecutter gh:TvanMeer/cookiecutter-python-package
```
It will ask you to enter a bunch of options, such as project name and description.   
Then the installer runs and the new project opens in Vscode.


## Portability

Should run on all operating systems, but I have only tested it on Linux.
