# -*- coding: utf-8 -*-
# insert_data.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.models.cliente import Cliente


def insert_data():
    # Configurações do banco de dados
    POSTGRES_USER = "fast"
    POSTGRES_PASSWORD = "25673275"
    POSTGRES_DB = "fastapi"
    POSTGRES_HOST = "fastapi-config-db-1"
    POSTGRES_PORT = "5432"

    # Crie a URL do banco de dados
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # Crie uma conexão com o banco de dados
    engine = create_engine(DATABASE_URL)

    # Crie uma sessão do SQLAlchemy
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Crie a instância da sessão
    db = SessionLocal()

    try:
        # Criar instância de Cliente e adicioná-la ao banco de dados
        db_cliente = Cliente(id=1)
        db.add(db_cliente)
        db.commit()
        db.refresh(db_cliente)

        print("Dados inseridos com sucesso!")

    except Exception as e:
        # Em caso de erro, faça rollback para desfazer alterações pendentes
        db.rollback()
        print(f"Erro ao inserir dados: {e}")


    finally:
        # Feche a sessão

        db.close()


if __name__ == "__main__":
    # Chame a função para inserir dados se este script for executado diretamente
    insert_data()