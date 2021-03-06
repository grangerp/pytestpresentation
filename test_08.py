"""
httpretty let you mock httplib2 urllib2 and requests responses
pytest test_08.py
"""
import pytest
import requests
import httpretty


@pytest.mark.httpretty
def test_instagram_oembed():
    httpretty.register_uri(
        httpretty.GET,
        'http://api.instagram.com/oembed/',
        body='{"author_url": "https://www.instagram.com/ledevoir"}',
        status=200,
        content_type='text/json',
    )

    post = 'https://www.instagram.com/p/BNKN7gFB6kV/'
    res = instagram_oembed(post)
    assert res.status_code == 200
    print(res.json()['author_url'])
    assert False


def instagram_oembed(post):
    url = f'http://api.instagram.com/oembed/?url={post}'
    return requests.get(url)
