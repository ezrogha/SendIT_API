from flask import request, jsonify
from run import app
from api.models.users import *


@app.route("/api/v2/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        password = content.get("password")
        email = content.get("email")
        phone = content.get("phone")
        address = content.get("address")
        return jsonify(setUser(username, email, phone, address, password)), 201
    return jsonify({"message": "Please Register"}), 200


@app.route("/api/v2/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        password = content.get("password")
        return jsonify(loginUser(username, password)), 200
    return jsonify({"message": "Please Login"}), 200

   
@app.route("/api/v1/users/<string:userId>/parcels", methods=["GET", "POST"])
def userParcels(userId):
    pass


@app.route("/api/v1/users", methods=["GET", "POST"])
def allUsers():
    pass




