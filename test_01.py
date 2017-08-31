"""
Basic function, no need to include pytest
pytest test_o1.py
"""


def f():
    return 3


def test_f():
    assert f() == 4
