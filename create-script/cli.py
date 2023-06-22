import subprocess
import re
import os


def create_files(files, root_directory):
    for file in files:
        directory, filename = os.path.split(file[0])
        if directory:
            os.makedirs(os.path.join(root_directory, directory), exist_ok=True)
            file_path = os.path.join(os.path.join(root_directory, directory), filename)
        else:
            file_path = os.path.join(root_directory, filename)

        content = file[1]

        with open(file_path, "w") as new_file:
            new_file.write(content)


def create_and_start_venv(root_directory):
    subprocess.run(["python", "-m", "venv", os.path.join(root_directory, ".venv")])
    subprocess.run(["source", os.path.join(root_directory, ".venv/Scripts/activate")])

def install_dependencies(root_directory):
    subprocess.run(
        ["pip", "install", "-r", os.path.join(root_directory, "requirements.txt")]
    )
    subprocess.run(
        ["pip", "install", "-r", os.path.join(root_directory, "requirements.dev.txt")]
    )

def main(root_directory):
    pattern = r'^[a-zA-Z0-9_-]+$'
    main = """from dotenv import load_dotenv
import os

load_env()

def main():
    print(os.getenv("YOUR_SECRET"))

if __name__ == "__main__":
    main()
    """
    test = """import unittest

class YourTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_yourcode(self):
        pass
    """
    read = """# Python Scripting

## Get Started

### install dev dependencies
```
$ pip install -r requirements.dev.txt
```

### run formatting
```
$ black . -v
```

### run linting
```
$ flake8
```

### run unit tests
```
$ python -m unittest discover test
```
    """
    black = """[tool.black]
exclude = "__pycache__,.venv"
line-length = 88
target-version = ['py37']
    """
    flake = """# Exclude files from linting
[flake8]
exclude = 
    __pycache__,
    .venv
ignore =
    E251,
    E302,
    W291,
    W292,
    W293
    """
    ignore = """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Vscode
.vscode
    """
    files = [
        ("scripts/main.py", main),
        ("test/__init__.py", ""),
        ("test/test.py", test),
        (".env", "YOUR_SECRET=Foo"),
        (".flake8", flake),
        (".gitignore", ignore),
        ("pyproject.toml", black),
        ("README.md", read),
        ("requirements.dev.txt", "flake8\nblack"),
        ("requirements.txt", "dotenv"),
    ]

    if re.match(pattern, root_directory):
        print("Creating Files")
        create_files(files, root_directory)
        print("Creating Virtual Enviroment")
        create_and_start_venv(root_directory)
        print("Installing Default Dependencies")
        install_dependencies(root_directory)
    else:
        print("Invalid Directory Name: Please enter a valid directory name or leave empty to create in root directory\n",
              "Examples:\n",
              "create-python script my-script\n",
              "create-python-script my_script\n",
              "create-python-script myScript\n",
              "create-python-script\n")