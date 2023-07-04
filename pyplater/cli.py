import os
import re
import toml
import shutil
import json
import subprocess
from cookiecutter.main import cookiecutter
import click
from pathlib import Path
from pyplater.utils.questionary import *
from pyplater.utils.tree import DisplayablePath

def validate_project_name(ctx, param, value):
    pattern = r'^[a-zA-Z0-9_-]+$'
    if value is not None and not re.match(pattern, value):
        raise click.BadParameter('Project name must contain only alphanumeric characters, hyphens or underscores.')
    return value

def add_supporting_files(path, context, root=None):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            os.mkdir(file)
            add_supporting_files(f"{path}/{file}", context, file)
        else:
            with open(f'{path}/{file}', 'r') as f:
                template = f.read()

            for key, value in context.items():
                rendered_template = template.replace('{{' + key + '}}', value)
            
            with open(f"{root}/{file}" if root else file, 'w') as f:
                f.write(rendered_template)

def get_options(name: str) -> list:
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, name)
    return os.listdir(templates_dir)

@click.group()
def pyplater():
    pass

@pyplater.command()
@click.argument('dir')
@click.argument('name')
@click.option('--type', prompt="type", type=click.Choice(['Template', 'Section'], case_sensitive=False), cls=QuestionaryOption)
def save(dir: str, name: str, type: str) -> None:
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, f'{type.lower()}s')
    os.mkdir(f'{templates_dir}/{name}')
    templates_dir = os.path.join(templates_dir, name)
    shutil.copytree(dir, f'{templates_dir}/{name}')
    if type.lower() == 'template':
        with open(f'{templates_dir}/cookiecutter.json', 'w') as f:
            json.dump({'project_slug': 'default_project'}, f)
        os.rename(f'{templates_dir}/{name}', templates_dir+'/{{cookiecutter.project_slug}}')
    print(f'{name} has been saved as a {type}')

@pyplater.command()
@click.argument('name')
@click.option('--type', prompt="type", type=click.Choice(['Template', 'Section'], case_sensitive=False), cls=QuestionaryOption)
def remove(name: str, type: str) ->  None:
    confirm = questionary.confirm(f"Are you sure you want to delete {name}").ask()
    if confirm:
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(current_script_dir, f'{type.lower()}s')
        shutil.rmtree(f'{templates_dir}/{name}')
        print(f'{name.title()} deleted')

@pyplater.command()
@click.argument('content')
@click.option('--name', default=None)
def view(content: str, name):
    if name:
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        if content == 'templates':
            templates_dir = os.path.join(current_script_dir, f'{content}/{name}/'+'{{cookiecutter.project_slug}}')
        else: 
            templates_dir = os.path.join(current_script_dir, f'{content}/{name}')
        paths = DisplayablePath.make_tree(
            Path(templates_dir)
        )
        for path in paths:
            print(path.displayable())
    else:
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        templates_dir = os.path.join(current_script_dir, f'{content}')
        print(content.title()+":")
        for file in os.listdir(templates_dir):
            print("\t"+file)

@pyplater.command()
@click.option('--struct', prompt='struct', type=click.Choice(get_options('sections'), case_sensitive=False), cls=QuestionaryOption)
def add(struct):
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, 'sections')
    context = {'project_slug': os.path.basename(os.getcwd()) }

    add_supporting_files(f'{templates_dir}/{struct}', context)

@pyplater.command()
@click.option('--name', prompt="Enter Project Name", callback=validate_project_name, is_eager=True, cls=QuestionaryInput)
@click.option('--template', prompt='template', type=click.Choice(get_options('templates'), case_sensitive=False), cls=QuestionaryOption)
def create(name: str, template: str) -> None:

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, 'templates')
    context = {'project_slug': name }

    cookiecutter(f'{templates_dir}/{template.lower()}', no_input=True, extra_context=context)
    

@pyplater.command()
@click.argument('script_name')
def run(script_name):
    pyproject = toml.load('pyproject.toml')

    script_command: str = pyproject.get('pyplater', {}).get('scripts', {}).get(script_name)

    if script_command is None:
        click.echo(f"No script named '{script_name}' found in pyproject.toml.")
        return

    command: list = script_command.split(' ')

    subprocess.run(command)

if __name__ == '__main__':
    pyplater()