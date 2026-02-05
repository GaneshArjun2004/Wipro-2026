import requests

BASE = "http://127.0.0.1:5000"

def test_get_movies():
    r = requests.get(f"{BASE}/api/movies")
    assert r.status_code == 200


def test_add_movie():
    movie = {
        "id": 102,
        "movie_name": "Inception",
        "language": "English",
        "duration": "2h 28m",
        "price": 220
    }
    r = requests.post(f"{BASE}/api/movies", json=movie)
    assert r.status_code == 201


def test_book_ticket():
    booking = {"movie_id": 101, "tickets": 2}
    r = requests.post(f"{BASE}/api/bookings", json=booking)
    assert r.status_code == 201
