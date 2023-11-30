import pytest
from loguru import logger


@pytest.fixture(params=["a", "b", "c", "d", "e"])
def letter(request):
    yield request.param


def test_parameterization(letter):
    logger.debug(f"Running test_parameterization with {letter}")
    pass
