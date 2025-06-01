from fastapi import FastAPI
from typing import List, Dict, Any

app = FastAPI()

produtos: list[Dict[str, Any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "preco": 10.0,
        "descricao": "Telefone inteligente "
    },
    {
        "id": 2,
        "nome": "Notebook",
        "preco": 20.0,
        "descricao": "Um notebook potente"
    },
    {
        "id": 3,
        "nome": "Tablet",
        "preco": 30.0,
        "descricao": "Um computador portátil"
    }


]

@app.get("/produtos", response_model=List[Dict[str, Any]])
def listar_produtos():
    return produtos

@app.get("/")
def ola_mundo():
    return {"Olá":"mundo!"}