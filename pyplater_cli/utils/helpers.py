from .constants import *
import click
import re
import os
import json


def ignore_files(dir, files):
    # Return a list of filenames to ignore
    return ["__pycache__"]


def validate_project_name(ctx, param, value):
    pattern = r"^[a-zA-Z0-9_-]+$"
    if value is not None and not re.match(pattern, value):
        raise click.BadParameter(
            "Project name must contain only alphanumeric \
                characters, hyphens, and underscores."
        )
    return value


def add_supporting_files(path, context, root=None):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            os.mkdir(file)
            add_supporting_files(f"{path}/{file}", context, file)
        else:
            with open(f"{path}/{file}", "r") as f:
                template = f.read()

            for key, value in context.items():
                rendered_template = template.replace("{{" + key + "}}", value)

            with open(f"{root}/{file}" if root else file, "w") as f:
                f.write(rendered_template)


def format_template(name, templates_dir, replace_string, search_string):
    with open(f"{templates_dir}/cookiecutter.json", "w") as f:
        json.dump({"project_slug": "default_project"}, f)

        for root, dirs, files in os.walk(f"{templates_dir}/{name}"):
            for dir in dirs:
                if dir == search_string:
                    dir_path = os.path.join(root, dir)
                    new_dir_name = dir.replace(search_string, replace_string)
                    new_dir_path = os.path.join(root, new_dir_name)

                    # Rename the directory
                    os.rename(dir_path, new_dir_path)

            for file in files:
                file_path = os.path.join(root, file)
                # Read the file contents
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                # Perform search and replace
                modified_content = content.replace(search_string, replace_string)
                # Write the modified content back to the file
                with open(file_path, "w") as f:
                    f.write(modified_content)

        os.rename(f"{templates_dir}/{name}", f"{templates_dir}/{replace_string}")


def get_options(name: str) -> list:
    return os.listdir(f"{BASE_PATH}/{name}")
