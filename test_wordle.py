from collections import Counter
import pytest
from src.modules import words
from src.modules.wordle import Wordle


@pytest.fixture(scope="function")
def wordle() -> Wordle:
    """создание объекта Wordle"""
    return Wordle()


def test_constructor() -> None:
    """тест конструктора класса Wordle"""
    wordle = Wordle()
    assert wordle.words == words.five_letter_words
    assert wordle.valid_words == words.valid_words
    assert wordle.chosen_word in wordle.words


def test_select_word(wordle: Wordle) -> None:
    """тест метода выбора слова"""
    word = wordle._select_word()
    assert word in wordle.words


@pytest.mark.parametrize("word", ["aback", "DICED", "Shops"])
def test_is_correct_guess_for_correct_situation(wordle: Wordle, word: str) -> None:
    """тест метода проверки ответа, в случае корректоного ответа"""
    wordle.chosen_word = word.lower()
    wordle.user_guess = word
    assert wordle.is_correct_guess()


@pytest.mark.parametrize("word, user_guess", [("aback", "aboba"), ("diced", "AloHA"), ("shops", "rifle")])
def test_is_correct_guess_for_incorrect_situation(wordle: Wordle, word: str, user_guess: str) -> None:
    """тест метода проверки ответа пользователя, в случае некорректоного ответа"""
    wordle.chosen_word = word
    wordle.user_guess = user_guess
    assert not wordle.is_correct_guess()


def test_check_word_correct(wordle: Wordle) -> None:
    """тест метода проверки слова, когда ответ верный"""
    wordle.user_guess = wordle.chosen_word
    is_correct, user_guess_validated = wordle.check_word()
    assert is_correct
    assert user_guess_validated == [{'letter': letter, 'index': index, 'color': 'spring_green2'} for index, letter
                                    in enumerate(wordle.chosen_word)]


@pytest.mark.parametrize("word", ["aboba", "deqrt", "sjgnm"])
def test_check_word_incorrect(wordle: Wordle, word: str) -> None:
    """тест метода проверки слова, когда ответ неверный"""
    wordle.user_guess = word
    is_correct, user_guess_validated = wordle.check_word()
    assert not is_correct
    chosen_word_list = list(wordle.chosen_word)
    correct_count = dict(Counter(wordle.chosen_word))
    word_validated = list()
    for index, letter in enumerate(word):
        tmp = {'letter': letter, 'index': index}
        if letter == chosen_word_list[index]:
            tmp['color'] = 'spring_green2'
            correct_count[letter] -= 1
        else:
            tmp['color'] = 'grey84'
        word_validated.append(tmp)
    for index, letter in enumerate(word):
        if letter in chosen_word_list:
            if correct_count[letter] != 0:
                if word_validated[index]['color'] != "spring_green2":
                    word_validated[index]['color'] = 'orange1'
                    correct_count[letter] -= 1
    assert word_validated == user_guess_validated


def test_get_user_guess_valid(wordle: Wordle, capsys, monkeypatch) -> None:
    """тест метода получения ввода пользователя в случае корректного ввода"""
    monkeypatch.setattr('builtins.input', lambda _: "hello")
    wordle.get_user_guess(remaining=1)
    captured = capsys.readouterr()
    assert "" in captured.out
