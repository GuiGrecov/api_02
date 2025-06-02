from fastapi import FastAPI
from .schema import ProdutoSchema
from .data import Produtos

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/produtos", response_model=list[ProdutoSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()

@app.get("/")
def ola_mundo():
    return {"Olá":"mundo!"}

@app.get("/produtos/{id}")
def buscar_produto(id: int, response_model=ProdutoSchema):
    return lista_de_produtos.buscar_produto(id)

@app.post("/produtos", response_model=ProdutoSchema)
def adicionar_produto(produto: ProdutoSchema):
    return lista_de_produtos.adicionar_produto(produto.model_dump())