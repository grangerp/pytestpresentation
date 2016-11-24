import pytest
import smtplib


#  @pytest.fixture(scope="function")
@pytest.fixture(scope="module")
def smtp():
    print("smtp")
    smtp = smtplib.SMTP("smtp.gmail.com")
    # tear down
    yield smtp
    smtp.close()
    print("smtp close")


@pytest.fixture(scope="function", params=['123456', 'abcdef'])
def password(request):
    yield request.param


#  @pytest.fixture(scope="function", autouse=True)
def always():
    print("always Start")
    yield
    print("always End")
