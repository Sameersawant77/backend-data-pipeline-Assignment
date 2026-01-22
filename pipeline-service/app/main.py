from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.customers import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Data Pipeline API")

app.include_router(router)


@app.get("/health")
def health():
    return {"status": "ok"}
