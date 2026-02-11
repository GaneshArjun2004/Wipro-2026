from flask import Blueprint, request, jsonify
import models

restaurant_bp = Blueprint("restaurant_bp", __name__)

# Register Restaurant
@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    global restaurant_id_counter
    
    data = request.json
    if not data.get("name"):
        return jsonify({"error": "Name required"}), 400

    restaurant_id = models.restaurant_id_counter
    models.restaurants[restaurant_id] = data
    models.restaurant_id_counter += 1

    return jsonify({"id": restaurant_id, "data": data}), 201


# View Restaurant
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def view_restaurant(restaurant_id):
    restaurant = models.restaurants.get(restaurant_id)
    if not restaurant:
        return jsonify({"error": "Not Found"}), 404
    
    return jsonify(restaurant), 200


# Add Dish
@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    if restaurant_id not in models.restaurants:
        return jsonify({"error": "Restaurant not found"}), 404

    data = request.json
    dish_id = models.dish_id_counter

    models.dishes[dish_id] = {
        "restaurant_id": restaurant_id,
        "data": data
    }

    models.dish_id_counter += 1
    return jsonify({"dish_id": dish_id}), 201
