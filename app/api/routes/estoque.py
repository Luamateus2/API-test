from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.estoque import create_estoque, get_estoque, get_all_estoques
from app.schemas.estoque import EstoqueRequest, EstoqueResponse
from app.core.database import get_db

router = APIRouter(prefix="/estoques", tags=["Estoques"])

@router.post("/", response_model=EstoqueResponse)
def create_estoque_endpoint(estoque_data: EstoqueRequest, db: Session = Depends(get_db)):
    return create_estoque(db, estoque_data)

@router.get("/{estoque_id}", response_model=EstoqueResponse)
def get_estoque_endpoint(estoque_id: int, db: Session = Depends(get_db)):
    estoque = get_estoque(db, estoque_id)
    if not estoque:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return estoque

@router.get("/", response_model=list[EstoqueResponse])
def get_all_estoques_endpoint(db: Session = Depends(get_db)):
    return get_all_estoques(db)
