# Create Python Script Package
Generates boilerplate structure for python scripts Including linting, formatting, and unit testing

## Get Setup

### Install Package
```
$ pip install create-python-script
```

### Create python project in new or current directory
```
$ create-python-script <project-name>

or 

$ create-python-script
```

## File Structure
```
your_project/
    ├── .venv/
    ├── scripts/
        └── main.py
    ├── test/
        ├── __init__.py
        └── test.py
    ├── .env
    ├── .flake8
    ├── .gitignore
    ├── pyproject.toml
    ├── requirements.txt
    ├── requirements.dev.txt
    └── README.md
```

## Default Library Configuration

- ***Linting:*** Flake8
- ***Formatting:*** Black
- ***Enviroment:*** Dotenv
- ***Testing:*** Unittest