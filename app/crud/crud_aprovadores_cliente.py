from sqlalchemy.orm import Session
from app.db.models.aprovadores_cliente import AprovadoresCliente
from app.crud.crud_configuracao_cliente import get_configuracao_cliente
from app.schemas.aprovadores_cliente import AprovadoresClienteCreate
from sqlalchemy import asc

def create_aprovadores_cliente(db: Session, aprovadores_cliente: AprovadoresClienteCreate):
    db_aprovadores_cliente = AprovadoresCliente(**aprovadores_cliente.dict())
    db.add(db_aprovadores_cliente)
    db.commit()
    db.refresh(db_aprovadores_cliente)
    return db_aprovadores_cliente


def get_all_aprovadores_cliente(db: Session, id_cliente: int):
    aprovadores_cliente = (
        db.query(AprovadoresCliente)
        .filter(AprovadoresCliente.id_cliente == id_cliente, AprovadoresCliente.active == True)
        .order_by(asc(AprovadoresCliente.cargo_aprovador))  # Adiciona essa linha para ordenar
        .all()
    )
    if not aprovadores_cliente:
        return None
    return aprovadores_cliente

def get_multi_aprovadores_cliente(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AprovadoresCliente).offset(skip).limit(limit).all()


def update_aprovadores_cliente(db: Session, db_obj: AprovadoresCliente, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_unic_aprovadores_cliente(db: Session, id_aprovador: int):
    return db.query(AprovadoresCliente).filter(AprovadoresCliente.id == id_aprovador).first()


def get_aprovadores_cliente(db: Session, id_aprovador: int):
    return db.query(AprovadoresCliente).filter(AprovadoresCliente.id == id_aprovador).first()


def delete_aprovadores_cliente(db: Session, aprovadores_cliente: AprovadoresCliente):
    db.delete(aprovadores_cliente)
    db.commit()
