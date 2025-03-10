from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base,engine
from sqlalchemy import create_engine

class Estoque(Base):
    __tablename__ = 'estoques'

    id_estoque = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer, nullable=False)
    roupa_id = Column(Integer, ForeignKey('roupas.id_roupa', ondelete="CASCADE"), nullable=False)
    roupa = relationship("Roupa", back_populates="estoques")


