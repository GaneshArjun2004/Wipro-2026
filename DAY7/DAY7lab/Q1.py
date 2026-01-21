from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data
users = [
    {"id": 1, "name": "Arjun"},
    {"id": 2, "name": "Ganesh"}
]

# GET1
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET2
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# POST r
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    if data is None or "name" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == "__main__":
    app.run(debug=True)
print("NEW CODE RUNNING")
