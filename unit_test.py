# импортируем модуль, который мы хотим протестировать
import code

# импортируем pytest и mock для тестирования
import pytest
import mock

# параметризуем тесты для функции mean
@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 3),
    (np.array([-1, -2, -3, -4, -5]), -3),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 2.5)
])
def test_mean(x, expected):
    # проверяем, что функция mean возвращает ожидаемый результат
    assert code.mean(x) == expected

# параметризуем тесты для функции variance
@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 2),
    (np.array([-1, -2, -3, -4, -5]), 2),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 0.6666666666666666)
])
def test_variance(x, expected):
    # проверяем, что функция variance возвращает ожидаемый результат
    assert code.variance(x) == expected

# параметризуем тесты для функции std
@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 1.4142135623730951),
    (np.array([-1, -2, -3, -4, -5]), 1.4142135623730951),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 0.816496580927726)
])
def test_std(x, expected):
    # проверяем, что функция std возвращает ожидаемый результат
    assert code.std(x) == expected