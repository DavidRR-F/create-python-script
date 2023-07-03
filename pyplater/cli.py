import re
import os
import toml
import subprocess
from cookiecutter.main import cookiecutter
import click
import questionary

# add package, flask, and data science templates
project_options = ['Scripting', 'FastAPI']
# add setuptools and pipenv templates
manager_options = ['PIP', 'Poetry']
tester_options = ['Unittest', 'PyTest']
add_options = ['tester', 'manager']
options = {
    'tester': ['pip', 'poetry'],
    'manager': ['unittest', 'pytest']
}

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
        if os.path.isdir(os.path.join(path, file)):
            os.mkdir(file)
            add_supporting_files(f"{path}/{file}", context)
        else:
            with open(f'{path}/{file}', 'r') as f:
                template = f.read()

            for key, value in context.items():
                rendered_template = template.replace('{{' + key + '}}', value)

            # Write the rendered template to a file
            with open(f'{path}/{file}', 'w') as f:
                f.write(rendered_template)

@click.group()
def pyplater():
    pass

@pyplater.command()
#@click.echo(click.style('PyPlater 🐍 (Alpha)', fg='cyan', bold=True, underline=True))
@click.argument('name', prompt="Enter Project Name", callback=validate_project_name, is_eager=True, cls=QuestionaryInput)
@click.option('--type', prompt='type', type=click.Choice(project_options, case_sensitive=False), cls=QuestionaryOption)
@click.option('--tester', prompt='tester', type=click.Choice(tester_options, case_sensitive=False), cls=QuestionaryOption)
@click.option('--manager', prompt='manager', type=click.Choice(manager_options, case_sensitive=False), cls=QuestionaryOption)
def create(name: str, type: str, manager: str, tester: str):

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, 'templates')
    context = {'project_slug': name }

    cookiecutter(f'{templates_dir}/base/{type.lower()}', no_input=True, extra_context=context)
    
    os.chdir(context['project_slug'])

    # Tester
    add_supporting_files(f'{templates_dir}/tester/{tester.lower()}', context)

    # Manager
    add_supporting_files(f'{templates_dir}/manager/{manager.lower()}', context)

    # To Do
    # API cookiecutter Flask/FastAPI
    # ORM Options (Pydantic, SQLAlchemy)

@pyplater.command()
@click.argument('content')
@click.option('--option')
def add(content, option=None):
    if content not in add_options:
        raise click.BadParameter(f'Invalid name. Valid names are: {", ".join(add_options)}.')
    
    if option and option not in options[content]:
        raise click.BadParameter(f'Invalid option. Valid options for {content} are: {", ".join(options[content])}.')
    
    if not option:
        option = click.prompt(prompt=content, type=click.Choice(options[content], case_sensitive=False), cls=QuestionaryOption)

    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(current_script_dir, 'templates')
    context = {'project_slug': os.path.basename(os.getcwd()) }

    add_supporting_files(f'{templates_dir}/{content}/{option}', context)
    

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