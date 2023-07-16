from click.testing import CliRunner
from unittest import mock
from pyplater_cli.cli import pyplater
import shutil
import pytest
import os


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def setup_and_teardown(tmp_path, request):
    yield
    temp_dir = getattr(request.node, "temp_dir", None)
    if temp_dir is not None and os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)


def test_save_template(tmp_path, request, runner, setup_and_teardown):
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    with open(source_dir / "test.txt", "w") as f:
        f.write("test_project content")

    result = runner.invoke(
        pyplater, ["save", str(source_dir), "test_project", "--type", "Template"]
    )

    assert result.exit_code == 0
    assert result.output == "test_project has been saved as a Template\n"

    temp_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates/test_project",
    )
    request.node.temp_dir = temp_dir


def test_save_snippet(tmp_path, request, runner, setup_and_teardown):
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    with open(source_dir / "test.txt", "w") as f:
        f.write("test_project content")

    result = runner.invoke(
        pyplater, ["save", str(source_dir), "test_project", "--type", "Snippet"]
    )

    assert result.exit_code == 0
    assert result.output == "test_project has been saved as a Snippet\n"

    temp_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "snippets/test_project",
    )
    request.node.temp_dir = temp_dir


def test_remove_template(runner, setup_and_teardown):
    templates_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates/test_template",
    )

    os.mkdir(templates_dir)

    with mock.patch("questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        result = runner.invoke(
            pyplater,
            ["remove", "test_template", "--type", "Template"],
            catch_exceptions=False,
        )

    assert result.exit_code == 0
    assert result.output == "Test_Template deleted\n"
    assert not os.path.exists(templates_dir)


def test_remove_snippet(runner, setup_and_teardown):
    snippet_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "snippets/test_snippet",
    )

    os.mkdir(snippet_dir)

    with mock.patch("questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        result = runner.invoke(
            pyplater,
            ["remove", "test_snippet", "--type", "Snippet"],
            catch_exceptions=False,
        )

    assert result.exit_code == 0
    assert result.output == "Test_Snippet deleted\n"
    assert not os.path.exists(snippet_dir)


def test_add_snippet(tmp_path, runner, setup_and_teardown):
    os.chdir(tmp_path)
    snippet_name = "sqlalchemy"
    result = runner.invoke(
        pyplater,
        ["add", "--snippet", snippet_name],
    )

    assert result.exit_code == 0
    assert (tmp_path / "db").exists()


def test_create_project(tmp_path, runner, setup_and_teardown):
    os.chdir(tmp_path)
    template_name = "starter"
    result = runner.invoke(
        pyplater,
        ["create", "--name", "test_project", "--template", template_name],
    )

    assert result.exit_code == 0
    assert (tmp_path / "test_project").exists()


def test_run_script(tmp_path, runner):
    os.chdir(tmp_path)
    script_name = "script"

    pyproject_content = """
        [pyplater.scripts]
        script = 'python my_script.py'
    """
    with open("my_script.py", "w") as f:
        f.write(pyproject_content)

    with open("pyproject.toml", "w") as f:
        f.write(pyproject_content)

    result = runner.invoke(pyplater, ["run", script_name])

    assert result.exit_code == 0


def test_view_command_with_name(runner):
    result = runner.invoke(pyplater, ["view", "templates", "--name", "starter"])

    assert result.exit_code == 0
    assert "<project-name>/" in result.output


def test_view_command_without_name(runner):
    result = runner.invoke(pyplater, ["view", "templates"])

    assert result.exit_code == 0
    assert "Templates:" in result.output
    assert "\n\tstarter\n" in result.output
