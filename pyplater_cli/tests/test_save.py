from click.testing import CliRunner
from ..groups.base import pyplater
from ..groups.save import save
from ..utils.constants import *
import pytest
import shutil
import os

pyplater.add_command(save)


@pytest.fixture
def runner() -> CliRunner:
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
        pyplater, ["save", "template", str(source_dir), "test_project"]
    )

    assert result.exit_code == 0
    assert result.output == "test_project has been saved\n"

    temp_dir = os.path.join(
        TEMPLATE_PATH,
        "test_project",
    )
    request.node.temp_dir = temp_dir


def test_save_template(tmp_path, request, runner, setup_and_teardown):
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    with open(source_dir / "test.txt", "w") as f:
        f.write("test_project content")

    result = runner.invoke(
        pyplater, ["save", "snippet", str(source_dir), "test_project"]
    )

    assert result.exit_code == 0
    assert result.output == "test_project has been saved\n"

    temp_dir = os.path.join(
        SNIPPET_PATH,
        "test_project",
    )
    request.node.temp_dir = temp_dir
