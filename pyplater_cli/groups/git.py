from .base import pyplater
from ..utils import *
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
def push(folder: str):
    git = Git()
    if git.push(folder):
        click.echo(f"{folder.title()} has been pushed!")
    else:
        click.echo(f"Failed to push {folder}")


@git.command()
def pull():
    git = Git()
    if not git.repo_exists():
        click.echo(
            f"https://github.com/{git._get_github_user()}/pyplater-templates does not exist"
        )
        return


@git.command()
def clone():
    print("Working on this")
