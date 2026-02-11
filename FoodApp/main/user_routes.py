from flask import Blueprint, request, jsonify
import models

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.json
    
    if not data.get("email"):
        return jsonify({"error": "Email required"}), 400

    user_id = models.user_id_counter
    models.users[user_id] = data
    models.user_id_counter += 1

    return jsonify({"user_id": user_id}), 201
