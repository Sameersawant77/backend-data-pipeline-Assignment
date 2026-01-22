from flask import Blueprint, jsonify, request, abort
from app.services.data_loader import load_customers

bp = Blueprint("customers", __name__)

CUSTOMERS = load_customers("data/customers.json")


@bp.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@bp.route("/api/customers", methods=["GET"])
def get_customers():
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 10))
    except ValueError:
        abort(400, description="Invalid pagination parameters")

    total = len(CUSTOMERS)
    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": CUSTOMERS[start:end],
        "total": total,
        "page": page,
        "limit": limit
    })


@bp.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = next((c for c in CUSTOMERS if c["customer_id"] == customer_id), None)
    if not customer:
        abort(404, description="Customer not found")
    return jsonify(customer)
