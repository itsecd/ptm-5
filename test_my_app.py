import pytest
from PyQt5 import QtCore


import main_window
import alg_luhn, graph, read_settings, gen_num, write_result


@pytest.fixture
def app(qtbot) -> main_window.Window:
    my_app = main_window.Window()
    qtbot.addWidget(my_app)
    return my_app


def test_start(app):
    """Ловим ошибку пустого поля"""
    app.variant_label.setText('')
    with pytest.raises(KeyError):
        app.button_start_click()


def test_start_label(app, qtbot):
    app.variant_label.setText('3')
    qtbot.mouseClick(app.button_start, QtCore.Qt.LeftButton)
    assert app.first_text.text() == "Вуаля, процесс закончен!\n   Что желаете сделать?"


@pytest.mark.parametrize(("numbers", "result"),
                         [('4529618049607621', False), ('4538912735659316', False), ('8225904637281519', False),
                          ('6352219737721156', True), ('3872278836666320', False), ('6094581715564255', False),
                          ('5166045463141790', True), ('1498845182739705', False), ('3206572148911478', False),
                          ('2202202138745688', False), ('7638294589620560', True)])
def test_luhn(numbers, result):
    assert alg_luhn.alg_luhn(numbers) == result


def test_graph():
    """Тест провалится если два массима разной длины"""

    cores = [7, 14, 11, 8, 15, 3, 6, 2, 13, 1, 9, 4, 5, 10, 12]
    times = [13, 10, 7, 9, 5, 2, 11, 6, 14, 4, 1, 3, 12, 8, 5]
    assert graph.show_plt(cores, times)


def test_read_settings():
    """я ожидаю что на самом деле ошибок нет, а значит при таком раскладе тест провален.."""

    with pytest.raises((KeyError, FileNotFoundError)):
        read_settings.read_json("21")


def test_write_file(tmpdir):
    text = "Вечер смешных шуток" \
           "– Почему птицы летят на юг? " \
           "– Потому что они не дойдут."

    a_sub_dir = tmpdir.mkdir('folder')
    a_file = a_sub_dir.join("text.txt")
    write_result.write_file(a_file, text)
    assert text == a_file.read()


data = {
    "hash": "bf67709b1216cb66038f3ae5ad2b4c066be03cbb",
    "bins": ["220220"],
    "last_num": "5688",
    "hash_format": "sha1"
}


@pytest.mark.parametrize("cores", [7, 8, 9, 10, 12, 13, 14])
def test_gen_num(cores):
    """Каково было мое удивление что питон работает с 10 потоками при имеющихся 8.
     Магия в использовании виртуальных потоков, а не физических, благодаря чему
     можно хоть 1000 потоков запустить, все упрется во время выполнения """
    assert gen_num.num_selection(data, cores)
