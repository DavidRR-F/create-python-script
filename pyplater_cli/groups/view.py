from .base import pyplater
from ..utils import *

from pathlib import Path


@pyplater.group()
def view():
    pass


@view.command(help="List currently saved snippets.")
def snippets():
    print("Snippets:")
    for file in os.listdir(SNIPPET_PATH):
        print("\t" + file)


@view.command(help="View file structure a currently saved snippet.")
@click.option(
    "-n",
    "--name",
    prompt="snippet",
    help="Name of the snippet",
    type=click.Choice(get_options("snippets"), case_sensitive=False),
    cls=QuestionaryOption,
)
def snippet(name: str):
    paths = DisplayablePath.make_tree(Path(os.path.join(SNIPPET_PATH, name)))
    for path in paths:
        print(path.displayable())


@view.command(help="List currently saved templates.")
def templates():
    print("Templates:")
    for file in os.listdir(TEMPLATE_PATH):
        print("\t" + file)


@view.command(help="View file structure a currently saved template.")
@click.option(
    "-n",
    "--name",
    prompt="template",
    help="Name of the template",
    type=click.Choice(get_options("templates"), case_sensitive=False),
    cls=QuestionaryOption,
)
def template(name: str):
    templates_dir = os.path.join(
        f"{TEMPLATE_PATH}/{name}/" + "{{cookiecutter.project_slug}}",
    )
    paths = DisplayablePath.make_tree(Path(templates_dir))
    for path in paths:
        print(path.displayable())
