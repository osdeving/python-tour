# Teste de integração com FastAPI
# test_fastapi.py
from fastapi.testclient import TestClient
from fastapi_exemplo import app
client = TestClient(app)
def test_home():
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.json()['mensagem'] == 'FastAPI rápido e moderno!'
