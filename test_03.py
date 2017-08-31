"""
assert introspection
pytest test_03.py
"""


def test_set_comp():
    s1 = set("1234")
    s2 = set("1254")
    assert s1 == s2
