from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Boolean, DateTime
from app.db.base_class import Base
from sqlalchemy.sql import func



class ConfiguracaoCliente(Base):
    __tablename__ = "configuracao_cliente"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    id_cliente = Column(Integer())
    id_tipo_limite = Column(Integer)
    id_limite = Column(Integer)
    id_input_carteira = Column(Integer)
    id_conversao = Column(Integer)
    valor_base_proprietaria = Column(DECIMAL)
    qtd_dias_validade_analise = Column(Integer)
    qtd_dias_intervalo_minimo_aprovacoes = Column(Integer)
    qtd_dias_intervalo_maximo_aprovacoes = Column(Integer)
    active = Column(Boolean, default=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())




