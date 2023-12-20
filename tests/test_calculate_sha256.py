import pytest
import os
from file_utils import calculate_sha256


@pytest.fixture
def setup_test_file():
    test_file_name = "temp_test_file.txt"
    with open(test_file_name, "w", encoding='UTF-8') as file:
        file.write("Hello, world!")
    yield test_file_name
    if os.path.exists(test_file_name):
        os.remove(test_file_name)


def test_calculate_sha256_valid_file(setup_test_file):
    test_file_name = setup_test_file
    expected_hash = "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3"
    calculated_hash = calculate_sha256(test_file_name)
    assert calculated_hash == expected_hash


def test_calculate_sha256_invalid_file():
    calculated_hash = calculate_sha256("non_existent_file.txt")
    assert calculated_hash is None
