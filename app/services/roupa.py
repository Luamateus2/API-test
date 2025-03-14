from sqlalchemy.orm import Session
from app.models.roupa import Roupa
from app.schemas.roupa import RoupaRequest, RoupaResponse

def create_roupa(db: Session, roupa_data: RoupaRequest) -> RoupaResponse:
    nova_roupa = Roupa(**roupa_data.dict())
    db.add(nova_roupa)
    db.commit()
    db.refresh(nova_roupa)
    return RoupaResponse.from_orm(nova_roupa)

def get_roupa(db: Session, roupa_id: int) -> RoupaResponse:
    roupa = db.query(Roupa).filter(Roupa.id_roupa == roupa_id).first()
    if not roupa:
        return None
    return RoupaResponse.from_orm(roupa)

def get_all_roupas(db: Session):
    return db.query(Roupa).all()

