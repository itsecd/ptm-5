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



# @pytest.mark.parametrize("filename", ['test_1.csv', 'test_2.csv'])
# def test_read_from_csv(filename):
#     hotel = Hotel('test.csv')

#     client1 = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')
#     client2 = Client('Jane', 'Doe', datetime.now(), datetime.now(), 'Standard')
#     hotel.add_client(client1)
#     hotel.add_client(client2)

#     with patch('builtins.open', new_callable=mock_open, read_data='John,Doe,2023-01-01,2023-01-10,Deluxe\nJane,Doe,2023-01-02,2023-01-11,Standard') as mock_file:
#         hotel.read_from_csv(filename)
#     print(hotel.clients)
#     assert len(hotel.clients) == 2
#     assert hotel.clients[0].first_name == 'John'
#     assert hotel.clients[0].last_name == 'Doe'
#     assert hotel.clients[1].first_name == 'Jane'
#     assert hotel.clients[1].last_name == 'Doe'


# @pytest.mark.parametrize("filename", ['test1.csv', 'test2.csv'])
# def test_write_to_csv(filename):
#     hotel = Hotel('test.csv')
#     client1 = Client('John', 'Doe', datetime.now(), datetime.now(), 'Deluxe')
#     client2 = Client('Jane', 'Doe', datetime.now(), datetime.now(), 'Standard')
#     hotel.add_client(client1)
#     hotel.add_client(client2)

#     with patch('builtins.open', new_callable=mock_open) as mock_file:
#         hotel.write_to_csv(filename)

#     mock_file.assert_called_once_with(filename, 'w')
#     mock_file.return_value.__enter__.return_value.writerow.assert_any_call(['First Name', 'Last Name', 'Check-in Date', 'Check-out Date', 'Room Class'])
#     mock_file.return_value.__enter__.return_value.writerow.assert_any_call([client1.first_name, client1.last_name, client1.check_in_date.strftime('%Y-%m-%d'), client1.check_out_date.strftime('%Y-%m-%d'), client1.room_class])
#     mock_file.return_value.__enter__.return_value.writerow.assert_any_call([client2.first_name, client2.last_name, client2.check_in_date.strftime('%Y-%m-%d'), client2.check_out_date.strftime('%Y-%m-%d'), client2.room_class])
    

if __name__ == "__main__":
    pytest.main(["-v", "-color=yes"])