from pydantic import BaseModel
from typing import List
from datetime import datetime

class AprovadoresClienteBase(BaseModel):
    id_cliente: int
    cargo_aprovador: str
    login_aprovador: str
    perfil_aprovador: str
    percentual_peso_aprovador: float
    active: bool = True
    data_criacao: datetime = datetime.now()

class AprovadoresClienteCreate(BaseModel):
    id_cliente: int
    cargo_aprovador: str
    login_aprovador: str
    perfil_aprovador: str
    percentual_peso_aprovador: float
    active: bool = True
    data_criacao: datetime = datetime.now()

class AprovadoresClienteUpdate(AprovadoresClienteBase):
    pass

class AprovadoresClienteInDB(AprovadoresClienteBase):
    id: int

    class Config:
        orm_mode = True

class AprovadoresCliente(AprovadoresClienteInDB):
    pass

class AprovadoresClienteUpdate(BaseModel):
    cargo_aprovador: str
    login_aprovador: str
    perfil_aprovador: str
    percentual_peso_aprovador: float
    active: bool = True
    data_criacao: datetime = datetime.now()