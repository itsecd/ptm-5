import pytest
from main import get_cube_size, get_color_distance, split_cube, Tile, contains_color, create_dither_tiles
import math

@pytest.mark.parametrize("cube", [[[0, 0, 0], [1, 1, 1]], [[-1, -2, -3], [1, 2, 3]], [[12, 1, 0], [0, 1, 12]]])
def test_get_cibe_size(cube: list) -> None:
    res = get_cube_size(cube)
    assert res == (cube[1][0] - cube[0][0], cube[1][1] - cube[0][1], cube[1][2] - cube[0][2])
    
@pytest.mark.parametrize("color1, color2", [([0, 0, 0], [1, 1, 2]), ([1, 2, 3], [10, 25, 17])])
def test_get_color_distance(color1, color2) -> None:
    res = get_color_distance(color1, color2)
    assert res == math.sqrt((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2)
    
@pytest.mark.parametrize("cube", [[[0, 0, 0], [1, 1, 2]]])
def test_split_cube(cube: list) -> None:
    res = split_cube(cube)
    assert res == (((0, 0, 0), (1, 1, 1)), ((0, 0, 2), (1, 1, 2)))
    

@pytest.mark.parametrize("colors", [[[0, 0, 0], [1, 1, 2]], [[11, 12, 13], [21, 22, 23]], [[10, 1, 100], [21, 1, 2]]]) 
def test_append_colors(colors) -> None:
    tile_elem = Tile(colors[0], colors[1])
    assert tile_elem.color1 == colors[0] and tile_elem.color2 == colors[1]

@pytest.mark.parametrize("colors", [[[0, 0, 0], [1, 1, 2]], [[11, 12, 13], [21, 22, 23]], [[10, 1, 100], [21, 1, 2]]])
def test_get_average_color(colors:list) -> None:
    tile_elem = Tile(colors[0], colors[1])
    res = tile_elem.get_average_color()
    assert res == ((tile_elem.color1[0] + tile_elem.color2[0]) // 2, (tile_elem.color1[1] + tile_elem.color2[1]) // 2, (tile_elem.color1[2] + tile_elem.color2[2]) // 2)

@pytest.mark.parametrize("cube, color", [([[0, 0, 0], [1, 1, 2]], [1, 1, 1]), ([[11, 12, 13], [21, 22, 23]], [1, 5, 9])])
def test_contains_color(cube: list, color:list) -> None:
    res = contains_color(cube, color)
    assert res == bool(cube[0][0] <= color[0] and cube[0][1] <= color[1] and cube[0][2] <= color[2] and cube[1][0] >= color[0] and cube[1][1] >= color[1] and cube[1][2] >= color[2])
        
@pytest.mark.parametrize("colors", [[[0, 0, 0], [1, 1, 2]], [[11, 12, 13], [21, 22, 23], [0, 0, 1]], [[10, 1, 100]]])
def test_create_dither_tiles(colors) -> None:
    res = create_dither_tiles(colors)
    tiles = []
    for i in range(len(colors)):
        for j in range(i, len(colors)):
            tiles.append(Tile(colors[i], colors[j]))
    print('res = ', res)
    print('tiles = ', tiles)
    assert len(res) == len(tiles)
    