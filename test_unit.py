import pytest
import os
from unittest.mock import patch

from main import Heroes


@pytest.fixture
def journal() -> Heroes:
    return Heroes()