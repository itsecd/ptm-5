import time
from collections import namedtuple

from loguru import logger

"""
Mostly stolen from https://github.com/pluralsight/intro-to-pytest
"""

DATA_SET_A = {
    "Foo": "Bar",
    "Baz": [5, 7, 11],
    "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
}
DATA_SET_B = DATA_SET_A
FakeRow = namedtuple("FakeRow", ("id", "name", "value"))


def db_service(query_parameters: str) -> list:
    """
    A fake DB service that takes a remarkably long time to yield results
    """
    logger.debug("Doing expensive database stuff!")
    time.sleep(5.0)
    data = [FakeRow(0, "Foo", 19.95), FakeRow(1, "Bar", 1.99), FakeRow(2, "Baz", 9.99)]
    logger.debug("Done doing expensive database stuff")
    return data


def count_service(query_parameters: str) -> int:
    logger.debug("count_service: Performing a query and counting the results")
    data = db_service(query_parameters)
    count = len(data)
    logger.debug(f"Found {count} result(s)!")
    return count
