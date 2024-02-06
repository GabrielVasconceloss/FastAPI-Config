from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_tipos_rating_cliente, crud_configuracao_cliente, crud_cliente
from app.schemas.tipos_rating_cliente import TiposRatingCliente, TiposRatingClienteCreate, TiposRatingClienteUpdate
from typing import List, Any
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get("/", response_model=List[TiposRatingCliente])
def read_tipos_rating_cliente_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Get All TiposRatingCliente.
    """
    tiposRating_liente = crud_tipos_rating_cliente.get_multi_tipos_rating_cliente(db, skip=skip, limit=limit)
    return tiposRating_liente


@router.get("/{id_cliente}", response_model=List[TiposRatingCliente])
def read_tipos_rating_cliente(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> TiposRatingCliente:
    """
    Get TiposRatingCliente by id_cliente.
    """
    configuracao_cliente = crud_configuracao_cliente.get_configuracao_cliente(db, id_cliente)
    if configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    tipos_rating_cliente = crud_tipos_rating_cliente.get_all_tipos_rating_cliente(db, id_cliente)
    if tipos_rating_cliente is None:
        raise HTTPException(status_code=404, detail="TiposRatingCliente not found")
    tipos_rating_cliente_dict = jsonable_encoder(tipos_rating_cliente)
    return tipos_rating_cliente_dict


@router.post("/", response_model=TiposRatingCliente)
def create_tipos_rating_cliente(
        *,
        db: Session = Depends(deps.get_db),
        tipos_rating_cliente_in: TiposRatingClienteCreate,
) -> Any:
    """
    Create TiposRatingCliente.
    """
    configuracao_cliente = crud_configuracao_cliente.get_configuracao_cliente(db, tipos_rating_cliente_in.id_cliente)
    if configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    created_configuracao_cliente = crud_tipos_rating_cliente.create_tipos_rating_cliente(
        db=db,
        tipos_rating_cliente_in=tipos_rating_cliente_in
    )
    return created_configuracao_cliente

@router.post("/{id_tipo_rating}", response_model=TiposRatingCliente)
def create_tipos_rating_cliente(
        id_tipo_rating: int,
        *,
        db: Session = Depends(deps.get_db),
        tipos_rating_cliente_in: TiposRatingClienteCreate,
) -> Any:
    """
    Create TiposRatingCliente.
    """
    configuracao_cliente = crud_configuracao_cliente.get_configuracao_cliente(db, tipos_rating_cliente_in.id_cliente)
    if configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    tipos_rating_cliente_in_db = crud_tipos_rating_cliente.get_unic_tipos_rating_cliente(db, id_tipo_rating)
    if tipos_rating_cliente_in_db:
        tipos_rating_cliente_in_db.active = False
        db.commit()
        db.refresh(tipos_rating_cliente_in_db)

    created_configuracao_cliente = crud_tipos_rating_cliente.create_tipos_rating_cliente(
        db=db,
        tipos_rating_cliente_in=tipos_rating_cliente_in,
    )
    return created_configuracao_cliente


# @router.put("/{id_tipo_rating}", response_model=TiposRatingCliente)
# def update_tipos_rating_cliente(
#         id_tipo_rating: int,
#         *,
#         db: Session = Depends(deps.get_db),
#         params: TiposRatingClienteUpdate,
# ) -> Any:
#     """
#     Update TiposRatingCliente by id_aprovador.
#     """
#     params_dict = dict(params)
#     tipos_rating_cliente_in_db = crud_tipos_rating_cliente.get_unic_tipos_rating_cliente(db, id_tipo_rating)
#     if tipos_rating_cliente_in_db is None:
#         raise HTTPException(status_code=404, detail="TiposRatingCliente  not found")
#
#
#
#     tipos_rating_cliente_db_updated = crud_tipos_rating_cliente.update_tipos_rating_cliente(
#         db, db_obj=tipos_rating_cliente_in_db, obj_in=params_dict
#     )
#     return tipos_rating_cliente_db_updated
#
#
# @router.delete("/{id_tipo_rating}", response_model=dict)
# def delete_tipos_rating_cliente(
#         id_tipo_rating: int,
#         db: Session = Depends(deps.get_db),
# ) -> Any:
#     """
#     Delete TiposRatingCliente by id_aprovador.
#     """
#     get_tipos_rating_cliente = crud_tipos_rating_cliente.get_tipos_rating_cliente(db, id_tipo_rating)
#     if get_tipos_rating_cliente is None:
#         raise HTTPException(status_code=404, detail="AprovadoresCliente not found")
#
#     crud_tipos_rating_cliente.delete_tipos_rating_cliente(db, get_tipos_rating_cliente)
#
#     return {"message": "ConfiguracaoCliente deleted successfully"}