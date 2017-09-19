"""
betamax let you record and replay requests
Turn network on and off
pytest test_09.py
"""
from unittest.mock import patch

import pytest
import requests


@pytest.mark.usefixtures('betamax_session')
def test_instagram_oembed(betamax_session):
    post = 'https://www.instagram.com/p/BNKN7gFB6kV/'

    with patch('test_09.requests', betamax_session):
        res = instagram_oembed(post)

    assert res.status_code == 200
    print(res.json()['author_url'])
    assert False


def instagram_oembed(post):
    url = f'http://api.instagram.com/oembed/?url={post}'
    return requests.get(url)
