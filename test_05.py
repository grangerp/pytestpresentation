"""
Fixtures
See conftest.py
Test with different scope
See object id
pytest test_05.py
"""


def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0


def test_noop(smtp):
    response, msg = smtp.noop()
    assert response == 250
    assert 0
