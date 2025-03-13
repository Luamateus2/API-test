from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.roupa import create_roupa, get_roupa, get_all_roupas
from app.schemas.roupa import RoupaRequest, RoupaResponse
from app.core.database import get_db

router = APIRouter(prefix="/roupas")

@router.post("/", response_model=RoupaResponse)
def create_roupa_endpoint(roupa_data: RoupaRequest, db: Session = Depends(get_db)):
    return create_roupa(db, roupa_data)

@router.get("/{roupa_id}", response_model=RoupaResponse)
def get_roupa_endpoint(roupa_id: int, db: Session = Depends(get_db)):
    roupa = get_roupa(db, roupa_id)
    if not roupa:
        raise HTTPException(status_code=404, detail="Roupa não encontrada")
    return roupa

@router.get("/", response_model=list[RoupaResponse])
def get_all_roupas_endpoint(db: Session = Depends(get_db)):
    return get_all_roupas(db)
