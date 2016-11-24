"""
Assert exceptions
"""
import pytest


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        1 / 0
