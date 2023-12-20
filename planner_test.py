import pytest

from planner import Planner


@pytest.fixture
def planner() -> Planner:
    """
    Функция для создания экземпляра Planner

    :return: Planner
    """
    return Planner()


def test_add_task():
    """
    Тест на добавление задачи в ежедневник
    """
    planner = Planner()
    planner.add_task("test time", "test task")
    assert len(planner.daily_planner["test time"]) == 1


def test_remove_task():
    """
    Тест на удаление задачи из ежедневника
    """
    planner = Planner()
    planner.add_task("test time", "test task")
    planner.remove_task("test time")
    assert len(planner.daily_planner) == 0
