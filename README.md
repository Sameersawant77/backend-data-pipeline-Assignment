## Architecture

Flask (Mock API) → FastAPI (Ingestion Pipeline) → PostgreSQL

## Commands to run and test the project

```
docker compose up -d --build
curl "http://localhost:5001/api/customers?page=1&limit=5"
curl -X POST http://localhost:8000/api/ingest
curl "http://localhost:8000/api/customers?page=1&limit=5"
