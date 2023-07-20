from click.testing import CliRunner
from ..groups.base import pyplater
from ..groups.view import view
import pytest

pyplater.add_command(view)


@pytest.fixture
def runner():
    return CliRunner()


def test_view_template(runner):
    result = runner.invoke(pyplater, ["view", "template", "-n", "starter"])

    assert result.exit_code == 0
    assert "<project-name>/" in result.output


def test_view_templates(runner):
    result = runner.invoke(pyplater, ["view", "templates"])

    assert result.exit_code == 0
    assert "Templates:" in result.output
    assert "\n\tstarter\n" in result.output


def test_view_snippet(runner):
    result = runner.invoke(pyplater, ["view", "snippet", "-n", "sqlalchemy"])

    assert result.exit_code == 0
    assert "sqlalchemy/" in result.output


def test_view_snippets(runner):
    result = runner.invoke(pyplater, ["view", "snippets"])

    assert result.exit_code == 0
    assert "Snippets:" in result.output
    assert "\n\tsqlalchemy\n" in result.output
