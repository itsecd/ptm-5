import pytest
import dicts.utils as ut

@pytest.mark.parametrize("expected,x,y", [("\x1b[6;2H", 2, 6), ("\x1b[400;50H",50, 400.7), ("\x1b[-600;5H",5.25, -600.666)])
def test_pos(expected, x, y):
    assert ut.pos(x, y) == expected

@pytest.mark.parametrize("text, corner, border, expected", [
    ("Hello", '+', '-', "+-----+\n|Hello|\n+-----+"),
    ("Line 1\nLine 2", '*', '=', "*======*\n|Line 1|\n|Line 2|\n*======*"),
    ("", '#', '~', "##\n||\n##"),
    ("Short\nA very long line", '@', '*', "@****************@\n|Short           |\n|A very long line|\n@****************@")
])
def test_banner(text, corner, border, expected):
    assert ut.banner(text, corner, border) == expected