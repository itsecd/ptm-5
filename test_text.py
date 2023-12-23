import pytest
from text import TextProcessor

@pytest.fixture
def processor():
    text = "Hello world! Hello universe. The world is beautiful."
    return TextProcessor(text)

# Тест для проверки частоты слов
def test_word_frequency(processor):
    frequency = processor.word_frequency()
    assert frequency["hello"] == 2
    assert frequency["world"] == 2
    assert frequency["the"] == 1

def test_most_common_words_one(processor):
    # Проверяем, возвращается ли одно самое частое слово
    assert processor.most_common_words(1) == ["hello"]

def test_most_common_words_two(processor):
    # Проверяем, возвращаются ли два самых частых слова
    assert processor.most_common_words(2) == ["hello", "world"]

# Тест для генерации облака тегов 
def test_generate_tag_cloud(processor):
    cloud = processor.generate_tag_cloud()
    assert "hello" in cloud
    assert cloud.count("world") == 2

# Тест для трансформации текста
def test_transform_text(processor):
    transformed = processor.transform_text(lambda x: x.upper())
    assert transformed == "HELLO WORLD HELLO UNIVERSE THE WORLD IS BEAUTIFUL"

