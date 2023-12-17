import math
import pytest
from main import get_cube_size, contains_color, get_color_distance, get_nearest_color, create_dither_tiles, create_tone_colors
from main import Tile
from unittest.mock import Mock


@pytest.mark.parametrize("cube, expected_result", [
    (((0, 0, 0), (1, 1, 1)), (1, 1, 1)),
    (((-1, -1, -1), (2, 2, 2)), (3, 3, 3)),
    (((-2, -2, -2), (0, 0, 0)), (2, 2, 2)),
])
def test_get_cube_size(cube, expected_result):
    result = get_cube_size(cube)
    assert result == expected_result


@pytest.mark.parametrize("cube, color, expected_result", [
    (((0, 0, 0), (1, 1, 1)), (0.5, 0.5, 0.5), True),
    (((0, 0, 0), (1, 1, 1)), (2, 2, 2), False),
    (((-1, -1, -1), (2, 2, 2)), (-0.5, -0.5, -0.5), True),
])
def test_contains_color(cube, color, expected_result):
    result = contains_color(cube, color)
    assert result == expected_result


@pytest.mark.parametrize("color1, color2, expected_distance", [
    ((0, 0, 0), (0, 0, 0), 0),
    ((255, 255, 255), (0, 0, 0), math.sqrt(255**2 + 255**2 + 255**2)),
    ((255, 0, 0), (0, 255, 0), math.sqrt(255**2 + 255**2)),
])
def test_get_color_distance(color1, color2, expected_distance):
    result = get_color_distance(color1, color2)
    assert result == expected_distance


@pytest.mark.parametrize("color, colors, expected_nearest_color", [
    ((0, 0, 0), [(255, 255, 255), (0, 0, 0), (128, 128, 128)], (0, 0, 0)),
    ((255, 255, 255), [(255, 255, 255), (0, 0, 0),
     (128, 128, 128)], (255, 255, 255)),
    ((0, 0, 0), [], None),
])
def test_get_nearest_color(color, colors, expected_nearest_color):
    result = get_nearest_color(color, colors)
    assert result == expected_nearest_color


class TestTile:
    @pytest.fixture
    def sample_tile(self):
        return Tile((255, 0, 0), (0, 255, 0))

    def test_initialization(self, sample_tile):
        assert sample_tile.color1 == (255, 0, 0)
        assert sample_tile.color2 == (0, 255, 0)

    def test_get_average_color(self, sample_tile):
        expected_result = ((255 + 0) // 2, (0 + 255) // 2, (0 + 0) // 2)
        assert sample_tile.get_average_color() == expected_result

    def test_get_color(self, sample_tile):
        sample_tile.get_color = Mock()
        sample_tile.get_color.return_value = (255, 0, 0)
        assert sample_tile.get_color(0, 0) == (255, 0, 0)
        sample_tile.get_color.assert_called_once_with(0, 0)
        sample_tile.get_color.reset_mock()
        sample_tile.get_color.return_value = (0, 255, 0)
        assert sample_tile.get_color(1, 0) == (0, 255, 0)
        sample_tile.get_color.assert_called_once_with(1, 0)


@pytest.mark.parametrize("colors, expected_num_tiles", [
    ([(255, 0, 0), (0, 255, 0), (0, 0, 255)], 6),
    ([(0, 0, 0), (255, 255, 255)], 3),
    ([(0, 255, 255)], 1),
    ([], 0),
])
def test_create_dither_tiles(colors, expected_num_tiles):
    tiles = create_dither_tiles(colors)
    assert len(tiles) == expected_num_tiles
    for color in colors:
        assert any(tile.color1 == color or tile.color2 ==
                   color for tile in tiles)


@pytest.mark.parametrize("tone_number, expected_num_colors", [
    (1, 1),
    (2, 8),
    (3, 27),
])
def test_create_tone_colors(tone_number, expected_num_colors):
    colors = create_tone_colors(tone_number)
    assert len(colors) == expected_num_colors
    for color in colors:
        assert all(0 <= value <= 255 for value in color)
