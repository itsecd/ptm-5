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