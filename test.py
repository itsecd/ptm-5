import pytest
import os
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


def test_write_and_read_to_csv(tmp_path, sample_manager):
    file_path = os.path.join(tmp_path, "test_clothes.csv")

    # Write to CSV
    sample_manager.write_to_csv(file_path)

    # Clear the store and read from CSV
    sample_manager.clear_store()
    sample_manager.read_from_csv(file_path)

    assert not sample_manager.is_null()
    assert len(sample_manager.clothes_store) == 3  # Assuming there are 3 unique items in the sample_manager


def test_clear_store(sample_manager):
    assert not sample_manager.is_null()
    sample_manager.clear_store()
    assert sample_manager.is_null()


def test_display_clothes(capfd, sample_manager):
    sample_manager.display_clothes()
    captured = capfd.readouterr()
    assert "Shirt" in captured.out
    assert "Blue" in captured.out
    assert "L" in captured.out
    assert "Levi's" in captured.out
    assert "Cotton" in captured.out
    assert "1500" in captured.out


def test_is_null(sample_manager):
    sample_manager.clear_store()
    result = sample_manager.is_null()
    assert result is True
