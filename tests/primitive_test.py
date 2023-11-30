from loguru import logger

from main import DATA_SET_A, DATA_SET_B


def test_nothing():
    logger.debug("Running test_example")
    pass


def test_primitive():
    logger.debug("Running test_primitive")
    assert DATA_SET_A == DATA_SET_B
