import pytest
import sqlite3
import os

from database import create_connection, create_table, insert_file_data, get_file_data


@pytest.fixture
def temp_db():
    db_path = "temp_test_db.sqlite"
    conn = create_connection(db_path)
    create_table(conn)
    yield conn
    conn.close()
    os.remove(db_path)


def test_create_connection(temp_db):
    assert isinstance(temp_db, sqlite3.Connection)


def test_insert_and_get_file_data(temp_db):
    test_path = "/test/path"
    test_size = 1234
    test_last_modified = 1616161616.1
    test_hash = "abcd1234"
    test_backup_path = "/backup/path"

    insert_file_data(temp_db, test_path, test_size, test_last_modified, test_hash, test_backup_path)
    result = get_file_data(temp_db, file_hash=test_hash)
    assert result == (test_path, test_size, test_last_modified, test_backup_path)
