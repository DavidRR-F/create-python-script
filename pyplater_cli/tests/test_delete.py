from ..groups.base import pyplater
from ..groups.delete import delete
from ..utils.constants import *
from click.testing import CliRunner
from unittest.mock import patch
import pytest
import os

import shutil

# pyplater.add_command(delete)


# @pytest.fixture
# def runner():
#     return CliRunner()


# @pytest.fixture(scope="function")
# def create_snippet_dir(tmp_path, request):
#     snippet_dir = os.path.join(SNIPPET_PATH, "test_snippet")
#     snippet_file = os.path.join(snippet_dir, "test_snippet.txt")
#     os.makedirs(snippet_dir, exist_ok=True)
#     with open(snippet_file, "w") as f:
#         f.write("This is a test snippet.")
#     yield snippet_dir


# def test_remove_snippet(runner: CliRunner, create_snippet_dir):
#     snippet_dir = create_snippet_dir
#     with patch("questionary.confirm") as mock_confirm:
#         mock_confirm.return_value.ask.return_value = True
#         result = runner.invoke(
#             pyplater,
#             ["delete", "snippet", "--name", "test_snippet"],
#             catch_exceptions=False,
#         )

#     # assert result.exit_code == 0
#     assert result.output.strip() == "Test_Snippet deleted\n"
#     assert not os.path.exists(snippet_dir)
