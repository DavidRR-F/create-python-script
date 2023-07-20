from .base import pyplater
from ..utils import *

from cookiecutter.main import cookiecutter
import click


@pyplater.group()
def insert():
    pass


@insert.command()
@click.option(
    "-n",
    "--name",
    prompt="snippet",
    help="Name of the snippet",
    type=click.Choice(get_options("snippets"), case_sensitive=False),
    cls=QuestionaryOption,
)
def snippet(name: str) -> None:
    context = {"project_slug": os.path.basename(os.getcwd())}
    add_supporting_files(f"{SNIPPET_PATH}/{name.lower()}", context)


@insert.command()
@click.option(
    "-n",
    "--name",
    prompt="Enter Project Name",
    help="Name of the project",
    callback=validate_project_name,
    is_eager=True,
    cls=QuestionaryInput,
)
@click.option(
    "-t",
    "--template",
    prompt="template",
    help="Name of the template",
    type=click.Choice(get_options("templates"), case_sensitive=False),
    cls=QuestionaryOption,
)
def template(name: str, template: str) -> None:
    context = {"project_slug": name}
    cookiecutter(
        f"{TEMPLATE_PATH}/{template.lower()}", no_input=True, extra_context=context
    )
