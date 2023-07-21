from ..groups.base import pyplater
from ..groups.edit import edit
from ..utils.constants import *
from click.testing import CliRunner
import pytest

pyplater.add_command(edit)


@pytest.fixture
def runner():
    return CliRunner()


def test_snippet_file_not_found(runner):
    # Test when the snippet file does not exist
    result = runner.invoke(pyplater, ["edit", "snippet", "-n", "nonexistent_snippet"])
    assert result.exit_code == 2


def test_template_file_not_found(runner):
    # Test when the snippet file does not exist
    result = runner.invoke(pyplater, ["edit", "template", "-n", "nonexistent_snippet"])
    assert result.exit_code == 2
