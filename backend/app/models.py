from pydantic import BaseModel, Field
from typing import Optional

class ProdutoBase(BaseModel):
    nome: str = Field(..., example="Parafuso M6")
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    preco: float = 0.0
    quantidade: int = 0
    unidade: Optional[str] = None
    codigo: Optional[str] = None

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(BaseModel):
    nome: Optional[str]
    descricao: Optional[str]
    categoria: Optional[str]
    preco: Optional[float]
    quantidade: Optional[int]
    unidade: Optional[str]
    codigo: Optional[str]


