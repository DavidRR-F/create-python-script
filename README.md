<div style="display: flex; justify-content: center; align-items: center; gap: 1rem;">
<img src="https://davidrr-f.github.io/codepen-hosted-assets/pyplater-banner.svg" alt="My logo" width="900" height="300">
</div>

**_in development_**

<div align="center">
  <a href="link-to-your-repository">
    <img src="https://img.shields.io/badge/Python-v3.10%2B-brightgreen" alt="Python Version">
  </a>
  <a href="link-to-your-repository">
    <img src="https://img.shields.io/pypi/v/pyplater-cli?color=%2334D058&label=pypi%20package" alt="Package Version">
  </a>
  <a href="https://github.com/DavidRR-F/pyplater/actions/workflows/ci.yml">
    <img src="https://github.com/DavidRR-F/pyplater/workflows/CD_Pipeline/badge.svg?event=push&branch=main" alt="Test Status">
  </a>
</div>
PyPlater is a Python CLI Tool to generate, build, and create boilerplate code for python projects Including linting, formatting, unit testing, and package managing from prebuilt and your own custom templates

# Get Setup

### Install PyPlater

```
$ pip install pyplater-cli
```

# Commands

PyPlater CLI supports two templating types:

- template: a project file structure using the cookiecutter library
- snippet: a small directory literal for commonly used modules

## Pyplater Save

Save project directorys as snippets or templates

[![PyPlater Save](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/save.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/save.gif)

### Options

- Type: template/snippet
- Directory: the directory you with to copy
- Name: the name of the new template/snippet

### Example

Save a template

```
$ pyplater save template path/to/folder <name>
```

Save a snippet

```
$ pyplater save snippet path/to/folder <name>
```

## PyPlater Insert

Add snippet files to existing projects or generate not template project

[![PyPlater Insert](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/insert.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/insert.gif)

### Options

- Type: template/snippet
- -n/--name: namee of template/snippet

### Example

Insert a template

```
$ pyplater insert template -n <custom_name> -t <saved_template>
```

Insert a snippet

```
$ pyplater insert snippet -n <saved_snippet>
```

## PyPlater Git

Initialize a git repository to hold your templates/snippets that you can then push an pull from

[![PyPlater Git](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/git.gif)](https://davidrr-f.github.io/codepen-hosted-assets/pyplater/git.gif)

### Options

- Actions: push/pull
- Options: template/snippet
- -n/--name: template/snippet name

### Examples

Initialize Git Repository (Personal access token is not stored)

```
$ pyplater git init -u <github_username> -t <personal_access_token>
```

Push templates to repository

```
$ pyplater git push all

or

$ pyplater git push snippet -n <snippet_name>
```

Pull templates from repository

```
$ pyplater pull all

or

$ pyplater pull snippet <snippet_name>
```

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

## PyPlater Edit

Open your template and snippets in vs code

### Options

- Types: template/snippet
- -n/--name: name of template or snippet

### Examples

```
$ pyplater edit snippet -n <name>
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
