import pytest
import os
from unittest.mock import patch

from main import StudentJournal


@pytest.fixture
def journal() -> StudentJournal:
    return StudentJournal()


def test_check_student_by_id(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    assert journal.check_student_by_id("1") == True
    assert journal.check_student_by_id("2") == False


def test_add_student(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    assert len(journal.students) == 1


def test_remove_student(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.remove_student("1")
    assert len(journal.students) == 0


def test_sort_by_average_grade(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("2", "2000-01-01", 2.5, 15, 20, True)
    journal.add_student("3", "2000-01-01", 5.0, 15, 20, True)
    journal.sort_by_average_grade(reverse=False)
    assert journal.students[0]["id"] == "2"


def test_sort_by_attended_lectures(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("2", "2000-01-01", 3.5, 12, 20, True)
    journal.add_student("3", "2000-01-01", 2.5, 15, 20, True)
    journal.sort_by_attended_lectures(reverse=True)
    assert journal.students[0]["id"] == "3"


def test_is_allowed_to_exam(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 9, 20, True)
    assert journal.is_allowed_to_exam("1") == False


def test_update_average_grade(journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.update_average_grade("1", 3.5)
    assert journal.students[0]["average_grade"] == 3.5


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_read_from_csv(journal: StudentJournal, filename: str):
    journal.read_from_csv(filename)


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_write_to_csv(journal: StudentJournal, filename: str):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("3", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("2", "2000-01-01", 3.5, 15, 20, True)
    journal.write_to_csv(filename)

    # Check if file exists
    assert os.path.exists(filename)

    # Check if file is not empty
    assert os.path.getsize(filename) > 0


@patch("main.logger")
def test_add_student_with_logger_mock(mock_logger, journal: StudentJournal):
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    assert len(journal.students) == 1
    mock_logger.info.assert_called_with("Client added: 1")


@patch("main.logger")
def test_remove_student(mock_logger, journal: StudentJournal):
    journal.add_student("22", "2000-01-01", 4.0, 10, 20, True)
    journal.remove_student("22")
    assert len(journal.students) == 0
    mock_logger.info.assert_called_with("Client removed: 22")


if __name__ == "__main__":
    pytest.main(["-v", "-color=yes"])