import pytest
from main import ShopInventory

@pytest.fixture
def shop() -> ShopInventory:
    return ShopInventory()


def test_add_item(shop: ShopInventory) -> None:
    shop.add_item("Test Item")
    assert "Test Item" in shop.inventory


def test_count_items(shop) -> None:
    shop.add_item("Item 1")
    shop.add_item("Item 2")
    assert shop.count_items() == 2


@pytest.mark.parametrize("filename", ["test_inventory.csv", "nonexistent_file.csv"])
def test_save_to_csv(shop: ShopInventory, filename: str) -> None:
    shop.add_item("Item 1")
    shop.add_item("Item 2")
    try:
        shop.save_to_csv(filename)
    except Exception as e:
        assert False, f"Возникло неожиданное исключение: {e}"


@pytest.mark.parametrize("filename", ["test_inventory.csv", "nonexistent_file.csv"])
def test_load_from_csv(shop: ShopInventory, filename: str) -> None:
    try:
        shop.load_from_csv(filename)
    except Exception as e:
        assert False, f"Возникло неожиданное исключение: {e}"


def test_search_item_by_name(shop: ShopInventory) -> None:
    shop.add_item("Apple")
    shop.add_item("Banana")
    shop.add_item("Cherry")
    assert shop.search_item_by_name("Ban") == ["Banana"]


def test_remove_existing_item(shop: ShopInventory) -> None:
    shop.add_item("Test Item")
    shop.remove_item("Test Item")
    assert "Test Item" not in shop.inventory


def test_clear_inventory(shop: ShopInventory) -> None:
    shop.add_item("Test Item")
    shop.clear_inventory()
    assert not shop.inventory

def test_check_item_exists(shop: ShopInventory):
    shop.add_item("Test item")
    assert shop.check_item_exists("Test item") == True
    assert f"Товар 'Test item' присутствует в инвентаре."


def test_display_inventory(shop: ShopInventory):
    shop.add_item("Item 1")
    shop.add_item("Item 2")
    shop.display_inventory()
    assert "Item 1" in shop.inventory
    assert "Item 2" in shop.inventory

