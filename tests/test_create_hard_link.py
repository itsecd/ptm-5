import pytest
import os

from file_utils import create_hard_link


@pytest.fixture
def setup_test_files():
    source_file = "source_file.txt"
    with open(source_file, "w") as file:
        file.write("Test content")
    yield source_file
    if os.path.exists(source_file):
        os.remove(source_file)


def test_create_hard_link_success(setup_test_files):
    source_file = setup_test_files
    link_name = "link_file.txt"
    create_hard_link(source_file, link_name)
    assert os.path.exists(link_name)
    if os.path.exists(link_name):
        os.remove(link_name)


def test_create_hard_link_existing_link(setup_test_files, caplog):
    source_file = setup_test_files
    link_name = "link_file.txt"
    with open(link_name, "w") as file:
        file.write("Different content")
    create_hard_link(source_file, link_name)
    assert "уже существует" in caplog.text
    if os.path.exists(link_name):
        os.remove(link_name)


def test_create_hard_link_invalid_source(caplog):
    non_existent_file = "non_existent_file.txt"
    link_name = "link_file.txt"
    create_hard_link(non_existent_file, link_name)
    assert "Ошибка при создании жесткой ссылки" in caplog.text
    if os.path.exists(link_name):
        os.remove(link_name)
