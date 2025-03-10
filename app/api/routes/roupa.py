from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.roupa import (
    create_roupa, get_roupa, get_all_roupas, update_roupa, delete_roupa
)
from app.schemas.roupa import RoupaRequest, RoupaResponse
from app.core.database import get_db

router = APIRouter(prefix="/roupas", tags=["Roupas"])

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

@router.put("/{roupa_id}", response_model=RoupaResponse)
def update_roupa_endpoint(roupa_id: int, roupa_data: RoupaRequest, db: Session = Depends(get_db)):
    roupa = update_roupa(db, roupa_id, roupa_data)
    if not roupa:
        raise HTTPException(status_code=404, detail="Roupa não encontrada")
    return roupa

@router.delete("/{roupa_id}", status_code=204)
def delete_roupa_endpoint(roupa_id: int, db: Session = Depends(get_db)):
    sucesso = delete_roupa(db, roupa_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Roupa não encontrada")
