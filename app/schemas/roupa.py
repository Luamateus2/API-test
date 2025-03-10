from decimal import Decimal
from pydantic import BaseModel
from typing import List

class RoupaResponse(BaseModel):
    id_roupa: int
    nome: str
    tamanho: str
    cor: str
    preco: Decimal
    class Config:
        from_attributes = True

class RoupaRequest(BaseModel):
    nome: str
    tamanho: str
    cor: str
    preco: Decimal
    class Config:
        from_attributes = True