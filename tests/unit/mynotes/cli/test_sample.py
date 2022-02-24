import sys
print(sys.path)

import pytest
from mynotes.cli.sample import *

@pytest.mark.parametrize("number,expected", [
    (0, 1), (1, 2), (-1, 0)
])
def test_add_one(number: int, expected: int) -> None:
    assert add_one(number) == expected
