from ..groups.base import pyplater
from ..groups.delete import delete
from ..utils.constants import *
from click.testing import CliRunner
from unittest.mock import patch
import pytest
import os

import shutil

pyplater.add_command(delete)


@pytest.fixture
def runner():
    return CliRunner()


def test_remove_snippet_no_existing_snippet(runner: CliRunner):
    with patch("questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        result = runner.invoke(
            pyplater,
            ["delete", "snippet", "--name", "test_snippet"],
            catch_exceptions=False,
        )

    assert result.exit_code == 2


def test_remove_template_no_existing_template(runner: CliRunner):
    with patch("questionary.confirm") as mock_confirm:
        mock_confirm.return_value.ask.return_value = True
        result = runner.invoke(
            pyplater,
            ["delete", "template", "--name", "test_template"],
            catch_exceptions=False,
        )

    assert result.exit_code == 2
