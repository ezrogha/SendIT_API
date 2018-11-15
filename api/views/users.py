from flask import jsonify, request, redirect, url_for
from run import app
from api.models.users import *

from datetime import datetime
from time import mktime


@app.route("/api/v1/users", methods=["GET", "POST"])
def allUsers():
  if request.method == "POST":
    firstname = request.form.get("firstname")
    if not firstname:
      return jsonify({ "message": "Please add your firstname" })
    lastname = request.form.get("lastname")
    if not lastname:
      return jsonify({ "message": "Please add your lastname" })
    email = request.form.get("email")
    phone = request.form.get("phone")
    address = request.form.get("address")
    if not address:
      return jsonify({ "message": "Please add your address" })
    password = request.form.get("password")
    if not password:
      return jsonify({ "message": "Please add a password" })
    dt = datetime.now()
    user_id = str(int(mktime(dt.timetuple()))) 
    return jsonify(set_user(firstname, lastname, email, phone, address, password, user_id))

  elif request.method == "GET":
    return jsonify(get_all_users())


@app.route("/api/v1/users/<string:userId>/parcels", methods=["GET", "POST"])
def userParcels(userId):
  user = check_user(userId)
  if not user:
    return jsonify({"404.html": f"User with this id {userId} was not found..."})
  if request.method == "POST":
    parcel_from = request.form.get("p_from")
    parcel_to = request.form.get("to")
    parcel_weight = request.form.get("weight")
    parcel_price = request.form.get("price")
    parcel_status = "Not Delivered"
    parcel_id = str(userId) + "_" + str(len(db["parcels"]))
    return jsonify(set_user_parcels(parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status, parcel_id, userId))

  elif request.method == "GET":
    return jsonify(get_user_parcels(userId))