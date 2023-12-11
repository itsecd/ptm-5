import pytest
import random

from main import To_do_list


@pytest.fixture
def to_do_list() -> To_do_list:
    """
    creating an instance of a class
    """
    return To_do_list()


def test_add_job(jobs: To_do_list) -> None:
    """
    test adding a jobs to the dictionary
    """
    jobs.add_job("test-job", 2)
    assert "test-job" in jobs.keys()


def test_delete_job(jobs: To_do_list) -> None:
    """
    test dleting a jobs from the dictionary
    """
    jobs.add_job("test-job-1", 10)
    jobs.delete_job("test-job-1")
    assert "test-job-1" not in jobs.keys()


def test_count_job(jobs: To_do_list) -> None:
    """
    test count of the number of jobs
    """
    for i in range(5):
        jobs.add_job(f"job-{i+1}", random.randint(1, 11))
    assert jobs.count_job == 5


@pytest.mark.parametrize("file", ["test_to_do_list.csv", "nonexistent_file.csv"])
def test_write_csv(jobs: To_do_list, file: str) -> None:
    """
    test entry of the dictionary in a csv file
    """
    jobs.add_job("job-1", 2)
    jobs.add_job("job-2", 4)
    jobs.write_csv(file)


@pytest.mark.parametrize("file", ["test_to_do_list.csv", "nonexistent_file.csv"])
def test_read_csv(jobs: To_do_list, file: str) -> None:
    """
    test reading into a dictionary from a csv file
    """
    jobs.read_csv(file)


def test_find_job(jobs: To_do_list) -> None:
    """
    test finding for a job in the dictionary
    """
    jobs.add_job("Go to dance", 7)
    jobs.add_job("Clear room", 10)
    jobs.add_job("Buy products", 5)
    assert jobs.find_job("Buy products") == True


def test_clear_dict(jobs: To_do_list) -> None:
    """
    test clear dictionary
    """
    jobs.add_job("job", 10)
    jobs.clear_list()
    assert not jobs.jobs
