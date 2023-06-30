import subprocess
import re
import os
import click
from .constants import *

@click.command()
def create_python_project():
    click.echo(click.style("Please select the type of project:", fg="cyan"))
    click.echo(click.style("> Script", fg='blue'))
    click.echo(click.style("> API", fg='red'))
    project_type: str = click.prompt('', 
                                type=click.Choice(['Script', 'API'], case_sensitive=False))
    
    click.echo(click.style('Please enter the project name:', fg='cyan'))
    project_name: str = click.prompt('', type=str, callback=validate_project_name)

    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    if project_type.lower() == 'script':
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
        
    elif project_type.lower() == 'api':
        print('Under construction come back later')

def validate_project_name(ctx, param, value):
    pattern = r'^[a-zA-Z0-9_-]+$'
    if not re.match(pattern, value):
        raise click.BadParameter('Project name must contain only alphanumeric characters, hyphens or underscores.')
    return value
        
if __name__ == '__main__':
    create_python_project()