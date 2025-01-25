from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def list_all_products():
    return jsonify([])  # Return an empty list for now

@app.route("/products/<int:id>", methods=["GET"])
def read_product(id):
    return jsonify({"id": id})  # Mock response for now

@app.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.json
    return jsonify({"id": id, "updated": data})

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    return "", 204

@app.route("/products", methods=["GET"])
def list_by_name():
    name = request.args.get("name")
    return jsonify({"name": name})

@app.route("/products", methods=["GET"])
def list_by_category():
    category = request.args.get("category")
    return jsonify({"category": category})

@app.route("/products", methods=["GET"])
def list_by_availability():
    availability = request.args.get("availability")
    return jsonify({"availability": availability})