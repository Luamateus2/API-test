from pydantic import BaseModel
from typing import List

class EstoqueResponse(BaseModel):
    id_estoque: int
    quantidade: int
    roupa_id: int
    class Config:
        from_attributes = True
class EstoqueRequest(BaseModel):
    quantidade: int
    roupa_id: int
    class Config:
       from_attributes = True