import pytest
import os
from unittest.mock import patch

from main import StudentJournal


@pytest.fixture
def journal() -> StudentJournal:
    return StudentJournal()


def test_check_student_by_id(journal: StudentJournal) -> None:
    """
    Test to check if a student with a specific ID exists in the journal.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    assert journal.check_student_by_id("1") == True
    assert journal.check_student_by_id("2") == False


def test_add_student(journal: StudentJournal) -> None:
    """
    Test to add a student to the journal.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    assert len(journal.students) == 1


def test_remove_student(journal: StudentJournal) -> None:
    """
    Test to remove a student from the journal.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.remove_student("1")
    assert len(journal.students) == 0


def test_sort_by_average_grade(journal: StudentJournal) -> None:
    """
    Test to sort students in the journal by their average grade.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("2", "2000-01-01", 2.5, 15, 20, True)
    journal.add_student("3", "2000-01-01", 5.0, 15, 20, True)
    journal.sort_by_average_grade(reverse=False)
    assert journal.students[0]["id"] == "2"


def test_sort_by_attended_lectures(journal: StudentJournal) -> None:
    """
    Test for the sort_by_attended_lectures() function. It checks the correctness of sorting
    students by the number of attended lectures.

    Args:
        journal (StudentJournal): An instance of the StudentJournal class.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("2", "2000-01-01", 3.5, 12, 20, True)
    journal.add_student("3", "2000-01-01", 2.5, 15, 20, True)
    journal.sort_by_attended_lectures(reverse=True)
    assert journal.students[0]["id"] == "3"


def test_is_allowed_to_exam(journal: StudentJournal) -> None:
    """
    Test for the is_allowed_to_exam() function. It checks if the function correctly
    returns the value that allows a student to take the exam or not.

    Args:
        journal (StudentJournal): An instance of the StudentJournal class.
    """
    journal.add_student("1", "2000-01-01", 4.0, 9, 20, True)
    assert journal.is_allowed_to_exam("1") == False


def test_update_average_grade(journal: StudentJournal) -> None:
    """
    Test for the update_average_grade() function. It checks if the function correctly
    updates the average grade of a student.

    Args:
        journal (StudentJournal): An instance of the StudentJournal class.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.update_average_grade("1", 3.5)
    assert journal.students[0]["average_grade"] == 3.5


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_read_from_csv(journal: StudentJournal, filename: str) -> None:
    """
    Test for the read_from_csv() function. It checks if the function correctly reads the
    student data from a CSV file.

    Args:
        journal (StudentJournal): An instance of the StudentJournal class.
        filename (str): Name of the test file to read from.
    """
    journal.read_from_csv(filename)


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_write_to_csv(journal: StudentJournal, filename: str) -> None:
    """
    Test for the write_to_csv() function. It checks if the function correctly writes the
    student data to a CSV file.

    Args:
        journal (StudentJournal): An instance of the StudentJournal class.
        filename (str): Name of the test file to write to.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("3", "2000-01-01", 4.0, 10, 20, True)
    journal.add_student("2", "2000-01-01", 3.5, 15, 20, True)
    journal.write_to_csv(filename)

    # Check if file exists
    assert os.path.exists(filename)

    # Check if file is not empty
    assert os.path.getsize(filename) > 0


@patch("main.logger")
def test_add_student_with_logger_mock(mock_logger, journal: StudentJournal) -> None:
    """
    Test for the add_student() function with a mocked logger object. It checks if the
    add_student() function correctly logs the added student's ID through the logger.

    Args:
        mock_logger: Mocked logger object.
        journal (StudentJournal): An instance of the StudentJournal class.
    """
    journal.add_student("1", "2000-01-01", 4.0, 10, 20, True)
    assert len(journal.students) == 1
    mock_logger.info.assert_called_with("Client added: 1")


@patch("main.logger")
def test_remove_student(mock_logger, journal: StudentJournal) -> None:
    """
    Test for the remove_student() function with a mocked logger object. It checks if the
    remove_student() function correctly logs the removed student's ID through the logger.

    Args:
        mock_logger: Mocked logger object.
        journal (StudentJournal): An instance of the StudentJournal class.
    """
    journal.add_student("22", "2000-01-01", 4.0, 10, 20, True)
    journal.remove_student("22")
    assert len(journal.students) == 0
    mock_logger.info.assert_called_with("Client removed: 22")
