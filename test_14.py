"""
WebTest test your stack wsgi
Can manipulate forms
HYPOTHESIS_VERBOSITY_LEVEL=verbose pytest test_14.py
"""
from hypothesis import strategies as st
from hypothesis import given
from webtest import TestApp as WebTest


@given(st.text())
def test_app(name):
    app = WebTest(application)
    res = app.get('/')
    assert res.status == '200 OK'
    assert res.status_int == 200

    form = res.forms[0]

    assert form['name'].value == 'Phil'

    form['name'] = name

    res = form.submit()
    assert res.status_int == 200


def application(environ, start_response):
    assert len(str(environ['QUERY_STRING'])) < 20

    body = b'''
    <html>
        <body>
            <form action="" method="GET">
                <input type="text" name="name" value="Phil"/>
                <input type="submit"/>
            </form>
        </body>
    </html>'''
    headers = [('Content-Type', 'text/html; charset=utf8'),
               ('Content-Length', str(len(body)))]
    start_response('200 OK', headers)
    return [body]
