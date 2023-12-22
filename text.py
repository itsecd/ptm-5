class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.words = self._preprocess(text)

    def _preprocess(self, text):
        # Удаляем знаки препинания и приводим к нижнему регистру
        return [word.lower() for word in text.split()]

    def word_frequency(self):
        # Подсчитываем частоту каждого слова в тексте
        frequency = {}
        for word in self.words:
            frequency[word] = frequency.get(word, 0) + 1
        return frequency

    def most_common_words(self, n):
        # Возвращаем n наиболее часто встречающихся слов
        frequency = self.word_frequency()
        return sorted(frequency, key=frequency.get, reverse=True)[:n]

    def generate_tag_cloud(self):
        # Генерируем простое облако тегов
        frequency = self.word_frequency()
        cloud = ""
        for word in frequency:
            cloud += f"{word} " * frequency[word]
        return cloud.strip()

    def transform_text(self, transform_function):
        # Трансформируем текст согласно пользовательской функции
        return ' '.join([transform_function(word) for word in self.words])