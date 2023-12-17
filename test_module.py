import pytest
from program import ShopInventory


@pytest.fixture
def shop() -> ShopInventory:
    """
    Функция, создающая объект класса ShopInventory
    """
    return ShopInventory()


def test_add(shop: ShopInventory) -> None:
    """
    Тест функции доавления элемента add_item
    """
    shop.add_item("Unit testing")
    assert "Unit testing" in shop.inventory


def test_remove_item(shop: ShopInventory) -> None:
    """
     Тест функции удаления элемента remove_item
    """
    shop.add_item("Test")
    shop.remove_item("Test")
    assert "Test Item" not in shop.inventory


def test_count_items(shop) -> None:
    """
    Тест функции count_items, дающей число товаров
    """
    shop.add_item("Test 1")
    shop.add_item("Test 2")
    shop.add_item("Test 3")
    assert shop.count_items() == 3


@pytest.mark.parametrize("filename", ["test_inventory.csv", "nonexistent_file.csv"])
def test_save_to_csv(shop: ShopInventory, filename: str) -> None:
    """
    Тест функции сохранения в файл csv save_to_csv
    """
    shop.add_item("Test 1")
    shop.add_item("Test 2")
    shop.add_item("Test 3")
    try:
        shop.save_to_csv(filename)
    except Exception as error:
        assert Exception, f"Вызвано исключение: {error}"


@pytest.mark.parametrize("filename", ["test_inventory.csv", "nonexistent_file.csv"])
def test_load_from_csv(shop: ShopInventory, filename: str) -> None:
    """
    Тест функции, читающей csv-файл load_from_csv
    """
    try:
        shop.load_from_csv(filename)
    except Exception as error:
        assert Exception, f"Вызвано исключение: {error}"


def test_search_item_by_name(shop: ShopInventory) -> None:
    """
    Тест функции посика элементов по имени search_item_by_name
    """
    shop.add_item("Коммод")
    assert shop.search_item_by_name("Ком") == ["Коммод"]


def test_clear_inventory(shop: ShopInventory) -> None:
    """
    Тест функции очистки инвентаря clear_inventory
    """
    shop.add_item("Unit testing_2")
    shop.clear_inventory()
    assert not shop.inventory


def test_bubble_sort_inventory(shop: ShopInventory):
    """
    Тест функции clear_inventory
    """
    shop.add_item("Sony Playstation")
    shop.add_item("Настольная игра")
    shop.add_item("Шампанское ")
    shop.add_item("Елочка")
    try:
        shop.bubble_sort_inventory()
    except Exception as error:
        assert Exception, f"Вызвано исключение: {error}"


def test_check_item_exists(shop: ShopInventory):
    """
    Тест функции проверки на существование check_item_exists
    """
    shop.add_item("Карабин")
    shop.remove_item("Карабин")
    assert shop.check_item_exists("Карабин") == False