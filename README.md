# FastAPI Config

Este é um projeto FastAPI Config que utiliza Docker Compose para configurar um ambiente de desenvolvimento. O Docker Compose é utilizado para construir e executar containers.

## Instruções de Uso

### Construir e Iniciar Containers

Para construir e iniciar os containers, execute o seguinte comando:

```bash
docker-compose build --no-cache
docker-compose up -d

## Acessar o Banco de Dados
### Para acessar o banco de dados PostgreSQL, utilize o seguinte comando:

docker exec -it fastapi-config-db-1 psql -U fast -d fastapi

INSERT INTO clientes (id) VALUES (1);
