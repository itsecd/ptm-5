import pytest
from music import MusicSubscription
from datetime import datetime 
@pytest.fixture
def subscription():
    return MusicSubscription()

def test_add_user(subscription):
    subscription.add_user("Иван", "Иванов", "01-01-2023", "01-07-2023", 6)
    assert subscription.users[-1]["name"] == "Иван"


def test_remove_user(subscription):
    subscription.add_user("Иван", "Иванов", "01-01-2023", "01-07-2023", 6)
    subscription.remove_user("Иван", "Иванов")
    assert not subscription.check_user_exists("Иван", "Иванов")
def test_update_user_surname(subscription):
    subscription.add_user("Иван", "Иванов", "01-01-2023", "01-07-2023", 6)
    subscription.update_user_surname("Иванов", "Петров")
    assert subscription.users[0]["surname"] == "Петров"

def test_extend_subscription(subscription):
    subscription.add_user("Мария", "Иванова", "01-01-2023", "01-04-2023", 3)
    subscription.extend_subscription("Мария", "Иванова", 2)
    assert subscription.users[0]["months_subscribed"] == 5
    assert subscription.users[0]["subscription_end"] == datetime(2023, 6, 1)


def test_check_user_exists(subscription):
    subscription.add_user("Сергей", "Сергеев", "01-01-2023", "01-07-2023", 6)
    assert subscription.check_user_exists("Сергей", "Сергеев")
    assert not subscription.check_user_exists("Алексей", "Алексеев")