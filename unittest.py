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

# параметризуем тесты для функции median
@pytest.mark.parametrize("x, expected", [
    (np.array([1, 2, 3, 4, 5]), 3),
    (np.array([-1, -2, -3, -4, -5]), -3),
    (np.array([0]), 0),
    (np.array([1.5, 2.5, 3.5]), 2.5),
    (np.array([1, 2, 3, 4]), 2.5),
    (np.array([-1, -2, -3, -4]), -2.5)
])
def test_median(x, expected):
    # проверяем, что функция median возвращает ожидаемый результат
    assert code.median(x) == expected
    
# параметризуем тесты для функции mode
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
    # проверяем, что функция mode возвращает ожидаемый результат
    assert np.array_equal(code.mode(x), expected)
    
# создаем фикстуру для генерации случайных массивов
@pytest.fixture
def random_array():
    # генерируем случайный массив из 10 элементов в диапазоне от -10 до 10
    x = np.random.randint(-10, 10, 10)
    # возвращаем массив
    return x

# тестируем функции mean, variance и std на случайных массивах
def test_random_array(random_array):
    # проверяем, что функции mean, variance и std возвращают правильные значения
    assert code.mean(random_array) == np.mean(random_array)
    assert code.variance(random_array) == np.var(random_array)
    assert code.std(random_array) == np.std(random_array)
    
# создаем фикстуру для мокирования функции mean
@pytest.fixture
def mock_mean():
    # создаем мок-объект для функции mean
    mock_mean = mock.Mock()
    # задаем возвращаемое значение для функции mean
    mock_mean.return_value = 0
    # возвращаем мок-объект
    return mock_mean

# тестируем функцию variance с мокированной функцией mean
def test_variance_with_mock_mean(mock_mean):
    # подменяем функцию mean на мок-объект
    code.mean = mock_mean
    # проверяем, что функция variance возвращает ноль, если функция mean возвращает ноль
    assert code.variance(np.array([1, 2, 3, 4, 5])) == 0
    # проверяем, что функция mean была вызвана один раз с правильным аргументом
    mock_mean.assert_called_once_with(np.array([1, 2, 3, 4, 5]))