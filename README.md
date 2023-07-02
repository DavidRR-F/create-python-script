# PyPlater

Generates boilerplate structure for python project Including linting, formatting, and unit testing

## Get Setup

### Install Package

```
$ pip install pyplater
```

### Create python project in new or current directory

```
$ pyplater --name my-project --type script
```

## File Structure

```
your_project/
    ├── script/
        └── main.py
    ├── test/
        ├── __init__.py
        └── test.py
    ├── .env
    ├── .flake8
    ├── .gitignore
    ├── pyproject.toml
    └── README.md
```

## Default Library Configuration

- **_Linting:_** Flake8
- **_Formatting:_** Black
- **_Enviroment:_** Dotenv
- **_Testing:_** Unittest
