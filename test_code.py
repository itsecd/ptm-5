import pytest
from main import MusicSubscription
from datetime import datetime


@pytest.fixture
def music_sub():
    return MusicSubscription()


@pytest.fixture
def mock_logger(mocker):
    return mocker.patch("main.logger")


@pytest.mark.parametrize("name, surname, subscription_start, subscription_end, months_subscribed", [
    ("Alice", "Smith", "01-01-2020", "31-12-2020", 12),
    ("Bob", "Jones", "15-03-2020", "14-03-2021", 11),
    ("Charlie", "Brown", "01-07-2020", "30-06-2021", 10)
])
def test_add_user(music_sub, mock_logger, name, surname, subscription_start, subscription_end, months_subscribed):
    music_sub.add_user(name, surname, subscription_start, subscription_end, months_subscribed)
    assert music_sub.users[-1] == {
        "name": name,
        "surname": surname,
        "subscription_start": datetime.strptime(subscription_start, "%d-%m-%Y"),
        "subscription_end": datetime.strptime(subscription_end, "%d-%m-%Y"),
        "months_subscribed": months_subscribed
    }
    mock_logger.debug.assert_called_with(f"User {name} {surname} added to the subscription list")


def test_remove_user(music_sub, mock_logger):
    music_sub.users = [
        {"name": "Alice", "surname": "Smith"},
        {"name": "Bob", "surname": "Jones"},
        {"name": "Charlie", "surname": "Brown"}
    ]
    music_sub.remove_user("Bob", "Jones")
    assert music_sub.users == [
        {"name": "Alice", "surname": "Smith"},
        {"name": "Charlie", "surname": "Brown"}
    ]
    mock_logger.debug.assert_called_with("User Bob Jones removed from the subscription list")


@pytest.fixture
def music_sub():
    return MusicSubscription()


@pytest.fixture
def mock_logger(mocker):
    return mocker.patch("main.logger")


@pytest.mark.parametrize("name, surname, expected", [
    ("Alice", "Smith", True),
    ("Bob", "Jones", True),
    ("Charlie", "Brown", True),
    ("David", "Green", False),
    ("Eve", "White", False)
])
def test_check_user_exists(music_sub, mock_logger, name, surname, expected):
    music_sub.users = [
        {"name": "Alice", "surname": "Smith"},
        {"name": "Bob", "surname": "Jones"},
        {"name": "Charlie", "surname": "Brown"}
    ]
    assert music_sub.check_user_exists(name, surname) == expected
    mock_logger.debug.assert_called_with(f"Checking if user {name} {surname} exists: {expected}")


def test_sort_users_by_name(music_sub, mock_logger):
    music_sub.users = [
        {"name": "Charlie", "surname": "Brown"},
        {"name": "Alice", "surname": "Smith"},
        {"name": "Bob", "surname": "Jones"}
    ]
    music_sub.sort_users_by_name()
    assert music_sub.users == [
        {"name": "Alice", "surname": "Smith"},
        {"name": "Bob", "surname": "Jones"},
        {"name": "Charlie", "surname": "Brown"}
    ]
    mock_logger.debug.assert_called_with("Users sorted by name")


def test_sort_users_by_subscription_months(music_sub, mock_logger):
    music_sub.users = [
        {"name": "Alice", "surname": "Smith", "months_subscribed": 12},
        {"name": "Bob", "surname": "Jones", "months_subscribed": 11},
        {"name": "Charlie", "surname": "Brown", "months_subscribed": 10}
    ]
    music_sub.sort_users_by_subscription_months()
    assert music_sub.users == [
        {"name": "Charlie", "surname": "Brown", "months_subscribed": 10},
        {"name": "Bob", "surname": "Jones", "months_subscribed": 11},
        {"name": "Alice", "surname": "Smith", "months_subscribed": 12}
    ]
    mock_logger.debug.assert_called_with("Users sorted by subscription months")


@pytest.mark.parametrize("name, surname, additional_months, expected_end_date, expected_months", [
    ("Alice", "Smith", 1, "31-01-2021", 13),
    ("Bob", "Jones", 2, "14-05-2021", 13),
    ("Charlie", "Brown", 3, "30-09-2021", 13)
])
def test_extend_subscription(music_sub, mock_logger, name, surname, additional_months, expected_end_date,
                             expected_months):
    music_sub.users = [
        {"name": "Alice", "surname": "Smith", "subscription_start": datetime(2020, 1, 1),
         "subscription_end": datetime(2020, 12, 31), "months_subscribed": 12},
        {"name": "Bob", "surname": "Jones", "subscription_start": datetime(2020, 3, 15),
         "subscription_end": datetime(2021, 3, 14), "months_subscribed": 11},
        {"name": "Charlie", "surname": "Brown", "subscription_start": datetime(2020, 7, 1),
         "subscription_end": datetime(2021, 6, 30), "months_subscribed": 10}
    ]
    music_sub.extend_subscription(name, surname, additional_months)
    for user in music_sub.users:
        if user["name"] == name and user["surname"] == surname:
            assert user["subscription_end"] == datetime.strptime(expected_end_date, "%d-%m-%Y")
            assert user["months_subscribed"] == expected_months
            mock_logger.debug.assert_called_with(
                f"User {name} {surname} extended subscription by {additional_months} months")


def test_read_from_csv(music_sub, mock_logger, mocker):
    file_path = "test.csv"
    file_content = """name,surname,subscription_start,subscription_end,months_subscribed
Alice,Smith,01-01-2020,31-12-2020,12
Bob,Jones,15-03-2020,14-03-2021,11
Charlie,Brown,01-07-2020,30-06-2021,10
"""
    mocker.patch("builtins.open", mocker.mock_open(read_data=file_content))
    music_sub.read_from_csv(file_path)
    assert music_sub.users == [
        {"name": "Alice", "surname": "Smith", "subscription_start": datetime(2020, 1, 1),
         "subscription_end": datetime(2020, 12, 31), "months_subscribed": 12},
        {"name": "Bob", "surname": "Jones", "subscription_start": datetime(2020, 3, 15),
         "subscription_end": datetime(2021, 3, 14), "months_subscribed": 11},
        {"name": "Charlie", "surname": "Brown", "subscription_start": datetime(2020, 7, 1),
         "subscription_end": datetime(2021, 6, 30), "months_subscribed": 10}
    ]
    mock_logger.info.assert_called_with(f"Read 3 users from {file_path}")
