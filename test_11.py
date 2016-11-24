"""
Use example tu be sure it use your corner case
Run with HYPOTHESIS_VERBOSITY_LEVEL=verbose for verbosity
"""
from hypothesis import example, given
from hypothesis.strategies import floats


#  @example(0.0, float('nan'))
@given(floats(), floats())
def test_floats_are_commutative(x, y):
    assert x + y == y + x
