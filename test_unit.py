import pytest
from main import ShopInventory


@pytest.fixture
def shop() -> ShopInventory:
    """
    функция для создания экземпляра ShopInventory
    """
    return ShopInventory()


def test_add_item(shop: ShopInventory) -> None:
    """
    тест для метода add_item
    """
    shop.add_item("Test Item")
    assert "Test Item" in shop.inventory


def test_count_items(shop) -> None:
    """
    тест для метода count_items
    """
    shop.add_item("Item 1")
    shop.add_item("Item 2")
    assert shop.count_items() == 2


@pytest.mark.parametrize("filename", ["test_inventory.csv", "nonexistent_file.csv"])
def test_save_to_csv(shop: ShopInventory, filename: str) -> None:
    """
    Тест для метода save_to_csv
    """
    shop.add_item("Item 1")
    shop.add_item("Item 2")
    try:
        shop.save_to_csv(filename)
    except Exception as e:
        assert False, f"Возникло неожиданное исключение: {e}"


@pytest.mark.parametrize("filename", ["test_inventory.csv", "nonexistent_file.csv"])
def test_load_from_csv(shop: ShopInventory, filename: str) -> None:
    """
    Тест для метода load_from_csv
    """
    try:
        shop.load_from_csv(filename)
    except Exception as e:
        assert False, f"Возникло неожиданное исключение: {e}"


def test_remove_existing_item(shop: ShopInventory) -> None:
    """
    тест для метода remove_item
    """
    shop.add_item("Test Item")
    shop.remove_item("Test Item")
    assert "Test Item" not in shop.inventory


def test_search_item_by_name(shop: ShopInventory) -> None:
    """
    тест для метода search_item_by_name
    """
    shop.add_item("Apple")
    shop.add_item("Banana")
    shop.add_item("Cherry")
    assert shop.search_item_by_name("Ban") == ["Banana"]


def test_clear_inventory(shop: ShopInventory) -> None:
    """
    тест для метода clear_inventory
    """
    shop.add_item("Test Item")
    shop.clear_inventory()
    assert not shop.inventory