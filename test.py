import pytest
from ClothingStore import Manager, Clothes


@pytest.fixture
def manager():
    return Manager()


def test_add_clothes(manager):
    clothes = Clothes("Shirt", "Blue", "L", "Levi's", "Cotton", 1500)
    manager.add_clothes(clothes)
    assert clothes in manager.clothes_store


@pytest.mark.parametrize("name", ["Jean", "Shirt"])
def test_find_clothes(manager, name):
    manager.read_from_csv("clothes.csv")
    result = manager.find_clothes(name)
    assert isinstance(result, list) or len(result) == 0


def test_remove_clothes(manager):
    clothes = Clothes("Hoodie", "Gray", "XL", "Palm Anger", "Polyester", 2599)
    manager.add_clothes(clothes)
    manager.remove_clothes(clothes)
    assert clothes not in manager.clothes_store


def test_is_null():
    manager_test = Manager()
    result = manager_test.is_null()
    assert result is True


def test_clear_store(manager):
    manager.read_from_csv("clothes.csv")
    manager.clear_store()
    assert len(manager.clothes_store) == 0


@pytest.mark.parametrize("file_path", ["clothes.csv", "clothes.txt"])
def test_read_from_csv(manager, file_path):
    manager.read_from_csv(file_path)


@pytest.mark.parametrize("file_path", ["test.csv", "nonexistent_file.csv"])
def test_write_to_csv(manager, file_path):
    clothes1 = Clothes("Hoodie", "Gray", "XL", "Palm Anger", "Polyester", 2599)
    clothes2 = Clothes("Hat", "Red", "M", "Adidas", "Wool", 1999)
    manager.add_clothes(clothes1)
    manager.add_clothes(clothes2)
    manager.write_to_csv(file_path)
