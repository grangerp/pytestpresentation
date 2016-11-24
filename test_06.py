"""
Fixtures with params
See conftest.py
Run 4 tests
"""


def test_pass1(password):
    assert password == '123456'


def test_pass2(password):
    assert password == '123456'
