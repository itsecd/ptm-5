import pytest
import logging
from main import Product, ProductStore


@pytest.fixture
def store() -> ProductStore:
    """
    The function for creating an instance ProductStore for testing
    Returns ProductStore
    """
    return ProductStore()


@pytest.fixture
def product() -> Product:
    """
    The function for creating an instance ProductStore for testing
    Returns Product
    """
    return Product()


def test_change_price() -> None:
    product = Product("TestProduct1", 10.0, 10, "2023-01-01")
    assert product.price == 10.0
    product.change_price(15.0)
    assert product.price == 15.0


def test_add_product(store: ProductStore) -> None:
    assert store.add_product(product1) == True
    assert len(store.products) == 1

    assert store.add_product(product1) == False
    assert len(store.products) == 1

    assert store.add_product(product2) == True
    assert len(store.products) == 2


def test_product_exists(store: ProductStore) -> None:
    store.add_product(product1)
    assert store.product_exists("TestProduct1") == True
    assert store.product_exists("TestProduct2") == False


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_write_to_csv(store: ProductStore, filename: str) -> None:
    """
    тест для метода write_to_csv
    :param shop: ShopInventory
    :param filename: имя файла str
    :return: None
    """
    store.add_product(product1)
    store.add_product(product2)
    store.write_to_csv(filename)


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_read_from_csv(store: ProductStore, filename: str) -> None:
    """
    тест для метода load_from_csv
    :param shop: ShopInventory
    :param filename: имя файла str
    :return: None
    """
    store.read_from_csv(filename)


def test_clear_products(store: ProductStore) -> None:
    store.add_product(product1)
    store.clear_products()
    assert len(store.products) == 0


def test_sort_by_price(store: ProductStore) -> None:
    store.add_product(product1)
    store.add_product(product2)
    store.add_product(product3)

    store.sort_by_price()

    assert store.products[0].name == "TestProduct2"
    assert store.products[1].name == "TestProduct1"
    assert store.products[2].name == "TestProduct3"


product1 = Product("TestProduct1", 1.00, 10, "2023-01-01")
product2 = Product("TestProduct2", 0.99, 3, "2022-01-01")
product3 = Product("TestProduct3", 1.50, 15, "1962-01-01")
pytest.main(["-v", "test_unit.py"])
