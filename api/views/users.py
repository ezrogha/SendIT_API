from flask import jsonify, request
from run import app
from api.models.users import *

from datetime import datetime
from time import mktime

import re
from validate_email import validate_email


@app.route("/api/v1/users", methods=["GET", "POST"])
def allUsers():
    if request.method == "POST":
        if request.json:
            content = request.json
            firstname = content.get("firstname")
            if not firstname:
                return jsonify({"message": "Please add your firstname"})
            elif type(validateString(firstname)) != str:
                return validateString(firstname)

            lastname = content.get("lastname")
            if not lastname:
                return jsonify({"message": "Please add your lastname"})
            elif type(validateString(lastname)) != str:
                return validateString(lastname)

            email = content.get("email")
            if not email:
                return jsonify({"message": "Please add your email"})
            elif not validate_email(email):
                return jsonify({"message": "Please enter a valid email"})

            phone = content.get("phone")
            if not phone:
                return jsonify({"message": "Please add your phone number"})
            elif validateNumString(phone):
                return validateNumString(phone)

            address = content.get("address")
            if not address:
                return jsonify({"message": "Please add your address"})

            password = content.get("password")
            if not password:
                return jsonify({"message": "Please add a password"})

            dt = datetime.now()
            user_id = str(int(mktime(dt.timetuple())))
            return jsonify(set_user(firstname, lastname, email, phone, address, password, user_id)), 201

    elif request.method == "GET":
        return jsonify(get_all_users()), 200


@app.route("/api/v1/users/<string:userId>/parcels", methods=["GET", "POST"])
def userParcels(userId):
    user = check_user(userId)
    if not user:
        return jsonify({"message": f"User with this id {userId} was not found..."}), 404
    if request.method == "POST":
        content = request.json
        parcel_from = content.get("p_from").strip()
        if not parcel_from:
            return jsonify({"message": "Please enter a parcel source"})

        parcel_to = content.get("to").strip()
        if not parcel_to:
            return jsonify({"message": "Please enter a destination"})

        parcel_weight = content.get("weight")
        if not parcel_weight:
            return jsonify({"message": "Please enter a weight"})
        elif type(parcel_weight) is not int:
            return jsonify({"message": "Please enter a valid weight"})

        parcel_price = content.get("price")
        if not parcel_price:
            return jsonify({"message": "Please add a price"})
        elif type(parcel_price) is not int:
            return jsonify({"message": "Please enter a valid price"})

        parcel_status = "Not Delivered"
        parcel_id = str(userId) + "_" + str(len(db["parcels"]))
        return jsonify(set_user_parcels(parcel_from, parcel_to, parcel_weight, parcel_price, parcel_status, parcel_id, userId)), 201

    elif request.method == "GET":
        return jsonify(get_user_parcels(userId)), 200


def validateString(name):
    if any(i.isdigit() for i in name):
        return jsonify({"message": "Please enter a valid name, there should be no numbers"})
    regex = re.compile("[@_!#$%^&*()<>?/\|}{~:;]")
    if regex.search(name) != None:
        return jsonify({"message": "Please enter a valid name, there should be no special characters"})
    return name


def validateNumString(number):
    if any(i.isalpha() for i in number):
        return jsonify({"message": "Please enter a valid phone number"})
