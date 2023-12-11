import pytest
import random

from main import To_do_list


@pytest.fixture
def to_do_list() -> To_do_list:
    """
    creating an instance of a class
    """
    return To_do_list()


def test_add_job(to_do_list: To_do_list) -> None:
    """
    test adding a jobs to the dictionary
    """
    to_do_list.add_job("test-job", 2)
    assert "test-job" in to_do_list.jobs.keys()


def test_delete_job(to_do_list: To_do_list) -> None:
    """
    test dleting a jobs from the dictionary
    """
    to_do_list.add_job("test-job-1", 10)
    to_do_list.delete_job("test-job-1")
    assert "test-job-1" not in to_do_list.jobs.keys()


def test_count_job(to_do_list: To_do_list) -> None:
    """
    test count of the number of jobs
    """
    for i in range(5):
        to_do_list.add_job(f"job-{i+1}", random.randint(1, 11))
    assert to_do_list.count_job == 5


@pytest.mark.parametrize("file", ["test_to_do_list.csv", "nonexistent_file.csv"])
def test_write_csv(to_do_list: To_do_list, file: str) -> None:
    """
    test entry of the dictionary in a csv file
    """
    to_do_list.add_job("job-1", 2)
    to_do_list.add_job("job-2", 4)
    to_do_list.write_csv(file)


@pytest.mark.parametrize("file", ["test_to_do_list.csv", "nonexistent_file.csv"])
def test_read_csv(to_do_list: To_do_list, file: str) -> None:
    """
    test reading into a dictionary from a csv file
    """
    to_do_list.read_csv(file)


def test_find_job(to_do_list: To_do_list) -> None:
    """
    test finding for a job in the dictionary
    """
    to_do_list.add_job("Go to dance", 7)
    to_do_list.add_job("Clear room", 10)
    to_do_list.add_job("Buy products", 5)
    assert to_do_list.find_job("Buy products") == True


def test_clear_dict(to_do_list: To_do_list) -> None:
    """
    test clear dictionary
    """
    to_do_list.add_job("job", 10)
    to_do_list.clear_list()
    assert not to_do_list.jobs
