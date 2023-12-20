import pytest
import logging
import csv
from Hotel import Client, Hotel
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, mock_open

@pytest.fixture
def store() -> Client:
    """
    The function for creating an instance ProductStore for testing
    Returns ProductStore
    """
    return Client()


@pytest.fixture
def product() -> Hotel:
    """
    The function for creating an instance ProductStore for testing
    Returns Product
    """
    return Hotel()


def test_add_client():
    hotel = Hotel('test.csv')
    client = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')

    with patch('Hotel.Hotel.append_client_to_csv') as mock_append:
        hotel.add_client(client)

    assert hotel.clients[0] == client
    mock_append.assert_called_once_with(client)

def test_append_client_to_csv():
    hotel = Hotel('test.csv')
    client = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')

    with patch('csv.writer') as mock_writer:
        hotel.append_client_to_csv(client)
    mock_writer.return_value.writerow.assert_called_once_with([client.first_name, client.last_name, client.check_in_date.strftime('%Y-%m-%d'), client.check_out_date.strftime('%Y-%m-%d'), client.room_class])

def test_remove_client():
    hotel = Hotel('test.csv')
    client1 = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')
    client2 = Client('Jane', 'Doe', datetime.now(), datetime.now(), 'Standard')
    hotel.add_client(client1)
    hotel.add_client(client2)

    hotel.remove_client('John', 'Doe')

    assert len(hotel.clients) == 1
    assert hotel.clients[0] == client2

def test_client_exists():
    hotel = Hotel('test.csv')
    client1 = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')
    client2 = Client('Jane', 'Doe', datetime.now(), datetime.now(), 'Standard')
    hotel.add_client(client1)
    hotel.add_client(client2)

    assert hotel.client_exists('John', 'Doe') == True
    assert hotel.client_exists('Jane', 'Smith') == False


def test_change_name():
    hotel = Hotel('test.csv')
    client1 = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')
    hotel.add_client(client1)

    hotel.change_name('John', 'Doe', 'Jane', 'Doe')

    assert hotel.clients[0].first_name == 'Jane'
    assert hotel.clients[0].last_name == 'Doe'

if __name__ == "__main__":
    pytest.main(["-v", "-color=yes"])