from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class LimitesProposta(Base):
    __tablename__ = "limites_proposta"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    id_cliente = Column(Integer())
    id_proposta = Column(Integer())
    id_contraparte = Column(Integer())
    tipo_limite = Column(Integer)
    rating = Column(String)
    valor_limite = Column(DECIMAL)
    valor_carteira = Column(DECIMAL)
    carteira_mwm = Column(DECIMAL)
    active = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
