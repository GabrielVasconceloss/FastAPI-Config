from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy.sql import func


class AprovadoresCliente(Base):
    __tablename__ = "aprovadores_cliente"
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    id_cliente = Column(Integer())
    cargo_aprovador = Column(String)
    login_aprovador = Column(String)
    perfil_aprovador = Column(String)
    percentual_peso_aprovador = Column(DECIMAL)
    active = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())



