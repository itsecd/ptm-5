import pytest
from db import *


@pytest.mark.parametrize("file", ["Employee.db"])
def test_data_base(file) -> Database:
    return Database(file)


@pytest.mark.parametrize("file", ["Employee.db"])
def test_fetch(file):
    data = Database(file)
    tmp = data.fetch()
    assert tmp == [(1, 'John Doe', '30', '2023-01-01', 'john@example.com', 'Male', '1234567890', '123 Main St'),
                   (2, 'Romie', '23', '2023-07-08', 'romie@gmail.com', 'Male', '1234567890', '759 Main St')]


@pytest.mark.parametrize("file, name, age, doj, email, gender, contact, address",
                         [("Employee.db", "Daniel", "30", "2000-01-07", "daniel@gmail.com", "Male", "0524567890",
                           "759 Puma St")])
def test_insert(file, name, age, doj, email, gender, contact, address):
    data = Database(file)
    data.insert(name, age, doj, email, gender, contact, address)
    assert len(data.fetch()) == 3


@pytest.mark.parametrize("file, ind", [("Employee.db", 1)])
def test_getDataInd(file, ind):
    data = Database(file)
    dt = data.get_data_ind(ind)
    assert dt == (1, 'John Doe', '30', '2023-01-01', 'john@example.com', 'Male', '1234567890', '123 Main St')


@pytest.mark.parametrize("file, name", [("Employee.db", "John")])
def test_FindName(file, name):
    data = Database(file)
    data_name = data.find_data(name)
    assert data_name == True


@pytest.mark.parametrize("file, idx, idx_expect", [("Employee.db", '3', '3')])
def test_remove(file, idx, idx_expect):
    data = Database(file)
    data.remove(idx)
    tmp = data.fetch()
    assert tmp == [(1, 'John Doe', '30', '2023-01-01', 'john@example.com', 'Male', '1234567890', '123 Main St'),
                   (2, 'Romie', '23', '2023-07-08', 'romie@gmail.com', 'Male', '1234567890', '759 Main St')]


@pytest.mark.parametrize("file", ["Employee.db"])
def test_clearAll(file):
    data = Database(file)
    data.clear_ALL()
    assert len(data.fetch()) == 0
