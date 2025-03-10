from sqlalchemy.orm import Session
from app.models.estoque import Estoque
from app.schemas.estoque import EstoqueRequest, EstoqueResponse
def create_estoque(db: Session, estoque_data: EstoqueRequest) -> EstoqueResponse:
    novo_estoque = Estoque(**estoque_data.dict())
    db.add(novo_estoque)
    db.commit()
    db.refresh(novo_estoque)
    return EstoqueResponse.from_orm(novo_estoque)

def get_estoque(db: Session, estoque_id: int) -> EstoqueResponse:
    estoque = db.query(Estoque).filter(Estoque.id_estoque == estoque_id).first()
    if not estoque:
        return None
    return EstoqueResponse.from_orm(estoque)

def get_all_estoques(db: Session):
    return db.query(Estoque).all()

def update_estoque(db: Session, estoque_id: int, estoque_data: EstoqueRequest) -> EstoqueResponse:
    estoque = db.query(Estoque).filter(Estoque.id_estoque== estoque_id).first()
    if not estoque:
        return None
    for key, value in estoque_data.dict().items():
        setattr(estoque, key, value)
    db.commit()
    db.refresh(estoque)
    return EstoqueResponse.from_orm(estoque)

def delete_estoque(db: Session, estoque_id: int) -> bool:
    estoque = db.query(Estoque).filter(Estoque.id_estoque == estoque_id).first()
    if not estoque:
        return False
    db.delete(estoque)
    db.commit()
    return True
