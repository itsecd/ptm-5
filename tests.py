import pytest
from unittest.mock import patch, MagicMock, mock_open

# Предполагается, что ваш класс GymJournal находится в файле gym_journal.py
from main import GymJournal

# Тест на проверку существования клиента
def test_check_client():
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    assert journal.check_client('Иван', 'Иванов') == True
    assert journal.check_client('Петр', 'Петров') == False

# Параметризованный тест на изменение имени клиента
@pytest.mark.parametrize("first_name, last_name, new_first_name, new_last_name, expected", [
    ('Иван', 'Иванов', 'Сергей', 'Сергеев', True),
    ('Петр', 'Петров', 'Алексей', 'Алексеев', False)
])
def test_change_name(first_name, last_name, new_first_name, new_last_name, expected):
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    assert journal.change_name(first_name, last_name, new_first_name, new_last_name) == expected

# Тест с моком логгера
@patch('main.logger')
def test_change_months_with_logger(mock_logger):
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов', 'months': 12}]
    journal.change_months('Иван', 'Иванов', 24)
    mock_logger.info.assert_called_with('Months changed for Иван Иванов to 24')

# Тест с использованием стаба
def test_change_name_with_stub():
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    with patch.object(journal, 'clients', new_callable=MagicMock) as mock_clients:
        mock_clients.__iter__.return_value = iter([{'first_name': 'Иван', 'last_name': 'Иванов'}])
        assert journal.change_name('Иван', 'Иванов', 'Сергей', 'Сергеев') == True
        mock_clients.__iter__.assert_called_with()

# Дополнительный параметризованный тест для функции check_client
@pytest.mark.parametrize("first_name, last_name, expected", [
    ('Иван', 'Иванов', True),
    ('Петр', 'Петров', False)
])
def test_check_client_parametrized(first_name, last_name, expected):
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    assert journal.check_client(first_name, last_name) == expected

# Тест на добавление клиента
def test_add_client():
    journal = GymJournal()
    journal.add_client('Иван', 'Иванов', '2023-01-01', '2023-12-31', 12)
    assert journal.clients[-1] == {
        "first_name": 'Иван',
        "last_name": 'Иванов',
        "purchase_date": '2023-01-01',
        "end_date": '2023-12-31',
        "months": 12,
    }

# Тест на удаление клиента
def test_remove_client():
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    assert journal.remove_client('Иван', 'Иванов') == True
    assert journal.clients == []

# Тест на неудачное удаление клиента
def test_remove_client_failure():
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    assert journal.remove_client('Петр', 'Петров') == False

# Тест на сортировку клиентов по имени
def test_sort_by_name():
    journal = GymJournal()
    journal.clients = [
        {'first_name': 'Сергей', 'last_name': 'Сергеев'},
        {'first_name': 'Иван', 'last_name': 'Иванов'}
    ]
    journal.sort_by_name()
    assert journal.clients == [
        {'first_name': 'Иван', 'last_name': 'Иванов'},
        {'first_name': 'Сергей', 'last_name': 'Сергеев'}
    ]

# Тест с моком логгера для добавления клиента
@patch('main.logger')
def test_add_client_with_logger(mock_logger):
    journal = GymJournal()
    journal.add_client('Иван', 'Иванов', '2023-01-01', '2023-12-31', 12)
    mock_logger.info.assert_called_with('Client added: Иван Иванов')

# Тест с моком логгера для удаления клиента
@patch('main.logger')
def test_remove_client_with_logger(mock_logger):
    journal = GymJournal()
    journal.clients = [{'first_name': 'Иван', 'last_name': 'Иванов'}]
    journal.remove_client('Иван', 'Иванов')
    mock_logger.info.assert_called_with('Client removed: Иван Иванов')

# Тест на сортировку клиентов по количеству месяцев
def test_sort_by_months():
    journal = GymJournal()
    journal.clients = [
        {'first_name': 'Иван', 'last_name': 'Иванов', 'months': 12},
        {'first_name': 'Сергей', 'last_name': 'Сергеев', 'months': 6}
    ]
    journal.sort_by_months()
    assert journal.clients == [
        {'first_name': 'Сергей', 'last_name': 'Сергеев', 'months': 6},
        {'first_name': 'Иван', 'last_name': 'Иванов', 'months': 12}
    ]

# Тест на чтение клиентов из CSV файла
@patch('builtins.open', new_callable=mock_open, read_data='first_name,last_name,months\nИван,Иванов,12\nСергей,Сергеев,6')
def test_read_from_csv(mock_file):
    journal = GymJournal()
    journal.read_from_csv('clients.csv')
    assert journal.clients == [
        {'first_name': 'Иван', 'last_name': 'Иванов', 'months': '12'},
        {'first_name': 'Сергей', 'last_name': 'Сергеев', 'months': '6'}
    ]

# Тест на запись клиентов в CSV файл
@patch('builtins.open', new_callable=mock_open)
@patch('csv.DictWriter.writerow')
def test_write_to_csv(mock_writer, mock_file):
    journal = GymJournal()
    journal.clients = [
        {'first_name': 'Иван', 'last_name': 'Иванов', 'months': 12},
        {'first_name': 'Сергей', 'last_name': 'Сергеев', 'months': 6}
    ]
    journal.write_to_csv('clients.csv')
    mock_writer.assert_called_with({'first_name': 'Сергей', 'last_name': 'Сергеев', 'months': 6})

# Тест с моком логгера для сортировки клиентов по количеству месяцев
@patch('main.logger')
def test_sort_by_months_with_logger(mock_logger):
    journal = GymJournal()
    journal.clients = [
        {'first_name': 'Иван', 'last_name': 'Иванов', 'months': 12},
        {'first_name': 'Сергей', 'last_name': 'Сергеев', 'months': 6}
    ]
    journal.sort_by_months()
    mock_logger.info.assert_called_with('Clients sorted by months')