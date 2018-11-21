from flask import request, jsonify
from run import app
from api.models.users import *
import jwt
import datetime

app.config["MY_SECRET_KEY"] = "sweetlordJesus"

@app.route("/api/v2/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        password = content.get("password")
        email = content.get("email")
        phone = content.get("phone")
        address = content.get("address")
        response = setUser(username, email, phone, address, password)
        if response == {"message": "username already exists"}:
            return(jsonify(response), 200)
        return(jsonify(response), 201)
    return jsonify({"message": "Please Register"}), 200


@app.route("/api/v2/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        password = content.get("password")
        result = loginUser(username, password)
        if type(result) == {"message": f"Welcome {username}"}:
            token = jwt.encode({ "user": "username", "role": "user", "exp": datetime.date.utcnow() + datetime.timedelta(minutes=40)}, app.config["MY_SECRET_KEY"])
            return jsonify(result)
        return jsonify(result)
    return jsonify({"message": "Please Login"}), 200

   
@app.route("/api/v1/users/<string:userId>/parcels", methods=["GET"])
def userParcels(userId):
    if request.method == "GET":
        return jsonify(SpecificUserparcels()), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route("/api/v1/users", methods=["POST"])
def allUsers():
    pass


