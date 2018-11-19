from flask import jsonify, request, redirect, url_for
from run import app
from api.models.parcels import *


@app.route("/")
def index():
    return redirect(url_for("home"))


@app.route("/api/v1/")
def home():
    return jsonify(home_model())


@app.route("/api/v1/parcels", methods=["GET", "POST"])
def allParcels():
    if request.method == "POST":
        content = request.json
        if not content.get("userId"):
            return jsonify({"404": "UserId not defined"})

        parcel_userId = content.get("userId")
        if parcel_userId not in list(db["users"]):
            return jsonify({"404": f"User with {parcel_userId} not defined"})

        parcel_from = content.get("p_from")
        if not parcel_from:
            return jsonify({"message": "Please add a source"})

        parcel_to = content.get("to")
        if not parcel_to:
            return jsonify({"message": "Please add a destination"})

        parcel_weight = content.get("weight")
        if not parcel_weight:
            return jsonify({"message": "Please add a weight"})
        elif type(parcel_weight) is not int:
            return jsonify({"message": "Please enter a valid weight"})

        parcel_price = content.get("price")
        if not parcel_price:
            return jsonify({"message": "Please add a price"})
        elif type(parcel_price) is not int:
            return jsonify({"message": "Please enter a valid price"})

        parcel_status = "Not Delivered"
        parcel_id = str(parcel_userId) + "_" + str(len(db["parcels"]))
        return jsonify(set_parcel(parcel_id, parcel_userId, parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status))

    elif request.method == "GET":
        return jsonify(get_all_parcels())


@app.route("/api/v1/parcels/<string:parcelId>")
def parcel(parcelId):
    parcel = check_parcel(parcelId)
    if not parcel:
        return jsonify({"404": f"The Parcel with this id {parcelId} was not found..."})
    return jsonify(parcel)


@app.route("/api/v1/parcels/<string:parcelId>/cancel", methods=["GET", "PUT"])
def cancelParcel(parcelId):
    parcel = check_parcel(parcelId)
    if not parcel:
        return jsonify({"404": f"Parcel with this id {parcelId} was not found..."})
    if request.method == "PUT":
        return jsonify(cancel_parcel(parcelId))
