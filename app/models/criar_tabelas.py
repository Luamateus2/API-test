from ..models.roupa import Roupa
from ..models.estoque import Estoque
from app.core.database import engine, Base

# Criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
