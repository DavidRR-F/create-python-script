import pytest
import os
from ..utils.classes import Git
from unittest.mock import patch, MagicMock, call
from subprocess import CalledProcessError


def setup_module(module):
    os.environ["HOME"] = "/tmp"


@pytest.fixture
def git():
    return Git()


def test_set_github_user(git):
    with patch("configparser.ConfigParser") as mock_config:
        config_instance = mock_config.return_value
        git.set_github_user("test_user")
        config_instance.__setitem__.assert_called_with(
            "GitHub", {"username": "test_user"}
        )
        assert config_instance.write.called


def test_get_github_user(git):
    with patch("configparser.ConfigParser") as mock_config:
        git.get_github_user()
        mock_config.return_value.read.assert_called()
