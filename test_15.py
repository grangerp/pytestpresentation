"""
What is next
Mutation testing: https://cosmic-ray.readthedocs.io/en/latest/
    http://schinckel.net/tags/mutation-testing/

Run with mut.py --target calculator --unit-test test_15 -m
"""
from unittest import TestCase

from calculator import mul


def mult(x, y):
    return x * y


def test_mult():
    assert mult(2, 2) == 4


""" 100% coverage
What is i change mult

def mult(x, y):
    return x * y

Tests still pass
We have mutate the code and the mutant survived.

Mutation testing mutate your code and be sure mutants does not pass tests
"""


class CalculatorTest(TestCase):

    def test_mul(self):
        self.assertEqual(mul(2, 2), 4)
