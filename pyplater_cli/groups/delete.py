from .base import pyplater
from ..utils import *
import questionary
import shutil
import click


@pyplater.group()
def delete():
    pass


@delete.command(help="Delete a snippet by name.")
@click.option(
    "-n",
    "--name",
    prompt="snippet",
    type=click.Choice(get_options("snippets"), case_sensitive=False),
    cls=QuestionaryOption,
    help="Name of the snippet.",
)
def snippet(name: str) -> None:
    confirm = questionary.confirm(f"Are you sure you want to delete {name}").ask()
    if confirm:
        shutil.rmtree(f"{SNIPPET_PATH}/{name}")
        print(f"{name.title()} deleted")


@delete.command(help="Delete a template by name.")
@click.option(
    "-n",
    "--name",
    prompt="template",
    type=click.Choice(get_options("templates"), case_sensitive=False),
    cls=QuestionaryOption,
    help="Name of the template.",
)
def template(name: str) -> None:
    confirm = questionary.confirm(f"Are you sure you want to delete {name}").ask()
    if confirm:
        shutil.rmtree(f"{TEMPLATE_PATH}/{name}")
        print(f"{name.title()} deleted")
