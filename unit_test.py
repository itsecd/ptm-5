import pytest
from Game import Globals
from Game import ScoreBoard
from unittest.mock import patch, MagicMock, create_autospec

@pytest.fixture
def globals_instance():
    return Globals()

@pytest.mark.parametrize("direction, expected_keys", [
    ("left", [97, 104, 260]),
    ("down", [115, 106, 258]),
    ("up", [119, 107, 259]),
    ("right", [100, 108, 261]),
    ("return", [32, 111, 10]),
])
def test_keys(globals_instance, direction, expected_keys):
    assert globals_instance.keys[direction] == expected_keys

@pytest.mark.parametrize("direction, expected_opposite", [
    ("right", "left"),
    ("left", "right"),
    ("up", "down"),
    ("down", "up"),
])
def test_opposite(globals_instance, direction, expected_opposite):
    assert globals_instance.oposite[direction] == expected_opposite

def test_menu_list(globals_instance):
    assert globals_instance.menu_list == ["Play", "Scoreboard", "EXIT"]

def test_directions_list(globals_instance):
    expected_directions_list = ["l","e","f","t", "d","o","w","n", "u","p", "r","i","g","h","t"]
    assert globals_instance.directions_list == expected_directions_list

def test_gen_directions(globals_instance):
    assert len(globals_instance.directions_list) == 15

@pytest.fixture
def scoreboard_instance():
    return ScoreBoard()


@pytest.mark.parametrize("scores, expected_result", [
    (["Player1", 100], ["Player1", 100]),
    (["Player2", 150], ["Player2", 150]),
    (["Player3", 120], ["Player3", 120])
])
def test_add_score(scoreboard_instance, scores, expected_result):
    scoreboard_instance.add_score(["Player1", 100])
    scoreboard_instance.add_score(["Player2", 150])
    scoreboard_instance.add_score(["Player3", 120])

    assert expected_result in scoreboard_instance._ScoreBoard__score_list


def test_run(scoreboard_instance):
    with patch("curses.curs_set"), \
         patch.object(scoreboard_instance, "_ScoreBoard__loop") as loop_mock:
        scoreboard_instance._ScoreBoard__run(MagicMock())

    loop_mock.assert_called_once()


if __name__ == "__main__":
    pytest.main()