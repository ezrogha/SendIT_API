from flask import Flask, jsonify, request, redirect, url_for
from data import db

from datetime import datetime
from time import mktime

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/api/v1/")
def index():
    db["_response"] = {
        "code": "200",
        "message": "Welcome to SendIT api"
    }
    return jsonify(db)


@app.route("/api/v1/users", methods=["GET", "POST"])
def users():
    if request.method == "POST":
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        password = request.form.get("password")
        dt = datetime.now()
        user_id = str(int(mktime(dt.timetuple())))
        db["users"][user_id] = {
            "userId": user_id,
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "phone": phone,
            "address": address,
            "password": password,
            "sent": 0,
            "received": 0,
            "status": "active"
        }
        db["_response"] = {
            "code": "201",
            "message": f"Hello {firstname}, your account was created, successfully"
        }
        users = db["users"]
        message = db["_response"]
        users_db = {
            "_response": message,
            "users": users
        }
        return jsonify(users_db)

    elif request.method == "GET":
        db["_response"] = {
            "code": "200",
            "message": "All Users"
        }
        users = db["users"]
        message = db["_response"]
        users_db = {
            "_response": message,
            "users": users
        }
        return jsonify(users_db)


@app.route("/api/v1/parcels", methods=["GET", "POST"])
def parcels():
    if request.method == "POST":
        if not request.form.get('userId'):
            return jsonify({"404": "UserId not defined"})
        parcel_userId = request.form.get('userId')
        if parcel_userId not in list(db["users"]):
            return jsonify({"404": f"User with {parcel_userId} not defined"})
        parcel_from = request.form.get("p_from")
        parcel_to = request.form.get("to")
        parcel_weight = request.form.get("weight")
        parcel_price = request.form.get("price")
        parcel_status = "Not Delivered"
        parcel_id = str(parcel_userId) + "_" + str(len(db["parcels"]))
        db["parcels"][parcel_id] = {
            "parcelId": parcel_id,
            "userId": parcel_userId,
            "from": parcel_from,
            "to": parcel_to,
            "weight": parcel_weight,
            "price": parcel_price,
            "status": parcel_status
        }
        db["_response"] = {
            "code": "201",
            "message": f"A parcel is created by user {parcel_userId}"
        }
        parcels = db["parcels"]
        message = db["_response"]
        parcels_db = {
            "_response": message,
            "parcels": parcels
        }
        return jsonify(parcels_db)

    elif request.method == "GET": 
        db["_response"] = {
            "code": "200",
            "message": "All Parcels"
        }
        parcels = db["parcels"]
        message = db["_response"]
        parcels_db = {
            "_response": message,
            "parcels": parcels
        }
        return jsonify(parcels_db)


@app.route("/api/v1/parcels/<string:parcelId>")
def get_parcel(parcelId):
    parcel = db["parcels"].get(parcelId)
    if not parcel:
        return jsonify({"404": f"The Parcel with this id {parcelId} was not found..."})
    return jsonify(parcel)


@app.route("/api/v1/users/<string:userId>/parcels", methods=["GET", "POST"])
def get_user_parcels(userId):
    if not db["users"].get(userId):
        return jsonify({"404.html": f"User with this id {userId} was not found..."})
    if request.method == "POST":
        parcel_from = request.form.get("p_from")
        parcel_to = request.form.get("to")
        parcel_weight = request.form.get("weight")
        parcel_price = request.form.get("price")
        parcel_status = "Not Delivered"
        parcel_id = str(userId) + "_" + str(len(db["parcels"]))
        db["parcels"][parcel_id] = {
            "parcelId": parcel_id,
            "userId": userId,
            "from": parcel_from,
            "to": parcel_to,
            "weight": parcel_weight,
            "price": parcel_price,
            "status": parcel_status
        }
        userdb = {}
        userdb["user"] = db["users"][userId]
        user_parcels = {}

        for parcelId in db["parcels"]:
            if not db["parcels"][parcelId] == {}:
                if userId == db["parcels"][parcelId]["userId"]:
                    user_parcels[parcelId] = db["parcels"][parcelId]
        userdb["parcels"] = user_parcels
        userparcels = userdb["parcels"]
        db["_response"] = {
            "code": "201",
            "message": f"A new parcel has been created by user {userId}"
        }
        message = db["_response"]
        user_db  = {
            "_response": message,
            "parcels": userparcels}
        return jsonify(user_db)

    elif request.method == "GET":
        userdb = {}
        userdb["user"] = db["users"][userId]
        user_parcels = {}

        for parcelId in db["parcels"]:
            if not db["parcels"][parcelId] == {}:
                if userId == db["parcels"][parcelId]["userId"]:
                    user_parcels[parcelId] = db["parcels"][parcelId]
        userdb["parcels"] = user_parcels
        userparcels = userdb["parcels"]
        db["_response"] = {
            "code": "200",
            "message": f"list of all parcels of user {userId}"
        }
        message = db["_response"]
        user_db  = {
            "_response": message,
            "parcels": userparcels}
        return jsonify(user_db)


@app.route("/api/v1/parcels/<string:parcelId>/cancel", methods=["GET", "PUT"])
def cancel_parcel(parcelId):
    if not db["parcels"].get(parcelId):
        return jsonify({"404": f"Parcel with this id {parcelId} was not found..."})
    if request.method == "PUT":
        db["parcels"][parcelId] = {}
        return jsonify({"204": f"Order {parcelId} has been cancelled"})


if __name__ == "__main__":
    app.run()
