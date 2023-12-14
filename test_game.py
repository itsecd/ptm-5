import pytest
from game import results, user_points, computer_points

# Мокируем глобальные переменные
@pytest.fixture(autouse=True)
def reset_game_state(monkeypatch):
    """сброс очков перед каждым тестом
    """
    monkeypatch.setattr('game.user_points', 0)
    monkeypatch.setattr('game.computer_points', 0)


@pytest.mark.parametrize("comp_choice, user_input, exp_user_points, exp_comp_points", [
    ('Snake', 's', 0, 0), 
    ('Water', 'w', 0, 0),
    ('Gun', 'g', 0, 0),   
    ('Snake', 'g', 1, 0),
    ('Water', 's', 1, 0), 
    ('Gun', 'w', 1, 0),   
    ('Snake', 'w', 0, 1), 
    ('Water', 'g', 0, 1), 
    ('Gun', 's', 0, 1),  
])
def test_game_results(comp_choice, user_input, exp_user_points, exp_comp_points, monkeypatch):
    """тестирование различных сценариев игры и проверка очков

    Args:
        comp_choice (_type_): выбор компьютера
        user_input (_type_): выбор пользователя
        exp_user_points (_type_): ожидаемое количество очков пользователя
        exp_comp_points (_type_): ожидаемое количество очков компьютера
    """
    monkeypatch.setattr('game.computer_choice', comp_choice)
    monkeypatch.setattr('game.user_choice', user_input)
    
    results()
    assert user_points == exp_user_points
    assert computer_points == exp_comp_points

def test_maximum_score(monkeypatch):
    """проверка на максимальное значение очков

    """
    max_rounds = 5
    monkeypatch.setattr('game.computer_choice', 'Gun')
    monkeypatch.setattr('game.user_choice', 's')
    for _ in range(max_rounds):
        results()
    assert computer_points == max_rounds
    assert user_points == 0
