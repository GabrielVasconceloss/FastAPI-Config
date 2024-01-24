from sqlalchemy.orm import Session
from app.db.models.tipos_rating_cliente import TiposRatingCliente
from app.schemas.tipos_rating_cliente import TiposRatingClienteCreate
from fastapi.encoders import jsonable_encoder

def create_tipos_rating_cliente(db: Session, tipos_rating_cliente_in: TiposRatingClienteCreate):
    db_tipos_rating_cliente = TiposRatingCliente(**tipos_rating_cliente_in.dict())
    db.add(db_tipos_rating_cliente)
    db.commit()
    db.refresh(db_tipos_rating_cliente)
    tipos_rating_cliente_dict = jsonable_encoder(db_tipos_rating_cliente)
    return tipos_rating_cliente_dict


def get_multi_tipos_rating_cliente(db: Session, skip: int = 0, limit: int = 10):
    tipos_rating_clientes = db.query(TiposRatingCliente).offset(skip).limit(limit).all()
    
    # Use jsonable_encoder para converter a lista de instâncias em uma lista de dicionários
    tipos_rating_clientes_list = jsonable_encoder(tipos_rating_clientes)

    return tipos_rating_clientes_list


def get_all_tipos_rating_cliente(db: Session, id_cliente: int):
    aprovadores_cliente = db.query(TiposRatingCliente).filter(TiposRatingCliente.id_cliente == id_cliente, TiposRatingCliente.active == True).all()
    if not aprovadores_cliente:
        return None
    return aprovadores_cliente


def get_unic_tipos_rating_cliente(db: Session, id_tipo_rating: int):
    return db.query(TiposRatingCliente).filter(TiposRatingCliente.id == id_tipo_rating).first()



def update_tipos_rating_cliente(db: Session, db_obj: TiposRatingCliente, obj_in: dict):
    for key, value in obj_in.items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)

    # Use jsonable_encoder para converter o objeto para um dicionário
    updated_obj_dict = jsonable_encoder(db_obj)

    return updated_obj_dict


def get_tipos_rating_cliente(db: Session, id_tipo_rating: int):
    return db.query(TiposRatingCliente).filter(TiposRatingCliente.id == id_tipo_rating).first()


def delete_tipos_rating_cliente(db: Session, tipos_rating_cliente: TiposRatingCliente):
    db.delete(tipos_rating_cliente)
    db.commit()

