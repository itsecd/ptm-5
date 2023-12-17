import pytest
from functions import minesCoordinates, cellsCoordinates, \
checkMoves, showMines, checkMinesAround,  checkCellsAround, addFlag


@pytest.mark.parametrize("rows, columns, mines, expected_result", [
    (5, 5, 5, True),    
    (8, 8, 10, True),  
    (5, 5, 0, True)    
])
def test_mines_coordinates(rows, columns, mines, expected_result):
    result = minesCoordinates(rows, columns, mines)
    assert len(result) == mines
    assert len(set(tuple(coord) for coord in result)) == mines
    assert isinstance(result, list) == expected_result
    if not expected_result:
        with pytest.raises(ValueError, match="Duplicate coordinates found"):
            minesCoordinates(rows, columns, mines)


@pytest.mark.parametrize("rows, columns, expected_result", [
    (3, 4, True),  
    (5, 0, True)  
])
def test_cells_coordinates(rows, columns, expected_result):
    result = cellsCoordinates(rows, columns)
    assert isinstance(result, dict)
    assert len(result) == rows
    for i in range(1, rows + 1):
        assert i in result
        assert len(result[i]) == columns + 1
        assert result[i][0] == "N/A"
        assert all(cell == "?" for cell in result[i][1:])
    if not expected_result:
        for i in range(1, rows + 1):
            assert len(result[i]) == 1
            assert result[i][0] == "N/A"


@pytest.mark.parametrize("points, flags, moves, last_move, expected_result", [
    (10, 5, 3, [10, 5], 3),       
    (15, 5, 3, [10, 5], 4),       
    (10, 8, 3, [10, 5], 4),       
    (15, 8, 3, [10, 5], 4)       
])
def test_check_moves(points, flags, moves, last_move, expected_result):
    result = checkMoves(points, flags, moves, last_move)
    assert result == expected_result


@pytest.mark.parametrize("cellsWithMines, initial_cells, expected_result", [
    ([(1, 2), (3, 4), (2, 1)],
     {
        1: [" ", " ", " ", " ", " "],
        2: [" ", " ", " ", " ", " "],
        3: [" ", " ", " ", " ", " "],
        4: [" ", " ", " ", " ", " "]
    },
        {
        1: [" ", " ", "M", " ", " "],
        2: [" ", "M", " ", " ", " "],
        3: [" ", " ", " ", " ", "M"],
        4: [" ", " ", " ", " ", " "]
    }
    )
])
def test_show_mines_parametrized(cellsWithMines, initial_cells, expected_result):
    showMines(cellsWithMines, initial_cells)
    for row in initial_cells.keys():
        assert initial_cells[row] == expected_result[row]


@pytest.mark.parametrize("row_chosen, column_chosen, rows, columns, cells_with_mines, expected_result", [
    (1, 1, 5, 5, [[1, 2], [2, 1], [2, 2]], 3),
    (3, 3, 5, 5, [[3, 2], [2, 3], [3, 4]], 3),
    (1, 1, 1, 1, [], 0)
])
def test_check_mines_around(row_chosen, column_chosen, rows, columns, cells_with_mines, expected_result):
    result = checkMinesAround(
        row_chosen, column_chosen, rows, columns, cells_with_mines)
    assert result == expected_result


@pytest.mark.parametrize("row_chosen, column_chosen, rows, columns, selected_cells, \
                        cells_with_mines, cells, selected_cell_mines_around, points, \
                        expected_result",
                        [(2, 2, 5, 5, [[1, 2], [3, 2]], [[1, 2], [3, 2], [2, 1], [2, 3]], [[' ', '1', ' ', ' ', ' '],
                                                                                            ['1', '2', ' ', ' ', ' '],
                                                                                            [' ', ' ', '2', ' ', ' '],
                                                                                            [' ', ' ', '1', ' ', ' '],
                                                                                            [' ', ' ', ' ', ' ', ' ']], 2, 0, 0)
                        ])
def test_check_cells_around(row_chosen, column_chosen, rows, columns, selected_cells, cells_with_mines, cells, selected_cell_mines_around, points, expected_result):
    result = checkCellsAround(row_chosen, column_chosen, rows, columns, selected_cells,
                              cells_with_mines, cells, selected_cell_mines_around, points)
    assert result == expected_result


@pytest.mark.parametrize("row_chosen, rows, column_chosen, columns, cells, flags, mines, expected_result", [
    (0, 5, 1, 5, [['?', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [
     ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']], 3, 5, 3)
])
def test_add_flag(row_chosen, rows, column_chosen, columns, cells, flags, mines, expected_result):
    result = addFlag(row_chosen, rows, column_chosen,
                     columns, cells, flags, mines)
    assert result == expected_result


if __name__ == '__main__':
    pytest.main()
