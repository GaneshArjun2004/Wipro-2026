from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
patients = []
pid = 1

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/patients", methods=["GET", "POST"])
def patients_api():
    global pid
    if request.method == "GET":
        return jsonify(patients)

    data = request.json
    data["id"] = pid
    pid += 1
    patients.append(data)
    return jsonify(data), 201

@app.route("/api/patients/<int:id>", methods=["GET", "PUT"])
def patient_detail(id):
    for p in patients:
        if p["id"] == id:
            if request.method == "GET":
                return jsonify(p)
            p.update(request.json)
            return jsonify(p)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
