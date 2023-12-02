import pytest

from task import TaskList


def test_add_task():
    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2)
    assert len(task_list.tasks) == 1


def test_remove_task():
    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2)
    task_list.remove_task(0)
    assert len(task_list.tasks) == 0


def test_complete_task():
    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2)
    task_list.complete_task(0)
    assert task_list.tasks[0].completed is True


def test_save_and_load_from_file(tmp_path):
    file_path = tmp_path / "tasks.txt"

    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2)
    task_list.save_to_file(file_path)

    new_task_list = TaskList()
    new_task_list.load_from_file(file_path)

    assert len(new_task_list.tasks) == 1
    assert new_task_list.tasks[0].description == "Buy groceries"


def test_filter_tasks():
    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2)
    task_list.add_task("Read a book")
    task_list.add_task("Call mom", priority=3)

    task_list.complete_task(0)

    completed_tasks = task_list.filter_tasks(completed=True)
    assert len(completed_tasks) == 1
    assert completed_tasks[0].description == "Buy groceries"


def test_filter_by_tag():
    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2, tags=["shopping"])
    task_list.add_task("Read a book")
    task_list.add_task("Call mom", priority=3, tags=["family"])

    shopping_tasks = task_list.filter_by_tag("shopping")
    assert len(shopping_tasks) == 1
    assert shopping_tasks[0].description == "Buy groceries"


def test_save_and_load_from_json(tmp_path):
    file_path = tmp_path / "tasks.json"

    task_list = TaskList()
    task_list.add_task("Buy groceries", priority=2, tags=["shopping"])
    task_list.save_to_json(file_path)

    new_task_list = TaskList()
    new_task_list.load_from_json(file_path)

    assert len(new_task_list.tasks) == 1
    assert new_task_list.tasks[0].description == "Buy groceries"
    assert "shopping" in new_task_list.tasks[0].tags


# Run tests
if __name__ == "__main__":
    pytest.main(["-v", "–color=yes"])