import pytest
from db import *
from main import *


@pytest.mark.parametrize("file", ["Employee.db"])
def test_data_base(file) -> Database:
    return Database(file)


@pytest.mark.parametrize("name, age, doj, email, gender, contact, address",
                         [("Le Loc Tho", "23", "Student", "leloctho@gmail.com", "123456789", "VietNam")])
def test_insert(name, age, doj, email, gender, contact, address):
    data = Database('Employee.db')
    return data.insert(name, age, doj, email, gender, contact, address)


@pytest.mark.parametrize("idx, idx_expect", [('1', '1')])
def test_remove(idx, idx_expect):
    data = Database('Employee.db')
    result = data.remove(idx)
    assert result == idx_expect


@pytest.fixture
def test_getData():
    """
        Check that enough data is gotted
        :return: None
    """
    data = Database('Employee.db')
    data.insert("Le Loc Tho", "23", "Student", "leloctho@gmail.com", "123456789", "VietNam")
    getData(data)
    assert name.get() == "Le Loc Tho"


def test_displayAll():
    """
        Check that enough data is displayed on the screen
        :return: None
    """
    data = Database('Employee.db')
    data.insert("Le Loc Tho", "23", "Student", "leloctho@gmail.com", "123456789", "VietNam")
    data.insert("David Phuc", "22", "Manager", "phuc@gmail.com", "456789123", "England")
    display_All()
    assert len(db.fetch()) == 2


def test_clearAll():
    """
        Check if all data has been deleted
        :return: None
    """
    clearAll()
    assert name.get() == " "


def test_delete_employee():
    """
        Check if a worker's data has been deleted
        :return: None
    """
    data = Database('Employee.db')
    delete_employee()
    assert len(data.fetch()) == 1
