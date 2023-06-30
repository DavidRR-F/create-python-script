import re
import os
import click
import questionary
from .constants import *

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
    if not re.match(pattern, value):
        raise click.BadParameter('Project name must contain only alphanumeric characters, hyphens or underscores.')
    return value

@click.command()
@click.echo(click.style('Create Python Project 🐍 (Alpha)', fg='cyan', bold=True, underline=True))
@click.option('--name', prompt="Enter Project Name:")
@click.option('--type', prompt='type', type=click.Choice(['Script','API'], case_sensitive=False), cls=QuestionaryOption)
def create_python_project(name: str, type: str) -> None:

    # Create new Directory
    os.makedirs(name, exist_ok=True)
    os.chdir(name)

    # Generate Files
    if type.lower() == 'script':
        os.makedirs('script', exist_ok=True)
        with open('script/main.py', 'w') as f:
            f.write(SCRIPT_MAIN)
        os.makedirs('tests', exist_ok=True)
        with open('tests/test.py', 'w') as f:
            f.write(TEST_UNITTEST)
        with open('.flake8', 'w') as f:
            f.write(FLAKE)
        with open('.gitignore', 'w') as f:
            f.write(IGNORE)
        with open('README.md', 'w') as f:
            f.write(SCRIPT_README)
        with open('requirements.dev.txt', 'w') as f:
            f.write("flake8\n") 
        with open('requirements.txt', 'w') as f:
            f.write("python-dotenv\n") 
        
    elif type.lower() == 'api':
        print('Under construction come back later')

        
if __name__ == '__main__':
    create_python_project()