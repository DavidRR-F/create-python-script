from .groups.base import pyplater
from .groups.delete import delete
from .groups.edit import edit
from .groups.git import git
from .groups.insert import insert
from .groups.save import save
from .groups.view import view

import subprocess
import click
import toml

pyplater.add_command(git)
pyplater.add_command(insert)
pyplater.add_command(delete)
pyplater.add_command(edit)
pyplater.add_command(save)
pyplater.add_command(view)


@pyplater.command()
@click.argument("script_name")
def run(script_name):
    pyproject = toml.load("pyproject.toml")

    script_command: str = (
        pyproject.get("pyplater", {}).get("scripts", {}).get(script_name)
    )

    if script_command is None:
        click.echo(f"No script named '{script_name}' found in pyproject.toml.")
        return

    command: list = script_command.split(" ")

    subprocess.run(command)


if __name__ == "__main__":
    pyplater()
