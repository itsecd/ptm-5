# импортируем необходимые модули
import code_1
import pytest
import mock
import numpy as np
from code_1 import quantile, covariance, correlation


@pytest.fixture
def random_data():
    """Генерирует случайные данные из нормального распределения.

    Возвращает:
        x (np.array): массив из 100 случайных чисел с мат. ожиданием 10 и стандартным отклонением 5.
        y (np.array): массив из 100 случайных чисел с мат. ожиданием 10 и стандартным отклонением 5.
    """
    mean = 10
    std = 5
    size = 100
    x = np.random.normal(mean, std, size)
    y = np.random.normal(mean, std, size)
    return x, y


@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 3),
    (np.array([-1, -2, -3, -4, -5]), -3),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 2.5)
])
def test_mean(x, expected):
    """Проверяет, что функция code.mean возвращает правильное среднее значение массива.

    Аргументы:
        x (np.array): массив чисел, для которого нужно найти среднее.
        expected (float): ожидаемое среднее значение массива.

    Предполагает, что функция code.mean возвращает среднее значение массива.
    """
    assert code.mean(x) == expected


@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 2),
    (np.array([-1, -2, -3, -4, -5]), 2),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 0.6666666666666666)
])
def test_variance(x, expected):
    """Проверяет, что функция code.variance возвращает правильную дисперсию массива.

    Аргументы:
        x (np.array): массив чисел, для которого нужно найти дисперсию.
        expected (float): ожидаемая дисперсия массива.

    Предполагает, что функция code.variance возвращает дисперсию массива.
    """
    assert code_1.variance(x) == expected


@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 1.4142135623730951),
    (np.array([-1, -2, -3, -4, -5]), 1.4142135623730951),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 0.816496580927726)
])
def test_std(x, expected):
    """Проверяет, что функция code.std возвращает правильное стандартное отклонение массива.

    Аргументы:
        x (np.array): массив чисел, для которого нужно найти стандартное отклонение.
        expected (float): ожидаемое стандартное отклонение массива.

    Предполагает, что функция code.std возвращает стандартное отклонение массива.
    """
    assert code_1.std(x) == expected


@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 3),
    (np.array([-1, -2, -3, -4, -5]), -3),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 2.5),
    (np.array([1, 2, 3, 4]), 2.5),
    (np.array([-1, -2, -3, -4]), -2.5)
])
def test_median(x, expected):
    """Проверяет, что функция code.median возвращает правильную медиану массива.

    Аргументы:
        x (np.array): массив чисел, для которого нужно найти медиану.
        expected (float): ожидаемая медиана массива.

    Предполагает, что функция code.median возвращает медиану массива.
    """
    assert code_1.median(x) == expected


@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), np.array([1, 2, 3, 4, 5])),
    (np.array([-1, -2, -3, -4, -5]), np.array([-1, -2, -3, -4, -5])),
    (np.array([0]), np.array([0])),
    (np.array([1.5, 2.5, 3.5]), np.array([1.5, 2.5, 3.5])),
    (np.array([1, 2, 3, 4, 1]), np.array([1])),
    (np.array([-1, -2, -3, -4, -1]), np.array([-1])),
    (np.array([1, 2, 3, 4, 1, 2]), np.array([1, 2]))
])
def test_mode(x, expected):
    """Проверяет, что функция code.mode возвращает правильную моду массива.

    Аргументы:
        x (np.array): массив чисел, для которого нужно найти моду.
        expected (np.array): ожидаемая мода массива.

    Предполагает, что функция code.mode возвращает моду массива.
    """
    assert np.array_equal(code_1.mode(x), expected)


@pytest.fixture
def random_array():
    """Генерирует случайный массив из 10 целых чисел в диапазоне от -10 до 10.

    Возвращает:
        x (np.array): массив из 10 случайных целых чисел.
    """
    x = np.random.randint(-10, 10, 10)
    return x


def test_random_array(random_array):
    """Проверяет, что функции code.mean, code.variance и code.std совпадают с соответствующими функциями из numpy.

    Аргументы:
        random_array (np.array): случайный массив из 10 целых чисел.

    Предполагает, что функции code.mean, code.variance и code.std возвращают те же значения, что и np.mean, np.var и np.std.
    """
    assert code_1.mean(random_array) == np.mean(random_array)
    assert code_1.variance(random_array) == np.var(random_array)
    assert code_1.std(random_array) == np.std(random_array)


@pytest.fixture
def mock_mean():
    """Создает подделку функции code.mean, которая всегда возвращает 0.

    Возвращает:
        mock_mean (mock.Mock): подделка функции code.mean.
    """
    mock_mean = mock.Mock()
    mock_mean.return_value = 0
    return mock_mean

def test_variance_with_mock_mean(mock_mean):
    """Проверяет, что функция code.variance работает правильно, если функция code.mean подменена подделкой.

    Аргументы:
        mock_mean (mock.Mock): подделка функции code.mean.

    Предполагает, что функция code.variance возвращает 0, если функция code.mean подменена подделкой, которая всегда возвращает 0.
    """
    code_1.mean = mock_mean
    assert code_1.variance(np.array([1, 2, 3, 4, 5])) == 0
    mock_mean.assert_called_once_with(np.array([1, 2, 3, 4, 5]))

@pytest.mark.parametrize("p, expected", [
    (0, 0),
    (0.5, 10),
    (1, 20),
    (-0.1, ValueError),
    (1.1, ValueError)
])
def test_quantile(random_data, p, expected):
    """Проверяет, что функция code.quantile возвращает правильный квантиль массива.

    Аргументы:
        random_data (np.array): массив из 100 случайных чисел с мат. ожиданием 10 и стандартным отклонением 5.
        p (float): уровень квантиля, должен быть в диапазоне от 0 до 1.
        expected (float или Exception): ожидаемый квантиль массива или исключение, если p неверный.

    Предполагает, что функция code.quantile возвращает квантиль массива или выбрасывает исключение, если p неверный.
    """
    x, _ = random_data
    if isinstance(expected, Exception):
        with pytest.raises(expected):
            quantile(x, p)
    else:
        assert np.isclose(quantile(x, p), expected, atol=1)


def test_covariance(random_data):
    """Проверяет, что функция code.covariance возвращает правильную ковариацию двух массивов.

    Аргументы:
        random_data (np.array): два массива из 100 случайных чисел с мат. ожиданием 10 и стандартным отклонением 5.

    Предполагает, что функция code.covariance возвращает ковариацию двух массивов и совпадает с функцией np.cov.
    """
    x, y = random_data
    cov = covariance(x, y)
    np_cov = np.cov(x, y, ddof=0)[0, 1]
    assert np.isclose(cov, np_cov)


def test_correlation(random_data):
    """Проверяет, что функция code.correlation возвращает правильный коэффициент корреляции двух массивов.

    Аргументы:
        random_data (np.array): два массива из 100 случайных чисел с мат. ожиданием 10 и стандартным отклонением 5.

    Предполагает, что функция code.correlation возвращает коэффициент корреляции двух массивов и совпадает с функцией np.corrcoef.
    """
    x, y = random_data
    corr = correlation(x, y)
    np_corr = np.corrcoef(x, y)[0, 1]
    assert np.isclose(corr, np_corr)