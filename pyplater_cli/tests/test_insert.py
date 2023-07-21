from click.testing import CliRunner
from ..groups.base import pyplater
from ..groups.insert import insert
from ..utils.constants import *
import pytest

pyplater.add_command(insert)


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_insert_template(tmp_path, runner):
    os.chdir(tmp_path)
    template_name = "starter"
    result = runner.invoke(
        pyplater,
        ["insert", "template", "-n", "test_project", "-t", template_name],
    )

    assert result.exit_code == 0
    assert (tmp_path / "test_project").exists()


def test_insert_snippet(tmp_path, runner):
    os.chdir(tmp_path)
    snippet_name = "sqlalchemy"
    result = runner.invoke(
        pyplater,
        ["insert", "snippet", "-n", snippet_name],
    )

    assert result.exit_code == 0
    assert (tmp_path / "db").exists()
