from .base import pyplater
from ..utils import *
import questionary
import click


@pyplater.group()
def git():
    pass


@git.command()
@click.option(
    "--username",
    prompt="Enter GitHub username",
    help="Your GitHub username",
    cls=QuestionaryInput,
)
@click.option(
    "--token",
    prompt="Enter GitHub personal access token",
    hide_input=True,
    help="Your GitHub personal access token",
    cls=QuestionaryPassword,
)
def init(username: str, token: str):
    git = Git()
    git.set_github_user(username)
    if not git.repo_exists(token):
        git.create_repo(token)
    else:
        click.echo("Repository already exists")


@git.command()
@click.argument("folder")
def push(folder: str) -> None:
    git = Git()
    # Check that repository has been initialized
    if not git.get_github_user():
        click.echo("User not initialized use command pyplater git init")
        return
    checked = True
    # if folder == "all": prompt for confirmation
    if folder == "all":
        checked = questionary.confirm(
            "Are you sure you want to push all folders?"
        ).ask()
    if checked:
        if git.push(folder):
            click.echo(f"{folder.title()} has been pushed")
        else:
            click.echo(f"Failed to push {folder}")


@git.command()
@click.argument("folder")
@click.option(
    "-t",
    "--type",
    prompt="type",
    help="template or snippet",
    type=click.Choice(["snippet", "template"], case_sensitive=False),
    cls=QuestionaryOption,
)
def pull(folder: str, type: str) -> None:
    git = Git()
    # Check that repository has been initialized
    if not git.get_github_user():
        click.echo("User not initialized use pyplater git init")
        return
    checked = True
    # if folder == "all": prompt for confirmation
    if folder == "all":
        checked = questionary.confirm(
            "Are you sure you want to pull all folders?"
        ).ask()
    if checked:
        if git.pull(f"{type}/{folder}"):
            click.echo(f"{type.title()} {folder.title()} has been pulled")
        else:
            click.echo(f"Failed to pull {folder}")
