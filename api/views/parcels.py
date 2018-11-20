from flask import jsonify, request
from run import app
from api.models.parcels import *


@app.route("/api/v1/")
def home():
    return jsonify(home_model()), 200


@app.route("/api/v1/parcels", methods=["GET", "POST"])
def allParcels():
    if request.method == "POST":
        content = request.json
        if not content.get("userId"):
            return jsonify({"message": "UserId not found"}), 404

        parcel_userId = content.get("userId")
        if parcel_userId not in list(db["users"]):
            return jsonify({"message": f"User with {parcel_userId} not defined"}), 200

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
        return jsonify(set_parcel(parcel_id, parcel_userId, parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status)), 201

    elif request.method == "GET":
        return jsonify(get_all_parcels()), 200


@app.route("/api/v1/parcels/<string:parcelId>")
def parcel(parcelId):
    parcel = check_parcel(parcelId)
    if not parcel:
        return jsonify({"message": f"Parcel with this id {parcelId} was not found..."}), 404
    return jsonify(parcel), 200


@app.route("/api/v1/parcels/<string:parcelId>/cancel", methods=["PUT"])
def cancelParcel(parcelId):
    parcel = check_parcel(parcelId)
    if not parcel:
        return jsonify({"message": f"Parcel with this id {parcelId} was not found..."}), 404
    if request.method == "PUT":
        return jsonify(cancel_parcel(parcelId)), 204
