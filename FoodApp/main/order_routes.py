from flask import Blueprint, request, jsonify
import models

order_bp = Blueprint("order_bp", __name__)

@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.json

    if not data.get("user_id") or not data.get("restaurant_id"):
        return jsonify({"error": "Missing fields"}), 400

    order_id = models.order_id_counter
    models.orders[order_id] = data
    models.order_id_counter += 1

    return jsonify({"order_id": order_id}), 201
