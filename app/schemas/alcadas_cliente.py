from pydantic import BaseModel
from typing import List
from datetime import datetime

class AlcadasClienteBase(BaseModel):
    limite_minimo_aprovacao: float
    limite_maximo_aprovacao: float
    perfil_aprovador: str
    percentual_aprovacao: float
    active: bool = True
    data_criacao: datetime = datetime.now()

class AlcadasClienteCreate(BaseModel):
    id_cliente: int
    id_tipo_rating: int
    limite_minimo_aprovacao: float
    limite_maximo_aprovacao: float
    perfil_aprovador: str
    percentual_aprovacao: float
    active: bool = True
    data_criacao: datetime = datetime.now()

class AlcadasClienteUpdate(AlcadasClienteBase):
    pass

class AlcadasClienteInDB(AlcadasClienteBase):
    id: int
    id_cliente: int
    id_tipo_rating: int

    class Config:
        orm_mode = True

class AlcadasCliente(AlcadasClienteInDB):
    pass

class AlcadasClienteUpdate(BaseModel):
    limite_minimo_aprovacao: float
    limite_maximo_aprovacao: float
    perfil_aprovador: str
    percentual_aprovacao: float
    active: bool = True
    data_criacao: datetime = datetime.now()