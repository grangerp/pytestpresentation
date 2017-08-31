"""
bonus git bisect

create file test.py


import fixme

def test_fixme():
    assert fixme.plusone(5) == 6

find first commit: 7d28e0ace912ee3cd2565df553d944349aa8aa4d

git bisect start HEAD 7d28e0ace912ee3cd2565df553d944349aa8aa4d
git bisect run pytest test.py
git bisect reset

"""

"""
https://www.youtube.com/watch?v=DJtef410XaM
The clean architecture
"""
