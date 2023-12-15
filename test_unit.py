import pytest
import logging
import csv
import os
from main import Product, ProductStore


@pytest.fixture
def store() -> ProductStore:
    """
    The function for creating an instance ProductStore for testing
    Returns ProductStore
    """
    return ProductStore()


def product() -> Product:
    """
    The function for creating an instance ProductStore for testing
    Returns Product
    """
    return Product()


def test_change_price() -> None:
    """
    test for the change_price method
    :return: None
    """
    product = Product("TestProduct1", 10.0, 10, "2023-01-01")
    assert product.price == 10.0
    product.change_price(15.0)
    assert product.price == 15.0


def test_add_product(store: ProductStore) -> None:
    """
    test for the add_product method
    :store: ProductStore
    :return: None
    """
    assert store.add_product(Product("TestProduct1", 1.00, 10, "2023-01-01")) == True
    assert len(store.products) == 1

    assert store.add_product(Product("TestProduct1", 1.00, 10, "2023-01-01")) == False
    assert len(store.products) == 1

    assert store.add_product(Product("TestProduct2", 0.99, 3, "2022-01-01")) == True
    assert len(store.products) == 2


def test_product_exists(store: ProductStore) -> None:
    """
    test for the product_exists method
    :store: ProductStore
    :return: None
    """
    store.add_product(Product("TestProduct1", 1.00, 10, "2023-01-01"))
    assert store.product_exists("TestProduct1") == True
    assert store.product_exists("TestProduct2") == False


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_write_to_csv(store: ProductStore, filename: str) -> None:
    """
    test for the write_to_csv method with parameterization
    :store: ProductStore
    :filename: str
    :return: None
    """
    store.add_product(Product("TestProduct1", 1.00, 10, "2023-01-01"))
    store.add_product(Product("TestProduct2", 0.99, 3, "2022-01-01"))
    store.write_to_csv(filename)

    # Check if file exists
    assert os.path.exists(filename)

    # Check if file is not empty
    assert os.path.getsize(filename) > 0


@pytest.mark.parametrize("filename", ["test_product.csv", "nonexistent_file.csv"])
def test_read_from_csv(store: ProductStore, filename: str) -> None:
    """
    test for the read_from_csv method without parameterization
    :store: ProductStore
    :filename: str
    :return: None
    """
    store.read_from_csv(filename)

    # Check if products were correctly read from the file
    assert len(store.products) > 0
    assert isinstance(store.products[0], Product)


def test_clear_products(store: ProductStore) -> None:
    """
    test for the clear_products method
    :store: ProductStore
    :return: None
    """
    store.add_product(Product("TestProduct1", 1.00, 10, "2023-01-01"))
    store.clear_products()
    assert len(store.products) == 0


def test_sort_by_price(store: ProductStore) -> None:
    """
    test for the sort_by_price method
    :store: ProductStore
    :return: None
    """
    store.add_product(Product("TestProduct1", 1.00, 10, "2023-01-01"))
    store.add_product(Product("TestProduct2", 0.99, 3, "2022-01-01"))
    store.add_product(Product("TestProduct3", 1.50, 15, "1962-01-01"))

    store.sort_by_price()

    assert store.products[0].name == "TestProduct2"
    assert store.products[1].name == "TestProduct1"
    assert store.products[2].name == "TestProduct3"


if __name__ == "__main__":
    pytest.main(["-v", "-color=yes"])
