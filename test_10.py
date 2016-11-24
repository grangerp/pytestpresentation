"""
HypothesisWorks: property based testing
Run with HYPOTHESIS_VERBOSITY_LEVEL=verbose for verbosity
"""
from hypothesis import given
from hypothesis.strategies import floats


@given(floats(), floats())
def test_floats_are_commutative(x, y):
    assert x + y == y + x
