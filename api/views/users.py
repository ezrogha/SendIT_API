from flask import request, jsonify, redirect, url_for
from run import app
from api.models.users import User
from api.models.parcels import Parcel
import re

User = User()
Parcel = Parcel()

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
from validate_email import validate_email

app.config["JWT_SECRET_KEY"] = "sweetlordJesus"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)


@app.route("/")
def index():
    return redirect(url_for("home"))

@app.route("/api/v2/")
def home():
    return jsonify({"message": "Welcome To SendIT"}), 200

@app.route("/api/v2/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        content = request.json
        username = content.get("username").strip()
        if not username:
            return jsonify({"message": "Please add a username"}), 400
        elif type(validateString(username)) != str:
                return validateString(username)

        password = content.get("password").strip()
        if not password:
            return jsonify({"message": "Please add a password"}), 400

        email = content.get("email").strip()
        if not email:
            return jsonify({"message": "Please add an email"}), 400
        elif validateEmail(email):
            return validateEmail(email)

        phone = content.get("phone").strip()
        if not phone:
            return jsonify({"message": "Please enter a phone number"}), 400
        elif validateNumString(phone):
            return validateNumString(phone)

        address = content.get("address").strip()
        if not address:
            return jsonify({"message": "Please enter an address"}), 400
        elif type(validateString(address)) != str:
                return validateString(address)

        role = content.get("role")

        response = User.setUser(username, email, phone, address, password, role)
        if response == {"message": "username or email already used"}:
            return jsonify(response), 409
        return jsonify(response), 201
    return jsonify({"message": "Please Register"}), 200


@app.route("/api/v2/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        content = request.json
        username = content.get("username")
        if not username:
            return jsonify({"message": "Please provide a username"}), 400

        password = content.get("password")
        if not password:
            return jsonify({"message": "Please provide a password"}), 400

        result = User.loginUser(username, password)
        if result == {"message": "User doesnot exist"}:
            return jsonify(result), 400
        access_token = create_access_token(identity=result)
        return jsonify(access_token=access_token), 200

    return jsonify({"message": "Please Login"}), 200


@app.route("/api/v2/users/<int:userId>/parcels", methods=["GET", "PUT"])
@jwt_required
def userParcels(userId):
    if request.method == "GET":
        result = User.specificUserparcels(userId)
        if result == {"message":"User doesnot exist"}:
            return jsonify(result), 400
        return jsonify(result), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route("/api/v2/users", methods=["GET"])
@jwt_required
def allUsers():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "GET":
            return jsonify(User.fetchAllUsers()), 200
        return jsonify({"message": "Method Not Allowed"}), 405
    return jsonify({"message": "Please login as admin to access data"}), 401


@app.route("/api/v2/parcels", methods=["GET", "POST"])
@jwt_required
def allParcels():
    if request.method == "POST":
        content = request.json

        current_user = get_jwt_identity()
        parcel_userId = current_user["userid"]
        
        parcel_from = content.get("source")
        if not parcel_from:
            return jsonify({"message": "Please add a source"}), 400

        parcel_to = content.get("destination")
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

        now = datetime.datetime.now()
        parcel_creation_date = str(now.strftime("%Y-%m-%d %H:%M"))

        return jsonify(Parcel.setParcels(parcel_userId, parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status, parcel_location, parcel_creation_date)), 201

    elif request.method == "GET":
        current_user = get_jwt_identity()
        if current_user["role"] == "admin":
            if request.method == "GET":
                return jsonify(Parcel.viewAllParcels()), 200
        return jsonify({"message": "Please login as admin to access data"}), 401


@app.route("/api/v2/parcels/<int:parcelId>")
@jwt_required
def parcel(parcelId):
    current_user = get_jwt_identity()
    userId = current_user["userid"]
    result = Parcel.parcelDetails(parcelId, userId)
    if result == {"message": "OrderId doesnot exist"}:
        return jsonify(result), 400
    return jsonify(result), 200


@app.route("/api/v2/parcels/<int:parcelId>/cancel", methods=["PUT"])
@jwt_required
def cancelParcel(parcelId):
    current_user = get_jwt_identity()
    userId = current_user["userid"]
    if request.method == "PUT":
        result = Parcel.cancelParcelOrder(parcelId, userId)
        if result == {"message": "OrderId does not exist"}:
            return jsonify(result), 404
        return jsonify(result), 200
    return jsonify({"message": "Method Not Allowed"}), 405


@app.route("/api/v2/parcels/<int:parcelId>/send", methods=["PUT"])
@jwt_required
def sendParcel(parcelId):
    current_user = get_jwt_identity()
    userId = current_user["userid"]
    if request.method == "PUT":
        result = Parcel.sendParcelOrder(parcelId, userId)
        if result == {"message": "OrderId does not exist"}:
            return jsonify(result), 404
        return jsonify(result), 200
    return jsonify({"message": "Method Not Allowed"}), 405
    

@app.route('/api/v2/parcels/<int:parcelId>/destination', methods=["PUT"])
@jwt_required
def changeDestination(parcelId):
    current_User = get_jwt_identity()
    if request.method == "PUT":
        current_User = get_jwt_identity()
        userId = current_User["userid"]
        destination = request.json.get("destination")
        response = Parcel.changeParcelDestination(parcelId, userId, destination)
        if response == {"message": "OrderId does not exist"}:
            return jsonify(response), 404
        return jsonify(response), 200
    return jsonify({"message": "Method Not Allowed"}), 405
    



@app.route('/api/v2/parcels/<int:parcelId>/location', methods=["PUT"])
@jwt_required
def changeLocation(parcelId):
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "PUT":
            location = request.json.get("current_location")
            return jsonify(Parcel.changeParcelLocation(parcelId, location)), 200
        return jsonify({"message": "Method Not Allowed"}), 405
    return jsonify({"message": "Please login as admin to make alteration"}), 401    


@app.route('/api/v2/parcels/<int:parcelId>/status', methods=["PUT"])
@jwt_required
def changeStatus(parcelId):
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        if request.method == "PUT":
            status = request.json.get("status")
            return jsonify(Parcel.changeParcelStatus(parcelId, status)), 200
        return jsonify({"message": "Method Not Allowed"}), 405
    return jsonify({"message": "Please login as admin to access data"}), 401    


def validateNumString(number):
    if any(i.isalpha() for i in number):
        return jsonify({"message": "Please enter a valid phone number"}), 400

def validateString(name):
    if any(i.isdigit() for i in name):
        return jsonify({"message": "Please enter a valid name, there should be no numbers"}), 400
    regex = re.compile("[@_!#$%^&*()<>?/\|}{~:;]")
    if regex.search(name) != None:
        return jsonify({"message": "Please enter a valid name, there should be no special characters"}), 400
    return name

def validateEmail(email):
    match = re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I)
    if not match:
        return jsonify({"message": "Please enter a valid email"}), 400