from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.database import Base,engine

class Roupa(Base):
    __tablename__ = 'roupas'

    id_roupa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(70), nullable=False)
    tamanho = Column(String(5), nullable=False)
    cor = Column(String(30), nullable=False)
    preco = Column(Numeric, nullable=False)

    estoques = relationship("Estoque", back_populates="roupa", cascade="all, delete")


