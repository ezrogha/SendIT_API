from flask import request, jsonify
from run import app
from api.models.users import *

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
from validate_email import validate_email


app.config["MY_SECRET_KEY"] = "sweetlordJesus"
jwt = JWTManager(app)


@app.route("/api/v2/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        if not username:
            return jsonify({"message": "Missing Username parameter"}), 400

        password = content.get("password")
        if not password:
            return jsonify({"message": "Missing Password parameter"}), 400

        email = content.get("email")
        if not email:
            return jsonify({"message": "Missing Email parameter"}), 400
        elif not validate_email(email):
            return jsonify({"message": "Email not valid"})

        phone = content.get("phone")
        if not phone:
            return jsonify({"message": "Missing Phone parameter"}), 400

        address = content.get("address")
        if not address:
            return jsonify({"message": "Missing address parameter"}), 400

        role = "user"

        response = setUser(username, email, phone, address, password, role)
        if response == {"message": "username already exists"}:
            return(jsonify(response), 200)
        return(jsonify(response), 201)
    return jsonify({"message": "Please Register"}), 200


@app.route("/api/v2/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        if not username:
            return jsonify({"message": "Missing Username parameter"}), 400

        password = content.get("password")
        if not password:
            return jsonify({"message": "Missing Password parameter"}), 400

        result = loginUser(username, password)
        if type(result) == {"message": f"Welcome {username}"}:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
        return jsonify(result)
    return jsonify({"message": "Please Login"}), 200


@app.route("/api/v1/users/<string:userId>/parcels", methods=["GET"])
@jwt_required
def userParcels(userId):
    if request.method == "GET":
        return jsonify(SpecificUserparcels()), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route("/api/v1/users", methods=["GET"])
@jwt_required
def allUsers():
    if request.method == "GET":
        return jsonify(fetchAllUsers()), 200
    return jsonify({"message": "Method Not Allowed"}), 405
