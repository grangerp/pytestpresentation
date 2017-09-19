"""
Stats of running tests
use --hypothesis-show-statistics
Param control
pytest test_13.py --hypothesis-show-statistics
"""
from hypothesis import strategies as st
from hypothesis import given, event


@given(st.integers().filter(lambda x: x % 2 == 0))
def test_is_even(i):
    event(f'i mod 3 = {i % 3}')
    assert i % 2 == 0
