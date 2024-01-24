from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func, false

from app.db.base_class import Base

class PropostaContraparte(Base):
    __tablename__ = "propostas_contraparte"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer())
    id_contraparte = Column(Integer)
    data_aprovacao_limite = Column(DateTime(timezone=False), nullable=True)
    grupo = Column(String)
    tipo_limite = Column(Integer)
    data_proposta = Column(DateTime(timezone=False), server_default=func.now(), nullable=True)
    tipo_analise = Column(Integer)
    status = Column(Integer)
    valor_utilizado_conversao = Column(DECIMAL)
    active = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
