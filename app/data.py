from typing import List, Dict, Any


class Produtos:
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

    def listar_produtos(self):
        return self.produtos
    
    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status":404, "Mensagem":"Produto não encontrado"}
    
    def adicionar_produto(self, produto): 
        self.produtos.append(produto)
        return produto      