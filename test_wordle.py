import pytest
from unittest.mock import patch, MagicMock

from wordle import Wordle  
from words import five_letter_words


@pytest.fixture
def wordle_instance() -> Wordle:
    """экземпляр класса для тестирования"""
    logger_mock = MagicMock()
    with patch('wordle.words', {'five_letter': ['apple'], 'valid_word': []}):
        return Wordle(logger_mock)


def test_select_word(wordle_instance):
    """_select_word возвращает одно из пятибуквенных слов"""
    word = wordle_instance._select_word()
    assert isinstance(word, str)
    assert word in five_letter_words 


@pytest.mark.parametrize("chosen_word, user_guess, expected_result", 
                        [('apple', 'apple', True),
                        ('apple', 'orange', False),
                        ('apple', 'apply', False)])
def test_is_correct_guess(wordle_instance, chosen_word, user_guess, expected_result):
    """is_correct_guess - совпадают ли выбранное слово и введенное пользователем"""
    wordle_instance.chosen_word = chosen_word
    wordle_instance.user_guess = user_guess
    assert wordle_instance.is_correct_guess() == expected_result


def test_check_word(wordle_instance):
    """check_word возвращает правильный результат и проверяет все буквы"""
    wordle_instance.chosen_word = 'apple'
    wordle_instance.user_guess = 'apply'
    is_correct, user_guess_validated = wordle_instance.check_word()

    assert not is_correct
    assert len(user_guess_validated) == 5 
    assert all(isinstance(item, dict) for item in user_guess_validated)


def test_get_user_guess_valid_length(wordle_instance):
    """get_user_guess корректно обрабатывает правильную длину введенного пользователем слова."""
    with patch('rich.prompt.Prompt.ask', return_value='apple'): # замена ввода пользователя
        wordle_instance.get_user_guess(remaining=3)

    assert wordle_instance.user_guess == 'apple'


def test_get_user_guess_invalid_length(wordle_instance):
    """get_user_guess - повторный запрос при неверной длине слова"""
    with patch('rich.prompt.Prompt.ask', side_effect=['orange', 'apple']):
        wordle_instance.get_user_guess(remaining=3)

    assert wordle_instance.user_guess == 'apple'


def test_get_user_guess_invalid_word(wordle_instance):
    """get_user_guess - повторный запрос при вводе недопустимого слова"""
    with patch('rich.prompt.Prompt.ask', side_effect=['apply', 'apple']):
        wordle_instance.get_user_guess(remaining=3)

    assert wordle_instance.user_guess == 'apple'