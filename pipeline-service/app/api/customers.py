from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.customer import Customer
from app.services.ingestion import ingest_customers

router = APIRouter(prefix="/api")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/ingest")
def ingest(db: Session = Depends(get_db)):
    count = ingest_customers(db)
    return {"status": "success", "records_processed": count}


@router.get("/customers")
def get_customers(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    offset = (page - 1) * limit
    data = db.query(Customer).offset(offset).limit(limit).all()
    total = db.query(Customer).count()

    return {
        "data": data,
        "total": total,
        "page": page,
        "limit": limit
    }


@router.get("/customers/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.get(Customer, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
