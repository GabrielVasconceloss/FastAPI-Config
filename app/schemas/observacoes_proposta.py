from pydantic import BaseModel
from typing import List
from datetime import datetime

class ObservacoesPropostaBase(BaseModel):
    id_cliente: int
    id_proposta: int
    id_contraparte: int
    tipo_observacao: int
    observacao_vigente: str
    observacao_sugerido: str
    observacao_aprovado: str
    active: bool = True
    data_criacao: datetime = datetime.now()


class ObservacoesPropostaCreate(BaseModel):
    id_cliente: int
    id_proposta: int
    id_contraparte: int
    tipo_observacao: int
    observacao_vigente: str
    observacao_sugerido: str
    observacao_aprovado: str
    active: bool = True
    data_criacao: datetime = datetime.now()

class ObservacoesPropostaUpdate(ObservacoesPropostaBase):
    pass

class ObservacoesPropostaInDB(ObservacoesPropostaBase):
    id: int

    class Config:
        orm_mode = True

class ObservacoesProposta(ObservacoesPropostaInDB):
    pass

class ObservacoesPropostaUpdate(BaseModel):
    tipo_observacao: int
    observacao_vigente: str
    observacao_sugerido: str
    observacao_aprovado: str
    active: bool = True
    data_criacao: datetime = datetime.now()
