import pytest
import os
import shutil
import sqlite3

from backup_manager import backup_files
from database import create_connection, create_table, get_file_data
from file_utils import calculate_sha256


@pytest.fixture
def temp_db():
    db_path = "temp_test_db.sqlite"
    conn = create_connection(db_path)
    create_table(conn)
    yield conn, db_path
    conn.close()
    if os.path.exists(db_path):
        os.remove(db_path)


@pytest.fixture
def source_and_destination_dirs():
    source_dir = "temp_source_dir"
    destination_dir = "temp_destination_dir"
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(destination_dir, exist_ok=True)

    yield source_dir, destination_dir

    shutil.rmtree(source_dir)
    shutil.rmtree(destination_dir)


def test_backup_files(source_and_destination_dirs, temp_db):
    source_dir, destination_dir = source_and_destination_dirs
    conn, db_path = temp_db

    # Создаем тестовый файл
    test_file_name = "test_file.txt"
    with open(os.path.join(source_dir, test_file_name), "w") as file:
        file.write("Test content")

    # Выполняем процесс резервного копирования
    backup_files(source_dir, destination_dir, db_path)

    # Извлекаем информацию о файле из базы данных
    file_data = get_file_data(conn, file_hash=calculate_sha256(os.path.join(source_dir, test_file_name)))
    if file_data:
        backup_file_path = file_data[3]  # Путь к резервной копии файла

        # Проверяем, что файл был скопирован
        assert os.path.exists(backup_file_path)
