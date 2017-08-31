"""
Assert exceptions
pytest test_01.py
"""
import pytest


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        1 / 0
