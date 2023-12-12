import pytest

from program import MultiTree

COUNT = 10


@pytest.fixture
def multi_tree() -> MultiTree:
    """Создание объекта класса MultiTree"""
    return MultiTree()


def test_append(tree: MultiTree) -> None:
    """Тест метода побавления элемента"""
    tmp_test = MultiTree()
    tree.append(tmp_test)
    assert tree.find(tmp_test) == True


def test_count(tree: MultiTree) -> None:
    """Тест метода подсчёта элементов в списке"""
    for _ in range(COUNT):
        tmp_test = MultiTree()
        tree.append(tmp_test)
    assert tree.count() == COUNT


def test_clear(tree: MultiTree) -> None:
    """Тест метода очистки списка"""
    for _ in range(COUNT):
        tmp_tmp_tree = MultiTree()
        for __ in range(COUNT):
            tmp_tree = MultiTree()
            tmp_tmp_tree.append(tmp_tree)
        tree.append(tmp_tmp_tree)
    tree.clear()
    assert tree.is_empty() == True


def test_find(tree: MultiTree) -> None:
    """Тест медода поиска элемента в списке"""
    tmp_tmp_tree = MultiTree()
    for _ in range(COUNT-1):
        tmp_tree = MultiTree()
        tree.append(tmp_tree)
    tree.append(tmp_tmp_tree)
    assert tree.find(tmp_tmp_tree) == True


def test_getitem(tree:MultiTree) -> None:
    """Тест обращения по индексу"""
    tmp_tmp_tree = MultiTree()
    for _ in range(COUNT-1):
        tmp_tree = MultiTree()
        tree.append(tmp_tree)
    tree.append(tmp_tmp_tree)
    assert tree[COUNT-1] == tmp_tmp_tree