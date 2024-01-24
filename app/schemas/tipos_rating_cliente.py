from typing import List
from pydantic import BaseModel
from datetime import datetime

class TiposRatingClienteBase(BaseModel):
    codigo_rating: str
    descricao_rating: str
    prob_default_inicial: float
    prob_default_final: float
    active: bool = True
    data_criacao: datetime = datetime.now()

class TiposRatingClienteCreate(TiposRatingClienteBase):
    id_cliente: int
    pass


class TiposRatingClienteUpdate(TiposRatingClienteBase):
    pass

class TiposRatingClienteInDB(TiposRatingClienteBase):
    id: int
    id_cliente: int



class TiposRatingCliente(TiposRatingClienteInDB):
    pass

class TiposRatingClienteUpdate(BaseModel):
    codigo_rating: str
    descricao_rating: str
    prob_default_inicial: float
    prob_default_final: float
    active: bool = True
    data_criacao: datetime = datetime.now()