import pytest

from unittest.mock import patch, mock_open
from main import CarServiceList

@pytest.fixture
def create_journal():
    return CarServiceList()

def test_car_exist(create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    assert create_journal.check_car_existence("Mazda", "Miata") == True
    assert create_journal.check_car_existence("Ford", "Focus") == False

def test_car_remove_successful(create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    assert create_journal.remove_car("Mazda", "Miata") == True
    assert create_journal.cars == []

def test_car_remove_unsuccessful(create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    assert create_journal.remove_car("Ford", "Focus") == False

def test_sort_cars_by_brand(create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    create_journal.add_car("BMW", "E320", "5000", "8732", 4)
    create_journal.sort_cars_by_brand()
    assert create_journal.cars == [
        {"brand": "BMW", "model": "E320", "mileage_last_checkup": "5000",
                 "mileage_current_checkup": "8732", "duration": 4},
        {"brand": "Mazda", "model": "Miata", "mileage_last_checkup": "10500",
            "mileage_current_checkup": "11000", "duration": 1},
    ]

@pytest.mark.parametrize("old_brand, old_model, new_brand, new_model, expected", [
    ("GAZ", "24", "VAZ", "2114", True),
    ("Lada", "Vesta", "Chevrolet", "Lanos", False),
    ("Honda", "Civic", "Hyundai", "Sonata", True),
])
def test_change_brand(old_brand, old_model, new_brand, new_model, expected, create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    create_journal.add_car("BMW", "E320", "5000", "8732", 4)
    assert create_journal.change_brand(
        old_brand, old_model, new_brand, new_model) == expected

@pytest.mark.parametrize("brand, model, new_duration, expected", [
    ("Mazda", "Miata", 5, True),
    ("Gaz", "24", 2, False),
    ("Honda", "Civic", 12, True),
])
def test_change_duration(brand, model, new_duration, expected, create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    create_journal.add_car("BMW", "E320", "5000", "8732", 4)
    assert create_journal.change_duration(
        brand, model, new_duration) == expected

@patch("builtins.open", new_callable=mock_open, read_data="John,Doe,2022-01-01,2022-12-31,1\nEmily,Johnson,2022-02-15,2023-02-15,121")
def test_read_from_file(mock_file, create_journal):
    create_journal.read_from_file("cars.txt")
    assert create_journal.cars == [
        {"brand": "Mazda", "model": "Miata", "mileage_last_checkup": "10500",
            "mileage_current_checkup": "11000", "duration": 1},
        {"brand": "BMW", "model": "E320", "mileage_last_checkup": "5000",
                 "mileage_current_checkup": "8732", "duration": 4}
    ]
    mock_file.assert_called_with("cars.txt", "r")

@patch("builtins.open", new_callable=mock_open)
def test_write_to_file(mock_file, create_journal):
    create_journal.add_car("Mazda", "Miata", "10500", "11000", 1)
    create_journal.add_car("BMW", "E320", "5000", "8732", 4)
    create_journal.write_to_file('sorted_cars.txt')
    mock_file.assert_called_with('sorted_cars.txt', 'w')