import re
import os
import toml
import subprocess
from cookiecutter.main import cookiecutter
import click
import questionary

project_options = ['Scripting', 'Data Science', 'Flask', 'FastAPI']
manager_options = ['PIP', 'Poetry']

class QuestionaryInput(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)

    def prompt_for_value(self, ctx):
        val = questionary.text(self.prompt).ask()
        return val
    
class QuestionaryConfirm(click.Option):
    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)

    def prompt_for_value(self, ctx):
        val = questionary.confirm(self.prompt).ask()
        return val    
    
class QuestionaryOption(click.Option):

    def __init__(self, param_decls=None, **attrs):
        click.Option.__init__(self, param_decls, **attrs)
        if not isinstance(self.type, click.Choice):
            raise Exception('Choice Option type arg must be click.Choice')

    def prompt_for_value(self, ctx):
        val = questionary.select(f"Choose {self.prompt}:", choices=self.type.choices).unsafe_ask()
        return val
    
def validate_project_name(ctx, param, value):
    pattern = r'^[a-zA-Z0-9_-]+$'
    if value is not None and not re.match(pattern, value):
        raise click.BadParameter('Project name must contain only alphanumeric characters, hyphens or underscores.')
    return value

def add_supporting_files(path, context):
    for file in os.listdir(path):
        with open(f'{path}/{file}', 'r') as f:
            template = f.read()

        for key, value in context.items():
            rendered_template = template.replace('{{' + key + '}}', value)

        # Write the rendered template to a file
        with open(f'{context["project_slug"]}/{file}', 'w') as f:
            f.write(rendered_template)

@click.group()
def pyplater():
    pass

@pyplater.command()
#@click.echo(click.style('PyPlater 🐍 (Alpha)', fg='cyan', bold=True, underline=True))
@click.option('--name', prompt="Enter Project Name", callback=validate_project_name, is_eager=True, cls=QuestionaryInput)
@click.option('--type', prompt='type', type=click.Choice(project_options, case_sensitive=False), cls=QuestionaryOption)
@click.option('--manager', prompt='manager', type=click.Choice(manager_options, case_sensitive=False), cls=QuestionaryOption)
def create(name: str, type: str, manager: str):

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, 'templates')
    context = {'project_slug': name }

    cookiecutter(f'{templates_dir}/base/{type.lower()}', no_input=True, extra_context=context)

    # Manager
    add_supporting_files(f'{templates_dir}/manager/{type.lower()}/{manager.lower()}', context)

    # To Do
    # Tests Options (Unittest, PyTest)
    # API cookiecutter Flask/FastAPI
    # ORM Options (Pydantic, SQLAlchemy)

@pyplater.command()
@click.argument('script_name')
def run(script_name):
    # Load the pyproject.toml file
    pyproject = toml.load('pyproject.toml')

    # Get the script command
    script_command: str = pyproject.get('pyplater', {}).get('scripts', {}).get(script_name)

    if script_command is None:
        click.echo(f"No script named '{script_name}' found in pyproject.toml.")
        return

    # Parse the command
    command: list = script_command.split(' ')

    # Execute the command
    subprocess.run(command)

if __name__ == '__main__':
    pyplater()