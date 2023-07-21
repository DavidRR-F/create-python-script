import pytest
from click.testing import CliRunner
from ..main import pyplater


@pytest.fixture
def runner():
    return CliRunner()


def test_run_command_with_existing_script(runner):
    result = runner.invoke(pyplater, ["run", "test"])
    assert result.exit_code == 0


def test_run_command_with_nonexistent_script(runner):
    result = runner.invoke(pyplater, ["run", "nonexistent_script"])
    assert result.exit_code == 0
