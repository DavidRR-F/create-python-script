from .base import pyplater
from ..utils import *
import shutil


@pyplater.group()
def save():
    pass


@save.command(help="Save a directory as a snippet.")
@click.argument("dir")
@click.argument("name")
def snippet(dir: str, name: str) -> None:
    os.mkdir(f"{SNIPPET_PATH}/{name}")
    base_dir = os.path.join(SNIPPET_PATH, name)
    shutil.copytree(dir, f"{base_dir}/{name}", ignore=ignore_files)
    print(f"{name} has been saved")


@save.command(help="Save a directory as a template.")
@click.argument("dir")
@click.argument("name")
def template(dir: str, name: str) -> None:
    replace_string = "{{cookiecutter.project_slug}}"
    search_string = name

    os.mkdir(f"{TEMPLATE_PATH}/{name}")
    templates_dir = os.path.join(TEMPLATE_PATH, name)
    shutil.copytree(dir, f"{templates_dir}/{name}", ignore=ignore_files)
    format_template(name, templates_dir, replace_string, search_string)
    print(f"{name} has been saved")
