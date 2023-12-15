import pytest
from functions import *


@pytest.fixture
def field():
    return {
        1: ['N/A', '?', '?', '?', '?'],
        2: ['N/A', '?', '?', '?', '?'],
        3: ['N/A', '?', '?', '?', '?'],
        4: ['N/A', '?', '?', '?', '?']
    }


@pytest.mark.parametrize('rows, columns, mines',
                         [(10, 10, 10),
                          (16, 16, 40),
                          (30, 16, 99)])
def test_mines_count(rows, columns, mines):
    """
    тест функции генерации мин на количество сгенерированных мин
    :param rows: количество строк в поле
    :param columns: количество столбцов в поле
    :param mines: заданное количество мин
    :return: ничего
    """
    mines_count = len(minesCoordinates(rows, columns, mines))
    assert mines_count == mines


@pytest.mark.parametrize('points, flags, moves, lastMove, new_moves',
                         [(10, 5, 15, [11, 5], 16),
                          (7, 7, 5, [7, 7], 5)])
def test_moves(points, flags, moves, lastMove, new_moves):
    """
    тест функции вывода количества ходов
    :param points: полученные очки
    :param flags: установленные флаги
    :param moves: количество ходов
    :param lastMove: последний ход
    :param new_moves: новое количество ходов
    :return: ничего
    """
    moves_count = checkMoves(points, flags, moves, lastMove)
    assert moves_count == new_moves


def test_field_generation(field):
    """
    тест функции генерации поля
    :param field: тестовое поле
    :return: ничего
    """
    generated_field = cellsCoordinates(4, 4)
    assert field == generated_field


def test_show_mines(field):
    """
    тест функции отображения всех мин на поле
    :param field: тестовое поле
    :return: ничего
    """
    showMines([[1, 2], [4, 4]], field)
    assert field == {1: ['N/A', '?', 'M', '?', '?'],
                     2: ['N/A', '?', '?', '?', '?'],
                     3: ['N/A', '?', '?', '?', '?'],
                     4: ['N/A', '?', '?', '?', 'M']}


def test_mines_around():
    """
    тест функции поиска мин вокруг выбранной клетки
    :return: ничего
    """
    row_chosen = 2
    column_chosen = 2
    rows = 10
    columns = 10
    cells_with_mines = [[1, 1], [3, 2], [1, 3], [9, 6]]
    mines_around = checkMinesAround(row_chosen, column_chosen, rows, columns, cells_with_mines)
    assert mines_around == 3


def test_cells_around(field):
    """
    тест функции поиска прилежащих клеток с таким же значением, как в выбранной клетке
    :param field: тестовое поле
    :return: ничего
    """
    row_chosen = 2
    column_chosen = 2
    rows = 4
    columns = 4
    selected_cells = []
    cells_with_mines = [[1, 4], [2, 4], [3, 4], [4, 1], [4, 2], [4, 3], [4, 4]]
    selected_cell_mines_around = 0
    points = 1
    new_points = checkCellsAround(row_chosen, column_chosen, rows, columns, selected_cells, cells_with_mines, field,
                                  selected_cell_mines_around, points)
    assert new_points == 5


def test_add_flag(field):
    """
    тест функции установки флага
    :param field: тестовое поле
    :return: ничего
    """
    row_chosen = 2
    column_chosen = 2
    rows = 4
    columns = 4
    flags = 3
    mines = 8
    new_flags = addFlag(row_chosen, rows, column_chosen, columns, field, flags, mines)
    assert new_flags == 2
