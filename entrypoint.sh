#!/bin/sh
# entrypoint.sh

# Wait for PostgreSQL to be ready
until nc -z -w 1 db 5432; do
  echo "Waiting for PostgreSQL..."
  sleep 1
done

# Run Alembic migrations
alembic upgrade head

# Start the application
exec uvicorn app.main:app --host 0.0.0.0 --port 8080
