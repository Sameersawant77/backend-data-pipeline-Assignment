
# Backend Data Pipeline

Dockerized backend data pipeline using Flask, FastAPI, and PostgreSQL.

## Architecture

Flask (Mock API) → FastAPI (Ingestion Pipeline) → PostgreSQL

---

## Setup

```bash
docker compose up -d --build
```

---

## API Endpoints

This project exposes APIs from two services:

- Flask Mock Server (data provider)
- FastAPI Pipeline Service (ingestion + query layer)

---

## Flask Mock Server (Port: 5001)

Base URL:
```
http://localhost:5001
```

### Health Check
**GET** `/api/health`

```bash
curl http://localhost:5001/api/health
```

---

### Get Customers (Paginated)
**GET** `/api/customers`

Query params: `page`, `limit`

```bash
curl "http://localhost:5001/api/customers?page=1&limit=5"
```

---

### Get Single Customer
**GET** `/api/customers/{customer_id}`

```bash
curl http://localhost:5001/api/customers/cust_001
```

Returns **404** if not found.

---

## FastAPI Pipeline Service (Port: 8000)

Base URL:
```
http://localhost:8000
```

### Health Check
**GET** `/health`

```bash
curl http://localhost:8000/health
```

---

### Ingest Customers into PostgreSQL
**POST** `/api/ingest`

```bash
curl -X POST http://localhost:8000/api/ingest
```

---

### Get Customers from Database (Paginated)
**GET** `/api/customers`

Query params: `page`, `limit`

```bash
curl "http://localhost:8000/api/customers?page=1&limit=5"
```

---

### Get Single Customer from Database
**GET** `/api/customers/{customer_id}`

```bash
curl http://localhost:8000/api/customers/cust_001
```

Returns **404** if not found.

---

## API Flow

```
Flask API → FastAPI Ingestion → PostgreSQL → FastAPI Query APIs
```

Swagger UI (FastAPI):
```
http://localhost:8000/docs
```

---

## Notes

- End-to-end pagination supported
- Idempotent upsert ingestion
- Environment-based configuration
- Clean microservice architecture
