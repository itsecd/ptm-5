import pytest
import logging
import csv
from Hotel import Client, Hotel
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, mock_open
import os
import shutil

path_dict = {
    "root": "test_folder",
    "file_exists": os.path.join("test_folder", "clients.csv"),
    "file_non_exists": os.path.join("test_folder", "non_exists_clients.csv"),
}

@pytest.fixture()
def create_tmp_dir():
    """ fixture for craete test folder and then remove it"""

    if os.path.exists(path_dict["root"]):
        shutil.rmtree(path_dict["root"])

    os.mkdir(path_dict["root"])
    with open(path_dict["file_exists"], "w") as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Last Name', 'Check-in Date', 'Check-out Date', 'Room Class'])
            
    yield path_dict

    shutil.rmtree(path_dict["root"])




@pytest.fixture
def store() -> Client:
    """
    The function for creating an instance ProductStore for testing
    Returns ProductStore
    """
    return Client()


@pytest.fixture
def hotel() -> Hotel:
    """
    The function for creating an instance ProductStore for testing
    Returns Product
    """
    return Hotel()



@pytest.mark.parametrize("path, expected", [(path_dict["file_exists"], True), (path_dict["file_non_exists"], False)])
def test_write_to_csv(create_tmp_dir, path: str, expected: bool):
    """test cwrite_to_csv function"""
    htl = Hotel("tmp.csv")
    assert htl.write_to_csv(path) == expected


@pytest.mark.parametrize("path, expected", [(path_dict["file_exists"], True), (path_dict["file_non_exists"], False)])
def test_read_from_csv(create_tmp_dir, path: str, expected: bool):
    """test cwrite_to_csv function"""
    htl = Hotel("tmp.csv")
    assert htl.read_from_csv(path) == expected


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