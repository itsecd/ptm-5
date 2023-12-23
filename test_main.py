import pytest
import os
from main import ProbabilityCalculator

@pytest.fixture
def probability_calculator():
    return ProbabilityCalculator()

def test_solve_dice_sum_problem(probability_calculator):
    # Проверяем, что функция solve_dice_sum_problem возвращает ожидаемое значение
    target_sum = 7
    num_dice = 2
    expected_result = 6/36  
    result = probability_calculator.solve_dice_sum_problem(target_sum, num_dice)
    assert result == pytest.approx(expected_result, rel=1e-2)

def test_plot_dice_sum_probability(probability_calculator):
    # Проверяем, что функция plot_dice_sum_probability не вызывает ошибок
    num_dice = 2
    try:
        probability_calculator.plot_dice_sum_probability(num_dice)
    except Exception as e:
        pytest.fail(f"plot_dice_sum_probability raised an exception: {str(e)}")

def test_read_input_file(probability_calculator):
    # Создаем временный файл для теста
    test_input_filename = "test_input.txt"
    with open(test_input_filename, "w") as test_file:
        test_file.write("Test input data")
    
    # Проверяем, что функция read_input_file читает содержимое файла
    result = probability_calculator.read_input_file(test_input_filename)
    assert result == ["Test input data"]
    
    # Удаляем временный файл
    os.remove(test_input_filename)

def test_write_output_file(probability_calculator):
    # Создаем временный файл для теста
    test_output_filename = "test_output.txt"
    
    # Проверяем, что функция write_output_file записывает данные в файл
    content = ["Test output data"]
    probability_calculator.write_output_file(test_output_filename, content)
    
    # Проверяем, что файл был создан и содержит правильные данные
    with open(test_output_filename, "r") as test_file:
        result = test_file.read()
    assert result == "Test output data"
    
    # Удаляем временный файл
    os.remove(test_output_filename)

@pytest.fixture
def probability_calculator():
    return ProbabilityCalculator()

# Тесты для функций ProbabilityCalculator
@pytest.mark.parametrize('dice_number, target_number, expected_probability', [(1, 3, 1/6), (2, 5, 0.16666666666666666)])
def test_probability_of_dice_roll(probability_calculator, dice_number, target_number, expected_probability):
    result = probability_calculator.dice_roll_probability.probability_of_dice_roll(dice_number, target_number)
    assert result == pytest.approx(expected_probability, rel=1e-2)

#pytest test.py


@pytest.mark.parametrize('target_sum, expected_probability', [(7, 6/36), (8, 5/36)])
def test_probability_of_dice_combination(probability_calculator, target_sum, expected_probability):
    result = probability_calculator.dice_combination_probability.probability_of_dice_combination(target_sum)
    assert result == pytest.approx(expected_probability, rel=1e-2)

# Создаем стаб-объект ProbabilityCalculator
class ProbabilityCalculatorStub(ProbabilityCalculator):
    def probability_of_dice_combination(self, target_sum):
        if target_sum == 7:
            return 0.2
        elif target_sum == 8:
            return 0.1
        else:
            return 0.0

@pytest.fixture
def probability_calculator_stub():
    return ProbabilityCalculatorStub() 

def test_probability_of_dice_combination_with_stub(probability_calculator_stub):
    # Вызываем функцию с использованием стаб-объекта
    result = probability_calculator_stub.dice_combination_probability.probability_of_dice_combination(7)
    # Проверяем, что результат равен ожидаемому значению
    assert result == 0.2

    result = probability_calculator_stub.dice_combination_probability.probability_of_dice_combination(8)
    assert result == 0.1

    result = probability_calculator_stub.dice_combination_probability.probability_of_dice_combination(9)
    assert result == 0.0
