from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.models.cliente import Cliente

from app.db.base_class import Base

class TiposRatingCliente(Base):
    __tablename__ = "tipos_rating_cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer())
    codigo_rating = Column(String)
    descricao_rating = Column(String)
    prob_default_inicial = Column(DECIMAL)
    prob_default_final = Column(DECIMAL)
    active = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

