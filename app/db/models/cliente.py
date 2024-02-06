from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer
from app.db.base_class import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)