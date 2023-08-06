from .base import pyplater
from ..utils import *
import questionary
import click


@pyplater.group()
def git():
    pass


@git.command(help="Initialize repository")
@click.option(
    "-u",
    "--username",
    prompt="Enter GitHub username",
    help="Your GitHub username",
    cls=QuestionaryInput,
)
@click.option(
    "-t",
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


@git.group()
def push():
    pass


@push.command(help="Push all folders")
def all():
    git = Git()
    # Check that repository has been initialized
    if not git.get_github_user():
        click.echo("User not initialized use command pyplater git init")
        return
    checked = True
    checked = questionary.confirm("Are you sure you want to push all folders?").ask()
    if checked:
        if git.push("all"):
            click.echo("All have been pushed")
        else:
            click.echo("Failed to push")


@push.command(help="Push specified a snippet folder")
@click.option(
    "-n",
    "--name",
    prompt="snippet",
    help="Name of the snippet",
    type=click.Choice(get_options("snippets"), case_sensitive=False),
    cls=QuestionaryOption,
)
def snippet(name: str) -> None:
    git = Git()
    if not git.get_github_user():
        click.echo("User not initialized use pyplater git init")
        return
    if git.push(f"snippets/{name}"):
        click.echo(f"{name} has been pushed")
    else:
        click.echo("Failed to push")


@push.command(help="Push specified a template folder")
@click.option(
    "-n",
    "--name",
    prompt="template",
    help="Name of the template",
    type=click.Choice(get_options("templates"), case_sensitive=False),
    cls=QuestionaryOption,
)
def template(name: str) -> None:
    git = Git()
    if not git.get_github_user():
        click.echo("User not initialized use pyplater git init")
        return
    if git.push(f"templates/{name}"):
        click.echo(f"{name} has been pushed")
    else:
        click.echo("Failed to push")


@git.group()
def pull():
    pass


@pull.command(help="Pull all folders")
def all():
    git = Git()
    # Check that repository has been initialized
    if not git.get_github_user():
        click.echo("User not initialized use pyplater git init")
        return
    checked = True
    # if folder == "all": prompt for confirmation
    checked = questionary.confirm("Are you sure you want to pull all folders?").ask()
    if checked:
        if git.pull("all"):
            click.echo("All has been pulled")
        else:
            click.echo("Failed to pull")


@pull.command(help="Pull specified a snippet folder")
@click.argument("name")
def snippet(name: str) -> None:
    git = Git()
    if not git.get_github_user():
        click.echo("User not initialized use pyplater git init")
        return
    if git.pull(f"snippets/{name}"):
        click.echo(f"{name} has been pulled")
    else:
        click.echo("Failed to pull")


@pull.command(help="Pull specified a template folder")
@click.argument("name")
def template(name: str) -> None:
    git = Git()
    if not git.get_github_user():
        click.echo("User not initialized use pyplater git init")
        return
    if git.pull(f"templates/{name}"):
        click.echo(f"{name} has been pulled")
    else:
        click.echo("Failed to pull")
