"""Tests for the console module."""

from pytest import CaptureFixture

from src.console import display_config, display_error, display_info, display_welcome


def test_display_welcome(capsys: CaptureFixture[str]) -> None:
    """Test welcome message display."""
    display_welcome()
    captured = capsys.readouterr()
    assert "Python Boilerplate" in captured.out
    assert "minimal Python project" in captured.out


def test_display_config(capsys: CaptureFixture[str]) -> None:
    """Test configuration display."""
    test_config = {"test_key": "test_value", "another_key": "another_value"}
    display_config(test_config)
    captured = capsys.readouterr()
    assert "test_key" in captured.out
    assert "test_value" in captured.out
    assert "another_key" in captured.out
    assert "another_value" in captured.out


def test_display_error(capsys: CaptureFixture[str]) -> None:
    """Test error message display."""
    test_error = Exception("Test error message")
    display_error(test_error)
    captured = capsys.readouterr()
    assert "Error:" in captured.out
    assert "Test error message" in captured.out


def test_display_info(capsys: CaptureFixture[str]) -> None:
    """Test info message display."""
    test_message = "Test info message"
    display_info(test_message)
    captured = capsys.readouterr()
    assert test_message in captured.out
