from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_ola_mundo():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Olá": "mundo!"}

def test_ola_mundo_conteudo():
    response = client.get("/")
    assert response.json() == {"Olá": "mundo!"}

def test_listar_produtos():
    response = client.get("/produtos")
    assert response.status_code == 200

def test_tamanho_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3

def test_pega_um_produto():
    response = client.get("/produtos/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "preco": 10.0,
        "descricao": "Telefone inteligente "
    }