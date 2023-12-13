import pytest
from ClothingStore import Manager, Clothes


@pytest.fixture
def sample_manager():
    manager = Manager()
    manager.add_clothes(Clothes("Shirt", "Blue", "L", "Levi's", "Cotton", 1500))
    manager.add_clothes(Clothes("Trouser", "Black", "30", "Wrangler", "Denim", 1799))
    manager.add_clothes(Clothes("Hoodie", "Gray", "XL", "Palm Anger", "Polyester", 2599))
    return manager


def test_add_clothes():
    manager = Manager()
    assert manager.is_null()
    manager.add_clothes(Clothes("Shirt", "Blue", "L", "Levi's", "Cotton", 1500))
    assert not manager.is_null()


def test_remove_clothes(sample_manager):
    assert not sample_manager.is_null()
    shirt = Clothes("Shirt", "Blue", "L", "Levi's", "Cotton", 1500)
    sample_manager.remove_clothes(shirt)
    assert len(sample_manager.clothes_store) == 2


def test_find_clothes(sample_manager):
    result = sample_manager.find_clothes("Shirt")
    assert len(result) == 1
    assert result[0].name == "Shirt"


@pytest.mark.parametrize("tmp_path", ["clothes.csv"])
def test_read_from_csv(tmp_path, sample_manager):
    sample_manager.clear_store()
    sample_manager.read_from_csv(tmp_path)


@pytest.mark.parametrize("tmp_path", ["clothes.csv", "non_exist.csv"])
def test_write_to_csv(tmp_path, sample_manager):
    sample_manager.write_to_csv(tmp_path)


def test_is_null(sample_manager):
    sample_manager.clear_store()
    result = sample_manager.is_null()
    assert result is True


def test_check_big_store(sample_manager):
    sample_manager = Manager()
    sample_manager.read_from_csv("clothes.csv")
    sample_manager.read_from_csv("clothes.csv")
    sample_manager.read_from_csv("clothes.csv")
    sample_manager.read_from_csv("clothes.csv")
    sample_manager.read_from_csv("clothes.csv")
    sample_manager.read_from_csv("clothes.csv")
    result = sample_manager.check_big_store()
    assert result is True
