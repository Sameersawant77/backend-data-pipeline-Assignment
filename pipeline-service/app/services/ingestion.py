import requests
from sqlalchemy.orm import Session
from app.core.config import MOCK_SERVER_URL
from app.models.customer import Customer


def ingest_customers(db: Session) -> int:
    page = 1
    limit = 10
    processed = 0

    while True:
        response = requests.get(
            f"{MOCK_SERVER_URL}/api/customers",
            params={"page": page, "limit": limit},
            timeout=10
        )
        response.raise_for_status()

        payload = response.json()
        customers = payload.get("data", [])

        if not customers:
            break

        for c in customers:
            existing = db.get(Customer, c["customer_id"])

            if existing:
                for key, value in c.items():
                    setattr(existing, key, value)
            else:
                db.add(Customer(**c))

            processed += 1

        db.commit()
        page += 1

    return processed
