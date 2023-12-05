import pytest
from plagiat_check import rabin_karp, knut_morris_pratt, boyer_moore, extract_keywords
from isb2 import frequency_bit_test, identical_consecutive_bit_test, unit_long_sequence_test


@pytest.mark.parametrize("bit_sequence, result", [("1110001100", 1.0)])
def test_frequency_bit_test(bit_sequence: str, result: float):
    assert frequency_bit_test(bit_sequence) == result


@pytest.mark.parametrize("bit_sequence, result", [("1110001100", 0.2059032107320683)])
def test_identical_consecutive_bit_test(bit_sequence: str, result: float):
    assert identical_consecutive_bit_test(bit_sequence) == result


@pytest.mark.parametrize("bit_sequence, result", [("00101110111111110000101100101000011110011001010011000000101001010101110100100100011111000110011" \
                   "101001000110010111100111111110011", 0.4304432330561101)])
def test_unit_long_sequence_test(bit_sequence: str, result: float):
    assert unit_long_sequence_test(bit_sequence) == result


@pytest.mark.parametrize(
    "verifiable_text, original_text, pattern",
    [
        ("hello", "hello", 10),
        ("hello", "world", 10),
        ("hello", "hello", 20),
        ("hello", "hello", 10),
    ]
)
def test_rabin_karp(verifiable_text: str, original_text: str, pattern: int):
    result = rabin_karp(verifiable_text, original_text, pattern)
    if verifiable_text == original_text:
        assert result is True
    else:
        assert result is False


@pytest.fixture
def sample_text():
    return "Python is a powerful language"


@pytest.mark.parametrize("expected", [{"Python", "is", "a", "powerful", "language"}])
def test_extract_keywords(sample_text, expected):
    assert extract_keywords(sample_text) == expected


@pytest.mark.parametrize("verifiable_text, docs, threshold, result", [("hello", ["dog", "hello", "house"], 0.5, (1, 1))])
def test_knut_morris_pratt(verifiable_text: str, docs: list, threshold: float, result: tuple):
    assert knut_morris_pratt(verifiable_text, docs, threshold) == result


@pytest.mark.parametrize(
    "text, pattern, expected",
    [("hello world", "hello", True),
     ("hello world", "cat", False),
     ("ABAAABCD", "ABB", False),
    ]
)
def test_boyer_moore(text: str, pattern: str, expected: bool):
    result = boyer_moore(text, pattern)
    assert result == expected