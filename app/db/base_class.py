from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    __allow_unmapped__ = True
    id: int = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
