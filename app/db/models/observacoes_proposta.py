from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class ObservacoesProposta(Base):
    __tablename__ = "observacoes_proposta"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    id_cliente = Column(Integer())
    id_proposta = Column(Integer())
    id_contraparte = Column(Integer())
    tipo_observacao = Column(Integer)
    observacao_vigente = Column(String)
    observacao_sugerido = Column(String)
    observacao_aprovado = Column(String)
    active = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())



