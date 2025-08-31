# Teste unitário com pytest
# test_flask.py
from flask_exemplo import app

def test_home():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Flask minimalista!' in resp.data
