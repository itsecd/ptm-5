import pytest

from unittest.mock import patch, mock_open
from main import ClientJournal

@pytest.fixture
def create_journal():
    return ClientJournal()

def test_client_exist(create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    assert create_journal.check_client_existence("John", "Doe") == True
    assert create_journal.check_client_existence("Johnny", "Depp") == False

def test_client_remove_successful(create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    assert create_journal.remove_client("John", "Doe") == True
    assert create_journal.clients == []

def test_client_remove_unsuccessful(create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    assert create_journal.remove_client("Johnny", "Depp") == False

def test_sort_clients_by_name(create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    create_journal.add_client("Emily", "Johnson", "2022-02-15", "2023-02-15", 12)
    create_journal.sort_clients_by_name()
    assert create_journal.clients == [
        {"name": "Emily", "surname": "Johnson", "purchase_date": "2022-02-15",
                 "end_date": "2023-02-15", "subscription_duration": 12},
        {"name": "John", "surname": "Doe", "purchase_date": "2022-01-01",
            "end_date": "2022-12-31", "subscription_duration": 1},
    ]

@pytest.mark.parametrize("old_name, old_surname, new_name, new_surname, expected", [
    ("John", "Doe", "Johnny", "Depp", True),
    ("Conor", "McGregor", "Khabib", "Nurmagomedov", False),
    ("Emily", "Johnson", "Emilia", "Clarck", True),
])
def test_change_name(old_name, old_surname, new_name, new_surname, expected, create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    create_journal.add_client("Emily", "Johnson", "2022-02-15", "2023-02-15", 12)
    assert create_journal.change_name(
        old_name, old_surname, new_name, new_surname) == expected

@pytest.mark.parametrize("name, surname, new_duration, expected", [
    ("John", "Doe", 5, True),
    ("Conor", "McGregor", 2, False),
    ("Emily", "Johnson", 12, True),
])
def test_change_subscription_duration(name, surname, new_duration, expected, create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    create_journal.add_client("Emily", "Johnson", "2022-02-15", "2023-02-15", 12)
    assert create_journal.change_subscription_duration(
        name, surname, new_duration) == expected

@patch("builtins.open", new_callable=mock_open, read_data="John,Doe,2022-01-01,2022-12-31,1\nEmily,Johnson,2022-02-15,2023-02-15,121")
def test_read_from_file(mock_file, create_journal):
    create_journal.read_from_file("clients.txt")
    assert create_journal.clients == [
        {"name": "John", "surname": "Doe", "purchase_date": "2022-01-01",
            "end_date": "2022-12-31", "subscription_duration": 1},
        {"name": "Emily", "surname": "Johnson", "purchase_date": "2022-02-15",
                 "end_date": "2023-02-15", "subscription_duration": 121}
    ]
    mock_file.assert_called_with("clients.txt", "r")

@patch("builtins.open", new_callable=mock_open)
def test_write_to_file(mock_file, create_journal):
    create_journal.add_client("John", "Doe", "2022-01-01", "2022-12-31", 1)
    create_journal.add_client("Emily", "Johnson", "2022-02-15", "2023-02-15", 12)
    create_journal.write_to_file('sorted_clients.txt')
    mock_file.assert_called_with('sorted_clients.txt', 'w')