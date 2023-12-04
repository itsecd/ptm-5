import os
import pytest
from main import clear
from wordle import Wordle
from unittest.mock import patch


def test_wordle_initialization():
    wordle = Wordle()
    assert isinstance(wordle, Wordle)
    assert wordle.user_guess == ""
    assert wordle.chosen_word in wordle.words
    assert wordle.max_words == 5


@pytest.mark.parametrize("invalid_guess", ["abcde", "12345", "word", "sixletters"])
def test_invalid_user_guess(invalid_guess):
    wordle = Wordle()
    patch("builtins.input", side_effect=invalid_guess)
    with pytest.raises(OSError):
        wordle.get_user_guess()
    assert wordle.user_guess == ""


@pytest.mark.parametrize("user_inputs, expected_output", [
    (["denim"], True),
    (["apple"], True),
])
def test_get_user_guess(user_inputs, expected_output):
    wordle = Wordle()
    with patch("builtins.input", side_effect=user_inputs):
        wordle.get_user_guess()
    assert (len(wordle.user_guess) == wordle.max_words or
            wordle.user_guess in wordle.words or
            wordle.user_guess not in wordle.valid_words) == expected_output


def test_correct_guess():
    wordle = Wordle()
    wordle.user_guess = wordle.chosen_word
    assert wordle.is_correct_guess() is True


def test_incorrect_guess():
    wordle = Wordle()
    wordle.user_guess = "wrongword"
    assert wordle.is_correct_guess() is False


def test_check_word_correct_guess():
    wordle = Wordle()
    wordle.user_guess = wordle.chosen_word
    status, result = wordle.check_word()
    assert status is True
    assert result != []


def test_check_word_incorrect_guess():
    wordle = Wordle()
    wordle.user_guess = "wrong"
    status, result = wordle.check_word()
    assert status is False


@patch('os.system')
def test_clear_windows(os_system):
    patch("os.name", return_value="nt")
    patch("os.system")
    patch("logger1.info")
    clear()
    os_system.assert_called_once_with("cls")
