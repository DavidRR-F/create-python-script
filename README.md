<div style="display: flex; justify-content: center; align-items: center; gap: 1rem;">
<img src="https://davidrr-f.github.io/codepen-hosted-assets/pyplater-banner.svg" alt="My logo" width="900" height="300">
</div>

**_in development_**

<!-- for reference when published -->
<!-- <p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p> -->

PyPlater is a Python CLI Tool to generates boilerplate code for python projects Including linting, formatting, unit testing, and package managing for
a variety of templates.

# Project Options

|    Templates     |     Testing      | Package Managers |    ORMs    |
| :--------------: | :--------------: | :--------------: | :--------: |
| Vanilla, FastAPI | Unittest, PyTest |   PIP, Poetry    | SqlAlchemy |

# Get Setup

### Install PyPlater

```
$ pip install pyplater
```

## Commands

## PyPlater Create

### Create Vanilla Project

```
$ pyplater create --name my-project --type vanilla --manager poetry --orm sqlalchemy
```

## File Structure

```
your_project/
    ├── your_project/
        ├── db/
            ├── database.py
            ├── crud.py
            ├── schema.py
            └── models.py
        ├── test/
            ├── __init__.py
            └── test.py
        ├── __init__.py
        ├── config.py
        └── main.py
    ├── .env.example
    ├── .flake8
    ├── .gitignore
    ├── pyproject.toml
    └── README.md
```

## Run custom commands

```
$ pyplater run install
$ pyplater run script
```

## pyproject.toml

```
[pyplater.scripts]
script = "poetry run python ./script/main.py"
install = "poetry install"
```

## Default Library Configuration

- **_Linting:_** Flake8
- **_Formatting:_** Black
- **_Enviroment:_** Dotenv
- **_Testing:_** Unittest
