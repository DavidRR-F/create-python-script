from click.testing import CliRunner
from unittest import mock
from pyplater.cli import pyplater
import shutil
import pytest
import os


@pytest.fixture
def setup_and_teardown(tmp_path, request):
    yield
    temp_dir = getattr(request.node, "temp_dir", None)
    # Teardown: Delete the directory
    if temp_dir is not None and os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


def test_save_template(tmp_path, request, setup_and_teardown):
    # Prepare test directory and file
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    with open(source_dir / "test.txt", "w") as f:
        f.write("test_project content")

    runner = CliRunner()
    result = runner.invoke(
        pyplater, ["save", str(source_dir), "test_project", "--type", "Template"]
    )

    # Check if the command ran successfully
    assert result.exit_code == 0
    assert result.output == "test_project has been saved as a Template\n"

    # Send Teardown Path
    temp_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates/test_project",
    )
    request.node.temp_dir = temp_dir


def test_save_snippet(tmp_path, request, setup_and_teardown):
    # Prepare test directory and file
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    with open(source_dir / "test.txt", "w") as f:
        f.write("test_project content")

    runner = CliRunner()
    result = runner.invoke(
        pyplater, ["save", str(source_dir), "test_project", "--type", "Snippet"]
    )

    # Check if the command ran successfully
    assert result.exit_code == 0
    assert result.output == "test_project has been saved as a Snippet\n"

    # Send Teardown Path
    temp_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "snippets/test_project",
    )
    request.node.temp_dir = temp_dir


def test_remove_template(setup_and_teardown):
    # Prepare test data: Create a template directory
    templates_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates/test_template",
    )

    os.mkdir(templates_dir)

    # Run the command
    runner = CliRunner()
    with mock.patch("questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        result = runner.invoke(
            pyplater,
            ["remove", "test_template", "--type", "Template"],
            catch_exceptions=False,
        )

    # Check if the command ran successfully
    assert result.exit_code == 0
    assert result.output == "Test_Template deleted\n"
    assert not os.path.exists(templates_dir)


def test_remove_snippet(setup_and_teardown):
    # Prepare test data: Create a template directory
    snippet_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "snippets/test_snippet",
    )

    os.mkdir(snippet_dir)

    # Run the command
    runner = CliRunner()
    with mock.patch("questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        result = runner.invoke(
            pyplater,
            ["remove", "test_snippet", "--type", "Snippet"],
            catch_exceptions=False,
        )

    # Check if the command ran successfully
    assert result.exit_code == 0
    assert result.output == "Test_Snippet deleted\n"
    assert not os.path.exists(snippet_dir)


def test_add_snippet(tmp_path, setup_and_teardown):
    os.chdir(tmp_path)
    # Set up the input for the command
    snippet_name = "sqlalchemy"
    # Run the command
    runner = CliRunner()
    result = runner.invoke(
        pyplater,
        ["add", "--snippet", snippet_name],
    )

    # Check if the command ran successfully
    assert result.exit_code == 0

    # Perform additional assertions as needed

    # Example: Check if the supporting files were added
    assert (tmp_path / "db").exists()


def test_create_project(tmp_path, setup_and_teardown):
    os.chdir(tmp_path)
    # Set up the input for the command
    template_name = "starter"
    # Run the command
    runner = CliRunner()
    result = runner.invoke(
        pyplater,
        ["create", "--name", "test_project", "--template", template_name],
    )

    # Check if the command ran successfully
    assert result.exit_code == 0

    # Perform additional assertions as needed

    # Example: Check if the supporting files were added
    assert (tmp_path / "test_project").exists()


def test_run_script(tmp_path):
    os.chdir(tmp_path)
    # Prepare test data
    script_name = "script"

    # Mock the pyproject.toml content
    pyproject_content = """
        [pyplater.scripts]
        script = 'python my_script.py'
    """
    with open("my_script.py", "w") as f:
        f.write(pyproject_content)

    with open("pyproject.toml", "w") as f:
        f.write(pyproject_content)

    # Run the command
    runner = CliRunner()
    result = runner.invoke(pyplater, ["run", script_name])

    # Check if the command ran successfully
    assert result.exit_code == 0
