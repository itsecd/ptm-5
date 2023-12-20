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
    planner.add_task("test task", "test time")
    assert len(planner.daily_planner["test time"]) == 1


def test_remove_task():
    """
    Тест на удаление задачи из ежедневника
    """
    planner = Planner()
    planner.add_task("test task", "test time")
    planner.remove_task("test task", "test time")
    assert len(planner.daily_planner) == 0


def test_multi_remove_tasks():
    """
    Тест на удаление нескольких задач из ежедневника
    """
    planner = Planner()
    planner.add_task("test task 1", "test time 1")
    planner.add_task("test task 2", "test time 1")
    planner.add_task("test task 3", "test time 2")
    planner.add_task("test task 4", "test time 2")
    planner.add_task("test task 5", "test time 3")
    planner.remove_task("test task 1", "test time 1")
    planner.remove_task("test task 2", "test time 1")
    planner.remove_task("test task 3", "test time 2")
    planner.remove_task("test task 4", "test time 2")
    assert len(planner.daily_planner) == 1
    assert planner.view_tasks("test time 1") == "\nНа test time 1 нет дел"
    assert planner.view_tasks("test time 2") == "\nНа test time 2 нет дел"


def test_delete_all_tasks():
    """
    Тест на удаление всех задач из ежедневника
    """
    planner = Planner()
    planner.add_task("test task 1", "test time 1")
    planner.add_task("test task 2", "test time 2")
    planner.add_task("test task 3", "test time 3")
    planner.add_task("test task 4", "test time 4")
    planner.add_task("test task 5", "test time 5")
    planner.delete_all_tasks()
    assert len(planner.daily_planner) == 0


@pytest.mark.parametrize("time, expected_result", [
    ("test time 1", "\nНа test time 1 нет дел"),
    ("test time 2", "\nДела на test time 2:\n- test task 1\n- test task 2\n- test task 3")
])
def test_view_tasks(time, expected_result):
    planner = Planner()
    planner.add_task("test task 1", "test time 1")
    planner.remove_task("test task 1", "test time 1")
    planner.add_task("test task 1", "test time 2")
    planner.add_task("test task 2", "test time 2")
    planner.add_task("test task 3", "test time 2")
    assert planner.view_tasks(time) == expected_result


@pytest.mark.parametrize("time, expected_result", [
    ("test time 1", "Отчет за период с test time 1 по test time 1\n\n"
                    "test time 1:\n- test task 1\n- test task 2\n"),
    ("test time 3", "За период с test time 3 по test time 3 нет дел\n")
])
def test_generate_report(time, expected_result):
    planner = Planner()
    planner.add_task("test task 1", "test time 1")
    planner.add_task("test task 2", "test time 1")
    assert planner.generate_report(time, time) == expected_result


def test_save_load_report(tmp_path):
    """
    Тест на экспорт/импорт информации в/из txt файла
    """
    file_path = tmp_path / "report_1.txt"
    planner = Planner()
    planner.add_task("test task 1", "test time 1")
    report = planner.generate_report("test time 1", "test time 1")
    planner.save_to_txt(file_path, report)
    new_planner = Planner()
    new_planner.load_from_txt(file_path)
    assert len(new_planner.daily_planner.items()) == 1
    assert new_planner.daily_planner["test time 1"] == ["test task 1"]
