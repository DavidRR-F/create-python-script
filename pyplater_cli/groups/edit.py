from .base import pyplater
from ..utils import *
import subprocess
import click


@pyplater.group()
def edit():
    pass


@edit.command()
@click.option(
    "-n",
    "--name",
    prompt="snippet",
    help="Name of the snippet",
    type=click.Choice(get_options("snippets"), case_sensitive=False),
    cls=QuestionaryOption,
)
def snippet(name: str) -> None:
    if not file_exists(f"{SNIPPET_PATH}/{name}"):
        click.echo(f"{name} does not exist.")
        return
    command = f"code {SNIPPET_PATH}/{name}"
    try:
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print("Visual Studio is not installed or the command is incorrect.")


@edit.command()
@click.option(
    "-n",
    "--name",
    prompt="template",
    help="Name of the template",
    type=click.Choice(get_options("templates"), case_sensitive=False),
    cls=QuestionaryOption,
)
def template(name: str) -> None:
    if not file_exists(f"{TEMPLATE_PATH}/{name}"):
        click.echo(f"{name} does not exist.")
        return
    command = f"code {TEMPLATE_PATH}/{name}"
    try:
        subprocess.run(command, shell=True)
    except FileNotFoundError:
        print("Visual Studio is not installed or the command is incorrect.")
