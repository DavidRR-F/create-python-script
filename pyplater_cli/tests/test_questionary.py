from unittest.mock import MagicMock
import click
from pyplater.utils.questionary import (
    QuestionaryInput,
    QuestionaryConfirm,
    QuestionaryOption,
)


def test_questionary_input_prompt_for_value(mocker):
    mock_ctx = MagicMock()

    mock_ask = MagicMock(return_value="Test")

    mock_text = mocker.patch("questionary.text")
    mock_text.return_value.ask = mock_ask

    instance = QuestionaryInput(["--name"], prompt="What is your name?")

    val = instance.prompt_for_value(mock_ctx)

    assert val == "Test"

    mock_text.assert_called_once_with("What is your name?")
    mock_ask.assert_called_once()


def test_questionary_confirm_prompt_for_value(mocker):
    mock_ctx = MagicMock()

    mock_ask = MagicMock(return_value=True)

    mock_confirm = mocker.patch("questionary.confirm")
    mock_confirm.return_value.ask = mock_ask

    instance = QuestionaryConfirm(["--confirm"], prompt="Do you confirm?")

    val = instance.prompt_for_value(mock_ctx)

    assert val is True

    mock_confirm.assert_called_once_with("Do you confirm?")
    mock_ask.assert_called_once()


def test_questionary_option_prompt_for_value(mocker):
    # Create a mock context (ctx)
    mock_ctx = MagicMock()

    # Mock the 'unsafe_ask' method to return 'option1'
    mock_unsafe_ask = MagicMock(return_value="option1")

    # Mock the 'select' function
    mock_select = mocker.patch("questionary.select")
    # Make it so that calling select() and then unsafe_ask() returns 'option1'
    mock_select.return_value.unsafe_ask = mock_unsafe_ask

    # Create an instance of your class with the correct arguments
    instance = QuestionaryOption(
        ["--option"], type=click.Choice(["option1", "option2"]), prompt="an option"
    )

    # Call the method under test
    val = instance.prompt_for_value(mock_ctx)

    # Assert that the method returns the expected value
    assert val == "option1"

    # Assert that the mock was called with the correct argument
    mock_select.assert_called_once_with(
        "Choose an option:", choices=["option1", "option2"]
    )
    mock_unsafe_ask.assert_called_once()
