# codewards

Code wards participation


## Version python

3.6, 3.7, 3.8, 3.9, 3.10

## Needed

> pyenv install 3.6.15 3.7.13 3.8.13 3.9.12 3.10.4
> python3 -m venv .venv
> . .venv/bin/activate
> pip install -r requirements

## CI

> pyenv local 3.6.15 3.7.13 3.8.13 3.9.12 3.10.4
> tox

## Build

> python setup.py bdist_wheel

## Install

> python -m pip install -e .
>
