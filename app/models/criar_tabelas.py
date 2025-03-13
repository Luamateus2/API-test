from ..models.roupa import Roupa
from ..models.estoque import Estoque
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)
