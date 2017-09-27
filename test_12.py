"""
Test more complexe types
https://hypothesis.readthedocs.io/en/master/data.html
https://hypothesis.readthedocs.io/en/master/django.html
Test with note
HYPOTHESIS_VERBOSITY_LEVEL=verbose pytest test_12.py
"""
from hypothesis import strategies as st
from hypothesis import given, note


@given(st.lists(st.integers()), st.randoms())
def test_shuffle_is_noop(ls, r):
    """ shuffle modify ls2 """
    ls2 = list(ls)
    r.shuffle(ls2)
    note(f'Note: Shuffle: {ls2}, r: {r}')
    assert ls == ls2
