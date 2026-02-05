from flask import Flask, request, jsonify

app = Flask(__name__)

movies = [{
    "id": 101,
    "movie_name": "Interstellar",
    "language": "English",
    "duration": "2h 49m",
    "price": 250
}]

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200


@app.route("/api/movies/<int:id>", methods=["GET"])
def get_movie(id):
    for m in movies:
        if m["id"] == id:
            return jsonify(m), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies", methods=["POST"])
def add_movie():
    movies.append(request.json)
    return jsonify({"message": "Movie added"}), 201


@app.route("/api/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    for m in movies:
        if m["id"] == id:
            m.update(request.json)
            return jsonify({"message": "Movie updated"}), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    for m in movies:
        if m["id"] == id:
            movies.remove(m)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    if request.json.get("tickets", 0) <= 0:
        return jsonify({"error": "Booking failed"}), 400
    return jsonify({"message": "Booking successful"}), 201


if __name__ == "__main__":
    app.run(debug=True)
