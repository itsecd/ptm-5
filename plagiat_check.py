from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np


def rabin_karp(verifiable_text: str, original_text: str, pattern: int) -> bool:
    """
    Проверка хэша текстов (если они равны то текст украден).
    :param verifiable_text: Проверяемый текст.
    :param original_text: Оригинальный текст.
    :param pattern: Значение для хеша.
    """
    # вычисление хеш-функций
    MOD = 10 ** 9 + 7
    hash1 = sum([ord(char) * pattern ** i for i, char in enumerate(verifiable_text)]) % MOD
    hash2 = sum([ord(char) * pattern ** i for i, char in enumerate(original_text)]) % MOD
    # сравнение хеш-значений
    if hash1 == hash2:
        return True
    else:
        return False


def preprocess(text: str) -> str:
    """
    Меняет все буквы в тексте на прописные, убирает лишние знаки из текста.
    :param text: Изменяемый текст.
    """
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text


def extract_keywords(text: str) -> list:
    """
    Разделяет слова в тексте.
    :param text: Текст.
    """
    keywords = set(text.split())
    return keywords


def compute_tfidf(corpus: list) -> tuple:
    """
    Преобразует коллекцию текстовых документов в матрицу TF-IDF.
    :param corpus: Коллекция текстовых документов.
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(corpus)
    return vectors, vectorizer


def compute_cosine_similarity(text: str, tfidf_parametrs: tuple) -> np.ndarray:
    """
    Вычисляет косинусную схожесть между заданным текстом и коллекцией документов, используя ранее вычисленные векторы TF-IDF
    :param text: Заданный текст.
    :param tfidf_parametrs: Кортеж, содержащий параметры vectors и vectorizer.
    """
    vectors, vectorizer = tfidf_parametrs
    text_tfidf = vectorizer.transform([text])
    cosine_similarities = cosine_similarity(text_tfidf, vectors).flatten()
    return cosine_similarities


def knut_morris_pratt(verifiable_text: str, docs: list, threshold: float):
    """
    Находит наиболее похожий на verifiable_text текст в docs.
    :param verifiable_text: Проверяемый текст.
    :param docs: Список с потенциальными оригиналами.
    :param threshold: Порог, выше которого текст является плагиатом.
    """
    docs = [preprocess(doc) for doc in docs]
    verifiable_text = preprocess(verifiable_text)
    keywords = extract_keywords(verifiable_text)
    res = 0
    index = -1
    for i, d in enumerate(docs):
        if len(set(d.split()).intersection(keywords)) == 0:
            continue
        cosine_similarities = compute_cosine_similarity(d, compute_tfidf(docs))
        cosine_similarity_max = cosine_similarities.max()
        if cosine_similarity_max == 1:
            return 1, 1
        elif cosine_similarity_max > threshold:
            res = cosine_similarity_max
            index = i
    return res, index


def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return True
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return False


if __name__ == "__main__":
    print(extract_keywords("hello my world"))
