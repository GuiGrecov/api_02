from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ola_mundo_conteudo():
    response = client.get("/")
    assert response.json() == {"Olá": "mundo!"}

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200