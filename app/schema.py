from pydantic import BaseModel, PositiveInt
from typing import Optional

class ProdutoSchema(BaseModel):
    id: int
    titulo: str
    preco: PositiveInt
    descricao: Optional[str] = None