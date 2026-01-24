## Architecture

Flask (Mock API) → FastAPI (Ingestion Pipeline) → PostgreSQL

I changed the port from 5000 to 5001 for testing the apis as macOS reserves port 5000 for AirPlay Receiver. Instead of disabling OS services, I remapped host ports using Docker Compose.

## Commands to run and test the project

```
docker compose up -d --build
curl "http://localhost:5001/api/customers?page=1&limit=5"
curl -X POST http://localhost:8000/api/ingest
curl "http://localhost:8000/api/customers?page=1&limit=5"
