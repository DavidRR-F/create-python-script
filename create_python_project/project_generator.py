import re
import os
from cookiecutter.main import cookiecutter
import click
import questionary
import toml

project_options = ['Script', 'API', 'Model', 'Data']

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

@click.command()
#@click.echo(click.style('PyPlater 🐍 (Alpha)', fg='cyan', bold=True, underline=True))
@click.option('--name', prompt="Enter Project Name", callback=validate_project_name, is_eager=True)
@click.option('--type', prompt='type', type=click.Choice(project_options, case_sensitive=False), cls=QuestionaryOption)
def create_python_project(name: str, type: str):

    # Create new Directory
    os.makedirs(name, exist_ok=True)
    os.chdir(name)

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, 'templates')

    cookiecutter(f'{templates_dir}/{type.lower()}', no_input=True, extra_context={'project_slug': name})

    # Update pyproject.toml
    pyproject_dict = toml.load('pyproject.toml')

    # Edit the 'name' under 'tool.poetry'
    pyproject_dict['tool']['poetry']['name'] = name

    # Write the changes back to the pyproject.toml file
    with open('pyproject.toml', 'w') as f:
        toml.dump(pyproject_dict, f)

if __name__ == '__main__':
    create_python_project()