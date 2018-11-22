from flask import request, jsonify
from run import app
from api.models.users import *
from api.models.parcels import *

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
from validate_email import validate_email


app.config["JWT_SECRET_KEY"] = "sweetlordJesus"
jwt = JWTManager(app)


@app.route("/api/v2/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        if not username:
            return jsonify({"message": "Please add a username"}), 400

        password = content.get("password")
        if not password:
            return jsonify({"message": "Please add a password"}), 400

        email = content.get("email")
        if not email:
            return jsonify({"message": "Please add an email"}), 400
        elif not validate_email(email):
            return jsonify({"message": "Please enter a valid Email"})

        phone = content.get("phone")
        if not phone:
            return jsonify({"message": "Please enter a phone number"}), 400

        address = content.get("address")
        if not address:
            return jsonify({"message": "Please enter an address"}), 400

        role = content.get("role")
        if not role:
            role = "user"

        response = setUser(username, email, phone, address, password, role)
        if response == {"message": "username already exists"}:
            return jsonify(response), 200
        return jsonify(response), 201
    return jsonify({"message": "Please Register"}), 200


@app.route("/api/v2/login", methods=["GET", "POST"])
def login():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify({"message": f"{current_user} already logged in"})

    if request.method == "POST":
        content = request.json
        username = content.get("username")
        if not username:
            return jsonify({"message": "Please provide a username"}), 400

        password = content.get("password")
        if not password:
            return jsonify({"message": "Please provide a password"}), 400

        result = loginUser(username, password)
        if result == {"message": "User doesnot exist"}:
            return jsonify(result)
        access_token = create_access_token(identity=result)
        return jsonify(access_token=access_token), 200
        
    return jsonify({"message": "Please Login"}), 200


@app.route("/api/v2/users/<string:userId>/parcels", methods=["GET"])
@jwt_required
def userParcels(userId):
    if request.method == "GET":
        return jsonify(SpecificUserparcels()), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route("/api/v2/users", methods=["GET"])
@jwt_required
def allUsers():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "GET":
            return jsonify(fetchAllUsers()), 200
        return jsonify({"message": "Method Not Allowed"}), 405
    return jsonify({"message": "Please login as admin to access data"}), 401


@app.route("/api/v2/parcels", methods=["GET", "POST"])
@jwt_required
def allParcels():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "POST":
            content = request.json

            parcel_userId = content.get("userId")
            if not parcel_userId:
                return jsonify({"message": "UserId not defined"}), 400

            parcel_from = content.get("p_from")
            if not parcel_from:
                return jsonify({"message": "Please add a source"}), 400

            parcel_to = content.get("to")
            if not parcel_to:
                return jsonify({"message": "Please add a destination"}), 400

            parcel_weight = content.get("weight")
            if not parcel_weight:
                return jsonify({"message": "Please add a weight"}), 400
            elif type(parcel_weight) is not int:
                return jsonify({"message": "Please enter a valid weight"}), 400

            parcel_price = content.get("price")
            if not parcel_price:
                return jsonify({"message": "Please add a price"}), 400
            elif type(parcel_price) is not int:
                return jsonify({"message": "Please enter a valid price"}), 400

            parcel_status = "Not Delivered"

            parcel_location = ""
            
            return jsonify(setParcels(parcel_userId, parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status, parcel_location)), 201

        elif request.method == "GET":
            return jsonify(viewAllParcels()), 200
    return jsonify({"message": "Please login as admin to access data"}), 401

@app.route("/api/v2/parcels/<int:parcelId>")
@jwt_required
def parcel(parcelId):
    current_user = get_jwt_identity()
    userId = current_user["userid"]
    result = parcelDetails(parcelId, userId)
    if result == {"message": "OrderId doesnot exist"}:
        return jsonify(result), 400
    return jsonify(result), 200


@app.route("/api/v2/parcels/<int:parcelId>/cancel", methods=["PUT"])
@jwt_required
def cancelParcel(parcelId):
    current_user = get_jwt_identity()
    userId = current_user["userid"]
    if request.method == "PUT":
        result = cancelParcelOrder(parcelId, userId)
        return jsonify(result), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route("/api/v2/parcels/<int:parcelId>/send", methods=["PUT"])
@jwt_required
def sendParcel(parcelId):
    current_user = get_jwt_identity()
    userId = current_user["userid"]
    if request.method == "PUT":
        result = sendParcelOrder(parcelId, userId)
        return jsonify(result), 200
    return jsonify({"message": "Method Not Allowed"}), 405
    

@app.route('/api/v2/parcels/<int:parcelId>/destination', methods=["PUT"])
@jwt_required
def changeDestination(parcelId):
    if request.method == "PUT":
        current_User = get_jwt_identity()
        userId = current_User["userid"]
        destination = request.json.get("destination")
        return jsonify(changeParcelDestination(parcelId, userId, destination)), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route('/api/v2/parcels/<int:parcelId>/location', methods=["PUT"])
@jwt_required
def changeLocation(parcelId):
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "PUT":
            location = request.json.get("location")
            return jsonify(changeParcelLocation(parcelId, location)), 200
        return jsonify({"message": "Method Not Allowed"}), 405
    return jsonify({"message": "Please login as admin to access data"}), 401    


@app.route('/api/v2/parcels/<int:parcelId>/status', methods=["PUT"])
@jwt_required
def changeStatus(parcelId):
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "PUT":
            status = request.json.get("status")
            return jsonify(changeParcelStatus(parcelId, status)), 200
        return jsonify({"message": "Method Not Allowed"}), 405
    return jsonify({"message": "Please login as admin to access data"}), 401    
