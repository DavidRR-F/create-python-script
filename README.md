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

PyPlater is a Python CLI Tool to generate, build, and create boilerplate code for python projects Including linting, formatting, unit testing, and package managing from prebuilt and your own custom templates

# Get Setup

### Install PyPlater

```
$ pip install pyplater
```

# Commands

## PyPlater Create

[![PyPlater Create](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/create.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/create.gif)

### Options

- --name: Project Name
- --template: Project Template

### Example

```
$ pyplater create --name your_project --type starter
```

## Pyplater Save

Save project directorys as snippets or templates

[![PyPlater Save](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/save.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/save.gif)

### Options

- [Directory]: the directory you with to copy
- [Name]: the name of the new template/snippet
- --type: (template, snippet)

### Example

```
$ pyplater save ./your_project newTemplate --type template
```

## PyPlater Add

Add snippet files to existing projects

[![PyPlater Create](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/add.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/add.gif)

### Options

- --snippet: Library for the chosen content

### Example

```
$ pyplater add --snippet pytest
```

### Starter Snippets

- pytest
- unittest
- pip
- poetry
- sqlalchemy

## PyPlater View

View all saved snippets/templates or view a specific snippet's/template's file structure

[![PyPlater View](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/view.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/view.gif)

### Options

- [Type]: (snippets, templates)
- --name: specific tamplate or snippet

### Examples

```
$ pyplater view snippets

$ pyplater view templates --name your_project
```

## PyPlater Run

Define commands in the pyproject.toml to run your custom scripts with pyplater

```
$ pyplater run script
$ pyplater run test
```

## pyproject.toml

```
[pyplater.scripts]
script = "python ./main/script/main.py"
test = "python -m unittest:discover tests/"
```

## PyPlater Remove

Remove Templates and/or Snippets from your device

### Options

- [Name]: name of the template/snippet
- --type: (template, snippet)

### Example

```
$ pyplater remove your_project --type template
```
