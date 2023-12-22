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

# Параметризованный тест для проверки наиболее частых слов
@pytest.mark.parametrize("n, expected", [(2, ["hello", "world"]), (3, ["hello", "world", "the"])])
def test_most_common_words(processor, n, expected):
    assert processor.most_common_words(n) == expected

# Тест для генерации облака тегов 
def test_generate_tag_cloud(processor):
    cloud = processor.generate_tag_cloud()
    assert "hello" in cloud
    assert cloud.count("world") == 2

# Тест для трансформации текста
def test_transform_text(processor):
    transformed = processor.transform_text(lambda x: x.upper())
    assert transformed == "HELLO WORLD HELLO UNIVERSE THE WORLD IS BEAUTIFUL"

