# content of test_main.py
import pytest
import logging
from main import GymJournal
from datetime import date
import csv
import os
# create a mock logger to avoid writing to the actual log file
@pytest.fixture
def mock_logger(monkeypatch):
    logger = logging.getLogger('GymJournalLogger')
    monkeypatch.setattr(logger, 'info', lambda msg: None)
    monkeypatch.setattr(logger, 'warning', lambda msg: None)
    return logger

# create a GymJournal instance with some sample clients
@pytest.fixture
def gym_journal(mock_logger):
    gj = GymJournal()
    gj.clients = [
        {"first_name": "Alice", "last_name": "Smith", "months": 12},
        {"first_name": "Bob", "last_name": "Jones", "months": 6},
        {"first_name": "Charlie", "last_name": "Brown", "months": 3}
    ]
    return gj

# parametrize the test cases for changing name
@pytest.mark.parametrize("first_name, last_name, new_first_name, new_last_name, expected", [
    ("Alice", "Smith", "Anna", "Smith", True),
    ("Bob", "Jones", "Bob", "Johnson", True),
    ("Charlie", "Brown", "Chuck", "Brown", True),
    ("David", "Green", "Dan", "Green", False)
])
def test_change_name(gym_journal, first_name, last_name, new_first_name, new_last_name, expected):
    assert gym_journal.change_name(first_name, last_name, new_first_name, new_last_name) == expected

# parametrize the test cases for changing months
@pytest.mark.parametrize("first_name, last_name, new_months, expected", [
    ("Alice", "Smith", 24, True),
    ("Bob", "Jones", 12, True),
    ("Charlie", "Brown", 6, True),
    ("David", "Green", 3, False)
])
def test_change_months(gym_journal, first_name, last_name, new_months, expected):
    assert gym_journal.change_months(first_name, last_name, new_months) == expected

# parametrize the test cases for checking client
@pytest.mark.parametrize("first_name, last_name, expected", [
    ("Alice", "Smith", True),
    ("Bob", "Jones", True),
    ("Charlie", "Brown", True),
    ("David", "Green", False)
])
def test_check_client(gym_journal, first_name, last_name, expected):
    assert gym_journal.check_client(first_name, last_name) == expected

@pytest.fixture
def gym_journal(mock_logger):
    gj = GymJournal()
    gj.clients = [
        {"first_name": "Alice", "last_name": "Smith", "purchase_date": date(2023, 1, 1), "end_date": date(2023, 12, 31), "months": 12},
        {"first_name": "Bob", "last_name": "Jones", "purchase_date": date(2023, 2, 1), "end_date": date(2023, 7, 31), "months": 6},
        {"first_name": "Charlie", "last_name": "Brown", "purchase_date": date(2023, 3, 1), "end_date": date(2023, 5, 31), "months": 3}
    ]
    return gj

# parametrize the test cases for adding client
@pytest.mark.parametrize("first_name, last_name, purchase_date, end_date, months", [
    ("David", "Green", date(2023, 4, 1), date(2023, 9, 30), 6),
    ("Eve", "White", date(2023, 5, 1), date(2023, 10, 31), 6),
    ("Frank", "Black", date(2023, 6, 1), date(2023, 11, 30), 6)
])
def test_add_client(gym_journal, first_name, last_name, purchase_date, end_date, months):
    # get the initial number of clients
    initial_count = len(gym_journal.clients)
    # add a new client
    gym_journal.add_client(first_name, last_name, purchase_date, end_date, months)
    # check that the number of clients increased by one
    assert len(gym_journal.clients) == initial_count + 1
    # check that the new client is in the list
    assert gym_journal.check_client(first_name, last_name) == True
    # check that the new client has the correct attributes
    for client in gym_journal.clients:
        if client["first_name"] == first_name and client["last_name"] == last_name:
            assert client["purchase_date"] == purchase_date
            assert client["end_date"] == end_date
            assert client["months"] == months

# parametrize the test cases for removing client
@pytest.mark.parametrize("first_name, last_name, expected", [
    ("Alice", "Smith", True),
    ("Bob", "Jones", True),
    ("Charlie", "Brown", True),
    ("David", "Green", False)
])
def test_remove_client(gym_journal, first_name, last_name, expected):
    # get the initial number of clients
    initial_count = len(gym_journal.clients)
    # remove a client
    result = gym_journal.remove_client(first_name, last_name)
    # check that the result matches the expected value
    assert result == expected
    # check that the number of clients decreased by one if the removal was successful
    if result == True:
        assert len(gym_journal.clients) == initial_count - 1
    else:
        assert len(gym_journal.clients) == initial_count
    # check that the removed client is not in the list
    assert gym_journal.check_client(first_name, last_name) == False

# test the sorting by name method
def test_sort_by_name(gym_journal):
    # sort the clients by name
    gym_journal.sort_by_name()
    # check that the clients are in alphabetical order by first name and last name
    assert gym_journal.clients == sorted(gym_journal.clients, key=lambda x: (x["first_name"], x["last_name"]))

# test the sorting by months method
def test_sort_by_months(gym_journal):
    # sort the clients by months
    gym_journal.sort_by_months()
    # check that the clients are in ascending order by months
    assert gym_journal.clients == sorted(gym_journal.clients, key=lambda x: x["months"])

@pytest.fixture
def mock_logger(monkeypatch):
    logger = logging.getLogger('GymJournalLogger')
    monkeypatch.setattr(logger, 'info', lambda msg: None)
    monkeypatch.setattr(logger, 'error', lambda msg: None)
    return logger

# create a GymJournal instance with some sample clients
@pytest.fixture
def gym_journal(mock_logger):
    gj = GymJournal()
    gj.clients = [
        {"first_name": "Alice", "last_name": "Smith", "purchase_date": date(2023, 1, 1), "end_date": date(2023, 12, 31), "months": 12},
        {"first_name": "Bob", "last_name": "Jones", "purchase_date": date(2023, 2, 1), "end_date": date(2023, 7, 31), "months": 6},
        {"first_name": "Charlie", "last_name": "Brown", "purchase_date": date(2023, 3, 1), "end_date": date(2023, 5, 31), "months": 3}
    ]
    return gj

# create a temporary directory for testing the CSV files
@pytest.fixture
def temp_dir(tmpdir):
    return tmpdir

# test the reading from CSV file method
def test_read_from_csv(gym_journal, temp_dir):
    # create a sample CSV file with some clients
    file_path = temp_dir.join("test.csv")
    with open(file_path, "w", newline="") as file:
        fieldnames = [
            "first_name",
            "last_name",
            "purchase_date",
            "end_date",
            "months",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"first_name": "David", "last_name": "Green", "purchase_date": date(2023, 4, 1), "end_date": date(2023, 9, 30), "months": 6})
        writer.writerow({"first_name": "Eve", "last_name": "White", "purchase_date": date(2023, 5, 1), "end_date": date(2023, 10, 31), "months": 6})
        writer.writerow({"first_name": "Frank", "last_name": "Black", "purchase_date": date(2023, 6, 1), "end_date": date(2023, 11, 30), "months": 6})
    # get the initial number of clients
    initial_count = len(gym_journal.clients)
    # read the clients from the CSV file
    gym_journal.read_from_csv(file_path)
    # check that the number of clients increased by the number of rows in the CSV file
    assert len(gym_journal.clients) == initial_count + 3
    # check that the clients from the CSV file are in the list
    assert gym_journal.check_client("David", "Green") == True
    assert gym_journal.check_client("Eve", "White") == True
    assert gym_journal.check_client("Frank", "Black") == True

# test the writing to CSV file method
