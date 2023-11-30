from pytest import fixture, raises
from loguru import logger

from main import count_service


@fixture
def reusable_db_mocker(mocker):
    mock_db_service = mocker.patch("main.db_service", autospec=True)
    mock_db_service.return_value = [(0, "fake row", 0.0)]
    return mock_db_service


def test_reusable_mocker(reusable_db_mocker):
    logger.debug("Running test_reusable_mocker")
    c = count_service("foo")
    reusable_db_mocker.assert_called_with("foo")
    assert c == 1


def test_mocker_with_exception(reusable_db_mocker):
    logger.debug("Running test_mocker_with_exception")
    reusable_db_mocker.side_effect = Exception("Oh noes!")
    with raises(Exception):
        count_service("foo")

