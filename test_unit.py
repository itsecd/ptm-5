import pytest
from db import Database

file_data = "AnotherDB.db"


@pytest.mark.parametrize("file", [file_data])
def test_data_base(file) -> Database:
    return Database(file)


@pytest.mark.parametrize("file, name, age, doj, email, gender, contact, address",
                         [(file_data, "Lisa", "29", "1999-04-07", "lisa111@gmail.com", "Female", "4424789440",
                           "759 Puma St")])
def test_insert(file, name, age, doj, email, gender, contact, address):
    data = Database(file)
    data.insert(name, age, doj, email, gender, contact, address)
    assert len(data.fetch()) == 3


@pytest.mark.parametrize("file", [file_data])
def test_fetch(file):
    data = Database(file)
    tmp = data.fetch()
    assert tmp == [(1, 'Daniel', '30', '2000-01-07', 'daniel@gmail.com', 'Male', '0524567890', '759 Puma St'),
                   (2, 'Alice', '25', '2022-03-15', 'alice@example.com', 'Female', '9876543210', '456 Oak St'),
                   (3, "Lisa", "29", "1999-04-07", "lisa111@gmail.com", "Female", "4424789440", "759 Puma St")]


@pytest.mark.parametrize("file, ind", [(file_data, 3)])
def test_getDataInd(file, ind):
    data = Database(file)
    dt = data.get_data_ind(ind)
    assert dt == (3, "Lisa", "29", "1999-04-07", "lisa111@gmail.com", "Female", "4424789440", "759 Puma St")


@pytest.mark.parametrize("file, name", [(file_data, "Lisa")])
def test_FindName(file, name):
    data = Database(file)
    data_name = data.find_data(name)
    assert data_name == True


@pytest.mark.parametrize("file, idx, idx_expect", [(file_data, '3', '3')])
def test_remove(file, idx, idx_expect):
    data = Database(file)
    data.remove(idx)
    tmp = data.fetch()
    assert tmp == [(1, 'Daniel', '30', '2000-01-07', 'daniel@gmail.com', 'Male', '0524567890', '759 Puma St'),
                   (2, 'Alice', '25', '2022-03-15', 'alice@example.com', 'Female', '9876543210', '456 Oak St')]


@pytest.mark.parametrize("file", [file_data])
def test_clearAll(file):
    data = Database(file)
    data.clear_ALL()
    assert len(data.fetch()) == 0
