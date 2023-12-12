import pytest

from program import MultiTree

COUNT = 10


@pytest.fixture
def multi_tree() -> MultiTree:
    """Создание объекта класса MultiTree"""
    return MultiTree()


def test_append(multi_tree: MultiTree) -> None:
    """Тест метода побавления элемента"""
    tmp_tree = MultiTree()
    multi_tree.append(tmp_tree)
    assert multi_tree.find(tmp_tree) == True


def test_count(multi_tree: MultiTree) -> None:
    """Тест метода подсчёта элементов в списке"""
    for _ in range(COUNT):
        tmp_tree = MultiTree()
        multi_tree.append(tmp_tree)
    assert multi_tree.count() == COUNT


def test_clear(multi_tree: MultiTree) -> None:
    """Тест метода очистки списка"""
    for _ in range(COUNT):
        tmp_tmp_tree = MultiTree()
        for __ in range(COUNT):
            tmp_tree = MultiTree()
            tmp_tmp_tree.append(tmp_tree)
        multi_tree.append(tmp_tmp_tree)
    multi_tree.clear()
    assert multi_tree.is_empty() == True


def test_find(multi_tree: MultiTree) -> None:
    """Тест медода поиска элемента в списке"""
    tmp_tmp_tree = MultiTree()
    for _ in range(COUNT-1):
        tmp_tree = MultiTree()
        multi_tree.append(tmp_tree)
    multi_tree.append(tmp_tmp_tree)
    assert multi_tree.find(tmp_tmp_tree) == True


def test_getitem(multi_tree: MultiTree) -> None:
    """Тест обращения по индексу"""
    tmp_tmp_tree = MultiTree()
    for _ in range(COUNT-1):
        tmp_tree = MultiTree()
        multi_tree.append(tmp_tree)
    multi_tree.append(tmp_tmp_tree)
    assert multi_tree[COUNT-1] == tmp_tmp_tree


@pytest.mark.parametrize("num", [2.86145, -3.9813, 5])
def test_getter_setter(multi_tree: MultiTree, num: float) -> None:
    """Тест геттера и сеттера"""
    multi_tree.value = num
    assert multi_tree.value == num


@pytest.mark.parametrize("count, flag", [(3, False), (1, False), (0, True)])
def test_is_empty(multi_tree: MultiTree, count: float, flag: bool) -> None:
    """Тест метода проверки списка на пустоту"""
    for _ in range(count):
        tmp_tree = MultiTree()
        multi_tree.append(tmp_tree)
    assert multi_tree.is_empty() == flag