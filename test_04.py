"""
Parametrizing tests
pytest test_04.py -v
"""
import pytest
from decimal import Decimal


def add(x, y):
    return x + y


@pytest.mark.parametrize("x,y,expected", [
    (1, 2, 3),
    (Decimal('100'), Decimal('200'), Decimal('300')),
    (1, 1, 1),
])
def test_add(x, y, expected):
    assert add(x, y) == expected
